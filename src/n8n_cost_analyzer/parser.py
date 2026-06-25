from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from n8n_cost_analyzer.models import N8nNode, N8nWorkflow
from n8n_cost_analyzer.node_classifier import NODE_CATEGORIES
from n8n_cost_analyzer.node_classifier import classify_node_type as classify_type

KNOWN_NODE_CATEGORIES: dict[str, str] = dict(NODE_CATEGORIES)


def classify_node_type(node_type: str) -> str:
    return classify_type(node_type)


def _extract_workflows(parsed: Any) -> list[dict[str, Any]]:
    """Normalize any export shape to a list of raw workflow dicts."""
    if isinstance(parsed, dict):
        if "nodes" in parsed:
            return [parsed]
        if "workflows" in parsed and isinstance(parsed["workflows"], list):
            return parsed["workflows"]
        if "data" in parsed:
            data = parsed["data"]
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                return [data]
        return [parsed]
    if isinstance(parsed, list):
        return parsed
    return [{"nodes": [], "name": "Unknown"}]


def _parse_single_workflow(
    raw: dict[str, Any],
    source_path: str | None = None,
) -> N8nWorkflow:
    nodes_raw: list[dict[str, Any]] = raw.get("nodes", [])
    nodes: list[N8nNode] = []
    warnings: list[str] = []
    known_types: set[str] = set(KNOWN_NODE_CATEGORIES.keys())

    for n in nodes_raw:
        pos_raw = n.get("position")
        position: tuple[float, float] | None = None
        if pos_raw is not None and isinstance(pos_raw, (list, tuple)) and len(pos_raw) >= 2:
            position = (float(pos_raw[0]), float(pos_raw[1]))
        elif pos_raw is not None and isinstance(pos_raw, dict):
            x = pos_raw.get("x", 0)
            y = pos_raw.get("y", 0)
            position = (float(x), float(y))

        node_type = n.get("type", "unknown")
        if node_type not in known_types:
            warn_msg = f"Unknown node type '{node_type}' in node '{n.get('name', 'Unnamed')}'"
            if warn_msg not in warnings:
                warnings.append(warn_msg)

        credentials_raw = n.get("credentials")
        credentials: dict[str, Any] | None = None
        if credentials_raw is not None:
            if isinstance(credentials_raw, dict):
                creds: dict[str, Any] = {}
                for ck, cv in credentials_raw.items():
                    if isinstance(cv, dict):
                        creds[ck] = {"id": cv.get("id"), "name": cv.get("name")}
                    else:
                        creds[ck] = {"id": None, "name": str(cv)}
                credentials = creds
            else:
                credentials = {"_": {"id": None, "name": str(credentials_raw)}}

        node = N8nNode(
            id=n.get("id"),
            name=n.get("name", "Unnamed"),
            type=node_type,
            parameters=n.get("parameters", {}),
            position=position,
            disabled=bool(n.get("disabled", False)),
            credentials=credentials,
            raw=n,
        )
        nodes.append(node)

    # Workflow name: try multiple sources, fall back to filename stem
    name: str = "Unnamed Workflow"
    raw_name = raw.get("name")
    if raw_name and isinstance(raw_name, str) and raw_name.strip():
        name = raw_name.strip()
    elif isinstance(raw.get("meta"), dict):
        meta_name = raw["meta"].get("name") or raw["meta"].get("title")
        if meta_name and isinstance(meta_name, str) and meta_name.strip():
            name = meta_name.strip()
    if name == "Unnamed Workflow" and source_path:
        name = Path(source_path).stem
        # If this is part of a collection, disambiguate with a suffix later

    tags_raw = raw.get("tags", [])
    tags: tuple[str, ...] = ()
    if isinstance(tags_raw, list):
        tags = tuple(str(t.get("name", t)) if isinstance(t, dict) else str(t) for t in tags_raw)

    metadata: dict[str, Any] = {}
    for key in ("versionId", "updatedAt", "createdAt", "triggerCount", "shared"):
        if key in raw:
            metadata[key] = raw[key]

    if not nodes_raw:
        warnings.append("Workflow has no nodes")

    return N8nWorkflow(
        id=raw.get("id"),
        name=name,
        active=raw.get("active"),
        nodes=tuple(nodes),
        connections=raw.get("connections", {}),
        settings=raw.get("settings", {}),
        source_path=source_path,
        tags=tags,
        metadata=metadata,
        parser_warnings=tuple(warnings),
    )


def parse_workflow_json(data: str | dict[str, Any], source_path: str | None = None) -> N8nWorkflow:
    """Parse a single workflow from a JSON string or dict."""
    if isinstance(data, str):
        try:
            parsed: dict[str, Any] = json.loads(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}") from e
    else:
        parsed = data

    workflows_raw = _extract_workflows(parsed)
    if not workflows_raw:
        return _parse_single_workflow({"nodes": [], "name": "Empty"}, source_path)
    return _parse_single_workflow(workflows_raw[0], source_path)


def parse_workflow_file(path: str | Path) -> N8nWorkflow:
    """Parse a single workflow file. If the file contains a collection, returns the first workflow."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Workflow file not found: {p}")
    raw = p.read_text(encoding="utf-8")
    return parse_workflow_json(raw, source_path=str(p))


def parse_workflow_collection(path: str | Path) -> list[N8nWorkflow]:
    """Parse a file that may contain one or more workflows (collection export)."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Workflow file not found: {p}")
    raw_text = p.read_text(encoding="utf-8")
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}") from e

    workflows_raw = _extract_workflows(parsed)
    result: list[N8nWorkflow] = []
    multiple = len(workflows_raw) > 1
    for i, wr in enumerate(workflows_raw, 1):
        try:
            wf = _parse_single_workflow(wr, source_path=str(p))
            # Disambiguate unnamed workflows in multi-workflow files
            if multiple and wf.name == Path(p).stem:
                wf = N8nWorkflow(
                    id=wf.id,
                    name=f"{wf.name}_{i}",
                    active=wf.active,
                    nodes=wf.nodes,
                    connections=wf.connections,
                    settings=wf.settings,
                    source_path=wf.source_path,
                    tags=wf.tags,
                    metadata=wf.metadata,
                    parser_warnings=wf.parser_warnings,
                )
            result.append(wf)
        except Exception:
            continue
    return result


def parse_workflow_directory(path: str | Path) -> list[N8nWorkflow]:
    p = Path(path)
    if not p.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {p}")
    workflows: list[N8nWorkflow] = []
    for f in sorted(p.iterdir()):
        if f.suffix.lower() == ".json":
            try:
                for wf in parse_workflow_collection(f):
                    workflows.append(wf)
            except (ValueError, json.JSONDecodeError):
                continue
    return workflows
