#!/usr/bin/env python3
"""
Download public n8n workflow templates to build a local corpus.

Usage examples:
  python scripts/download_n8n_templates.py --category ai --limit 50 --output-dir examples/corpus/batch_002_ai
  python scripts/download_n8n_templates.py --search "gmail openai" --limit 25 --output-dir examples/corpus/batch_003_gmail_ai
  python scripts/download_n8n_templates.py --limit 200 --output-dir examples/corpus/general --allow-large

Safe, rate-limited, endpoint-first. No HTML scraping, no login, no Playwright.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CANDIDATE_BASE_URLS: list[str] = [
    "https://api.n8n.io",
    "https://templates.n8n.io",
    "https://n8n.io",
    "https://api.n8n.cloud",
]

CANDIDATE_ENDPOINTS: list[str] = [
    "/templates/search",
    "/rest/templates/search",
    "/templates",
    "/workflows/templates",
]

TEMPLATE_FETCH_PATHS: list[str] = [
    "/workflows/templates/{}",
    "/templates/workflows/{}",
    "/rest/templates/workflows/{}",
    "/api/templates/{}",
    "/api/workflows/templates/{}",
]

HARD_LIMIT_CAP = 200
DEFAULT_LIMIT = 50
DEFAULT_PAGE_SIZE = 20
DEFAULT_SLEEP_SECONDS = 0.5
REQUEST_TIMEOUT = 10
MAX_RETRIES = 1

USER_AGENT = "n8n-cost-analyzer-corpus-builder/0.1 (+local research; no auth)"


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

@dataclass
class TemplateInfo:
    id: str
    name: str
    category: str | None = None
    source_url: str = ""


@dataclass
class DownloadResult:
    workflows: list[dict[str, Any]] = field(default_factory=list)
    failed: list[dict[str, Any]] = field(default_factory=list)
    skipped: int = 0
    warnings: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Networking helpers
# ---------------------------------------------------------------------------

def _build_opener() -> urllib.request.OpenerDirector:
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", USER_AGENT)]
    return opener


def _fetch_json(url: str, opener: urllib.request.OpenerDirector) -> Any:
    req = urllib.request.Request(url, method="GET")
    with opener.open(req, timeout=REQUEST_TIMEOUT) as resp:
        raw = resp.read()
    return json.loads(raw.decode("utf-8"))


def _safe_fetch(url: str, opener: urllib.request.OpenerDirector) -> tuple[Any, str | None]:
    for attempt in range(1 + MAX_RETRIES):
        try:
            data = _fetch_json(url, opener)
            return data, None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, "HTTP 404"
            if e.code == 403:
                return None, "HTTP 403"
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return None, f"HTTP {e.code}"
        except urllib.error.URLError as e:
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return None, str(e.reason)
        except json.JSONDecodeError as e:
            return None, f"invalid JSON: {e}"
        except OSError as e:
            if attempt < MAX_RETRIES:
                time.sleep(1)
                continue
            return None, str(e)
    return None, "max retries exceeded"


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def _discover_base_url(opener: urllib.request.OpenerDirector) -> tuple[str, str]:
    for base in CANDIDATE_BASE_URLS:
        for ep in CANDIDATE_ENDPOINTS:
            url = f"{base}{ep}"
            data, err = _safe_fetch(url, opener)
            if data is not None:
                return base, ep
    return "", ""


def _discover_search_endpoint(base_url: str, opener: urllib.request.OpenerDirector) -> str:
    for ep in CANDIDATE_ENDPOINTS:
        url = f"{base_url}{ep}?page=1&rows=5"
        data, err = _safe_fetch(url, opener)
        if data is not None:
            return ep
    return "/templates/search"


def _discover_template_fetch_path(base_url: str, opener: urllib.request.OpenerDirector) -> str:
    for path in TEMPLATE_FETCH_PATHS:
        url = f"{base_url}{path.format(1)}"
        data, err = _safe_fetch(url, opener)
        if data is not None:
            return path
    return TEMPLATE_FETCH_PATHS[0]


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------

def _extract_template_ids(data: Any, limit: int) -> list[TemplateInfo]:
    if isinstance(data, dict):
        results = data.get("results") or data.get("data") or data.get("workflows") or data.get("templates") or []
    elif isinstance(data, list):
        results = data
    else:
        return []

    ids: list[TemplateInfo] = []
    for item in results:
        if not isinstance(item, dict):
            continue
        tid = str(item.get("id") or item.get("workflowId") or item.get("templateId") or "")
        if not tid:
            continue
        name = str(item.get("name") or item.get("displayName") or item.get("title") or item.get("description", ""))
        cat = str(item.get("category") or item.get("categories") or "")
        if isinstance(cat, list):
            cat = ", ".join(cat)
        ids.append(TemplateInfo(id=tid, name=name, category=cat or None))
        if len(ids) >= limit:
            break
    return ids


def _normalize_workflow_response(data: Any) -> dict[str, Any] | None:
    if not isinstance(data, dict):
        return None

    # Shape A: {"id": ..., "name": ..., "workflow": {"nodes": [...], "connections": ...}}
    workflow_wrapper = data.get("workflow")
    if isinstance(workflow_wrapper, dict):
        inner = workflow_wrapper.get("workflow") or workflow_wrapper
        if isinstance(inner, dict) and "nodes" in inner:
            result = dict(inner)
            if "name" not in result:
                result["name"] = workflow_wrapper.get("name") or data.get("name", "unnamed")
            if "id" not in result:
                result["id"] = str(workflow_wrapper.get("id") or data.get("id", ""))
            return result
        if "nodes" in workflow_wrapper:
            result = dict(workflow_wrapper)
            if "name" not in result:
                result["name"] = data.get("name", "unnamed")
            if "id" not in result:
                result["id"] = str(data.get("id", ""))
            return result

    # Shape B: {"id": ..., "name": ..., "nodes": [...], "connections": ...}
    if "nodes" in data:
        result = dict(data)
        if "name" not in result:
            result["name"] = "unnamed"
        if "id" not in result:
            result["id"] = ""
        return result

    # Shape C: {"nodes": [...], "connections": ...} at top level
    if "nodes" in data:
        result = dict(data)
        result.setdefault("name", "unnamed")
        result.setdefault("id", "")
        return result

    return None


def _normalize_workflow_response_debug(data: Any) -> str:
    """Return a debug description of the response shape for error reporting."""
    if not isinstance(data, dict):
        return "not a dict"
    keys = list(data.keys())
    if "workflow" in data:
        inner_shape = type(data["workflow"]).__name__
        if isinstance(data["workflow"], dict):
            inner_keys = list(data["workflow"].keys())
            return f"workflow wrapper (keys: {keys}, inner keys: {inner_keys})"
        return f"workflow wrapper of type {inner_shape}"
    return f"top-level keys: {keys}"


def _slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = s.strip("-")
    return s[:80]


# ---------------------------------------------------------------------------
# Workflow validation
# ---------------------------------------------------------------------------

SUSPICIOUS_KEYS: set[str] = {
    "apikey", "api_key", "apisecret", "api_secret",
    "password", "passwd", "token", "accesstoken", "access_token",
    "authorization", "auth", "bearer", "jwt", "secret",
    "sshprivatekey", "ssh-private-key", "privatekey", "private_key",
    "clientid", "client_id", "clientsecret", "client_secret",
    "refreshtoken", "refresh_token", "sessionkey", "session_key",
}


def _validate_workflow(item: dict[str, Any]) -> tuple[bool, str | None]:
    """Return (is_valid, warning_message)."""
    nodes = item.get("nodes")
    if not isinstance(nodes, list) or len(nodes) == 0:
        return False, "no nodes"

    suspicious: set[str] = set()
    for node in nodes:
        params = node.get("parameters", {}) if isinstance(node, dict) else {}
        _scan_suspicious_keys(params, "", suspicious)

    if suspicious:
        return True, f"Suspicious key names found: {', '.join(sorted(suspicious))}; values not printed."

    return True, None


def _scan_suspicious_keys(obj: Any, prefix: str, acc: set[str]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            full_key = f"{prefix}.{k}" if prefix else k
            key_lower = k.lower()
            if any(sk in key_lower for sk in SUSPICIOUS_KEYS):
                acc.add(full_key)
            _scan_suspicious_keys(v, full_key, acc)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _scan_suspicious_keys(item, f"{prefix}[{i}]", acc)


# ---------------------------------------------------------------------------
# Search / list templates
# ---------------------------------------------------------------------------

def _build_search_url(
    base_url: str,
    search_endpoint: str,
    page: int,
    page_size: int,
    category: str | None,
    search: str | None,
) -> str:
    params: dict[str, str] = {
        "page": str(page),
        "rows": str(page_size),
    }
    if category:
        params["category"] = category
    if search:
        params["search"] = search
    qs = urllib.parse.urlencode(params)
    return f"{base_url}{search_endpoint}?{qs}"


def _search_templates(
    base_url: str,
    search_endpoint: str,
    limit: int,
    page_size: int,
    category: str | None,
    search: str | None,
    opener: urllib.request.OpenerDirector,
    sleep_seconds: float,
) -> list[TemplateInfo]:
    all_templates: list[TemplateInfo] = []
    page = 1
    while len(all_templates) < limit:
        url = _build_search_url(base_url, search_endpoint, page, page_size, category, search)
        data, err = _safe_fetch(url, opener)
        if data is None:
            break
        templates = _extract_template_ids(data, limit - len(all_templates))
        if not templates:
            break
        all_templates.extend(templates)
        if len(templates) < page_size:
            break
        page += 1
        time.sleep(sleep_seconds)
    return all_templates[:limit]


def _search_templates_dry_run(
    base_url: str,
    search_endpoint: str,
    limit: int,
    page_size: int,
    category: str | None,
    search: str | None,
    opener: urllib.request.OpenerDirector,
    sleep_seconds: float,
) -> list[TemplateInfo]:
    page = 1
    has_more = True
    all_templates: list[TemplateInfo] = []
    while has_more and len(all_templates) < limit:
        url = _build_search_url(base_url, search_endpoint, page, page_size, category, search)
        data, err = _safe_fetch(url, opener)
        if data is None:
            break
        templates = _extract_template_ids(data, limit)
        if not templates:
            break
        all_templates.extend(templates)
        has_more = len(templates) >= page_size
        page += 1
        time.sleep(sleep_seconds)
    return all_templates[:limit]


# ---------------------------------------------------------------------------
# Fetch single template
# ---------------------------------------------------------------------------

def _fetch_template(
    template_id: str,
    template_name: str,
    base_url: str,
    fetch_path: str,
    opener: urllib.request.OpenerDirector,
    sleep_seconds: float,
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    url = f"{base_url}{fetch_path.format(template_id)}"
    data, err = _safe_fetch(url, opener)
    if data is None:
        return None, err, url

    workflow = _normalize_workflow_response(data)
    if workflow is None:
        shape_desc = _normalize_workflow_response_debug(data)
        return None, f"unexpected response shape: {shape_desc}", url

    if "name" not in workflow or not workflow.get("name"):
        workflow["name"] = template_name or f"template-{template_id}"

    if "id" not in workflow or not workflow.get("id"):
        workflow["id"] = template_id

    return workflow, None, url


# ---------------------------------------------------------------------------
# Slug / filename helpers
# ---------------------------------------------------------------------------

def _make_filename(template_id: str, name: str) -> str:
    slug = _slugify(name)
    return f"{template_id}-{slug}.json" if slug else f"{template_id}.json"


def _workflow_trigger_types(nodes: list[Any]) -> list[str]:
    triggers: list[str] = []
    for node in nodes:
        if isinstance(node, dict):
            ntype = node.get("type", "")
            if "trigger" in ntype.lower() or ntype.endswith("Trigger") or "webhook" in ntype.lower():
                triggers.append(ntype)
    return triggers


# ---------------------------------------------------------------------------
# Download orchestration
# ---------------------------------------------------------------------------

def download_templates(
    output_dir: str,
    limit: int = DEFAULT_LIMIT,
    category: str | None = None,
    search: str | None = None,
    page_size: int = DEFAULT_PAGE_SIZE,
    sleep_seconds: float = DEFAULT_SLEEP_SECONDS,
    dry_run: bool = False,
    overwrite: bool = False,
    base_url: str | None = None,
) -> DownloadResult:
    opener = _build_opener()
    result = DownloadResult()

    out = Path(output_dir)
    workflows_dir = out / "workflows"

    # Discover endpoints
    if base_url:
        effective_base = base_url
        search_ep = _discover_search_endpoint(effective_base, opener)
        fetch_path = _discover_template_fetch_path(effective_base, opener)
    else:
        effective_base, initial_ep = _discover_base_url(opener)
        if not effective_base:
            raise RuntimeError(
                "No public JSON template endpoint discovered. "
                "Manual download or --base-url required."
            )
        search_ep = _discover_search_endpoint(effective_base, opener)
        fetch_path = _discover_template_fetch_path(effective_base, opener)

    # Search
    search_fn = _search_templates_dry_run if dry_run else _search_templates
    templates = search_fn(
        effective_base, search_ep, limit, page_size, category, search, opener, sleep_seconds
    )

    if not templates:
        if dry_run:
            result.warnings.append("No templates found matching criteria.")
        return result

    # In dry run, just report
    if dry_run:
        result.warnings.append(f"Dry-run: would download up to {len(templates)} templates.")
        for t in templates[:20]:
            result.warnings.append(f"  - [{t.id}] {t.name or '(no name)'}")
        if len(templates) > 20:
            result.warnings.append(f"  ... and {len(templates) - 20} more.")
        return result

    # Create output directories
    out.mkdir(parents=True, exist_ok=True)
    workflows_dir.mkdir(parents=True, exist_ok=True)

    # Download each template
    workflow_entries: list[dict[str, Any]] = []
    for ti in templates:
        wf_path = workflows_dir / _make_filename(ti.id, ti.name or "unnamed")

        if wf_path.exists() and not overwrite:
            result.skipped += 1
            continue

        wf, fetch_err, source_url = _fetch_template(
            ti.id, ti.name or "", effective_base, fetch_path, opener, sleep_seconds
        )

        if wf is None:
            result.failed.append({
                "id": ti.id,
                "name": ti.name,
                "reason": fetch_err or "unknown",
                "source_url": source_url,
            })
            continue

        is_valid, warning = _validate_workflow(wf)
        if not is_valid:
            result.failed.append({
                "id": ti.id,
                "name": ti.name,
                "reason": warning or "invalid",
                "source_url": source_url,
            })
            continue

        if warning:
            result.warnings.append(f"[{ti.id}] {ti.name}: {warning}")

        wf_path.write_text(json.dumps(wf, indent=2, ensure_ascii=False), encoding="utf-8")

        nodes = wf.get("nodes", [])
        trigger_types = _workflow_trigger_types(nodes)
        workflow_entries.append({
            "id": ti.id,
            "name": ti.name or wf.get("name", "unnamed"),
            "file": f"workflows/{wf_path.name}",
            "node_count": len(nodes),
            "trigger_types": trigger_types,
            "source_url": source_url or "",
            "category": ti.category or category or "",
        })

        time.sleep(sleep_seconds)

    result.workflows = workflow_entries
    return result


# ---------------------------------------------------------------------------
# Report / manifest writers
# ---------------------------------------------------------------------------

def _write_manifest(
    out: Path,
    category: str | None,
    search: str | None,
    base_url_used: str,
    limit: int,
    result: DownloadResult,
) -> None:
    manifest = {
        "source": "n8n_templates",
        "category": category,
        "search": search,
        "base_url_used": base_url_used,
        "limit": limit,
        "downloaded_count": len(result.workflows),
        "failed_count": len(result.failed),
        "skipped_count": result.skipped,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "workflows": result.workflows,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


def _write_failed(out: Path, result: DownloadResult) -> None:
    (out / "failed_downloads.json").write_text(
        json.dumps(result.failed, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _write_report(
    out: Path,
    category: str | None,
    search: str | None,
    base_url_used: str,
    search_endpoint: str,
    fetch_path: str,
    limit: int,
    page_size: int,
    sleep_seconds: float,
    dry_run: bool,
    overwrite: bool,
    result: DownloadResult,
    command_line: str,
) -> None:
    lines: list[str] = []
    lines.append("# n8n Template Download Report")
    lines.append("")
    lines.append(f"- **Command:** `{command_line}`")
    lines.append(f"- **Base URL:** {base_url_used}")
    lines.append(f"- **Search endpoint:** {search_endpoint}")
    lines.append(f"- **Fetch path:** {fetch_path}")
    lines.append(f"- **Category:** {category or '(none)'}")
    lines.append(f"- **Search query:** {search or '(none)'}")
    lines.append(f"- **Requested limit:** {limit}")
    lines.append(f"- **Page size:** {page_size}")
    lines.append(f"- **Sleep seconds:** {sleep_seconds}")
    lines.append(f"- **Dry run:** {dry_run}")
    lines.append(f"- **Overwrite:** {overwrite}")
    lines.append(f"- **Output directory:** `{out}`")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append(f"- **Downloaded:** {len(result.workflows)}")
    lines.append(f"- **Failed:** {len(result.failed)}")
    lines.append(f"- **Skipped (duplicates):** {result.skipped}")
    lines.append("")

    if result.workflows:
        lines.append("## Downloaded Workflows")
        lines.append("")
        for entry in result.workflows[:20]:
            lines.append(f"- [{entry['id']}] {entry['name']} ({entry['node_count']} nodes)")
        if len(result.workflows) > 20:
            lines.append(f"- ... and {len(result.workflows) - 20} more.")
        lines.append("")

    if result.failed:
        lines.append("## Failed Downloads")
        lines.append("")
        for f in result.failed:
            lines.append(f"- [{f['id']}] {f.get('name', '?')}: {f['reason']}")
        lines.append("")

    if result.warnings:
        lines.append("## Warnings")
        lines.append("")
        for w in result.warnings:
            lines.append(f"- {w}")
        lines.append("")

    (out / "download_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download public n8n workflow templates to build a local corpus.",
    )
    parser.add_argument("--category", type=str, default=None, help="Template category filter")
    parser.add_argument("--search", type=str, default=None, help="Free-text search query")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                        help=f"Max templates to download (default: {DEFAULT_LIMIT})")
    parser.add_argument("--output-dir", type=str, default="examples/corpus/downloaded",
                        help="Output directory")
    parser.add_argument("--page-size", type=int, default=DEFAULT_PAGE_SIZE,
                        help=f"Page size for search (default: {DEFAULT_PAGE_SIZE})")
    parser.add_argument("--sleep-seconds", type=float, default=DEFAULT_SLEEP_SECONDS,
                        help=f"Delay between HTTP calls (default: {DEFAULT_SLEEP_SECONDS})")
    parser.add_argument("--dry-run", action="store_true", help="Discover and list templates without downloading")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing workflow files")
    parser.add_argument("--base-url", type=str, default=None, help="Override base URL for API discovery")
    parser.add_argument("--allow-large", action="store_true", help=f"Allow limits above {HARD_LIMIT_CAP}")
    return parser.parse_args(argv)


def _confirm_cap(limit: int, allow_large: bool) -> int:
    if limit > HARD_LIMIT_CAP and not allow_large:
        print(
            f"Limit {limit} exceeds hard cap of {HARD_LIMIT_CAP}. "
            f"Capping to {HARD_LIMIT_CAP}. Use --allow-large to override.",
            file=sys.stderr,
        )
        return HARD_LIMIT_CAP
    return limit


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    limit = _confirm_cap(args.limit, args.allow_large)

    if not args.category and not args.search:
        pass

    download_result = download_templates(
        output_dir=args.output_dir,
        limit=limit,
        category=args.category,
        search=args.search,
        page_size=args.page_size,
        sleep_seconds=args.sleep_seconds,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
        base_url=args.base_url,
    )

    if args.dry_run:
        print(f"Dry-run: {len(download_result.warnings)}")
        for w in download_result.warnings:
            print(f"  {w}")
        return 0

    # Write output files
    out = Path(args.output_dir)
    base_url_used = args.base_url or "discovered"
    cmdl = " ".join(sys.argv[1:]) if argv is None else " ".join(argv)

    _write_manifest(out, args.category, args.search, base_url_used, limit, download_result)
    _write_failed(out, download_result)
    _write_report(
        out,
        args.category,
        args.search,
        base_url_used,
        "",
        "",
        limit,
        args.page_size,
        args.sleep_seconds,
        args.dry_run,
        args.overwrite,
        download_result,
        cmdl,
    )

    print(f"Downloaded: {len(download_result.workflows)}")
    print(f"Failed: {len(download_result.failed)}")
    print(f"Skipped (duplicates): {download_result.skipped}")
    print(f"Output: {out.resolve()}")

    if download_result.failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
