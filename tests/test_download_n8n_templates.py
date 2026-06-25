from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from scripts.download_n8n_templates import (
    _build_search_url,
    _extract_template_ids,
    _make_filename,
    _normalize_workflow_response,
    _normalize_workflow_response_debug,
    _scan_suspicious_keys,
    _slugify,
    _validate_workflow,
    _workflow_trigger_types,
    download_templates,
    main,
)

FIXTURES = Path(__file__).parent / "fixtures"


# ---------------------------------------------------------------------------
# slugify
# ---------------------------------------------------------------------------

def test_slugify_basic():
    assert _slugify("Hello World") == "hello-world"


def test_slugify_special_chars():
    assert _slugify("AI/ML & NLP 2024!") == "aiml-nlp-2024"


def test_slugify_max_length():
    long_name = "a" * 200
    assert len(_slugify(long_name)) == 80


def test_slugify_empty():
    assert _slugify("") == ""


# ---------------------------------------------------------------------------
# normalize
# ---------------------------------------------------------------------------

def test_normalize_flat_workflow_response():
    data = {"nodes": [{"name": "n1"}], "connections": {}, "name": "test", "id": "123"}
    result = _normalize_workflow_response(data)
    assert result is not None
    assert result["name"] == "test"
    assert result["id"] == "123"
    assert len(result["nodes"]) == 1


def test_normalize_workflow_response_shape_a():
    data = {
        "id": 999,
        "name": "Wrapper",
        "workflow": {"nodes": [{"name": "n1"}], "connections": {}},
    }
    result = _normalize_workflow_response(data)
    assert result is not None
    assert "nodes" in result
    assert len(result["nodes"]) == 1
    assert result.get("name") == "Wrapper"


def test_normalize_workflow_response_shape_b():
    data = {
        "workflow": {
            "id": 456,
            "name": "Inner",
            "workflow": {"nodes": [{"name": "x"}], "connections": {}},
        }
    }
    result = _normalize_workflow_response(data)
    assert result is not None
    assert "nodes" in result
    assert result["name"] == "Inner"


def test_normalize_workflow_response_no_nodes():
    data = {"id": "1", "name": "empty"}
    result = _normalize_workflow_response(data)
    assert result is None


def test_normalize_workflow_response_none():
    assert _normalize_workflow_response(None) is None
    assert _normalize_workflow_response([]) is None


def test_normalize_workflow_response_debug():
    data = {"id": 1, "name": "x", "workflow": {"nodes": []}}
    desc = _normalize_workflow_response_debug(data)
    assert "workflow wrapper" in desc


# ---------------------------------------------------------------------------
# extract template ids
# ---------------------------------------------------------------------------

def test_extract_template_ids_from_search_response():
    data = {
        "results": [
            {"id": 1, "name": "WF1", "category": "ai"},
            {"id": 2, "name": "WF2"},
            {"id": 3, "name": "WF3", "category": "automation"},
        ]
    }
    ids = _extract_template_ids(data, 10)
    assert len(ids) == 3
    assert ids[0].id == "1"
    assert ids[0].name == "WF1"
    assert ids[0].category == "ai"


def test_extract_template_ids_respects_limit():
    data = {"results": [{"id": i, "name": f"WF{i}"} for i in range(100)]}
    ids = _extract_template_ids(data, 5)
    assert len(ids) == 5


def test_extract_template_ids_empty():
    assert _extract_template_ids({}, 10) == []
    assert _extract_template_ids([], 10) == []


def test_extract_template_ids_list_response():
    data = [
        {"id": "a", "name": "WF A"},
        {"id": "b", "name": "WF B"},
    ]
    ids = _extract_template_ids(data, 10)
    assert len(ids) == 2


def test_extract_template_ids_alternative_keys():
    data = {
        "data": [
            {"workflowId": "42", "displayName": "My WF"},
        ]
    }
    ids = _extract_template_ids(data, 10)
    assert len(ids) == 1
    assert ids[0].id == "42"
    assert ids[0].name == "My WF"


# ---------------------------------------------------------------------------
# workflow validation
# ---------------------------------------------------------------------------

def test_validate_workflow_passes():
    item = {"nodes": [{"name": "n1", "type": "test", "parameters": {}}], "connections": {}}
    valid, warning = _validate_workflow(item)
    assert valid is True
    assert warning is None


def test_validate_workflow_no_nodes():
    item = {"nodes": []}
    valid, warning = _validate_workflow(item)
    assert valid is False
    assert warning == "no nodes"


