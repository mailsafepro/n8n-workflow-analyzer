# n8n Workflow Cost & Risk Report

## How to Read This Report

If you only have a few minutes, start with these sections:

1. **Audit Summary** — overall risk scores at a glance
2. **Top Workflows To Review First** — ranked by risk
3. **Workflow Summaries** — one-line narrative per workflow
4. **Quick Wins** — immediate actions with the most impact

For a deeper review, read the full report in order.

## Audit Summary

- **Overall Risk Score:** 15/100 █░░░░░░░░░
- **Risk Level:** 🟢 Low
- **Workflows analyzed:** 36 workflows
- **High-risk workflows:** 26
- **Total findings:** 155 findings (1 critical, 8 highs)
- **Top risk category:** cost
- **Most urgent workflow:** Workflow Patterns & Boilerplate for Scaling up
- **Parser warnings:** 79 warnings

## Parser Warnings

- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'News sentiment Analyzer'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Tool: Inject Creativity'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Tool: Build Prompt Structure'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreQdrant' in node 'Qdrant Vector Store'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOllama' in node 'Embeddings Ollama'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatOllama' in node 'Ollama Chat Model'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreQdrant' in node 'Qdrant Vector Store1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOllama' in node 'Embeddings Ollama1'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'get_a_joke'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWikipedia' in node 'wikipedia'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolCode' in node 'calculate_loan_payment'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Get Weather'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Analyze Data'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'Analyze image'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'Analyze voice message'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Register User'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Update Profile Data'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Get Profile Data'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'Get Report'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Append Meal Data'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'Gmail MCP'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'Google Tasks MCP'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpTrigger' in node 'Gmail MCP Server'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpTrigger' in node 'Calendar MCP Server'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'Calendar MCP'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpTrigger' in node 'Task Manager MCP'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'Finance Tracker'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpTrigger' in node 'Finance Manager MCP Server'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Get all Expenses'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Create Expense'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Delete Expense'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpTrigger' in node 'Google Contacts MCP'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'Google Contacts'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory2'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.memoryMongoDbChat' in node 'MongoDB Chat Memory3'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatGroq' in node 'Groq Chat Model1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatGroq' in node 'Groq Chat Model'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'Document OCR via VLM'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger' in node 'New Website Visitors'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'D1 - Get prospect'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'D1 - Update prospect'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'D1 - Get prospect for final update: Success'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'D1 - Update Tags: Success'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'D1 - Get prospect for final update: Fail'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'D1 - Update Tags: Fail'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'E1 - Get prospect'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'E1 - Update Tags: Fail'
- ⚠ Unknown node type '@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro' in node 'E1 - Update Tags: Success'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolCalculator' in node 'Calculator'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'Summarizer'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Web search'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'Embeddings OpenAI'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreQdrant' in node 'Search_db'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Anthropic'
- ⚠ Unknown node type 'n8n-nodes-upload-post.uploadPost' in node 'Upload Post'
- ⚠ Unknown node type 'n8n-nodes-upload-post.uploadPost' in node 'Schedule to TikTok, Instagram, and YouTube'
- ⚠ Unknown node type 'n8n-nodes-browseract.browserAct' in node 'Run BrowserAct Workflow'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'database'
- ⚠ Unknown node type 'n8n-nodes-serpapi.serpApi' in node 'Search LinkedIn Posts via SerpAPI'
- ⚠ Unknown node type 'n8n-nodes-connectsafely-ai.connectSafelyLinkedIn' in node 'Fetch Post Comments via ConnectSafely'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model4'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.informationExtractor' in node 'Information Extractor'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.informationExtractor' in node 'Information Extractor1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'Embeddings OpenAI'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreMongoDBAtlas' in node 'MongoDB Vector Search'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreMongoDBAtlas' in node 'MongoDB Vector Store Inserter'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'OpenAI Embeddings Generator'
- ⚠ Unknown node type 'n8n-nodes-base.whatsAppTrigger' in node 'WhatsApp Trigger'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Gets WhatsApp Voicemail Source URL'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Gets WhatsApp Image Source URL'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Gets WhatsApp Document Source URL'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Send Unsupported Response'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Send Response'

## Executive Summary

- **Cost Risk Score:** 41/100 ████░░░░░░
- **Operational Risk Score:** 0/100 ░░░░░░░░░░
- **Complexity Score:** 5/100 ░░░░░░░░░░

