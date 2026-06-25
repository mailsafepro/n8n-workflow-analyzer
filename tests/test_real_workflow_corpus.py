from __future__ import annotations

from pathlib import Path

import pytest

from n8n_cost_analyzer.parser import parse_workflow_directory
from n8n_cost_analyzer.rules import analyze_workflows
from n8n_cost_analyzer.scoring import (
    compute_node_inventory,
    score_analysis,
)

CORPUS = Path(__file__).parent.parent / "examples" / "real_workflows"


def test_corpus_exists() -> None:
    if not CORPUS.is_dir():
        pytest.skip("Real workflow corpus not available")


def test_corpus_parses_at_least_one_workflow() -> None:
    if not CORPUS.is_dir():
        pytest.skip("Real workflow corpus not available")
    workflows = parse_workflow_directory(CORPUS)
    assert len(workflows) >= 1


def test_corpus_no_unnamed_workflow() -> None:
    if not CORPUS.is_dir():
        pytest.skip("Real workflow corpus not available")
    workflows = parse_workflow_directory(CORPUS)
    unnamed = [wf for wf in workflows if wf.name == "Unnamed Workflow"]
    assert len(unnamed) == 0, f"{len(unnamed)} workflow(s) still named 'Unnamed Workflow'"


def test_corpus_unknown_node_types_below_threshold() -> None:
    if not CORPUS.is_dir():
        pytest.skip("Real workflow corpus not available")
    workflows = parse_workflow_directory(CORPUS)
    reports = analyze_workflows(workflows)
    result = score_analysis(reports)
    ni = compute_node_inventory(result.reports, workflows)
    assert len(ni.unknown_node_types) <= 20, (
        f"Unknown node types: {len(ni.unknown_node_types)} "
        f"(threshold: 20): {sorted(ni.unknown_node_types)}"
    )


def test_corpus_has_node_category_counts() -> None:
    if not CORPUS.is_dir():
        pytest.skip("Real workflow corpus not available")
    workflows = parse_workflow_directory(CORPUS)
    reports = analyze_workflows(workflows)
    result = score_analysis(reports)
    ni = compute_node_inventory(result.reports, workflows)
    assert len(ni.node_category_counts) > 0
    assert ni.node_category_counts.get("unknown", 0) <= 20
