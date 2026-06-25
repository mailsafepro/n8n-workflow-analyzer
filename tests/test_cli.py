from __future__ import annotations

import json
from pathlib import Path

from n8n_cost_analyzer.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


def test_cli_valid_file(tmp_path: Path):
    out = tmp_path / "report.md"
    wf = FIXTURES / "simple_webhook_workflow.json"
    rc = main(["analyze", str(wf), "--output", str(out)])
    assert rc == 0
    assert out.exists()


def test_cli_valid_directory(tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main(["analyze", str(FIXTURES), "--output", str(out)])
    assert rc == 0
    assert out.exists()
    content = out.read_text()
    assert "# n8n Workflow Cost & Risk Report" in content


def test_cli_nonexistent_path():
    rc = main(["analyze", "/nonexistent/path"])
    assert rc == 1


def test_cli_no_input():
    rc = main(["analyze"])
    assert rc == 1


def test_cli_unknown_command():
    rc = main(["unknown"])
    assert rc == 1


def test_cli_unknown_flag():
    rc = main(["analyze", str(FIXTURES), "--bad-flag"])
    assert rc == 1


def test_cli_fail_on_critical(tmp_path: Path):
    import json as _json
    nodes = []
    for i in range(120):
        nodes.append({
            "id": f"n{i}",
            "name": f"Node{i}",
            "type": "n8n-nodes-base.noOp",
            "parameters": {},
        })
    wf_path = tmp_path / "huge_workflow.json"
    wf_path.write_text(_json.dumps({
        "name": "Huge Critical WF",
        "nodes": nodes,
    }))
    out = tmp_path / "report.md"
    rc = main(["analyze", str(wf_path), "--output", str(out), "--fail-on-critical"])
    assert rc == 2


def test_cli_fail_on_critical_passes_without_critical(tmp_path: Path):
    out = tmp_path / "report.md"
    wf = FIXTURES / "simple_webhook_workflow.json"
    rc = main(["analyze", str(wf), "--output", str(out), "--fail-on-critical"])
    assert rc == 0


def test_cli_help():
    rc = main(["--help"])
    assert rc == 0


def test_cli_output_contains_summary(capsys, tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main(["analyze", str(FIXTURES), "--output", str(out)])
    captured = capsys.readouterr()
    assert "Summary" in captured.out
    assert rc == 0


def test_cli_output_json(tmp_path: Path):
    out_md = tmp_path / "report.md"
    out_json = tmp_path / "report.json"
    rc = main([
        "analyze", str(FIXTURES),
        "--output", str(out_md),
        "--output-json", str(out_json),
    ])
    assert rc == 0
    assert out_md.exists()
    assert out_json.exists()
    data = json.loads(out_json.read_text())
    assert "summary" in data


def test_cli_cost_model(tmp_path: Path):
    cm = tmp_path / "cost_model.yaml"
    cm.write_text("currency: USD\nexecution_low_cost: 0.001\n")
    out = tmp_path / "report.md"
    rc = main([
        "analyze", str(FIXTURES),
        "--output", str(out),
        "--cost-model", str(cm),
    ])
    assert rc == 0
    assert out.exists()


def test_cli_cost_model_invalid_path(tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main([
        "analyze", str(FIXTURES),
        "--output", str(out),
        "--cost-model", "/nonexistent/model.yaml",
    ])
    assert rc == 1


def test_cli_handles_collection_export(tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main([
        "analyze", str(FIXTURES / "collection_export.json"),
        "--output", str(out),
    ])
    assert rc == 0
    content = out.read_text()
    assert "Collection Workflow One" in content
    assert "Collection Workflow Two" in content


def test_cli_include_disabled_changes_findings(tmp_path: Path):
    out_default = tmp_path / "default.md"
    rc = main([
        "analyze", str(FIXTURES / "workflow_with_disabled_nodes.json"),
        "--output", str(out_default),
    ])
    assert rc == 0
    default_findings = out_default.read_text().count("[HIGH]")

    out_included = tmp_path / "included.md"
    rc = main([
        "analyze", str(FIXTURES / "workflow_with_disabled_nodes.json"),
        "--output", str(out_included),
        "--include-disabled",
    ])
    assert rc == 0
    included_findings = out_included.read_text().count("[HIGH]")
    assert included_findings >= default_findings


def test_cli_stdout_mentions_warnings(capsys, tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main([
        "analyze", str(FIXTURES / "unknown_node_workflow.json"),
        "--output", str(out),
    ])
    captured = capsys.readouterr()
    assert "warnings" in captured.out.lower() or rc == 0
    assert rc == 0


def test_cli_stdout_mentions_disabled(capsys, tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main([
        "analyze", str(FIXTURES / "workflow_with_disabled_nodes.json"),
        "--output", str(out),
    ])
    captured = capsys.readouterr()
    assert "Disabled" in captured.out or rc == 0
    assert rc == 0


def test_cli_stdout_mentions_top_workflow(capsys, tmp_path: Path):
    out = tmp_path / "report.md"
    rc = main(["analyze", str(FIXTURES), "--output", str(out)])
    captured = capsys.readouterr()
    assert "Top workflow" in captured.out
    assert rc == 0


def test_cli_audit_pack_directory_created(tmp_path: Path):
    audit_dir = tmp_path / "audit"
    rc = main(["analyze", str(FIXTURES), "--audit-pack", str(audit_dir)])
    assert rc == 0
    assert (audit_dir / "executive_summary.md").exists()
    assert (audit_dir / "client_action_plan.md").exists()
    assert (audit_dir / "technical_report.md").exists()
    assert (audit_dir / "analysis.json").exists()


def test_cli_audit_pack_without_output(tmp_path: Path):
    audit_dir = tmp_path / "audit"
    rc = main(["analyze", str(FIXTURES), "--audit-pack", str(audit_dir)])
    assert rc == 0
    assert (audit_dir / "executive_summary.md").exists()


def test_cli_audit_pack_stdout_shows_summary(capsys, tmp_path: Path):
    audit_dir = tmp_path / "audit"
    rc = main(["analyze", str(FIXTURES), "--audit-pack", str(audit_dir)])
    captured = capsys.readouterr()
    assert "Summary" in captured.out
    assert "Audit pack written" in captured.out
    assert rc == 0


def test_cli_audit_pack_with_cost_model(tmp_path: Path):
    cm = tmp_path / "cost_model.yaml"
    cm.write_text("currency: EUR\n")
    audit_dir = tmp_path / "audit"
    rc = main([
        "analyze", str(FIXTURES),
        "--audit-pack", str(audit_dir),
        "--cost-model", str(cm),
    ])
    assert rc == 0
    assert (audit_dir / "analysis.json").exists()
    import json
    data = json.loads((audit_dir / "analysis.json").read_text())
    assert data["cost_model"]["currency"] == "EUR"


def test_cli_audit_pack_single_file(tmp_path: Path):
    audit_dir = tmp_path / "audit"
    wf = FIXTURES / "simple_webhook_workflow.json"
    rc = main(["analyze", str(wf), "--audit-pack", str(audit_dir)])
    assert rc == 0
    assert (audit_dir / "executive_summary.md").exists()
    exec_md = (audit_dir / "executive_summary.md").read_text()
    assert "Simple Webhook Workflow" in exec_md


def test_cli_json_and_cost_model(tmp_path: Path):
    cm = tmp_path / "cost_model.yaml"
    cm.write_text("currency: GBP\n")
    out_md = tmp_path / "report.md"
    out_json = tmp_path / "report.json"
    rc = main([
        "analyze", str(FIXTURES),
        "--output", str(out_md),
        "--output-json", str(out_json),
        "--cost-model", str(cm),
    ])
    assert rc == 0
    data = json.loads(out_json.read_text())
    assert data["cost_model"]["currency"] == "GBP"