> **Note:** 6 community/custom node types found. These may have cost or
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
| n8n_fluidx_create_session | Review recommended (65) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Add rate limits and concurrency controls |
| Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | High priority (80) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Add rate limits and concurrency controls |
| Create Video with Google Veo3 and Upload to Youtube | Moderate (35) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | Highest priority (95) | Has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls. | Estimate and monitor costs before production |
| Automated AI YouTube Shorts Factory for ASMR (Seedance) | Highest priority (95) | Has 5 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Estimate and monitor costs before production |
| RAG Pipeline | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| 🤖 Build an interactive AI agent with chat interface and multiple tools | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | Review recommended (60) | Has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Build your first AI agent | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Talk to your Google Sheets using ChatGPT-5 | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | Highest priority (90) | Has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; is a large workflow that is harder to maintain and debug. | Estimate and monitor costs before production |
| Jarvis template | Review recommended (60) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; is a large workflow that is harder to maintain and debug. | Estimate and monitor costs before production |
| Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 8 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls; is a large workflow that is harder to maintain and debug. | Add rate limits and concurrency controls |
| PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | Moderate (30) | Lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load. | Configure error workflow |
| Smart Inventory Replenishment & Auto-Purchase Orders | Moderate (35) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Process large documents with OCR using SubworkflowAI and Gemini | Moderate (20) | Lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Auto Generate Descriptive Node Names with AI for Workflow Readability | High priority (75) | Has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Workflow Patterns & Boilerplate for Scaling up | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls; is a large workflow that is harder to maintain and debug; chains webhook triggers which can cascade unexpectedly. | Add rate limits and concurrency controls |
| 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
| 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
| Multi-Agent Evaluation (eval nodes) | Review recommended (60) | Has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Track AI agent token usage and estimate costs in Google Sheets | Highest priority (90) | Has 5 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| 🧑‍🎓 Test your data access techniques with progressive expression challenges | Moderate (30) | Lacks error handling for failure scenarios; is a large workflow that is harder to maintain and debug. | Configure error workflow |
| Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | Moderate (20) | Lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | Review recommended (50) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Estimate and monitor costs before production |
| Physician Profile Enricher | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
| eCommerce Ai Agent ( Telegram Bot ) | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Comment Analyse and Reporter | High priority (75) | Has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| New Appointment → Welcome SMS | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
*... and 6 more workflows (table truncated for readability)*

## Node Inventory

- **Total unique node types:** 101 types
- **Trigger nodes:** 59 nodes
- **Disabled nodes:** 5 nodes
- **Credential references:** 241 references
- **Unknown node types:** 6 types

### Node Categories

| Category | Count |
|----------|-------|
| control_flow | 544 |
| transform | 224 |
| ai | 138 |
| http_api | 96 |
| trigger | 48 |
| spreadsheet | 41 |
| communication | 33 |
| email | 26 |
| unknown | 15 |
| marketing | 12 |
| crm | 12 |
| human_input | 8 |
| storage | 7 |
| scraping | 7 |
| calendar | 7 |
| database | 7 |
| devops | 6 |
| document | 4 |

### Node Types

| Node Type | Count |
|-----------|-------|
| n8n-nodes-base.stickyNote | 412 |
| n8n-nodes-base.httpRequest | 93 |
| n8n-nodes-base.set | 90 |
| n8n-nodes-base.code | 70 |
| n8n-nodes-base.if | 56 |
| n8n-nodes-base.googleSheets | 32 |
| @n8n/n8n-nodes-langchain.agent | 31 |
| n8n-nodes-base.wait | 26 |
| n8n-nodes-base.telegram | 20 |
| n8n-nodes-base.executeWorkflow | 20 |
| n8n-nodes-base.dataTable | 16 |
| @n8n/n8n-nodes-langchain.lmChatOpenAi | 15 |
| n8n-nodes-base.gmail | 13 |
| n8n-nodes-base.noOp | 12 |
| @n8n/n8n-nodes-langchain.lmChatGoogleGemini | 12 |
| n8n-nodes-base.manualTrigger | 12 |
| n8n-nodes-base.scheduleTrigger | 11 |
| n8n-nodes-base.filter | 11 |
| @blotato/n8n-nodes-blotato.blotato | 10 |
| n8n-nodes-base.merge | 10 |
*... and 81 more node types (table truncated for readability)*

## Community / Custom / Unclassified Node Types

The following 6 node types are from community packages, custom builds,
or unrecognized sources.
They may have custom cost or risk profiles not covered by built-in rules:

- `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro`
- `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger`
- `n8n-nodes-browseract.browserAct`
- `n8n-nodes-connectsafely-ai.connectSafelyLinkedIn`
- `n8n-nodes-serpapi.serpApi`
- `n8n-nodes-upload-post.uploadPost`

## Connection Inventory

