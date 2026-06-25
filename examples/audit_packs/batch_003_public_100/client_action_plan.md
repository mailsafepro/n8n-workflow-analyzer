# Client Action Plan — n8n Workflow Audit

## How to Read This Plan

This plan is organized by priority. Start with Priority 0, then work through
Cost Controls, Reliability, and Maintainability. The 7-day plan at the end
provides a suggested schedule.

## Priority 0 — Highest-Risk Workflows

The following items require immediate attention:

- [CRITICAL] Workflow Patterns & Boilerplate for Scaling up: Workflow has 240 nodes, making it very complex to maintain and debug

## Priority 1 — Cost Controls

- Add rate limits, concurrency controls, or move HTTP calls outside loops in 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide, 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide, n8n_fluidx_create_session, Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini, 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide, Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq, 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE, Workflow Patterns & Boilerplate for Scaling up, Fetch live ETF metrics from JustETF to Excel with one-click updates, Apply to Jobs from Excel and Track Application Status, 💥 Automate Scrape Google Maps Business Leads (Email, Phone, Website) using Apify -vide II, Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter, AI Lead Machine Agent, Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review, Automated n8n workflow backup to GitHub with deletion tracking, Reels Trends Watcher, AI Automated TikTok/Youtube Shorts/Reels Generator, Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot, Auto WordPress Blog Generator (GPT + Postgres + WP Media), Export AI agent conversation logs from Postgres to Google Sheets, Generate Shopify product listings from images with Gemini AI and Airtable, Automate Template Delivery to Customers from Stripe Payments.
- Set usage limits and monitoring for AI/API nodes before production.
-   Highest AI exposure:
-     - Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq: 8 AI nodes
-     - Dynamically Selects Models Based on Input Type: 8 AI nodes
-     - LinkedIn AI Content Automation - Agentic Vibe: 7 AI nodes
-     - 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE: 7 AI nodes
-     - AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG: 6 AI nodes
- Review high fan-out nodes that may cause unexpected API load in 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide, 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide, Triage emails and draft Gmail replies using Gemini and Google Calendar, AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG, Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide, 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide, Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq, 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE, PPC campaign intelligence & optimization with Google Ads, Sheets & Slack, Workflow Patterns & Boilerplate for Scaling up, Build your own N8N workflows MCP server, Sync New Shopify Customers to Odoo Contacts with Email, SMS & WhatsApp Notifications.
- Review if all external HTTP calls in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide' are necessary (Build Public Image URL, Download VEED Video, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL).
- Review if all external HTTP calls in 'n8n_fluidx_create_session' are necessary (fluidX API - Create Session, fluidX API - Download Photo THEEYE Session, fluidX API - Get Session Info, fluidX API - Media Info HTTP Request GET, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary, fluidX API - Send SMS User).
- Review if all external HTTP calls in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini' are necessary (1 day, 1 hour, 15 min, News).
- Review if all external HTTP calls in 'AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG' are necessary (Download Document, Download Image, Download Voicemail).
- Review if all external HTTP calls in 'Create Video with Google Veo3 and Upload to Youtube' are necessary (Create Video, Get File Video, Get Url Video, Get status, HTTP Request).
- Review if all external HTTP calls in 'Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide' are necessary (BLUESKY, Call Veo3 API to Generate Video, FACEBOOK, INSTAGRAM, LINKEDIN, PINTEREST, Retrieve Final Video URL from Veo3, THREADS, TIKTOK, TWETTER, Upload Video to Blotato, YOUTUBE).
- Review if all external HTTP calls in 'Automated AI YouTube Shorts Factory for ASMR (Seedance)' are necessary (Create Clips, Create Sounds, Download Final Video, Get Clips, Get Final Video, Get Sounds, Sequence Video).
- Review if all external HTTP calls in '💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide' are necessary (Generate ASMR Sound (Fal AI), Generate Video Clips (seedance), Merge Clips into Final Video (Fal AI), Retrieve Final Merged Video, Retrieve Final Sound Output, Retrieve Video Clips).
- Review if all external HTTP calls in 'Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X' are necessary (Animate Image, Check Animation Status, Check Colorization Status, Colorize Image, Download Video, Get Animated Video, Get Colorized Image, Upload Image to imgbb).
- Review if all external HTTP calls in 'Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq' are necessary (Comment, If Reddit?, If n8n Community?, Reddit, Reddit Search page (no time), Reddit Search page JSON (has time), Reddit Search page JSON (no keyword), n8n Community Fetch, n8n Community Fetch JSON).
- Review if all external HTTP calls in '💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE' are necessary (ChatGPT Image – fetch generated image, Check Merge Status, Download Video from VEO3, Download image from Seedream, Generate 4o Image（GPT IMAG 1）, Generate Video with VEO3, Merge 3 Videos, NanoBanana – fetch edited image, NanoBanana: Create Image, Seedream: Generate image from texte).
- Review if all external HTTP calls in 'Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini' are necessary (Check Audio Job Status, Check Short Job Status, Download Audio, Download Short, FFmpeg: Extract Audio, FFmpeg: Upload & Cut, Whisper: Transcribe with Timestamps).
- Review if all external HTTP calls in 'Loyverse Sales Report Agent' are necessary (Get Yesterday's Receipts From Loyverse, Get Yesterday's Shifts From Loyverse, Get all products from Loyverse).
- Review if all external HTTP calls in 'Smart Inventory Replenishment & Auto-Purchase Orders' are necessary (Fetch Current Inventory, Fetch Sales Velocity, Log to ERP System, Send PO to Supplier).
- Review if all external HTTP calls in 'Process large documents with OCR using SubworkflowAI and Gemini' are necessary (Check Job Status, Extract API, Get Dataset, Get Dataset Items).
- Review if all external HTTP calls in 'Workflow Patterns & Boilerplate for Scaling up' are necessary (B1 - Get Items, B2 - Get Items, B3 - Get Items, C2 - Get Items, C3 - Get Items, Search Companies by Bedrijfsdata ID, Search Companies by Domain).
- Review if all external HTTP calls in 'AI Self-Healing Engine & Auto-Patching System' are necessary (Get Workflow JSON, Retry Execution, Update Workflow).
- Review if all external HTTP calls in 'Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter' are necessary (Get LinkedIn Company, Get LinkedIn Person, Google Search for Company LinkedIn, Google Search for Person LinkedIn).
- Review if all external HTTP calls in 'Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review' are necessary (Crunchbase_URL, Linkedin_URL, Linkedin_URL_COMPANY, results, results1, results2).
- Review if all external HTTP calls in 'Smart Event Follow-Up & Networking Assistant' are necessary (Enrich LinkedIn Data, Get Attendees, Get Interactions, Send LinkedIn, Slack Notification).
- Review if all external HTTP calls in 'Building Prospecting Lists' are necessary (Search ICP Companies, Search People in Companies, Surfe Bulk Enrichments API, Surfe check enrichement status).
- Review if all external HTTP calls in 'Reels Trends Watcher' are necessary (Download Video, Gemini Analyze, Get File State, Upload to Gemini).
- Review if all external HTTP calls in 'Wordpress Blog Post Generator for WPML' are necessary (Link Translation Posts, Post Media to WP API, Post in Language 1, Post in Language 2, Update Post Image Lang 1, Update Post Image Lang 2).
- Review if all external HTTP calls in 'AI Automated TikTok/Youtube Shorts/Reels Generator' are necessary (Generate Image, Generate voice, Get Final Video, Get Raw File, Get Video, Get image, Image-to-Video, Render Final Video).
- Review if all external HTTP calls in 'Veo3 Instagram Agent Workflow' are necessary (HTTP Get Request, Publish to IG, Upload Bloatato, Veo3 Video Generator).
- Review if all external HTTP calls in 'Auto WordPress Blog Generator (GPT + Postgres + WP Media)' are necessary (Download Image, Load Categories, Media Upload to WP, Post to WP).
- Review if all external HTTP calls in 'Build a knowledge base chatbot with Jotform, RAG Supabase, Together AI & Gemini' are necessary (Embedding Uploaded document, Embend User Message, Grab New knowledgebase, Grab the uploaded knowledgebase file link, Search Embeddings).
- Review if all external HTTP calls in 'Glassdoor Job Finder: Bright Data Scraping + Keyword-Based Automation' are necessary (Check Delivery Status of Snap ID, Getting Job Lists, Scrap data).
- Review if all external HTTP calls in 'Stock market daily digest with Bright Data scraping & Gemini AI email reports' are necessary (Financial times scraper, Get progress, Get snapshot + data).
- Review if all external HTTP calls in 'Apify_lead_generation' are necessary (Get Results (Apify), Get Results (Apify)1, Start Results (Apify)).
- Review if all external HTTP calls in 'Automated Stripe Invoicing' are necessary (Create Invoice, Create item invoice, Send invoice).

