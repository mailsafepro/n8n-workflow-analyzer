# n8n Workflow Cost & Risk Report

## How to Read This Report

If you only have a few minutes, start with these sections:

1. **Audit Summary** — overall risk scores at a glance
2. **Top Workflows To Review First** — ranked by risk
3. **Workflow Summaries** — one-line narrative per workflow
4. **Quick Wins** — immediate actions with the most impact

For a deeper review, read the full report in order.

## Audit Summary

- **Overall Risk Score:** 12/100 █░░░░░░░░░
- **Risk Level:** 🟢 Low
- **Workflows analyzed:** 10 workflows
- **High-risk workflows:** 6
- **Total findings:** 31 findings (0 criticals, 1 high)
- **Top risk category:** cost
- **Most urgent workflow:** 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide

## Executive Summary

- **Cost Risk Score:** 35/100 ███░░░░░░░
- **Operational Risk Score:** 0/100 ░░░░░░░░░░
- **Complexity Score:** 1/100 ░░░░░░░░░░

## How to Interpret Risk Scores

Risk scores are a relative indicator, not an absolute measure:

| Range | Meaning |
|-------|---------|
| 0 | No risks detected |
| 1–20 | Low risk — maintain current practices |
| 21–40 | Moderate risk — monitor and plan mitigation |
| 41–70 | Review recommended — address in the next cycle |
| 71–100 | High priority — take immediate action |

**Important:** The portfolio-level score (e.g., 12/100) can be low even if individual
workflows have high scores. Always check the workflow rankings and per-workflow
details to identify the most urgent items.

## Severity Legend

| Severity | Meaning |
|----------|---------|
| CRITICAL | Immediate attention required. High probability of significant cost overruns or system failure. |
| HIGH | Important risk that should be addressed in the next sprint/cycle. |
| MEDIUM | Notable risk. Monitor and plan mitigation. |
| LOW | Informational. Low probability of material impact. |

## Workflow Summaries

| Workflow | Priority | Narrative | Next Action |
|----------|----------|-----------|-------------|
| ai | Review recommended (60) | Has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| backupn8n | Low (0) | No significant risks detected. | Review and assess |
| chathub | Review recommended (45) | Has 3 AI/LLM nodes with variable token-based costs. | Estimate and monitor costs before production |
| email | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| RAG Workflow For Company Documents stored in Google Drive | Highest priority (90) | Has 5 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| salesforce | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
| scrape | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
| ScrapeNinja: AI generated web scraper | Moderate (30) | Has AI/LLM nodes with variable token-based costs. | Review and assess |
| trackseo | Review recommended (60) | Has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls. | Add rate limits and concurrency controls |

## Node Inventory

- **Total unique node types:** 48 types
- **Trigger nodes:** 13 nodes
- **Disabled nodes:** 0 nodes
- **Credential references:** 58 references

### Node Categories

| Category | Count |
|----------|-------|
| control_flow | 38 |
| ai | 32 |
| transform | 15 |
| trigger | 13 |
| marketing | 10 |
| spreadsheet | 6 |
| email | 6 |
| storage | 6 |
| http_api | 6 |
| communication | 4 |
| crm | 3 |
| scraping | 3 |
| calendar | 2 |
| devops | 2 |

### Node Types

