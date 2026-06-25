# Building a Public n8n Workflow Corpus

This guide explains how to use `scripts/download_n8n_templates.py` to build a local corpus of public n8n workflow templates, then analyze them with the n8n Cost Analyzer.

## Why Use Public Templates

- **Diversity**: n8n's public template collection covers hundreds of real-world use cases (AI, CRM, email, data pipelines, etc.)
- **Robustness testing**: More workflows = better coverage of edge cases in the analyzer (node types, connection patterns, risk combinations)
- **Non-sensitive data**: Public templates contain no real credentials (though we scan for accidental exposures as a safety measure)

## Safe Download Principles

1. **Endpoint-first**: The downloader tries documented JSON API endpoints before any other method. No HTML scraping.
2. **Rate-limited**: A configurable sleep (default 0.5s) between requests prevents server overload.
3. **Polite User-Agent**: Requests identify themselves as `n8n-cost-analyzer-corpus-builder/0.1`.
4. **Bounded**: Hard cap of 200 templates per run unless `--allow-large` is explicitly given.
5. **Validation**: Downloaded workflows are validated (must have a `nodes` list), suspicious key names are flagged but values are never printed.
6. **Deduplication**: Already-downloaded IDs are skipped unless `--overwrite` is used.

## Quick Start

```bash
# Install the analyzer (if not already)
pip install -e .

# Download 50 AI-related templates
python scripts/download_n8n_templates.py \
  --category ai \
  --limit 50 \
  --output-dir examples/corpus/batch_002_ai

# Analyze the downloaded corpus
PYTHONPATH=src python -m n8n_cost_analyzer.cli analyze examples/corpus/batch_002_ai/workflows \
  --audit-pack examples/audit_packs/batch_002_ai \
  --cost-model cost_model.example.yaml
```

## Commands

### Download by category

```bash
python scripts/download_n8n_templates.py \
  --category ai \
  --limit 50 \
  --output-dir examples/corpus/ai_templates
```

Available categories depend on what n8n's template API exposes. Common categories include: `ai`, `crm`, `email`, `marketing`, `sales`, `data`, `productivity`, `communication`.

### Search by keyword

```bash
python scripts/download_n8n_templates.py \
  --search "gmail openai" \
  --limit 25 \
  --output-dir examples/corpus/gmail_openai
```

### Download general listing

```bash
python scripts/download_n8n_templates.py \
  --limit 100 \
  --output-dir examples/corpus/general
```

### Dry run (discover only, no downloads)

```bash
python scripts/download_n8n_templates.py \
  --category ai \
  --limit 50 \
  --output-dir examples/corpus/ai_preview \
  --dry-run
```

### Override base URL

```bash
python scripts/download_n8n_templates.py \
  --category ai \
  --limit 50 \
  --output-dir examples/corpus/ai_custom \
  --base-url https://templates.n8n.io
```

## All CLI Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--category` | — | Template category filter (e.g. `ai`, `crm`) |
| `--search` | — | Free-text search query |
| `--limit` | `50` | Max templates to download (hard cap `200` unless `--allow-large`) |
| `--allow-large` | — | Allow limits above 200 |
| `--output-dir` | `examples/corpus/downloaded` | Output directory |
| `--page-size` | `20` | Page size for the search endpoint |
| `--sleep-seconds` | `0.5` | Delay between HTTP requests |
| `--dry-run` | — | List templates without downloading |
| `--overwrite` | — | Overwrite existing workflow files |
| `--base-url` | — | Override base URL for API discovery |

## Output Structure

```
examples/corpus/batch_002_ai/
├── workflows/              # Individual workflow JSON files
│   ├── 123-template-name.json
│   └── ...
├── manifest.json           # Metadata about downloaded workflows
├── failed_downloads.json   # Failed fetch attempts
└── download_report.md      # Human-readable summary
```

## Recommended Batch Sizes

| Goal | Batch Size | Sleep | Notes |
|------|-----------|-------|-------|
| Quick smoke test | 5 | 1.0s | Verify connectivity |
| Small corpus | 25–50 | 0.5s | First pass |
| Medium corpus | 100–200 | 0.5s | Steady collection |
| Large corpus | 200+ (allow-large) | 1.0s+ | Extended collection |

## Categories to Collect

A well-rounded test corpus for the analyzer should include:

- **AI workflows**: OpenAPI + AI/LLM nodes (token-based cost patterns)
- **Polling workflows**: Schedule triggers, RSS, email polling (FREQ_POLL patterns)
- **Webhook workflows**: Incoming/outgoing webhooks
- **Complex workflows**: Many nodes, high fan-out, branching logic
- **Error handling workflows**: Workflows with error handler sub-workflows
- **Integration workflows**: CRM, database, HTTP API combinations

## How to Run the Analyzer on Downloaded Corpus

```bash
# Set PYTHONPATH so the analyzer discovers its source
export PYTHONPATH=src

# Analyze a downloaded corpus
python -m n8n_cost_analyzer.cli analyze \
  examples/corpus/batch_002_ai/workflows \
  --audit-pack examples/audit_packs/batch_002_ai \
  --cost-model cost_model.example.yaml

# Or use the CLI directly
python -m n8n_cost_analyzer.cli analyze \
  examples/corpus/batch_002_ai/workflows \
  --output examples/corpus/batch_002_ai/analyzed.json
```

## Privacy / Security Caveats

- Public n8n templates should not contain real credentials, but we scan for suspicious key names as a safety measure.
- **If suspicious keys are found, the key names are reported but values are never printed or saved.**
- The downloader does **not** attempt to use, validate, or test credentials.
- All analysis is local and offline. No data is sent anywhere.
- Review downloaded workflows before committing to any shared repository.

## Do Not Commit Sensitive Workflows

If you create custom test workflows or download templates that may contain internal logic:

1. Check the `manifest.json` for suspicious key warnings
2. Review workflow files for any accidental credential exposure
3. Consider adding a `.gitignore` entry for downloaded workflow directories

## What to Do If the API Is Unavailable

If no public JSON template endpoint is discovered, the downloader will exit with:

```
RuntimeError: No public JSON template endpoint discovered.
```

In this case:

1. Check if a custom base URL is needed: `--base-url https://templates.n8n.io`
2. Check n8n's current API documentation for updated endpoints
3. As a last resort, manually download individual workflows from https://n8n.io/workflows/ and place them in your corpus directory

We do **not** scrape HTML from n8n.io pages. If the JSON API is unavailable, the tool stops with a clear message.
