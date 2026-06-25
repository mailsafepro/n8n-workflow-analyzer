# n8n Workflow Cost & Risk Report

## How to Read This Report

If you only have a few minutes, start with these sections:

1. **Audit Summary** — overall risk scores at a glance
2. **Top Workflows To Review First** — ranked by risk
3. **Workflow Summaries** — one-line narrative per workflow
4. **Quick Wins** — immediate actions with the most impact

For a deeper review, read the full report in order.

## Audit Summary

- **Overall Risk Score:** 23/100 ██░░░░░░░░
- **Risk Level:** 🟠 Medium
- **Workflows analyzed:** 5 workflows
- **High-risk workflows:** 5
- **Total findings:** 31 findings (0 criticals, 3 highs)
- **Top risk category:** cost
- **Most urgent workflow:** Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq
- **Parser warnings:** 15 warnings

## Parser Warnings

- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'News sentiment Analyzer'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'get_a_joke'
- ⚠ Unknown node type 'n8n-nodes-base.dateTimeTool' in node 'days_from_now'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWikipedia' in node 'wikipedia'
- ⚠ Unknown node type 'n8n-nodes-base.cryptoTool' in node 'create_password'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolCode' in node 'calculate_loan_payment'
- ⚠ Unknown node type 'n8n-nodes-base.rssFeedReadTool' in node 'n8n_blog_rss_feed'
- ⚠ Unknown node type 'n8n-nodes-base.rssFeedReadTool' in node 'Get News'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Get Weather'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory2'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory3'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatGroq' in node 'Groq Chat Model1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatGroq' in node 'Groq Chat Model'

## Executive Summary

- **Cost Risk Score:** 61/100 ██████░░░░
- **Operational Risk Score:** 0/100 ░░░░░░░░░░
- **Complexity Score:** 9/100 ░░░░░░░░░░

> **Note:** 4 community/custom node types found. These may have cost or
> risk profiles not covered by built-in rules. See the Community/Custom section for details.

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
| 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls. | Add rate limits and concurrency controls |
| Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | High priority (80) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Add rate limits and concurrency controls |
| 🤖 Build an interactive AI agent with chat interface and multiple tools | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Build your first AI agent | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 8 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls; is a large workflow that is harder to maintain and debug. | Add rate limits and concurrency controls |

## Node Inventory

- **Total unique node types:** 32 types
- **Trigger nodes:** 6 nodes
- **Disabled nodes:** 1 node
- **Credential references:** 34 references
- **Unknown node types:** 4 types

### Node Categories

| Category | Count |
|----------|-------|
| control_flow | 52 |
| ai | 24 |
| transform | 21 |
| http_api | 18 |
| marketing | 10 |
| communication | 9 |
| trigger | 6 |
| unknown | 6 |
| database | 4 |
| scraping | 4 |
| spreadsheet | 2 |

### Node Types

| Node Type | Count |
|-----------|-------|
| n8n-nodes-base.stickyNote | 39 |
| n8n-nodes-base.httpRequest | 18 |
| n8n-nodes-base.code | 15 |
| @blotato/n8n-nodes-blotato.blotato | 10 |
| n8n-nodes-base.telegram | 9 |
| @n8n/n8n-nodes-langchain.agent | 7 |
| n8n-nodes-base.set | 6 |
| n8n-nodes-base.merge | 6 |
| @n8n/n8n-nodes-langchain.lmChatGoogleGemini | 5 |
| @n8n/n8n-nodes-langchain.memoryMongoDbChat | 4 |
| n8n-nodes-base.html | 4 |
| n8n-nodes-base.telegramTrigger | 3 |
| n8n-nodes-base.switch | 3 |
| @n8n/n8n-nodes-langchain.openAi | 2 |
| n8n-nodes-base.googleSheets | 2 |
| @n8n/n8n-nodes-langchain.memoryBufferWindow | 2 |
| @n8n/n8n-nodes-langchain.chatTrigger | 2 |
| n8n-nodes-base.httpRequestTool | 2 |
| n8n-nodes-base.rssFeedReadTool | 2 |
| n8n-nodes-base.if | 2 |
| @n8n/n8n-nodes-langchain.lmChatGroq | 2 |
| n8n-nodes-base.perplexity | 1 |
| n8n-nodes-base.wait | 1 |
| @n8n/n8n-nodes-langchain.googleGemini | 1 |
| @n8n/n8n-nodes-langchain.lmChatOpenAi | 1 |
| n8n-nodes-base.dateTimeTool | 1 |
| @n8n/n8n-nodes-langchain.toolWikipedia | 1 |
| n8n-nodes-base.cryptoTool | 1 |
| @n8n/n8n-nodes-langchain.toolCode | 1 |
| @n8n/n8n-nodes-langchain.outputParserStructured | 1 |
| n8n-nodes-base.scheduleTrigger | 1 |
| n8n-nodes-base.executeWorkflow | 1 |

## Community / Custom / Unclassified Node Types

