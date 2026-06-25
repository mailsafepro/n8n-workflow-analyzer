# Client Action Plan — n8n Workflow Audit

## How to Read This Plan

This plan is organized by priority. Start with Priority 0, then work through
Cost Controls, Reliability, and Maintainability. The 7-day plan at the end
provides a suggested schedule.

## Priority 0 — Highest-Risk Workflows

The following items require immediate attention:

- [CRITICAL] Workflow Patterns & Boilerplate for Scaling up: Workflow has 240 nodes, making it very complex to maintain and debug

## Priority 1 — Cost Controls

- Add rate limits, concurrency controls, or move HTTP calls outside loops in 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide, n8n_fluidx_create_session, Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini, Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq, Workflow Patterns & Boilerplate for Scaling up, Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter, AI Lead Machine Agent, Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review.
- Set usage limits and monitoring for AI/API nodes before production.
-   Highest AI exposure:
-     - Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq: 8 AI nodes
-     - Autonomous B2B Supplier Price Negotiation Agent: 6 AI nodes
-     - AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG: 6 AI nodes
-     - Automated AI YouTube Shorts Factory for ASMR (Seedance): 5 AI nodes
-     - Track AI agent token usage and estimate costs in Google Sheets: 5 AI nodes
- Review high fan-out nodes that may cause unexpected API load in 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide, Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide, Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq, PPC campaign intelligence & optimization with Google Ads, Sheets & Slack, Workflow Patterns & Boilerplate for Scaling up, Triage emails and draft Gmail replies using Gemini and Google Calendar, AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG.
- Review if all external HTTP calls in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide' are necessary (Build Public Image URL, Download VEED Video, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL).
- Review if all external HTTP calls in 'n8n_fluidx_create_session' are necessary (fluidX API - Create Session, fluidX API - Download Photo THEEYE Session, fluidX API - Get Session Info, fluidX API - Media Info HTTP Request GET, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary, fluidX API - Send SMS User).
- Review if all external HTTP calls in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini' are necessary (1 day, 1 hour, 15 min, News).
- Review if all external HTTP calls in 'Create Video with Google Veo3 and Upload to Youtube' are necessary (Create Video, Get File Video, Get Url Video, Get status, HTTP Request).
- Review if all external HTTP calls in 'Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide' are necessary (BLUESKY, Call Veo3 API to Generate Video, FACEBOOK, INSTAGRAM, LINKEDIN, PINTEREST, Retrieve Final Video URL from Veo3, THREADS, TIKTOK, TWETTER, Upload Video to Blotato, YOUTUBE).
- Review if all external HTTP calls in 'Automated AI YouTube Shorts Factory for ASMR (Seedance)' are necessary (Create Clips, Create Sounds, Download Final Video, Get Clips, Get Final Video, Get Sounds, Sequence Video).
- Review if all external HTTP calls in 'Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq' are necessary (Comment, If Reddit?, If n8n Community?, Reddit, Reddit Search page (no time), Reddit Search page JSON (has time), Reddit Search page JSON (no keyword), n8n Community Fetch, n8n Community Fetch JSON).
- Review if all external HTTP calls in 'Smart Inventory Replenishment & Auto-Purchase Orders' are necessary (Fetch Current Inventory, Fetch Sales Velocity, Log to ERP System, Send PO to Supplier).
- Review if all external HTTP calls in 'Process large documents with OCR using SubworkflowAI and Gemini' are necessary (Check Job Status, Extract API, Get Dataset, Get Dataset Items).
- Review if all external HTTP calls in 'Workflow Patterns & Boilerplate for Scaling up' are necessary (B1 - Get Items, B2 - Get Items, B3 - Get Items, C2 - Get Items, C3 - Get Items, Search Companies by Bedrijfsdata ID, Search Companies by Domain).
- Review if all external HTTP calls in 'Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X' are necessary (Animate Image, Check Animation Status, Check Colorization Status, Colorize Image, Download Video, Get Animated Video, Get Colorized Image, Upload Image to imgbb).
- Review if all external HTTP calls in 'Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini' are necessary (Check Audio Job Status, Check Short Job Status, Download Audio, Download Short, FFmpeg: Extract Audio, FFmpeg: Upload & Cut, Whisper: Transcribe with Timestamps).
- Review if all external HTTP calls in 'Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter' are necessary (Get LinkedIn Company, Get LinkedIn Person, Google Search for Company LinkedIn, Google Search for Person LinkedIn).
- Review if all external HTTP calls in 'Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review' are necessary (Crunchbase_URL, Linkedin_URL, Linkedin_URL_COMPANY, results, results1, results2).
- Review if all external HTTP calls in 'AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG' are necessary (Download Document, Download Image, Download Voicemail).

