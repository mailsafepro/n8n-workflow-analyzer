# Pilot Instructions — n8n Cost Analyzer

Thank you for participating in the n8n Cost Analyzer pilot! This guide walks you through running the tool and providing feedback.

## Prerequisites

- Python 3.10+
- n8n workflow exports (JSON files)

## Installation

```bash
pip install .
```

## Usage

### 1. Run analysis on a single workflow

```bash
n8n-cost-analyzer path/to/workflow.json
```

### 2. Run analysis on a directory of workflows

```bash
n8n-cost-analyzer path/to/workflows/
```

### 3. Run analysis with audit pack output

```bash
n8n-cost-analyzer path/to/workflows/ --audit-pack ./audit_pack
```

This generates:
- `executive_summary.md` — high-level findings for stakeholders
- `technical_report.md` — detailed technical analysis
- `client_action_plan.md` — prioritized remediation steps
- `analysis.json` — structured data for further processing

## What to Evaluate

1. **Accuracy**: Do the findings reflect real risks in your workflows?
2. **False Positives**: Are any findings incorrect or irrelevant?
3. **Missing Risks**: Are there risks the tool should catch but doesn't?
4. **Usability**: Is the output clear and actionable?
5. **Performance**: How does the tool handle your workflow collection?

## Providing Feedback

Use the pilot feedback form (`pilot_feedback_form.md`) or report issues at:
https://github.com/anomalyco/opencode/issues