The following 4 node types are from community packages, custom builds,
or unrecognized sources.
They may have custom cost or risk profiles not covered by built-in rules:

- `n8n-nodes-base.cryptoTool`
- `n8n-nodes-base.dateTimeTool`
- `n8n-nodes-base.httpRequestTool`
- `n8n-nodes-base.rssFeedReadTool`

## Connection Inventory

- **Total edges:** 137
- **Max outgoing edges:** 9
- **High fan-out nodes:** Branch by Intent, Google Gemini Chat Model1, Upload Video to BLOTATO
- **Isolated nodes:** Author Message1, How It Works, Introduction Note, Main Overview1, OpenAI, Section , Section 6, Section 7, Section 8, Section 9, Setup Guide - Start Here, Step 1 - Telegram Setup, Step 2 - API Keys Configuration, Step 3 - AI Processing, Step 4 - Voice & Video Generation, Step 5 - Publishing, Sticky Note, Sticky Note1, Sticky Note10, Sticky Note12, Sticky Note13, Sticky Note15, Sticky Note16, Sticky Note2, Sticky Note3, Sticky Note4, Sticky Note5, Sticky Note6, Sticky Note7, Sticky Note8, Sticky Note9, Warning1

## Top Workflows To Review First

| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |
|------|----------|-------------|-----------|----------|------|-------------|
| 1 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | 100 | 100 | 0 | 1 | LOOP_HTTP, AI_NODE, LARGE_WF |
| 2 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 3 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 80 | 65 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 4 | Build your first AI agent | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 5 | 🤖 Build an interactive AI agent with chat interface and multiple tools | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |

## Workflow Inventory

| # | Workflow | Active | Nodes | Triggers | Risk Score |
|---|----------|--------|-------|----------|------------|
| 1 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ❌ | 35 | n8n-nodes-base.telegramTrigger | 100 |
| 2 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | ❌ | 28 | n8n-nodes-base.telegramTrigger | 80 |
| 3 | 🤖 Build an interactive AI agent with chat interface and multiple tools | ❌ | 17 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 4 | Build your first AI agent | ❌ | 13 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 5 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | ❌ | 63 | n8n-nodes-base.scheduleTrigger, n8n-nodes-base.telegramTrigger | 100 |

## Quick Wins

1. Add rate limits and concurrency controls around the HTTP loop in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide'.
2. Add rate limits and concurrency controls around the HTTP loop in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini'.
3. Add rate limits and concurrency controls around the HTTP loop in 'Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq'.
4. Review AI cost exposure in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide' — 3 AI nodes with variable token-based costs.
5. Review AI cost exposure in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini' — 2 AI nodes with variable token-based costs.

## Top Risks

| Severity | Category | Workflow | Message |
|----------|----------|----------|---------|
| HIGH | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate |
| MEDIUM | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate |
| MEDIUM | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate |
| MEDIUM | reliability | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Workflow has no error workflow configured |
| MEDIUM | complexity | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |
| MEDIUM | cost | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | cost | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate |

## Cost Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| HIGH | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Merge1, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Search Trends with Perplexity | AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Script with GPT-4 | AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Caption with GPT-4 | AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate |
| LOW | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | Workflow has 5 HTTP Request nodes, increasing external dependency and cost |
| HIGH | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Merge, Merge1, 1 hour, 15 min, 1 day, News | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Google Gemini Chat Model1 | AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Crypto Agent | AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate |
| LOW | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 1 hour, 15 min, 1 day, News | Workflow has 4 HTTP Request nodes, increasing external dependency and cost |
| MEDIUM | 🤖 Build an interactive AI agent with chat interface and multiple tools | Gemini | AI/LLM node 'Gemini' has variable token-based cost that can escalate |
| MEDIUM | 🤖 Build an interactive AI agent with chat interface and multiple tools | Your First AI Agent | AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate |
| MEDIUM | Build your first AI agent | Your First AI Agent | AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate |
| MEDIUM | Build your first AI agent | Connect Gemini | AI/LLM node 'Connect Gemini' has variable token-based cost that can escalate |
| HIGH | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Merge Sources1, Merge Link Content, Merge Search Result, If Reddit?, Comment, If n8n Community?, Reddit Search page JSON (has time), Reddit Search page (no time), Reddit Search page JSON (no keyword), n8n Community Fetch JSON, Reddit, n8n Community Fetch | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Google Gemini Chat Model1 | AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Detect User Intent | AI/LLM node 'Detect User Intent' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | AI Summarizer Clarify | AI/LLM node 'AI Summarizer Clarify' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | AI Summarizer Deep-dive | AI/LLM node 'AI Summarizer Deep-dive' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | AI Summarizer Overview | AI/LLM node 'AI Summarizer Overview' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Google Gemini Chat Model jaynguyena01 | AI/LLM node 'Google Gemini Chat Model jaynguyena01' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Groq Chat Model1 | AI/LLM node 'Groq Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Groq Chat Model | AI/LLM node 'Groq Chat Model' has variable token-based cost that can escalate |
| LOW | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | If Reddit?, Comment, If n8n Community?, Reddit Search page JSON (has time), Reddit Search page (no time), Reddit Search page JSON (no keyword), n8n Community Fetch JSON, Reddit, n8n Community Fetch | Workflow has 9 HTTP Request nodes, increasing external dependency and cost |

