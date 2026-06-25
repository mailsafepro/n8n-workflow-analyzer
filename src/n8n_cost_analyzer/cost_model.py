from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from n8n_cost_analyzer.models import CostModel

DEFAULT_COST_MODEL = CostModel()


def _try_load_yaml(path: Path) -> dict[str, Any] | None:
    try:
        import yaml  # type: ignore
    except ImportError:
        return None
    with path.open(encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return {}
        data: dict[str, Any] = yaml.safe_load(content)
    if data is None:
        return {}
    return data


def _try_load_json(path: Path) -> dict[str, Any] | None:
    try:
        with path.open(encoding="utf-8") as f:
            data: dict[str, Any] = json.load(f)
        return data
    except (json.JSONDecodeError, ValueError):
        return None


def _try_load_simple(path: Path) -> dict[str, Any] | None:
    """Simple key: value parser as last resort."""
    data: dict[str, Any] = {}
    try:
        with path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" not in line:
                    continue
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip()
                if not key:
                    continue
                data[key] = _coerce_value(val)
        return data if data else None
    except OSError:
        return None


def _coerce_value(val: str) -> Any:
    val = val.strip().strip('"').strip("'")
    if val.lower() in ("true", "yes"):
        return True
    if val.lower() in ("false", "no"):
        return False
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        pass
    return val


def _merge_with_defaults(data: dict[str, Any]) -> dict[str, Any]:
    merged = {
        "currency": DEFAULT_COST_MODEL.currency,
        "execution_low_cost": DEFAULT_COST_MODEL.execution_low_cost,
        "execution_medium_cost": DEFAULT_COST_MODEL.execution_medium_cost,
        "execution_high_cost": DEFAULT_COST_MODEL.execution_high_cost,
        "ai_node_multiplier": DEFAULT_COST_MODEL.ai_node_multiplier,
        "http_loop_multiplier": DEFAULT_COST_MODEL.http_loop_multiplier,
        "polling_multiplier": DEFAULT_COST_MODEL.polling_multiplier,
        "critical_risk_multiplier": DEFAULT_COST_MODEL.critical_risk_multiplier,
    }
    merged.update(data)
    return merged


def load_cost_model(path: str | Path | None) -> CostModel:
    if path is None:
        return DEFAULT_COST_MODEL

    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Cost model file not found: {p}")

    data: dict[str, Any] | None = None
    for loader in (_try_load_yaml, _try_load_json, _try_load_simple):
        data = loader(p)
        if data is not None:
            break

    if data is None:
        raise ValueError(f"Could not parse cost model file: {p}")

    merged = _merge_with_defaults(data)

    return CostModel(
        currency=str(merged["currency"]),
        execution_low_cost=float(merged["execution_low_cost"]),
        execution_medium_cost=float(merged["execution_medium_cost"]),
        execution_high_cost=float(merged["execution_high_cost"]),
        ai_node_multiplier=float(merged["ai_node_multiplier"]),
        http_loop_multiplier=float(merged["http_loop_multiplier"]),
        polling_multiplier=float(merged["polling_multiplier"]),
        critical_risk_multiplier=float(merged["critical_risk_multiplier"]),
    )