## Priority 2 — Reliability

- Configure error workflows for the 99 workflows without error handling:
-   - 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide
-   - 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide
-   - n8n_fluidx_create_session
-   - Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini
-   - eCommerce Ai Agent ( Telegram Bot )
-   - Triage emails and draft Gmail replies using Gemini and Google Calendar
-   - AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG
-   - Create Video with Google Veo3 and Upload to Youtube
-   - LinkedIn AI Content Automation - Agentic Vibe
-   - Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide
-   *... and 89 more workflows (table truncated for readability)*
- Add idempotency keys and review webhook chain depth to prevent cascading failures.
- Move database operations outside loops or batch them to avoid performance issues.
- Review isolated nodes (no connections) — they may be unused or misconfigured.

## Priority 3 — Maintainability

- Split large workflows into smaller, focused workflows to improve maintainability.
- Review 36 unknown/custom node types for compatibility and support (showing 10 of 36):
-   - `@apify/n8n-nodes-apify.apify`
-   - `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro`
-   - `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger`
-   - `@blotato/n8n-nodes-blotato.blotatoTool`
-   - `@mendable/n8n-nodes-firecrawl.firecrawlTool`
-   - `n8n-nodes-base.aiTransform`
-   - `n8n-nodes-base.asana`
-   - `n8n-nodes-base.clickUp`
-   - `n8n-nodes-base.clickUpTrigger`
-   - `n8n-nodes-base.crypto`
-   *... and 26 more types (table truncated for readability)*
- Review 9 disabled nodes — clean up or re-enable if needed.
- Review credential references for governance and rotation policies.