def test_validate_workflow_missing_nodes_key():
    item = {"connections": {}}
    valid, warning = _validate_workflow(item)
    assert valid is False


def test_validate_workflow_suspicious_keys():
    item = {
        "nodes": [
            {
                "name": "n1",
                "type": "test",
                "parameters": {"apiKey": "sk-secret-123"},
            }
        ]
    }
    valid, warning = _validate_workflow(item)
    assert valid is True
    assert warning is not None
    assert "apiKey" in warning
    assert "sk-secret-123" not in warning


def test_no_values_printed_for_suspicious_keys():
    acc: set[str] = set()
    _scan_suspicious_keys({"apiKey": "super-secret-value", "safe": "hello"}, "", acc)
    assert len(acc) >= 1
    assert all("super-secret-value" not in k for k in acc)


# ---------------------------------------------------------------------------
# trigger types
# ---------------------------------------------------------------------------

def test_workflow_trigger_types():
    nodes = [
        {"type": "n8n-nodes-base.webhook"},
        {"type": "n8n-nodes-base.noOp"},
        {"type": "n8n-nodes-base.scheduleTrigger"},
    ]
    triggers = _workflow_trigger_types(nodes)
    assert "n8n-nodes-base.webhook" in triggers
    assert "n8n-nodes-base.scheduleTrigger" in triggers
    assert "n8n-nodes-base.noOp" not in triggers


# ---------------------------------------------------------------------------
# filename helpers
# ---------------------------------------------------------------------------

def test_make_filename():
    assert _make_filename("123", "Hello World").startswith("123-hello-world")
    assert _make_filename("123", "Hello World").endswith(".json")


def test_make_filename_handles_empty_name():
    name = _make_filename("42", "")
    assert "42" in name


# ---------------------------------------------------------------------------
# build search url
# ---------------------------------------------------------------------------

def test_build_search_url():
    url = _build_search_url("https://api.n8n.io", "/templates/search", 1, 20, "ai", None)
    assert "page=1" in url
    assert "rows=20" in url
    assert "category=ai" in url
    assert "search=" not in url


def test_build_search_url_with_search():
    url = _build_search_url("https://api.n8n.io", "/templates/search", 2, 10, None, "gmail openai")
    assert "page=2" in url
    assert "rows=10" in url
    assert "search=gmail+openai" in url or "search=gmail%20openai" in url


# ---------------------------------------------------------------------------
# download orchestration with mocked HTTP
# ---------------------------------------------------------------------------

def _make_search_response(count: int = 5) -> dict:
    return {
        "results": [
            {"id": i, "name": f"Template {i}", "category": "ai"} for i in range(1, count + 1)
        ]
    }


def _make_template_response(tid: int) -> dict:
    return {
        "id": tid,
        "name": f"Template {tid}",
        "nodes": [
            {"name": "Webhook", "type": "n8n-nodes-base.webhook", "parameters": {}},
            {"name": "Set", "type": "n8n-nodes-base.set", "parameters": {}},
        ],
        "connections": {"Webhook": {"main": [[{"node": "Set", "type": "main", "index": 0}]]}},
    }


def _make_safe_fetch(search_data: Any, template_map: dict[str, Any]) -> Any:
    """Return a _safe_fetch replacement that returns canned data by URL."""
    def _mock(url: str, opener: Any) -> tuple[Any, str | None]:
        if "search" in url.lower():
            return search_data, None
        for tid, data in template_map.items():
            if str(tid) in url:
                return data, None
        return None, "HTTP 404"
    return _mock


def _patch_discovery(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "scripts.download_n8n_templates._discover_base_url",
        lambda _: ("https://api.n8n.io", "/templates/search"),
    )
    monkeypatch.setattr(
        "scripts.download_n8n_templates._discover_search_endpoint",
        lambda _, __: "/templates/search",
    )
    monkeypatch.setattr(
        "scripts.download_n8n_templates._discover_template_fetch_path",
        lambda _, __: "/workflows/templates/{}",
    )


# ---------------------------------------------------------------------------
# integration-like tests with mocked HTTP
# ---------------------------------------------------------------------------