- **Total edges:** 872
- **Max outgoing edges:** 11
- **High fan-out nodes:** Branch by Intent, Google Gemini Chat Model, Google Gemini Chat Model1, OpenAI Chat Model, Route Document Types, Route by Draft Type, Route by Performance, Simple Memory, Telegram Trigger, Upload Video to BLOTATO, Upload Video to Blotato, Wait, When Executed by [trigger workflow], When clicking ‘Execute workflow’
- **Isolated nodes:** ## Create THE EYE Session, Answer - Array Access, Answer - Array of Objects, Answer - Basic Access, Answer - Final, Answer - JS Function, Answer - Nested Object, Answer Note - Array Access, Answer Note - Array of Objects, Answer Note - Basic Access, Answer Note - Final, Answer Note - JS Function, Answer Note - Nested Object, Anthropic, Author Message1, Congratulations!, Documentation, Feedback Correct1, Feedback Correct2, Feedback Correct3, Feedback Correct4, Feedback Correct5, Feedback Correct6, Feedback Incorrect1, Feedback Incorrect2, Feedback Incorrect3, Feedback Incorrect4, Feedback Incorrect5, Feedback Incorrect6, How It Works, Instruction - Array Access, Instruction - Array of Objects, Instruction - Basic Access, Instruction - Basic Access1, Instruction - Final, Instruction - JS Function, Instruction - Nested Object, Introduction Note, LLM Flow Sticky Note, MCP Client, Main Overview1, Note: AI Ideation, Note: Asset Generation, Note: Distribution, Note: Final Assembly, Post Processing Sticky Note, Post Processing Sticky Note1, Post Processing Sticky Note2, Post Processing Sticky Note4, SUBMISSION GUIDE, Section , Section 6, Section 7, Section 8, Section 9, Section: AI Selection (Gemini), Section: FFmpeg Audio Job Loop, Section: FFmpeg Short Job Loop, Section: Intake & Form, Section: Scheduling, Section: Transcription & Parsing, Setup Guide - Start Here, Setup Instructions, Step 1 - Telegram Setup, Step 1 Explanation, Step 2 - API Keys Configuration, Step 2 Explanation, Step 3 - AI Processing, Step 4 - Voice & Video Generation, Step 5 - Publishing, Sticky Note, Sticky Note – AI Intent Agent, Sticky Note – Approved Trigger, Sticky Note – Build Report, Sticky Note – Fetch Comments, Sticky Note – Flatten Comments, Sticky Note – Format Reply, Sticky Note – Parse & Filter, Sticky Note – Parse Sentiment Output, Sticky Note – Pipeline 2 Header, Sticky Note – Pipeline 3 Header, Sticky Note – Reply Agent, Sticky Note – Save to Sheet, Sticky Note – Send Email, Sticky Note – SerpAPI Search, Sticky Note – Sheet Trigger P2, Sticky Note – Trigger, Sticky Note – Workflow Overview, Sticky Note – Write Reply, Sticky Note — DPO Retry Path, Sticky Note — Email Dispatch, Sticky Note — MCTS Draft Generation, Sticky Note — Outcome Logging, Sticky Note — Pick Best Draft, Sticky Note — Reply Decision, Sticky Note — Reply Monitoring, Sticky Note — Self-Critique Rounds, Sticky Note — Slack Notifications, Sticky Note — Trigger, Sticky Note — Validation, Sticky Note — Workflow Overview, Sticky Note1, Sticky Note10, Sticky Note100, Sticky Note101, Sticky Note102, Sticky Note103, Sticky Note104, Sticky Note105, Sticky Note106, Sticky Note107, Sticky Note108, Sticky Note109, Sticky Note11, Sticky Note110, Sticky Note12, Sticky Note13, Sticky Note14, Sticky Note15, Sticky Note16, Sticky Note17, Sticky Note18, Sticky Note19, Sticky Note2, Sticky Note20, Sticky Note21, Sticky Note22, Sticky Note23, Sticky Note24, Sticky Note25, Sticky Note26, Sticky Note27, Sticky Note28, Sticky Note29, Sticky Note3, Sticky Note30, Sticky Note31, Sticky Note32, Sticky Note33, Sticky Note34, Sticky Note35, Sticky Note36, Sticky Note37, Sticky Note38, Sticky Note39, Sticky Note4, Sticky Note40, Sticky Note41, Sticky Note42, Sticky Note43, Sticky Note44, Sticky Note45, Sticky Note46, Sticky Note47, Sticky Note48, Sticky Note49, Sticky Note5, Sticky Note50, Sticky Note51, Sticky Note52, Sticky Note53, Sticky Note54, Sticky Note55, Sticky Note56, Sticky Note57, Sticky Note58, Sticky Note59, Sticky Note6, Sticky Note60, Sticky Note61, Sticky Note62, Sticky Note63, Sticky Note64, Sticky Note65, Sticky Note66, Sticky Note67, Sticky Note68, Sticky Note69, Sticky Note7, Sticky Note70, Sticky Note71, Sticky Note72, Sticky Note73, Sticky Note74, Sticky Note75, Sticky Note76, Sticky Note77, Sticky Note78, Sticky Note79, Sticky Note8, Sticky Note80, Sticky Note81, Sticky Note82, Sticky Note83, Sticky Note84, Sticky Note85, Sticky Note86, Sticky Note87, Sticky Note88, Sticky Note89, Sticky Note9, Sticky Note90, Sticky Note91, Sticky Note92, Sticky Note93, Sticky Note94, Sticky Note95, Sticky Note96, Sticky Note97, Sticky Note98, Sticky Note99, Triggers Section Sticky Note, Triggers Section Sticky Note1, Triggers Section Sticky Note2, Usage Instructions, Warning1, Workflow Description, ℹ️ Viewer Tips, ℹ️ Viewer Tips1, ℹ️ Viewer Tips2, ℹ️ Viewer Tips3, ℹ️ Viewer Tips4, ℹ️ Viewer Tips5, ℹ️ Viewer Tips6, ℹ️ Viewer Tips7, ℹ️ Viewer Tips9, 📝 Setup & Instructions