## Suggested 7-Day Plan

**Day 1 — Initial Review:**
- Review top workflow: Workflow Patterns & Boilerplate for Scaling up
- Identify production-critical paths

**Day 2 — Cost Controls:**
- Add rate limits and concurrency controls around loops in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide'
- Add rate limits and concurrency controls around loops in '💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide'
- Add rate limits and concurrency controls around loops in 'n8n_fluidx_create_session'
- Add rate limits and concurrency controls around loops in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini'
- Add rate limits and concurrency controls around loops in '💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide'
- Add rate limits and concurrency controls around loops in 'Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq'
- Add rate limits and concurrency controls around loops in '💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE'
- Add rate limits and concurrency controls around loops in 'Workflow Patterns & Boilerplate for Scaling up'
- Add rate limits and concurrency controls around loops in 'Fetch live ETF metrics from JustETF to Excel with one-click updates'
- Add rate limits and concurrency controls around loops in 'Apply to Jobs from Excel and Track Application Status'
- Add rate limits and concurrency controls around loops in '💥 Automate Scrape Google Maps Business Leads (Email, Phone, Website) using Apify -vide II'
- Add rate limits and concurrency controls around loops in 'Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter'
- Add rate limits and concurrency controls around loops in 'AI Lead Machine Agent'
- Add rate limits and concurrency controls around loops in 'Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review'
- Add rate limits and concurrency controls around loops in 'Automated n8n workflow backup to GitHub with deletion tracking'
- Add rate limits and concurrency controls around loops in 'Reels Trends Watcher'
- Add rate limits and concurrency controls around loops in 'AI Automated TikTok/Youtube Shorts/Reels Generator'
- Add rate limits and concurrency controls around loops in 'Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot'
- Add rate limits and concurrency controls around loops in 'Auto WordPress Blog Generator (GPT + Postgres + WP Media)'
- Add rate limits and concurrency controls around loops in 'Export AI agent conversation logs from Postgres to Google Sheets'
- Add rate limits and concurrency controls around loops in 'Generate Shopify product listings from images with Gemini AI and Airtable'
- Add rate limits and concurrency controls around loops in 'Automate Template Delivery to Customers from Stripe Payments'
- Set spend limits and monitoring for AI/API nodes
- Document current trigger configurations

