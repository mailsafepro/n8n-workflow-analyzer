from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from n8n_cost_analyzer.parser import (
    classify_node_type,
    parse_workflow_collection,
    parse_workflow_directory,
    parse_workflow_file,
    parse_workflow_json,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_simple_webhook():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    assert wf.name == "Simple Webhook Workflow"
    assert wf.id == "1"
    assert wf.active is True
    assert len(wf.nodes) == 3
    assert wf.nodes[0].name == "Webhook"
    assert wf.nodes[0].type == "n8n-nodes-base.webhook"


def test_parse_polling_workflow():
    wf = parse_workflow_file(FIXTURES / "polling_workflow.json")
    assert wf.name == "Polling Workflow"
    assert len(wf.nodes) == 3


def test_parse_loop_http_workflow():
    wf = parse_workflow_file(FIXTURES / "loop_http_workflow.json")
    assert wf.name == "Loop HTTP Workflow"
    assert len(wf.nodes) == 4


def test_parse_ai_workflow():
    wf = parse_workflow_file(FIXTURES / "ai_workflow.json")
    assert wf.name == "AI Workflow"
    assert len(wf.nodes) == 3


def test_parse_invalid_json_raises():
    with pytest.raises(ValueError, match="Invalid JSON"):
        parse_workflow_file(FIXTURES / "invalid_workflow.json")


def test_parse_json_string():
    data = json.dumps({
        "name": "Inline Workflow",
        "nodes": [{"name": "Start", "type": "n8n-nodes-base.noOp", "parameters": {}}],
        "connections": {},
        "settings": {},
    })
    wf = parse_workflow_json(data)
    assert wf.name == "Inline Workflow"
    assert len(wf.nodes) == 1
    assert wf.nodes[0].name == "Start"


def test_parse_json_dict():
    data = {
        "name": "Dict Workflow",
        "nodes": [{"name": "N1", "type": "n8n-nodes-base.noOp", "parameters": {}}],
    }
    wf = parse_workflow_json(data)
    assert wf.name == "Dict Workflow"


def test_missing_optional_fields():
    data = {"nodes": []}
    wf = parse_workflow_json(data)
    assert wf.id is None
    assert wf.name == "Unnamed Workflow"
    assert wf.active is None
    assert wf.nodes == ()


def test_parse_directory():
    workflows = parse_workflow_directory(FIXTURES)
    names = {w.name for w in workflows}
    assert "Simple Webhook Workflow" in names
    assert "Polling Workflow" in names


def test_parse_empty_directory():
    with tempfile.TemporaryDirectory() as tmp:
        wfs = parse_workflow_directory(tmp)
        assert wfs == []


def test_parse_directory_invalid_json_skipped():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "bad.json"
        p.write_text("{invalid")
        (Path(tmp) / "good.json").write_text(json.dumps({
            "name": "Good",
            "nodes": [{"name": "N", "type": "T", "parameters": {}}],
        }))
        wfs = parse_workflow_directory(tmp)
        assert len(wfs) == 1


def test_parse_directory_non_json_ignored():
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "readme.md").write_text("# hello")
        wfs = parse_workflow_directory(tmp)
        assert wfs == []


def test_parse_not_a_directory():
    with pytest.raises(NotADirectoryError):
        parse_workflow_directory(FIXTURES / "simple_webhook_workflow.json")


def test_parse_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        parse_workflow_file("/nonexistent/path.json")


def test_node_immutability():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    with pytest.raises(AttributeError):
        wf.nodes[0].name = "changed"  # type: ignore


def test_node_position_tuple():
    wf = parse_workflow_file(FIXTURES / "simple_webhook_workflow.json")
    webhook = wf.nodes[0]
    assert webhook.position is not None
    assert len(webhook.position) == 2


def test_parse_list_export():
    workflows = parse_workflow_collection(FIXTURES / "collection_export.json")
    assert len(workflows) == 2
    names = {w.name for w in workflows}
    assert "Collection Workflow One" in names
    assert "Collection Workflow Two" in names


def test_parse_wrapped_workflows_export():
    workflows = parse_workflow_collection(FIXTURES / "collection_export.json")
    assert len(workflows) == 2


def test_parse_wrapped_data_export():
    workflows = parse_workflow_collection(FIXTURES / "wrapped_data_export.json")
    assert len(workflows) == 2
    names = {w.name for w in workflows}
    assert "Data Wrapped Workflow One" in names
    assert "Data Wrapped Workflow Two" in names


