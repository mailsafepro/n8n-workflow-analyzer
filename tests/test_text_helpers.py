from __future__ import annotations

from n8n_cost_analyzer.text_helpers import pluralize


def test_pluralize_singular():
    assert pluralize(1, "workflow") == "1 workflow"


def test_pluralize_regular():
    assert pluralize(2, "workflow") == "2 workflows"
    assert pluralize(5, "workflow") == "5 workflows"


def test_pluralize_custom_plural():
    assert pluralize(1, "finding", "findings") == "1 finding"
    assert pluralize(3, "finding", "findings") == "3 findings"


def test_pluralize_zero():
    assert pluralize(0, "workflow") == "0 workflows"


def test_pluralize_singular_with_es():
    assert pluralize(1, "node") == "1 node"
    assert pluralize(2, "node") == "2 nodes"
    assert pluralize(1, "reference") == "1 reference"
    assert pluralize(3, "reference") == "3 references"