## Estimated Cost Exposure

- **💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **🤖 Build an interactive AI agent with chat interface and multiple tools:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Gemini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Build your first AI agent:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Connect Gemini' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Detect User Intent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Summarizer Clarify' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Summarizer Deep-dive' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Summarizer Overview' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model jaynguyena01' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Groq Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Groq Chat Model' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 9 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count

*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*

## Operational Risk Findings

No operational findings.

## Complexity Findings

| Severity | Workflow | Finding |
|----------|----------|---------|
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Workflow has 63 nodes, which increases complexity |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Node 'Branch by Intent' has 6 outgoing connections (high fan-out) |

## Recommendations

1. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
2. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
3. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
4. Review if all external HTTP calls are necessary. Consider caching or batching to reduce dependency costs.
5. Split large workflows into smaller focused workflows to improve maintainability and reduce blast radius.

## Workflow-Level Details

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

### Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini

- **ID:** 11366
- **Active:** N/A
- **Nodes:** 28
- **Triggers:** n8n-nodes-base.telegramTrigger
- **Scores:** Cost=65 | Ops=0 | Complexity=0 | Overall=80

**Findings:**
  - [HIGH] [cost] LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
    - Nodes: Merge, Merge1, 1 hour, 15 min, 1 day, News
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate
    - Nodes: Google Gemini Chat Model1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate
    - Nodes: Crypto Agent
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
    - Nodes: 1 hour, 15 min, 1 day, News

### 🤖 Build an interactive AI agent with chat interface and multiple tools

- **ID:** 5819
- **Active:** N/A
- **Nodes:** 17
- **Triggers:** @n8n/n8n-nodes-langchain.chatTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Gemini' has variable token-based cost that can escalate
    - Nodes: Gemini
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate
    - Nodes: Your First AI Agent
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Build your first AI agent

- **ID:** 6270
- **Active:** N/A
- **Nodes:** 13
- **Triggers:** @n8n/n8n-nodes-langchain.chatTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate
    - Nodes: Your First AI Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Connect Gemini' has variable token-based cost that can escalate
    - Nodes: Connect Gemini
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq

- **ID:** 8573
- **Active:** N/A
- **Nodes:** 63
- **Triggers:** n8n-nodes-base.scheduleTrigger, n8n-nodes-base.telegramTrigger
- **Scores:** Cost=100 | Ops=0 | Complexity=30 | Overall=100

**Findings:**
  - [HIGH] [cost] LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
    - Nodes: Merge Sources1, Merge Link Content, Merge Search Result, If Reddit?, Comment, If n8n Community?, Reddit Search page JSON (has time), Reddit Search page (no time), Reddit Search page JSON (no keyword), n8n Community Fetch JSON, Reddit, n8n Community Fetch
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate
    - Nodes: Google Gemini Chat Model1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Detect User Intent' has variable token-based cost that can escalate
    - Nodes: Detect User Intent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Summarizer Clarify' has variable token-based cost that can escalate
    - Nodes: AI Summarizer Clarify
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Summarizer Deep-dive' has variable token-based cost that can escalate
    - Nodes: AI Summarizer Deep-dive
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Summarizer Overview' has variable token-based cost that can escalate
    - Nodes: AI Summarizer Overview
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Google Gemini Chat Model jaynguyena01' has variable token-based cost that can escalate
    - Nodes: Google Gemini Chat Model jaynguyena01
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Groq Chat Model1' has variable token-based cost that can escalate
    - Nodes: Groq Chat Model1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Groq Chat Model' has variable token-based cost that can escalate
    - Nodes: Groq Chat Model
  - [MEDIUM] [complexity] LARGE_WF: Workflow has 63 nodes, which increases complexity
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 9 HTTP Request nodes, increasing external dependency and cost
    - Nodes: If Reddit?, Comment, If n8n Community?, Reddit Search page JSON (has time), Reddit Search page (no time), Reddit Search page JSON (no keyword), n8n Community Fetch JSON, Reddit, n8n Community Fetch
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Branch by Intent' has 6 outgoing connections (high fan-out)
    - Nodes: Branch by Intent

## Workflow Risk Ranking

| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |
|------|----------|---------|------|-----|------------|----------|
| 1 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | 100 | 100 | 0 | 30 | 13 |
| 2 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 15 | 7 |
| 3 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 80 | 65 | 0 | 0 | 5 |
| 4 | Build your first AI agent | 45 | 30 | 0 | 0 | 3 |
| 5 | 🤖 Build an interactive AI agent with chat interface and multiple tools | 45 | 30 | 0 | 0 | 3 |

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