def test_download_with_mocked_http(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    temps = {"1": _make_template_response(1), "2": _make_template_response(2)}
    monkeypatch.setattr(
        "scripts.download_n8n_templates._safe_fetch",
        _make_safe_fetch(_make_search_response(2), temps),
    )
    _patch_discovery(monkeypatch)

    result = download_templates(
        output_dir=str(tmp_path),
        limit=2,
        category="ai",
        page_size=5,
        sleep_seconds=0.01,
        overwrite=False,
        base_url="https://api.n8n.io",
    )

    assert len(result.workflows) == 2
    assert len(result.failed) == 0
    assert (tmp_path / "workflows").exists()
    assert len(list((tmp_path / "workflows").iterdir())) == 2


def test_failed_downloads_written(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "scripts.download_n8n_templates._safe_fetch",
        _make_safe_fetch(_make_search_response(2), {}),
    )
    _patch_discovery(monkeypatch)

    result = download_templates(
        output_dir=str(tmp_path),
        limit=2,
        category="ai",
        page_size=5,
        sleep_seconds=0.01,
        base_url="https://api.n8n.io",
    )

    assert len(result.failed) == 2


def test_manifest_written(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "scripts.download_n8n_templates._safe_fetch",
        _make_safe_fetch(_make_search_response(1), {"1": _make_template_response(1)}),
    )
    _patch_discovery(monkeypatch)

    result = download_templates(
        output_dir=str(tmp_path),
        limit=1,
        category="ai",
        page_size=5,
        sleep_seconds=0.01,
        base_url="https://api.n8n.io",
    )

    from scripts.download_n8n_templates import _write_manifest
    _write_manifest(tmp_path, "ai", None, "https://api.n8n.io", 1, result)

    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert manifest["source"] == "n8n_templates"
    assert manifest["downloaded_count"] == 1
    assert len(manifest["workflows"]) == 1


def test_dry_run_does_not_write_workflows(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "scripts.download_n8n_templates._safe_fetch",
        _make_safe_fetch(_make_search_response(3), {}),
    )
    _patch_discovery(monkeypatch)

    result = download_templates(
        output_dir=str(tmp_path),
        limit=3,
        category="ai",
        page_size=5,
        sleep_seconds=0.01,
        dry_run=True,
        base_url="https://api.n8n.io",
    )

    assert len(result.workflows) == 0
    assert not (tmp_path / "workflows").exists() or len(list((tmp_path / "workflows").iterdir())) == 0


def test_limit_cap_enforced(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("scripts.download_n8n_templates.HARD_LIMIT_CAP", 10)
    from scripts.download_n8n_templates import _confirm_cap
    assert _confirm_cap(50, allow_large=False) == 10
    assert _confirm_cap(5, allow_large=False) == 5
    assert _confirm_cap(50, allow_large=True) == 50


def test_dedup_skips_existing(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    (tmp_path / "workflows").mkdir(parents=True, exist_ok=True)
    (tmp_path / "workflows" / "1-template-1.json").write_text("{}", encoding="utf-8")

    temps = {"1": _make_template_response(1), "2": _make_template_response(2)}
    monkeypatch.setattr(
        "scripts.download_n8n_templates._safe_fetch",
        _make_safe_fetch(_make_search_response(2), temps),
    )
    _patch_discovery(monkeypatch)

    result = download_templates(
        output_dir=str(tmp_path),
        limit=2,
        category="ai",
        page_size=5,
        sleep_seconds=0.01,
        base_url="https://api.n8n.io",
    )

    assert result.skipped == 1
    assert len(result.workflows) == 1


def test_cli_success_with_fake_client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    temps = {"1": _make_template_response(1), "2": _make_template_response(2)}
    monkeypatch.setattr(
        "scripts.download_n8n_templates._safe_fetch",
        _make_safe_fetch(_make_search_response(2), temps),
    )
    _patch_discovery(monkeypatch)

    rc = main([
        "--category", "ai",
        "--limit", "2",
        "--output-dir", str(tmp_path),
        "--sleep-seconds", "0.01",
        "--base-url", "https://api.n8n.io",
    ])

    assert rc == 0
    assert (tmp_path / "manifest.json").exists()
    assert (tmp_path / "failed_downloads.json").exists()
    assert (tmp_path / "download_report.md").exists()


def test_cli_fails_gracefully_when_no_endpoint_works(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def _discover_none(_opener: Any) -> tuple[str, str]:
        return "", ""

    monkeypatch.setattr("scripts.download_n8n_templates._discover_base_url", _discover_none)

    with pytest.raises(RuntimeError, match="No public JSON template endpoint discovered"):
        download_templates(
            output_dir=str(tmp_path),
            limit=2,
            category="ai",
            page_size=5,
            sleep_seconds=0.01,
        )


def test_cli_allow_large_bypasses_cap(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("scripts.download_n8n_templates.HARD_LIMIT_CAP", 10)
    from scripts.download_n8n_templates import _confirm_cap
    assert _confirm_cap(200, allow_large=True) == 200