**Day 3 — Reliability:**
- Configure error handling for 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide, 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide, n8n_fluidx_create_session, Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini, eCommerce Ai Agent ( Telegram Bot ), Triage emails and draft Gmail replies using Gemini and Google Calendar, AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG, Create Video with Google Veo3 and Upload to Youtube, LinkedIn AI Content Automation - Agentic Vibe, Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide, Automated AI YouTube Shorts Factory for ASMR (Seedance), RAG Pipeline, 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide, Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X, 🤖 Build an interactive AI agent with chat interface and multiple tools, Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis, Build your first AI agent, Build your first email agent with fall back model, Talk to your Google Sheets using ChatGPT-5, Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets, Jarvis template, Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq, 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE, Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini, PPC campaign intelligence & optimization with Google Ads, Sheets & Slack, Loyverse Sales Report Agent, Smart Inventory Replenishment & Auto-Purchase Orders, Process large documents with OCR using SubworkflowAI and Gemini, Meeting Notes Automation, Automated Pharmacy Inventory Alerts for Low Stock & Expiry Dates with Google Sheets, Auto Generate Descriptive Node Names with AI for Workflow Readability, Workflow Patterns & Boilerplate for Scaling up, AI Self-Healing Engine & Auto-Patching System, AI Error diagnosis system, Build your own N8N workflows MCP server, 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners, 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners, Multi-Agent Evaluation (eval nodes), Track AI agent token usage and estimate costs in Google Sheets, 🧑‍🎓 Test your data access techniques with progressive expression challenges, Dynamically Selects Models Based on Input Type, Learn secure webhook APIs with authentication and Supabase integration, Fetch live ETF metrics from JustETF to Excel with one-click updates, Apply to Jobs from Excel and Track Application Status, 💥 Automate Scrape Google Maps Business Leads (Email, Phone, Website) using Apify -vide II, Physician Profile Enricher, Comment Analyse and Reporter, New Appointment → Welcome SMS, Autonomous B2B Supplier Price Negotiation Agent, Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter, AI Lead Machine Agent, LeadBot Autopilot: Chat-to-Lead for Salesforce Automation, Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review, whats app agent community, RAG Starter Template using Simple Vector Stores, Form trigger and OpenAI, Automate email filtering & AI summarization. 100% free & effective, works 7/24, Automated daily workflow backup to GitHub, Automatic workflow & credentials backup to GitHub with change detection, Automated n8n workflow backup to GitHub with deletion tracking, Daily workflow backup to GitLab with Slack notifications, Email_Summarizer, Get started with Google Sheets in n8n, Smart Event Follow-Up & Networking Assistant, Learn Customer Onboarding Automation with n8n, Building Prospecting Lists, Create HubSpot companies & tasks from Jotform submissions with Google Sheets, Identify Buying-Intent Leads on Twitter & Instagram using GPT-4o-mini with Slack Alerts and Notion CRM, Reels Trends Watcher, Wordpress Blog Post Generator for WPML, AI Automated TikTok/Youtube Shorts/Reels Generator, Veo3 Instagram Agent Workflow, Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot, Klaviyo List Decay Detection Deploy, Auto WordPress Blog Generator (GPT + Postgres + WP Media), Export AI agent conversation logs from Postgres to Google Sheets, Build a knowledge base chatbot with Jotform, RAG Supabase, Together AI & Gemini, Automate invoice processing with OCR, GPT-4 & Salesforce opportunity creation, Automate stale deal follow-ups in Salesforce with GPT-5.1, email, Slack & tasks, Discover creators among loyalty program contacts on Salesforce and send email, Salesforce lead capture with GPT-4 personalized email & SMS follow-up, Automated Lead Scraper: Apify to Google Sheets, Glassdoor Job Finder: Bright Data Scraping + Keyword-Based Automation, Stock market daily digest with Bright Data scraping & Gemini AI email reports, Apify_lead_generation, Generate Shopify product listings from images with Gemini AI and Airtable, Turn new Shopify products into SEO blogs with Perplexity, Gemini and Sheets, E-commerce Product Visual Generator, Sync New Shopify Customers to Odoo Contacts with Email, SMS & WhatsApp Notifications, AI blog generator for Shopify product listings:  Using GPT-4o and Google Sheets, Automate Template Delivery to Customers from Stripe Payments, SaaS Onboarding Template, CFO forecasting Agent, 🚀 Automated Stripe payment recovery: track failures & follow-up emails, Automated Stripe Invoicing, AI Agent Content, Convert inbound lead data from Webhook to AI-qualified Asana tasks, AI Workflow Generator, Prevent duplicate webhook executions in n8n, Scrape, search and browse the web with a Firecrawl AI agent webhook
- Add idempotency guards to webhook chains
- Refactor database operations outside loops
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