## Top Workflows To Review First

| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |
|------|----------|-------------|-----------|----------|------|-------------|
| 1 | Workflow Patterns & Boilerplate for Scaling up | 100 | 35 | 1 | 1 | LOOP_HTTP, LARGE_WF, NO_ERROR_HANDLING |
| 2 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | 100 | 100 | 0 | 1 | LOOP_HTTP, AI_NODE, LARGE_WF |
| 3 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 4 | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | 100 | 95 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 5 | Autonomous B2B Supplier Price Negotiation Agent | 100 | 90 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 6 | Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review | 95 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 7 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | 95 | 80 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 8 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | 95 | 65 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 9 | Track AI agent token usage and estimate costs in Google Sheets | 90 | 75 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 10 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | 90 | 60 | 0 | 0 | AI_NODE, LARGE_WF, NO_ERROR_HANDLING |
| 11 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 80 | 65 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 12 | Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter | 80 | 65 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 13 | AI Lead Machine Agent | 75 | 60 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 14 | Auto Generate Descriptive Node Names with AI for Workflow Readability | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 15 | Comment Analyse and Reporter | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 16 | n8n_fluidx_create_session | 65 | 50 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 17 | Multi-Agent Evaluation (eval nodes) | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 18 | Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 19 | Jarvis template | 60 | 30 | 0 | 0 | AI_NODE, LARGE_WF, NO_ERROR_HANDLING |
| 20 | Triage emails and draft Gmail replies using Gemini and Google Calendar | 60 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, HIGH_FAN_OUT |
| 21 | Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | 50 | 35 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 22 | Build your first AI agent | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 23 | RAG Pipeline | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 24 | Talk to your Google Sheets using ChatGPT-5 | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 25 | eCommerce Ai Agent ( Telegram Bot ) | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 26 | 🤖 Build an interactive AI agent with chat interface and multiple tools | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 27 | Create Video with Google Veo3 and Upload to Youtube | 35 | 20 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 28 | Smart Inventory Replenishment & Auto-Purchase Orders | 35 | 20 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 29 | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | 30 | 0 | 0 | 0 | NO_ERROR_HANDLING, HIGH_FAN_OUT |
| 30 | 🧑‍🎓 Test your data access techniques with progressive expression challenges | 30 | 0 | 0 | 0 | LARGE_WF, NO_ERROR_HANDLING |
| 31 | Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 32 | Process large documents with OCR using SubworkflowAI and Gemini | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 33 | New Appointment → Welcome SMS | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 34 | Physician Profile Enricher | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 35 | 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 36 | 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |

## Workflow Inventory