| Node Type | Count |
|-----------|-------|
| n8n-nodes-base.stickyNote | 27 |
| @blotato/n8n-nodes-blotato.blotato | 10 |
| n8n-nodes-base.set | 8 |
| n8n-nodes-base.httpRequest | 6 |
| @n8n/n8n-nodes-langchain.agent | 5 |
| n8n-nodes-base.gmailTool | 5 |
| n8n-nodes-base.googleDrive | 5 |
| n8n-nodes-base.if | 4 |
| n8n-nodes-base.telegram | 4 |
| @n8n/n8n-nodes-langchain.lmChatOpenAi | 4 |
| @n8n/n8n-nodes-langchain.memoryBufferWindow | 4 |
| n8n-nodes-base.googleSheets | 4 |
| n8n-nodes-base.merge | 4 |
| @n8n/n8n-nodes-langchain.openAi | 3 |
| n8n-nodes-base.manualTrigger | 3 |
| n8n-nodes-base.scheduleTrigger | 3 |
| @n8n/n8n-nodes-langchain.lmChatGoogleGemini | 3 |
| n8n-nodes-base.salesforce | 3 |
| n8n-nodes-base.code | 3 |
| CUSTOM.scrapeNinja | 3 |
| n8n-nodes-base.telegramTrigger | 2 |
| n8n-nodes-base.baserowTool | 2 |
| @n8n/n8n-nodes-langchain.chatTrigger | 2 |
| n8n-nodes-base.wait | 2 |
| @n8n/n8n-nodes-langchain.vectorStorePinecone | 2 |
| @n8n/n8n-nodes-langchain.embeddingsGoogleGemini | 2 |
| n8n-nodes-base.googleDriveTrigger | 2 |
| n8n-nodes-base.googleCalendarTool | 1 |
| n8n-nodes-base.n8n | 1 |
| n8n-nodes-base.splitInBatches | 1 |
| n8n-nodes-base.convertToFile | 1 |
| n8n-nodes-base.filter | 1 |
| @n8n/n8n-nodes-langchain.lmChatOpenRouter | 1 |
| @tavily/n8n-nodes-tavily.tavilyTool | 1 |
| n8n-nodes-base.gmailTrigger | 1 |
| @n8n/n8n-nodes-langchain.documentDefaultDataLoader | 1 |
| @n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter | 1 |
| @n8n/n8n-nodes-langchain.toolVectorStore | 1 |
| n8n-nodes-base.itemLists | 1 |
| n8n-nodes-base.renameKeys | 1 |
| n8n-nodes-base.gmail | 1 |
| n8n-nodes-base.noOp | 1 |
| n8n-nodes-base.googleCalendar | 1 |
| @n8n/n8n-nodes-langchain.chainLlm | 1 |
| n8n-nodes-mcp.mcpClientTool | 1 |
| @n8n/n8n-nodes-langchain.outputParserAutofixing | 1 |
| @n8n/n8n-nodes-langchain.outputParserStructured | 1 |
| n8n-nodes-base.perplexity | 1 |

## Connection Inventory

- **Total edges:** 121
- **Max outgoing edges:** 9
- **High fan-out nodes:** Upload Video to BLOTATO
- **Isolated nodes:** How It Works, MCP Client, Setup Guide - Start Here, Step 1 - Telegram Setup, Step 2 - API Keys Configuration, Step 3 - AI Processing, Step 4 - Voice & Video Generation, Step 5 - Publishing, Sticky Note, Sticky Note1, Sticky Note2, Sticky Note3, Sticky Note4, Sticky Note5, Sticky Note7, Sticky Note9

## Top Workflows To Review First

| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |
|------|----------|-------------|-----------|----------|------|-------------|
| 1 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 2 | RAG Workflow For Company Documents stored in Google Drive | 90 | 75 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 3 | ai | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 4 | trackseo | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 5 | chathub | 45 | 45 | 0 | 0 | AI_NODE |
| 6 | email | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 7 | ScrapeNinja: AI generated web scraper | 30 | 30 | 0 | 0 | AI_NODE |
| 8 | salesforce | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 9 | scrape | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 10 | backupn8n | 0 | 0 | 0 | 0 | — |

## Workflow Inventory

