from __future__ import annotations

import json
from pathlib import Path

import pytest

from n8n_cost_analyzer.cost_model import load_cost_model


def test_load_defaults_when_none():
    cm = load_cost_model(None)
    assert cm.currency == "EUR"
    assert cm.execution_low_cost == 0.0001
    assert cm.execution_medium_cost == 0.001
    assert cm.execution_high_cost == 0.01
    assert cm.ai_node_multiplier == 5.0
    assert cm.http_loop_multiplier == 3.0
    assert cm.polling_multiplier == 2.0
    assert cm.critical_risk_multiplier == 4.0


def test_load_yaml_example(tmp_path: Path):
    yaml_path = tmp_path / "cost_model.yaml"
    yaml_path.write_text("""
currency: USD
execution_low_cost: 0.001
execution_medium_cost: 0.01
execution_high_cost: 0.1
ai_node_multiplier: 10
http_loop_multiplier: 5
polling_multiplier: 3
critical_risk_multiplier: 6
""")
    cm = load_cost_model(yaml_path)
    assert cm.currency == "USD"
    assert cm.execution_low_cost == 0.001
    assert cm.execution_high_cost == 0.1
    assert cm.ai_node_multiplier == 10.0


def test_load_json(tmp_path: Path):
    json_path = tmp_path / "cost_model.json"
    data = {
        "currency": "GBP",
        "execution_low_cost": 0.0002,
        "ai_node_multiplier": 8,
    }
    json_path.write_text(json.dumps(data))
    cm = load_cost_model(json_path)
    assert cm.currency == "GBP"
    assert cm.execution_low_cost == 0.0002
    assert cm.ai_node_multiplier == 8.0
    # Defaults for missing fields
    assert cm.execution_medium_cost == 0.001
    assert cm.http_loop_multiplier == 3.0


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError, match="not found"):
        load_cost_model("/nonexistent/path.yaml")


def test_partial_file_uses_defaults(tmp_path: Path):
    p = tmp_path / "partial.yaml"
    p.write_text("currency: CHF\n")
    cm = load_cost_model(p)
    assert cm.currency == "CHF"
    assert cm.execution_low_cost == 0.0001  # default
    assert cm.critical_risk_multiplier == 4.0  # default


def test_load_simple_format(tmp_path: Path):
    p = tmp_path / "simple.txt"
    p.write_text("currency: JPY\nexecution_low_cost: 0.5\nai_node_multiplier: 2\n")
    cm = load_cost_model(p)
    assert cm.currency == "JPY"
    assert cm.execution_low_cost == 0.5
    assert cm.ai_node_multiplier == 2.0


def test_empty_file_falls_back_to_defaults(tmp_path: Path):
    p = tmp_path / "empty.yaml"
    p.write_text("")
    cm = load_cost_model(p)
    assert cm.currency == "EUR"


def test_float_coercion(tmp_path: Path):
    p = tmp_path / "coerce.txt"
    p.write_text("ai_node_multiplier: 3\npolling_multiplier: 2.5\n")
    cm = load_cost_model(p)
    assert cm.ai_node_multiplier == 3.0
    assert cm.polling_multiplier == 2.5