| # | Workflow | Active | Nodes | Triggers | Risk Score |
|---|----------|--------|-------|----------|------------|
| 1 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ❌ | 35 | n8n-nodes-base.telegramTrigger | 100 |
| 2 | n8n_fluidx_create_session | ❌ | 50 | n8n-nodes-base.formTrigger | 65 |
| 3 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | ❌ | 28 | n8n-nodes-base.telegramTrigger | 80 |
| 4 | Create Video with Google Veo3 and Upload to Youtube | ❌ | 23 | n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger | 35 |
| 5 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | ❌ | 29 | n8n-nodes-base.scheduleTrigger | 95 |
| 6 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | ❌ | 32 | n8n-nodes-base.scheduleTrigger | 95 |
| 7 | RAG Pipeline | ❌ | 13 | @n8n/n8n-nodes-langchain.chatTrigger, n8n-nodes-base.formTrigger | 45 |
| 8 | 🤖 Build an interactive AI agent with chat interface and multiple tools | ❌ | 17 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 9 | Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | ❌ | 16 | n8n-nodes-base.scheduleTrigger | 60 |
| 10 | Build your first AI agent | ❌ | 13 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 11 | Talk to your Google Sheets using ChatGPT-5 | ❌ | 11 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 12 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | ❌ | 63 | n8n-nodes-base.executeWorkflowTrigger, n8n-nodes-base.telegramTrigger | 90 |
| 13 | Jarvis template | ❌ | 52 | @n8n/n8n-nodes-langchain.mcpTrigger, n8n-nodes-base.telegramTrigger | 60 |
| 14 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | ❌ | 63 | n8n-nodes-base.scheduleTrigger, n8n-nodes-base.telegramTrigger | 100 |
| 15 | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | ❌ | 23 | n8n-nodes-base.scheduleTrigger | 30 |
| 16 | Smart Inventory Replenishment & Auto-Purchase Orders | ❌ | 24 | n8n-nodes-base.scheduleTrigger | 35 |
| 17 | Process large documents with OCR using SubworkflowAI and Gemini | ❌ | 16 | n8n-nodes-base.manualTrigger | 20 |
| 18 | Auto Generate Descriptive Node Names with AI for Workflow Readability | ❌ | 33 | n8n-nodes-base.formTrigger, n8n-nodes-base.manualTrigger | 75 |
| 19 | Workflow Patterns & Boilerplate for Scaling up | ❌ | 244 | @bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger, n8n-nodes-base.errorTrigger, n8n-nodes-base.executeWorkflowTrigger, n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger | 100 |
| 20 | 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners | ❌ | 24 | n8n-nodes-base.manualTrigger | 15 |
| 21 | 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners | ❌ | 27 | n8n-nodes-base.manualTrigger | 15 |
| 22 | Multi-Agent Evaluation (eval nodes) | ❌ | 15 | @n8n/n8n-nodes-langchain.chatTrigger, n8n-nodes-base.evaluationTrigger | 60 |
| 23 | Track AI agent token usage and estimate costs in Google Sheets | ❌ | 24 | n8n-nodes-base.executeWorkflowTrigger, n8n-nodes-base.manualTrigger | 90 |
| 24 | 🧑‍🎓 Test your data access techniques with progressive expression challenges | ❌ | 62 | n8n-nodes-base.manualTrigger | 30 |
| 25 | Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | ❌ | 19 | n8n-nodes-base.formTrigger | 20 |
| 26 | Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | ❌ | 26 | n8n-nodes-base.formTrigger | 50 |
| 27 | Physician Profile Enricher | ❌ | 11 | n8n-nodes-base.manualTrigger | 15 |
| 28 | eCommerce Ai Agent ( Telegram Bot ) | ❌ | 16 | n8n-nodes-base.telegramTrigger | 45 |
| 29 | Comment Analyse and Reporter | ❌ | 35 | n8n-nodes-base.googleSheetsTrigger | 75 |
| 30 | New Appointment → Welcome SMS | ❌ | 20 | n8n-nodes-base.scheduleTrigger, n8n-nodes-base.twilioTrigger, n8n-nodes-base.typeformTrigger | 15 |
*... and 6 more workflows (table truncated for readability)*

## Quick Wins

1. Add rate limits and concurrency controls around the HTTP loop in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide'.
2. Add rate limits and concurrency controls around the HTTP loop in 'n8n_fluidx_create_session'.
3. Add rate limits and concurrency controls around the HTTP loop in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini'.
4. Add rate limits and concurrency controls around the HTTP loop in 'Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq'.
5. Add rate limits and concurrency controls around the HTTP loop in 'Workflow Patterns & Boilerplate for Scaling up'.

## Top Risks

| Severity | Category | Workflow | Message |
|----------|----------|----------|---------|
| CRITICAL | complexity | Workflow Patterns & Boilerplate for Scaling up | Workflow has 240 nodes, making it very complex to maintain and debug |
| HIGH | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | n8n_fluidx_create_session | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Workflow Patterns & Boilerplate for Scaling up | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | AI Lead Machine Agent | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate |

## Cost Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| HIGH | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Merge1, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Search Trends with Perplexity | AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Script with GPT-4 | AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Caption with GPT-4 | AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate |
| LOW | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | Workflow has 5 HTTP Request nodes, increasing external dependency and cost |
| HIGH | n8n_fluidx_create_session | Split photoRefs (Item Lists), Merge Analyze + URL, Merge photoRefs, Merge, fluidX API - Media Info HTTP Request GET, fluidX API - Create Session, fluidX API - Send SMS User, fluidX API - Get Session Info, fluidX API - Download Photo THEEYE Session, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | n8n_fluidx_create_session | Analyze image | AI/LLM node 'Analyze image' has variable token-based cost that can escalate |
| LOW | n8n_fluidx_create_session | fluidX API - Media Info HTTP Request GET, fluidX API - Create Session, fluidX API - Send SMS User, fluidX API - Get Session Info, fluidX API - Download Photo THEEYE Session, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary | Workflow has 7 HTTP Request nodes, increasing external dependency and cost |
| HIGH | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Merge, Merge1, 1 hour, 15 min, 1 day, News | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Google Gemini Chat Model1 | AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Crypto Agent | AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate |
| LOW | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 1 hour, 15 min, 1 day, News | Workflow has 4 HTTP Request nodes, increasing external dependency and cost |
| MEDIUM | Create Video with Google Veo3 and Upload to Youtube | Generate title | AI/LLM node 'Generate title' has variable token-based cost that can escalate |
| LOW | Create Video with Google Veo3 and Upload to Youtube | Get status, Create Video, Get Url Video, Get File Video, HTTP Request | Workflow has 5 HTTP Request nodes, increasing external dependency and cost |
| MEDIUM | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | AI Agent: Generate Video Concept | AI/LLM node 'AI Agent: Generate Video Concept' has variable token-based cost that can escalate |
| MEDIUM | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | LLM: Generate Idea & Caption (GPT-4.1) | AI/LLM node 'LLM: Generate Idea & Caption (GPT-4.1)' has variable token-based cost that can escalate |
| MEDIUM | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | AI Agent: Create Veo3-Compatible Prompt | AI/LLM node 'AI Agent: Create Veo3-Compatible Prompt' has variable token-based cost that can escalate |
| MEDIUM | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | LLM: Format Prompt for Veo3 (GPT-4.1) | AI/LLM node 'LLM: Format Prompt for Veo3 (GPT-4.1)' has variable token-based cost that can escalate |
| LOW | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | Upload Video to Blotato, INSTAGRAM, YOUTUBE, TIKTOK, FACEBOOK, THREADS, TWETTER, LINKEDIN, BLUESKY, PINTEREST, Call Veo3 API to Generate Video, Retrieve Final Video URL from Veo3 | Workflow has 12 HTTP Request nodes, increasing external dependency and cost |
| MEDIUM | Automated AI YouTube Shorts Factory for ASMR (Seedance) | OpenAI Chat Model | AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate |
*... and 86 more findings (table truncated for readability)*

## Estimated Cost Exposure

- **💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **n8n_fluidx_create_session:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Analyze image' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Create Video with Google Veo3 and Upload to Youtube:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Generate title' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent: Generate Video Concept' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM: Generate Idea & Caption (GPT-4.1)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent: Create Veo3-Compatible Prompt' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM: Format Prompt for Veo3 (GPT-4.1)' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 12 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Automated AI YouTube Shorts Factory for ASMR (Seedance):** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Prompts AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '1. Generate Trendy Idea' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '2. Enrich Idea into Plan' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **RAG Pipeline:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Ollama Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **🤖 Build an interactive AI agent with chat interface and multiple tools:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Gemini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '🤖 SERP Scraper Agent (MCP)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Build your first AI agent:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Your First AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Connect Gemini' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Talk to your Google Sheets using ChatGPT-5:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Talk to Your Data' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Register Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Cal IA Agent' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Jarvis template:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Jarvis' has variable token-based cost that can escalate
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
- **PPC campaign intelligence & optimization with Google Ads, Sheets & Slack:** 🟢 LOW — minimal (heuristic)
- **Smart Inventory Replenishment & Auto-Purchase Orders:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'AI Demand Forecasting' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Process large documents with OCR using SubworkflowAI and Gemini:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
- **Auto Generate Descriptive Node Names with AI for Workflow Readability:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Prepare LLM Validation Data' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Node Rename Mapping' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM Flow Sticky Note' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Workflow Patterns & Boilerplate for Scaling up:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
- **🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners:** 🟢 LOW — minimal (heuristic)
- **🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners:** 🟢 LOW — minimal (heuristic)
- **Multi-Agent Evaluation (eval nodes):** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Search Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Embeddings OpenAI' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Track AI agent token usage and estimate costs in Google Sheets:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Sum Token Totals - aggregate by model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gemini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Anthropic' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **🧑‍🎓 Test your data access techniques with progressive expression challenges:** 🟢 LOW — minimal (heuristic)
- **Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 8 HTTP Request nodes, increasing external dependency and cost
- **Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent - Select Viral Clips' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Physician Profile Enricher:** 🟢 LOW — minimal (heuristic)
- **eCommerce Ai Agent ( Telegram Bot ):** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Comment Analyse and Reporter:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Sentiment & Intent Detection Agent1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Reply Drafting Agent1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Azure OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Azure OpenAI Chat Model4' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **New Appointment → Welcome SMS:** 🟢 LOW — minimal (heuristic)
- **Autonomous B2B Supplier Price Negotiation Agent:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node '⚡ LLM — Draft Generator (GPT-4o)1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '🧠 MCTS — Generate 3 Negotiation Drafts1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '⚡ LLM — Critique Model (GPT-4o)1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '🔁 Self-Critique Round 1 — Refine Draft1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '⚡ LLM — Final Polish Model (GPT-4o)1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '🔁 Self-Critique Round 2 — Final Polish1' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Generate Personalized Email' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **AI Lead Machine Agent:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Agent One' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Judge Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 6 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Triage emails and draft Gmail replies using Gemini and Google Calendar:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Draft and Label Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gemini Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Knowledge Base Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Embeddings OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Embeddings Generator' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI1' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count