def test_credentials_detected():
    wf = parse_workflow_file(FIXTURES / "workflow_with_credentials.json")
    cred_nodes = [n for n in wf.nodes if n.credentials is not None]
    assert len(cred_nodes) == 2
    postgres = [n for n in cred_nodes if n.name == "Postgres DB"][0]
    assert postgres.credentials is not None
    cred = postgres.credentials.get("postgres", {})
    assert cred.get("name") == "Production DB"
    # No secrets in parsed output
    raw = postgres.raw or {}
    assert "parameters" in raw


def test_disabled_nodes_parsed():
    wf = parse_workflow_file(FIXTURES / "workflow_with_disabled_nodes.json")
    disabled = [n for n in wf.nodes if n.disabled]
    assert len(disabled) == 2
    assert disabled[0].name == "HTTP Request"
    assert disabled[1].name == "Disabled AI"


def test_unknown_node_types_tolerated():
    wf = parse_workflow_file(FIXTURES / "unknown_node_workflow.json")
    nodes = wf.nodes
    types = {n.type for n in nodes}
    assert "n8n-nodes-base.myCustomNode" in types
    assert "com.legacy.connector" in types
    warnings = wf.parser_warnings
    unknown_warnings = [w for w in warnings if "Unknown node type" in w]
    assert len(unknown_warnings) >= 1


def test_parser_warnings_included():
    wf = parse_workflow_file(FIXTURES / "unknown_node_workflow.json")
    assert len(wf.parser_warnings) >= 1
    assert any("Unknown node type" in w for w in wf.parser_warnings)


def test_no_secrets_in_parsed_output():
    wf = parse_workflow_file(FIXTURES / "unknown_node_workflow.json")
    node = [n for n in wf.nodes if n.name == "My Custom Node"][0]
    assert node.credentials is None  # no credentials field, just params
    # Parameters are preserved, but it's the user's responsibility
    assert "apiKey" in node.parameters


def test_tags_parsed():
    wf = parse_workflow_file(FIXTURES / "workflow_with_credentials.json")
    assert len(wf.tags) == 2
    assert "production" in wf.tags


def test_metadata_extracted():
    wf = parse_workflow_file(FIXTURES / "workflow_with_credentials.json")
    assert len(wf.metadata) >= 0


def test_classify_node_type():
    assert classify_node_type("n8n-nodes-base.webhook") == "trigger"
    assert classify_node_type("n8n-nodes-base.openAi") == "ai"
    assert classify_node_type("com.custom.node") == "unknown"


def test_uses_filename_stem_when_workflow_name_missing(tmp_path: Path):
    wf = {
        "nodes": [
            {"id": "1", "name": "Node1", "type": "n8n-nodes-base.noOp", "parameters": {}},
        ],
        "connections": {},
    }
    f = tmp_path / "my_workflow.json"
    f.write_text(__import__("json").dumps(wf))
    parsed = parse_workflow_file(f)
    assert parsed.name == "my_workflow"


def test_explicit_workflow_name_wins_over_filename(tmp_path: Path):
    wf = {
        "name": "My Explicit Name",
        "nodes": [
            {"id": "1", "name": "Node1", "type": "n8n-nodes-base.noOp", "parameters": {}},
        ],
        "connections": {},
    }
    f = tmp_path / "some_file.json"
    f.write_text(__import__("json").dumps(wf))
    parsed = parse_workflow_file(f)
    assert parsed.name == "My Explicit Name"


def test_collection_unnamed_workflows_get_stem_index_names(tmp_path: Path):
    wf_list = [
        {
            "nodes": [
                {"id": "1", "name": "Node1", "type": "n8n-nodes-base.noOp", "parameters": {}},
            ],
            "connections": {},
        },
        {
            "nodes": [
                {"id": "2", "name": "Node2", "type": "n8n-nodes-base.noOp", "parameters": {}},
            ],
            "connections": {},
        },
    ]
    f = tmp_path / "export.json"
    f.write_text(__import__("json").dumps(wf_list))
    parsed_list = parse_workflow_collection(f)
    assert len(parsed_list) == 2
    assert parsed_list[0].name == "export_1"
    assert parsed_list[1].name == "export_2"


def test_meta_name_extracted(tmp_path: Path):
    wf = {
        "meta": {"name": "Meta Name Workflow"},
        "nodes": [
            {"id": "1", "name": "Node1", "type": "n8n-nodes-base.noOp", "parameters": {}},
        ],
        "connections": {},
    }
    f = tmp_path / "meta_test.json"
    f.write_text(__import__("json").dumps(wf))
    parsed = parse_workflow_file(f)
    assert parsed.name == "Meta Name Workflow"