| # | Workflow | Active | Nodes | Triggers | Risk Score |
|---|----------|--------|-------|----------|------------|
| 1 | ai | ❌ | 15 | n8n-nodes-base.telegramTrigger | 60 |
| 2 | backupn8n | ❌ | 10 | n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger | 0 |
| 3 | chathub | ❌ | 9 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 4 | email | ❌ | 13 | n8n-nodes-base.gmailTrigger | 45 |
| 5 | RAG Workflow For Company Documents stored in Google Drive | ❌ | 18 | @n8n/n8n-nodes-langchain.chatTrigger, n8n-nodes-base.googleDriveTrigger | 90 |
| 6 | salesforce | ❌ | 12 | n8n-nodes-base.manualTrigger | 15 |
| 7 | scrape | ❌ | 12 | n8n-nodes-base.scheduleTrigger | 15 |
| 8 | ScrapeNinja: AI generated web scraper | ❌ | 6 | n8n-nodes-base.manualTrigger | 30 |
| 9 | trackseo | ❌ | 16 | n8n-nodes-base.scheduleTrigger | 60 |
| 10 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ❌ | 35 | n8n-nodes-base.telegramTrigger | 100 |

## Quick Wins

1. Add rate limits and concurrency controls around the HTTP loop in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide'.
2. Review AI cost exposure in 'ai' — 3 AI nodes with variable token-based costs.
3. Review AI cost exposure in 'chathub' — 3 AI nodes with variable token-based costs.
4. Review AI cost exposure in 'email' — 2 AI nodes with variable token-based costs.
5. Review AI cost exposure in 'RAG Workflow For Company Documents stored in Google Drive' — 5 AI nodes with variable token-based costs.

## Top Risks

| Severity | Category | Workflow | Message |
|----------|----------|----------|---------|
| HIGH | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | cost | ai | AI/LLM node 'Speech to Text' has variable token-based cost that can escalate |
| MEDIUM | cost | ai | AI/LLM node 'Angie, AI Assistant' has variable token-based cost that can escalate |
| MEDIUM | cost | ai | AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate |
| MEDIUM | reliability | ai | Workflow has no error workflow configured |
| MEDIUM | cost | chathub | AI/LLM node 'AI Agent' has variable token-based cost that can escalate |
| MEDIUM | cost | chathub | AI/LLM node 'Chat Model' has variable token-based cost that can escalate |
| MEDIUM | cost | chathub | AI/LLM node 'Search' has variable token-based cost that can escalate |
| MEDIUM | cost | email | AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | cost | email | AI/LLM node 'Gmail labelling agent' has variable token-based cost that can escalate |

## Cost Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| MEDIUM | ai | Speech to Text | AI/LLM node 'Speech to Text' has variable token-based cost that can escalate |
| MEDIUM | ai | Angie, AI Assistant | AI/LLM node 'Angie, AI Assistant' has variable token-based cost that can escalate |
| MEDIUM | ai | OpenAI Chat Model | AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate |
| MEDIUM | chathub | AI Agent | AI/LLM node 'AI Agent' has variable token-based cost that can escalate |
| MEDIUM | chathub | Chat Model | AI/LLM node 'Chat Model' has variable token-based cost that can escalate |
| MEDIUM | chathub | Search | AI/LLM node 'Search' has variable token-based cost that can escalate |
| MEDIUM | email | OpenAI Chat Model1 | AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | email | Gmail labelling agent | AI/LLM node 'Gmail labelling agent' has variable token-based cost that can escalate |
| MEDIUM | RAG Workflow For Company Documents stored in Google Drive | Embeddings Google Gemini | AI/LLM node 'Embeddings Google Gemini' has variable token-based cost that can escalate |
| MEDIUM | RAG Workflow For Company Documents stored in Google Drive | AI Agent | AI/LLM node 'AI Agent' has variable token-based cost that can escalate |
| MEDIUM | RAG Workflow For Company Documents stored in Google Drive | Embeddings Google Gemini (retrieval) | AI/LLM node 'Embeddings Google Gemini (retrieval)' has variable token-based cost that can escalate |
| MEDIUM | RAG Workflow For Company Documents stored in Google Drive | Google Gemini Chat Model | AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate |
| MEDIUM | RAG Workflow For Company Documents stored in Google Drive | Google Gemini Chat Model (retrieval) | AI/LLM node 'Google Gemini Chat Model (retrieval)' has variable token-based cost that can escalate |
| MEDIUM | ScrapeNinja: AI generated web scraper | Google Gemini Chat Model | AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate |
| MEDIUM | ScrapeNinja: AI generated web scraper | Generate JS eval code via LLM | AI/LLM node 'Generate JS eval code via LLM' has variable token-based cost that can escalate |
| MEDIUM | trackseo | OpenAI Chat Model | AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate |
| MEDIUM | trackseo | 🤖 SERP Scraper Agent (MCP) | AI/LLM node '🤖 SERP Scraper Agent (MCP)' has variable token-based cost that can escalate |
| MEDIUM | trackseo | OpenAI Chat Model1 | AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate |
| HIGH | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Merge1, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Search Trends with Perplexity | AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Script with GPT-4 | AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Caption with GPT-4 | AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate |
| LOW | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | Workflow has 5 HTTP Request nodes, increasing external dependency and cost |