*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*

## Operational Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| LOW | Workflow Patterns & Boilerplate for Scaling up | Webhook | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |

## Complexity Findings

| Severity | Workflow | Finding |
|----------|----------|---------|
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |
| MEDIUM | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | Node 'Upload Video to Blotato' has 10 outgoing connections (high fan-out) |
| MEDIUM | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | Workflow has 63 nodes, which increases complexity |
| MEDIUM | Jarvis template | Workflow has 52 nodes, which increases complexity |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Workflow has 63 nodes, which increases complexity |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Node 'Branch by Intent' has 6 outgoing connections (high fan-out) |
| MEDIUM | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | Node 'Route by Performance' has 8 outgoing connections (high fan-out) |
| CRITICAL | Workflow Patterns & Boilerplate for Scaling up | Workflow has 240 nodes, making it very complex to maintain and debug |
| MEDIUM | Workflow Patterns & Boilerplate for Scaling up | Node 'When Executed by [trigger workflow]' has 5 outgoing connections (high fan-out) |
| MEDIUM | 🧑‍🎓 Test your data access techniques with progressive expression challenges | Workflow has 62 nodes, which increases complexity |
| MEDIUM | Triage emails and draft Gmail replies using Gemini and Google Calendar | Node 'Route by Draft Type' has 6 outgoing connections (high fan-out) |
| MEDIUM | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | Node 'Route Document Types' has 11 outgoing connections (high fan-out) |

## Recommendations

1. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
2. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
3. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
4. Review if all external HTTP calls are necessary. Consider caching or batching to reduce dependency costs.
5. Split large workflows into smaller focused workflows to improve maintainability and reduce blast radius.
6. Review webhook chain depth and add idempotency keys to prevent duplicate processing.

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

### n8n_fluidx_create_session

- **ID:** r8Qe7WuBooLIDbHv
- **Active:** ❌
- **Nodes:** 50
- **Triggers:** n8n-nodes-base.formTrigger
- **Scores:** Cost=50 | Ops=0 | Complexity=0 | Overall=65

**Findings:**
  - [HIGH] [cost] LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
    - Nodes: Split photoRefs (Item Lists), Merge Analyze + URL, Merge photoRefs, Merge, fluidX API - Media Info HTTP Request GET, fluidX API - Create Session, fluidX API - Send SMS User, fluidX API - Get Session Info, fluidX API - Download Photo THEEYE Session, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Analyze image' has variable token-based cost that can escalate
    - Nodes: Analyze image
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
    - Nodes: fluidX API - Media Info HTTP Request GET, fluidX API - Create Session, fluidX API - Send SMS User, fluidX API - Get Session Info, fluidX API - Download Photo THEEYE Session, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary

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

### Create Video with Google Veo3 and Upload to Youtube

- **ID:** eZdA1ppXX1RX9AqubV9gu
- **Active:** ❌
- **Nodes:** 23
- **Triggers:** n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=20 | Ops=0 | Complexity=0 | Overall=35

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Generate title' has variable token-based cost that can escalate
    - Nodes: Generate title
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
    - Nodes: Get status, Create Video, Get Url Video, Get File Video, HTTP Request

### Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide

- **ID:** eFkkWqS5KdrxZ43P
- **Active:** ❌
- **Nodes:** 29
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=65 | Ops=0 | Complexity=15 | Overall=95

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Agent: Generate Video Concept' has variable token-based cost that can escalate
    - Nodes: AI Agent: Generate Video Concept
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'LLM: Generate Idea & Caption (GPT-4.1)' has variable token-based cost that can escalate
    - Nodes: LLM: Generate Idea & Caption (GPT-4.1)
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Agent: Create Veo3-Compatible Prompt' has variable token-based cost that can escalate
    - Nodes: AI Agent: Create Veo3-Compatible Prompt
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'LLM: Format Prompt for Veo3 (GPT-4.1)' has variable token-based cost that can escalate
    - Nodes: LLM: Format Prompt for Veo3 (GPT-4.1)
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 12 HTTP Request nodes, increasing external dependency and cost
    - Nodes: Upload Video to Blotato, INSTAGRAM, YOUTUBE, TIKTOK, FACEBOOK, THREADS, TWETTER, LINKEDIN, BLUESKY, PINTEREST, Call Veo3 API to Generate Video, Retrieve Final Video URL from Veo3
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Upload Video to Blotato' has 10 outgoing connections (high fan-out)
    - Nodes: Upload Video to Blotato