## Priority 2 — Reliability

- Configure error workflows for the 36 workflows without error handling:
-   - 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide
-   - n8n_fluidx_create_session
-   - Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini
-   - Create Video with Google Veo3 and Upload to Youtube
-   - Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide
-   - Automated AI YouTube Shorts Factory for ASMR (Seedance)
-   - RAG Pipeline
-   - 🤖 Build an interactive AI agent with chat interface and multiple tools
-   - Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis
-   - Build your first AI agent
-   *... and 26 more workflows (table truncated for readability)*
- Add idempotency keys and review webhook chain depth to prevent cascading failures.
- Review isolated nodes (no connections) — they may be unused or misconfigured.

## Priority 3 — Maintainability

- Split large workflows into smaller, focused workflows to improve maintainability.
- Review 6 unknown/custom node types for compatibility and support:
-   - `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro`
-   - `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger`
-   - `n8n-nodes-browseract.browserAct`
-   - `n8n-nodes-connectsafely-ai.connectSafelyLinkedIn`
-   - `n8n-nodes-serpapi.serpApi`
-   - `n8n-nodes-upload-post.uploadPost`
- Review 5 disabled nodes — clean up or re-enable if needed.
- Review credential references for governance and rotation policies.

## Suggested 7-Day Plan

**Day 1 — Initial Review:**
- Review top workflow: Workflow Patterns & Boilerplate for Scaling up
- Identify production-critical paths

**Day 2 — Cost Controls:**
- Add rate limits and concurrency controls around loops in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide'
- Add rate limits and concurrency controls around loops in 'n8n_fluidx_create_session'
- Add rate limits and concurrency controls around loops in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini'
- Add rate limits and concurrency controls around loops in 'Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq'
- Add rate limits and concurrency controls around loops in 'Workflow Patterns & Boilerplate for Scaling up'
- Add rate limits and concurrency controls around loops in 'Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter'
- Add rate limits and concurrency controls around loops in 'AI Lead Machine Agent'
- Add rate limits and concurrency controls around loops in 'Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review'
- Set spend limits and monitoring for AI/API nodes
- Document current trigger configurations

**Day 3 — Reliability:**
- Configure error handling for 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide, n8n_fluidx_create_session, Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini, Create Video with Google Veo3 and Upload to Youtube, Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide, Automated AI YouTube Shorts Factory for ASMR (Seedance), RAG Pipeline, 🤖 Build an interactive AI agent with chat interface and multiple tools, Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis, Build your first AI agent, Talk to your Google Sheets using ChatGPT-5, Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets, Jarvis template, Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq, PPC campaign intelligence & optimization with Google Ads, Sheets & Slack, Smart Inventory Replenishment & Auto-Purchase Orders, Process large documents with OCR using SubworkflowAI and Gemini, Auto Generate Descriptive Node Names with AI for Workflow Readability, Workflow Patterns & Boilerplate for Scaling up, 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners, 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners, Multi-Agent Evaluation (eval nodes), Track AI agent token usage and estimate costs in Google Sheets, 🧑‍🎓 Test your data access techniques with progressive expression challenges, Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X, Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini, Physician Profile Enricher, eCommerce Ai Agent ( Telegram Bot ), Comment Analyse and Reporter, New Appointment → Welcome SMS, Autonomous B2B Supplier Price Negotiation Agent, Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter, AI Lead Machine Agent, Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review, Triage emails and draft Gmail replies using Gemini and Google Calendar, AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG
- Add idempotency guards to webhook chains
- Review retry behavior for HTTP requests

**Day 4 — Cost Monitoring:**
- Estimate token/API costs for AI nodes
- Review external API call volume and pricing
- Add monitoring for execution count per workflow

**Day 5 — Maintainability:**
- Review unknown/custom node types for compatibility
- Clean up or document disabled nodes
- Plan splitting large workflows into smaller units
- Document workflow ownership

**Day 6 — Validation:**
- Validate changes in staging environment
- Test error handling paths
- Verify cost controls are working as expected

**Day 7 — Documentation & Handover:**
- Document final architecture
- Update runbooks and alerting
- Schedule follow-up audit

*Adjust timeline based on workflow criticality and team capacity.*

## Open Questions For Client

- Which workflows are production-critical and need the highest reliability guarantees?
- What is the acceptable monthly execution volume and budget per workflow?
- Which external AI/API services have usage-based pricing and what are the current monthly costs?
- What is the typical batch size processed in loop workflows?
- Are any workflows customer-facing or tied to SLAs?
- Who manages credential rotation and what is the current policy?
- Who maintains the custom node types and are they actively supported?
- Who owns each workflow and how is ownership documented?

---
*Generated by n8n Cost Analyzer v0.7.1 — Audit Pack*