## Estimated Cost Exposure

- **ai:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Speech to Text' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Angie, AI Assistant' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **backupn8n:** ⚪ UNKNOWN — unknown
- **chathub:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Search' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **email:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gmail labelling agent' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **RAG Workflow For Company Documents stored in Google Drive:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Embeddings Google Gemini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Embeddings Google Gemini (retrieval)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model (retrieval)' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **salesforce:** 🟢 LOW — minimal (heuristic)
- **scrape:** 🟢 LOW — minimal (heuristic)
- **ScrapeNinja: AI generated web scraper:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate JS eval code via LLM' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **trackseo:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '🤖 SERP Scraper Agent (MCP)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count

*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*

## Operational Risk Findings

No operational findings.

## Complexity Findings

| Severity | Workflow | Finding |
|----------|----------|---------|
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |

## Recommendations

1. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
2. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
3. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
4. Review if all external HTTP calls are necessary. Consider caching or batching to reduce dependency costs.

## Workflow-Level Details

### ai

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 15
- **Triggers:** n8n-nodes-base.telegramTrigger
- **Scores:** Cost=45 | Ops=0 | Complexity=0 | Overall=60

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Speech to Text' has variable token-based cost that can escalate
    - Nodes: Speech to Text
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Angie, AI Assistant' has variable token-based cost that can escalate
    - Nodes: Angie, AI Assistant
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### backupn8n

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 10
- **Triggers:** n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=0

### chathub

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 9
- **Triggers:** @n8n/n8n-nodes-langchain.chatTrigger
- **Scores:** Cost=45 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
    - Nodes: AI Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Chat Model' has variable token-based cost that can escalate
    - Nodes: Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Search' has variable token-based cost that can escalate
    - Nodes: Search

### email

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 13
- **Triggers:** n8n-nodes-base.gmailTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Gmail labelling agent' has variable token-based cost that can escalate
    - Nodes: Gmail labelling agent
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### RAG Workflow For Company Documents stored in Google Drive

- **ID:** 7cXvgkl9170QXzT2
- **Active:** ❌
- **Nodes:** 18
- **Triggers:** @n8n/n8n-nodes-langchain.chatTrigger, n8n-nodes-base.googleDriveTrigger
- **Scores:** Cost=75 | Ops=0 | Complexity=0 | Overall=90

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Embeddings Google Gemini' has variable token-based cost that can escalate
    - Nodes: Embeddings Google Gemini
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
    - Nodes: AI Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Embeddings Google Gemini (retrieval)' has variable token-based cost that can escalate
    - Nodes: Embeddings Google Gemini (retrieval)
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
    - Nodes: Google Gemini Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Google Gemini Chat Model (retrieval)' has variable token-based cost that can escalate
    - Nodes: Google Gemini Chat Model (retrieval)
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### salesforce

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 12
- **Triggers:** n8n-nodes-base.manualTrigger
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=15