### Automated AI YouTube Shorts Factory for ASMR (Seedance)

- **ID:** LPUpZtHK7gGRA5wa
- **Active:** ❌
- **Nodes:** 32
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=80 | Ops=0 | Complexity=0 | Overall=95

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Prompts AI Agent' has variable token-based cost that can escalate
    - Nodes: Prompts AI Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node '1. Generate Trendy Idea' has variable token-based cost that can escalate
    - Nodes: 1. Generate Trendy Idea
  - [MEDIUM] [cost] AI_NODE: AI/LLM node '2. Enrich Idea into Plan' has variable token-based cost that can escalate
    - Nodes: 2. Enrich Idea into Plan
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
    - Nodes: Create Sounds, Get Sounds, Sequence Video, Get Final Video, Create Clips, Get Clips, Download Final Video

### RAG Pipeline

- **ID:** L9nteAq0NLYqIGxH
- **Active:** ❌
- **Nodes:** 13
- **Triggers:** @n8n/n8n-nodes-langchain.chatTrigger, n8n-nodes-base.formTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
    - Nodes: AI Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Ollama Chat Model' has variable token-based cost that can escalate
    - Nodes: Ollama Chat Model
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

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

### Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis

- **ID:** 5962
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

*... and 26 more workflows with hidden details (table truncated for readability)*

## Workflow Risk Ranking

| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |
|------|----------|---------|------|-----|------------|----------|
| 1 | Workflow Patterns & Boilerplate for Scaling up | 100 | 35 | 5 | 65 | 6 |
| 2 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | 100 | 100 | 0 | 30 | 13 |
| 3 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 15 | 7 |
| 4 | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | 100 | 95 | 0 | 15 | 9 |
| 5 | Autonomous B2B Supplier Price Negotiation Agent | 100 | 90 | 0 | 0 | 7 |
| 6 | Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review | 95 | 80 | 0 | 0 | 6 |
| 7 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | 95 | 80 | 0 | 0 | 7 |
| 8 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | 95 | 65 | 0 | 15 | 7 |
| 9 | Track AI agent token usage and estimate costs in Google Sheets | 90 | 75 | 0 | 0 | 6 |
| 10 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | 90 | 60 | 0 | 15 | 6 |
| 11 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 80 | 65 | 0 | 0 | 5 |
| 12 | Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter | 80 | 65 | 0 | 0 | 5 |
| 13 | AI Lead Machine Agent | 75 | 60 | 0 | 0 | 4 |
| 14 | Auto Generate Descriptive Node Names with AI for Workflow Readability | 75 | 60 | 0 | 0 | 5 |
| 15 | Comment Analyse and Reporter | 75 | 60 | 0 | 0 | 5 |
| 16 | n8n_fluidx_create_session | 65 | 50 | 0 | 0 | 4 |
| 17 | Multi-Agent Evaluation (eval nodes) | 60 | 45 | 0 | 0 | 4 |
| 18 | Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | 60 | 45 | 0 | 0 | 4 |
| 19 | Jarvis template | 60 | 30 | 0 | 15 | 4 |
| 20 | Triage emails and draft Gmail replies using Gemini and Google Calendar | 60 | 30 | 0 | 15 | 4 |
| 21 | Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | 50 | 35 | 0 | 0 | 4 |
| 22 | Build your first AI agent | 45 | 30 | 0 | 0 | 3 |
| 23 | RAG Pipeline | 45 | 30 | 0 | 0 | 3 |
| 24 | Talk to your Google Sheets using ChatGPT-5 | 45 | 30 | 0 | 0 | 3 |
| 25 | eCommerce Ai Agent ( Telegram Bot ) | 45 | 30 | 0 | 0 | 3 |
| 26 | 🤖 Build an interactive AI agent with chat interface and multiple tools | 45 | 30 | 0 | 0 | 3 |
| 27 | Create Video with Google Veo3 and Upload to Youtube | 35 | 20 | 0 | 0 | 3 |
| 28 | Smart Inventory Replenishment & Auto-Purchase Orders | 35 | 20 | 0 | 0 | 3 |
| 29 | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | 30 | 0 | 0 | 15 | 2 |
| 30 | 🧑‍🎓 Test your data access techniques with progressive expression challenges | 30 | 0 | 0 | 15 | 2 |
| 31 | Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | 20 | 5 | 0 | 0 | 2 |
| 32 | Process large documents with OCR using SubworkflowAI and Gemini | 20 | 5 | 0 | 0 | 2 |
| 33 | New Appointment → Welcome SMS | 15 | 0 | 0 | 0 | 1 |
| 34 | Physician Profile Enricher | 15 | 0 | 0 | 0 | 1 |
| 35 | 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | 1 |
| 36 | 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | 1 |

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