# Sample Report — n8n Workflow Cost & Risk Analyzer

This sample uses a public-template corpus. Your results will differ.

## Portfolio snapshot

- **107 workflows analyzed**
- **392 findings**
- **72 workflows with AI/API cost exposure**
- **99 workflows without error handling**
- **22 workflows with loop + HTTP combinations**
- **587 credential references detected without exposing secret values**

## What this means

Most risk is not evenly distributed. A handful of workflows tend to concentrate the highest-risk patterns: loops that multiply HTTP calls, AI/API nodes with variable cost, missing error handling, and large workflow graphs that become hard to maintain.

## Example top risk patterns

### AI/API cost exposure

AI and LLM nodes often create variable costs because usage depends on token volume, input size, model choice, and execution frequency.

### Loop + HTTP combinations

A workflow that calls external APIs inside a loop or batch can multiply request volume quickly. This is often where unexpected API bills or rate-limit problems begin.

### Missing error handling

Workflows without error handling can fail silently. In production workflows, this can become an operational reliability issue.

### Credential footprint

Credential references are counted, but credential values are not inspected or printed. High credential reference density may indicate a need for governance, ownership, and rotation policies.

## Example “What To Do First”

1. Review the top 3 highest-priority workflows.
2. Add error handling to workflows currently without it.
3. Add limits and monitoring around AI/API nodes.
4. Inspect loop + HTTP combinations.
5. Review credential usage, ownership, and rotation.

## Caveats

- Static analysis only.
- No runtime logs used.
- No exact billing forecast.
- No credentials inspected.
- Not a security or compliance audit.
- Not affiliated with n8n.