**Findings:**
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### scrape

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 12
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=0 | Ops=0 | Complexity=0 | Overall=15

**Findings:**
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### ScrapeNinja: AI generated web scraper

- **ID:** ALTwr1xWxmqGdCtZ
- **Active:** ❌
- **Nodes:** 6
- **Triggers:** n8n-nodes-base.manualTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=30

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
    - Nodes: Google Gemini Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Generate JS eval code via LLM' has variable token-based cost that can escalate
    - Nodes: Generate JS eval code via LLM

### trackseo

- **ID:** N/A
- **Active:** N/A
- **Nodes:** 16
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=45 | Ops=0 | Complexity=0 | Overall=60

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node '🤖 SERP Scraper Agent (MCP)' has variable token-based cost that can escalate
    - Nodes: 🤖 SERP Scraper Agent (MCP)
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model1
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide

- **ID:** PpVBvs5fecatpTbx
- **Active:** ❌
- **Nodes:** 35
- **Triggers:** n8n-nodes-base.telegramTrigger
- **Scores:** Cost=80 | Ops=0 | Complexity=15 | Overall=100

**Findings:**
  - [HIGH] [cost] LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
    - Nodes: Merge1, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate
    - Nodes: Search Trends with Perplexity
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate
    - Nodes: Generate Script with GPT-4
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate
    - Nodes: Generate Caption with GPT-4
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
    - Nodes: ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out)
    - Nodes: Upload Video to BLOTATO

## Workflow Risk Ranking

| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |
|------|----------|---------|------|-----|------------|----------|
| 1 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 15 | 7 |
| 2 | RAG Workflow For Company Documents stored in Google Drive | 90 | 75 | 0 | 0 | 6 |
| 3 | ai | 60 | 45 | 0 | 0 | 4 |
| 4 | trackseo | 60 | 45 | 0 | 0 | 4 |
| 5 | chathub | 45 | 45 | 0 | 0 | 3 |
| 6 | email | 45 | 30 | 0 | 0 | 3 |
| 7 | ScrapeNinja: AI generated web scraper | 30 | 30 | 0 | 0 | 2 |
| 8 | salesforce | 15 | 0 | 0 | 0 | 1 |
| 9 | scrape | 15 | 0 | 0 | 0 | 1 |
| 10 | backupn8n | 0 | 0 | 0 | 0 | 0 |

## Assumptions

- Analysis is based on exported JSON workflow definitions only.
- Actual execution volume depends on trigger frequency and input data size.
- AI/LLM costs are estimated based on node presence, not actual token usage.
- HTTP call costs assume external API pricing not included.
- Webhook chains are inferred from node types and URL patterns.
- Cost estimates are heuristic and not financial quotes.
- Credential references are counted; secrets are never exposed.
- Disabled nodes are excluded from risk analysis by default.

## Appendix

### Rule Reference

| Rule ID | Description | Default Severity | Category |
|---------|-------------|------------------|----------|
| FREQ_POLL | Frequent polling/schedule trigger | high | cost |
| LOOP_HTTP | Loop/batch combined with HTTP request | high | cost |
| AI_NODE | AI/LLM node detected | medium | cost |
| LARGE_WF | Workflow with many nodes | medium/critical | complexity |
| NO_ERROR_HANDLING | Missing error workflow | medium | reliability |
| WEBHOOK_CHAIN | Webhook chaining to internal URLs | medium/low | operational |
| DB_IN_LOOP | Database operation inside loop | high | operational |
| MANY_HTTP | Multiple HTTP Request nodes | low | cost |
| HIGH_FAN_OUT | Node with 5+ outgoing connections | medium | complexity |

---
*Generated by n8n Cost Analyzer v0.7.1*