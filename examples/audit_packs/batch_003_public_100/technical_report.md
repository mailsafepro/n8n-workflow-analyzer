# n8n Workflow Cost & Risk Report

## How to Read This Report

If you only have a few minutes, start with these sections:

1. **Audit Summary** — overall risk scores at a glance
2. **Top Workflows To Review First** — ranked by risk
3. **Workflow Summaries** — one-line narrative per workflow
4. **Quick Wins** — immediate actions with the most impact

For a deeper review, read the full report in order.

## Audit Summary

- **Overall Risk Score:** 13/100 █░░░░░░░░░
- **Risk Level:** 🟢 Low
- **Workflows analyzed:** 107 workflows
- **High-risk workflows:** 68
- **Total findings:** 392 findings (1 critical, 25 highs)
- **Top risk category:** cost
- **Most urgent workflow:** Workflow Patterns & Boilerplate for Scaling up
- **Parser warnings:** 202 warnings

## Parser Warnings

- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'News sentiment Analyzer'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'database'
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
- ⚠ Unknown node type 'n8n-nodes-base.linkedIn' in node 'LinkedIn'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Tool: Inject Creativity'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Tool: Build Prompt Structure'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreQdrant' in node 'Qdrant Vector Store'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOllama' in node 'Embeddings Ollama'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatOllama' in node 'Ollama Chat Model'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreQdrant' in node 'Qdrant Vector Store1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOllama' in node 'Embeddings Ollama1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Tool: Inject Creative Perspective (Idea)'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Tool: Refine and Validate Prompts1'
- ⚠ Unknown node type 'n8n-nodes-upload-post.uploadPost' in node 'Upload Post'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'get_a_joke'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWikipedia' in node 'wikipedia'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolCode' in node 'calculate_loan_payment'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Get Weather'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Append or update row in sheet in Google Sheets'
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
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think1'
- ⚠ Unknown node type 'n8n-nodes-upload-post.uploadPost' in node 'Schedule to TikTok, Instagram, and YouTube'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.googleGemini' in node 'Document OCR via VLM'
- ⚠ Unknown node type 'n8n-nodes-base.rssFeedReadTrigger' in node 'YouTube RSS Trigger'
- ⚠ Unknown node type 'n8n-nodes-deapi.deapi' in node 'deAPI Transcribe Video'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Anthropic Chat Model'
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
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Haiku 4.5 fallback 2'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Haiku 4.5 fallback 1'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Sonnet 4.6 - 2'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Sonnet 4.6 - 1'
- ⚠ Unknown node type 'n8n-nodes-resend.resend' in node 'New error notification'
- ⚠ Unknown node type 'n8n-nodes-resend.resend' in node 'Full diagnosis email'
- ⚠ Unknown node type 'n8n-nodes-resend.resend' in node 'Diagnosis with reservation email'
- ⚠ Unknown node type 'n8n-nodes-resend.resend' in node 'Error notification low confidence'
- ⚠ Unknown node type 'n8n-nodes-resend.resend' in node 'Alert: context missing'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'MCP Client'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpTrigger' in node 'N8N Workflows MCP Server'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'Add Workflow'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'RemoveWorkflow'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'List Workflows'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'SearchWorkflows'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'ExecuteWorkflow'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolCalculator' in node 'Calculator'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolWorkflow' in node 'Summarizer'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Web search'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'Embeddings OpenAI'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreQdrant' in node 'Search_db'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Anthropic'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.modelSelector' in node 'Model Selector'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Opus 4'
- ⚠ Unknown node type '@apify/n8n-nodes-apify.apify' in node 'Get dataset items'
- ⚠ Unknown node type '@apify/n8n-nodes-apify.apify' in node 'Run Google Maps Scraper'
- ⚠ Unknown node type 'n8n-nodes-browseract.browserAct' in node 'Run BrowserAct Workflow'
- ⚠ Unknown node type 'n8n-nodes-serpapi.serpApi' in node 'Search LinkedIn Posts via SerpAPI'
- ⚠ Unknown node type 'n8n-nodes-connectsafely-ai.connectSafelyLinkedIn' in node 'Fetch Post Comments via ConnectSafely'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model4'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.informationExtractor' in node 'Information Extractor'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.informationExtractor' in node 'Information Extractor1'
- ⚠ Unknown node type 'n8n-nodes-base.salesforceTool' in node 'check_duplicate_lead'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.toolThink' in node 'Think'
- ⚠ Unknown node type 'n8n-nodes-base.salesforceTool' in node 'update_lead'
- ⚠ Unknown node type 'n8n-nodes-base.salesforceTool' in node 'create_lead'
- ⚠ Unknown node type 'n8n-nodes-base.emailSendTool' in node 'send_notification_client'
- ⚠ Unknown node type 'n8n-nodes-base.slackTool' in node 'send_notification_internal'
- ⚠ Unknown node type 'n8n-nodes-base.microsoftOutlook' in node 'Send a message'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Anthropic Chat Model'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Send Pre-approved Template Message to Reopen the Conversation'
- ⚠ Unknown node type 'n8n-nodes-base.whatsApp' in node 'Send AI Agent's Answer'
- ⚠ Unknown node type 'n8n-nodes-base.whatsAppTrigger' in node 'when message received'
- ⚠ Unknown node type 'n8n-nodes-base.aiTransform' in node 'Prepare Prompt'
- ⚠ Unknown node type 'n8n-nodes-base.dateTime' in node 'Date & Time'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'Embeddings OpenAI'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreInMemory' in node 'Insert Data to Store'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.vectorStoreInMemory' in node 'Query Data Tool'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatGroq' in node 'Groq Chat Model1'
- ⚠ Unknown node type 'n8n-nodes-base.readWriteFile' in node 'Read Workflow Data'
- ⚠ Unknown node type 'n8n-nodes-base.executeCommand' in node 'Execute Workflow Backup'
- ⚠ Unknown node type 'n8n-nodes-base.readWriteFile' in node 'Read File'
- ⚠ Unknown node type 'n8n-nodes-base.crypto' in node 'Hash Data'
- ⚠ Unknown node type 'n8n-nodes-base.readWriteFile' in node 'Read Credential Data'
- ⚠ Unknown node type 'n8n-nodes-base.executeCommand' in node 'Execute Credential Backup'
- ⚠ Unknown node type 'n8n-nodes-base.ftp' in node 'FTP: List Files'
- ⚠ Unknown node type 'n8n-nodes-base.ftp' in node 'FTP: Download File'
- ⚠ Unknown node type 'n8n-nodes-base.jotFormTrigger' in node 'JotForm Trigger'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.mcpClientTool' in node 'External Social Search & Enrichment Tool (MCP Client)'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'LLM Reasoning Engine for Lead Qualification'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.chat' in node 'Generate CRM-Ready Lead Discovery Response'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'LLM Reasoning Engine for Insight Structuring'
- ⚠ Unknown node type '@apify/n8n-nodes-apify.apify' in node 'Get dataset items'
- ⚠ Unknown node type '@apify/n8n-nodes-apify.apify' in node 'Get Status'
- ⚠ Unknown node type '@apify/n8n-nodes-apify.apify' in node 'Run an Actor'
- ⚠ Unknown node type 'n8n-nodes-base.readBinaryFile' in node 'Read From File'
- ⚠ Unknown node type 'n8n-nodes-base.spreadsheetFile' in node 'Convert To Spreadsheet'
- ⚠ Unknown node type 'n8n-nodes-base.jotFormTrigger' in node 'JotForm Trigger'
- ⚠ Unknown node type 'n8n-nodes-base.microsoftOneDrive' in node 'Update File to One Drive'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'query_soql'
- ⚠ Unknown node type 'n8n-nodes-base.sendGrid' in node 'Send Email'
- ⚠ Unknown node type 'n8n-nodes-base.salesforceTrigger' in node 'Salesforce Trigger'
- ⚠ Unknown node type 'n8n-nodes-influencersclub.influencersClub' in node 'Enrich by Email'
- ⚠ Unknown node type 'n8n-nodes-base.salesforceTrigger' in node 'Check for any latest checkouts'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatGoogleVertex' in node 'Give Away Personalised Offers'
- ⚠ Unknown node type 'n8n-nodes-base.sendInBlue' in node 'Send offer via email'
- ⚠ Unknown node type 'n8n-nodes-base.shopify' in node 'Create a product'
- ⚠ Unknown node type 'n8n-nodes-base.shopifyTrigger' in node 'Shopify Trigger'
- ⚠ Unknown node type 'n8n-nodes-base.shopifyTrigger' in node 'Shopify Trigger'
- ⚠ Unknown node type 'n8n-nodes-deapi.deapi' in node 'deAPI Generate Image'
- ⚠ Unknown node type 'n8n-nodes-deapi.deapi' in node 'deAPI Remove Background'
- ⚠ Unknown node type 'n8n-nodes-base.shopify' in node 'Shopify Update Product'
- ⚠ Unknown node type 'n8n-nodes-deapi.deapiTool' in node 'Image prompt booster in deAPI'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAnthropic' in node 'Anthropic Chat Model'
- ⚠ Unknown node type 'n8n-nodes-rapiwa.rapiwa' in node 'Rapiwa (Send a WhatsApp message)'
- ⚠ Unknown node type 'n8n-nodes-rapiwa.rapiwa' in node 'Rapiwa (Send a WhatsApp message)1'
- ⚠ Unknown node type 'n8n-nodes-rapiwa.rapiwa' in node 'Rapiwa ( Check Number is On WhatsApp OR Not )'
- ⚠ Unknown node type 'n8n-nodes-rapiwa.rapiwa' in node 'Rapiwa (Check Number is On WhatsApp OR Not )'
- ⚠ Unknown node type 'n8n-nodes-base.messageBird' in node 'Send an SMS Confirmation'
- ⚠ Unknown node type 'n8n-nodes-base.odoo' in node 'Odoo (Create Contact)'
- ⚠ Unknown node type 'n8n-nodes-base.odoo' in node 'Odoo (Search Contact)'
- ⚠ Unknown node type 'n8n-nodes-base.shopifyTrigger' in node 'Shopify Trigger (Customer Created)'
- ⚠ Unknown node type 'n8n-nodes-base.shopify' in node 'Shopify'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Create Blog id'
- ⚠ Unknown node type 'n8n-nodes-base.httpRequestTool' in node 'Create Articles'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Read Sheet'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Update Sheet'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model1'
- ⚠ Unknown node type 'n8n-nodes-base.googleSheetsTool' in node 'Get row(s) in sheet in Google Sheets'
- ⚠ Unknown node type 'n8n-nodes-base.stripe' in node 'Stripe Data Collection'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'OpenAI Embeddings'
- ⚠ Unknown node type 'n8n-nodes-base.stripeTrigger' in node 'Stripe Trigger'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.embeddingsOpenAi' in node 'Embeddings OpenAI'
- ⚠ Unknown node type 'n8n-nodes-base.stripe' in node 'Fetch Stripe Charges'
- ⚠ Unknown node type 'n8n-nodes-base.stripeTrigger' in node 'Detect Failed Payments'
- ⚠ Unknown node type 'n8n-nodes-base.sendInBlue' in node 'Send First Email'
- ⚠ Unknown node type 'n8n-nodes-base.sendInBlue' in node 'Send Second Email'
- ⚠ Unknown node type 'n8n-nodes-base.clickUpTrigger' in node 'ClickUp Trigger'
- ⚠ Unknown node type 'n8n-nodes-base.stripe' in node 'Create Customer'
- ⚠ Unknown node type 'n8n-nodes-base.clickUp' in node 'ClickUp'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'Instagram Publisher'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'LinkedIn Publisher'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'Source Collector'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'Source Retriever'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'Infographic Generator'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'Slideshow Video Generator'
- ⚠ Unknown node type '@blotato/n8n-nodes-blotato.blotatoTool' in node 'Visual Asset Retriever'
- ⚠ Unknown node type 'n8n-nodes-base.asana' in node 'Create Asana Task'
- ⚠ Unknown node type '@n8n/n8n-nodes-langchain.lmChatAzureOpenAi' in node 'Azure OpenAI Chat Model1'
- ⚠ Unknown node type '@mendable/n8n-nodes-firecrawl.firecrawlTool' in node '/scrape with Firecrawl'
- ⚠ Unknown node type '@mendable/n8n-nodes-firecrawl.firecrawlTool' in node '/search with Firecrawl'
- ⚠ Unknown node type '@mendable/n8n-nodes-firecrawl.firecrawlTool' in node 'Interact context with Firecrawl'
- ⚠ Unknown node type '@mendable/n8n-nodes-firecrawl.firecrawlTool' in node 'Execute interaction with Firecrawl'
- ⚠ Unknown node type '@mendable/n8n-nodes-firecrawl.firecrawlTool' in node 'Stop interaction with Firecrawl'

## Executive Summary

- **Cost Risk Score:** 36/100 ███░░░░░░░
- **Operational Risk Score:** 1/100 ░░░░░░░░░░
- **Complexity Score:** 2/100 ░░░░░░░░░░

> **Note:** 36 community/custom node types found. These may have cost or
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
| 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | Highest priority (90) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load. | Add rate limits and concurrency controls |
| n8n_fluidx_create_session | Review recommended (65) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Add rate limits and concurrency controls |
| Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | High priority (80) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Add rate limits and concurrency controls |
| eCommerce Ai Agent ( Telegram Bot ) | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Triage emails and draft Gmail replies using Gemini and Google Calendar | Review recommended (60) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load. | Estimate and monitor costs before production |
| AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | Highest priority (100) | Has 6 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls. | Estimate and monitor costs before production |
| Create Video with Google Veo3 and Upload to Youtube | Moderate (35) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| LinkedIn AI Content Automation - Agentic Vibe | Highest priority (100) | Has 7 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | Highest priority (95) | Has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls. | Estimate and monitor costs before production |
| Automated AI YouTube Shorts Factory for ASMR (Seedance) | Highest priority (95) | Has 5 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Estimate and monitor costs before production |
| RAG Pipeline | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls. | Add rate limits and concurrency controls |
| Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | Moderate (20) | Lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| 🤖 Build an interactive AI agent with chat interface and multiple tools | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | Review recommended (60) | Has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Build your first AI agent | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Build your first email agent with fall back model | Review recommended (60) | Has 3 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Talk to your Google Sheets using ChatGPT-5 | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | Highest priority (90) | Has 4 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; is a large workflow that is harder to maintain and debug. | Estimate and monitor costs before production |
| Jarvis template | Review recommended (60) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; is a large workflow that is harder to maintain and debug. | Estimate and monitor costs before production |
| Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 8 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls; is a large workflow that is harder to maintain and debug. | Add rate limits and concurrency controls |
| 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | Highest priority (100) | Combines HTTP calls inside loop or batch logic, creating a runaway execution risk; has 7 AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load; makes many external HTTP calls; is a large workflow that is harder to maintain and debug. | Add rate limits and concurrency controls |
| Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | Review recommended (50) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Estimate and monitor costs before production |
| PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | Moderate (30) | Lacks error handling for failure scenarios; has a high fan-out node that may cause unexpected API load. | Configure error workflow |
| Loyverse Sales Report Agent | Moderate (20) | Lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Smart Inventory Replenishment & Auto-Purchase Orders | Moderate (35) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Process large documents with OCR using SubworkflowAI and Gemini | Moderate (20) | Lacks error handling for failure scenarios; makes many external HTTP calls. | Configure error workflow |
| Meeting Notes Automation | Review recommended (45) | Has AI/LLM nodes with variable token-based costs; lacks error handling for failure scenarios. | Estimate and monitor costs before production |
| Automated Pharmacy Inventory Alerts for Low Stock & Expiry Dates with Google Sheets | Low (15) | Lacks error handling for failure scenarios. | Configure error workflow |
*... and 77 more workflows (table truncated for readability)*

## Node Inventory

- **Total unique node types:** 155 types
- **Trigger nodes:** 135 nodes
- **Disabled nodes:** 9 nodes
- **Credential references:** 587 references
- **Unknown node types:** 36 types

### Node Categories

| Category | Count |
|----------|-------|
| control_flow | 1064 |
| transform | 402 |
| ai | 321 |
| http_api | 198 |
| trigger | 136 |
| spreadsheet | 108 |
| unknown | 82 |
| communication | 59 |
| email | 56 |
| marketing | 40 |
| crm | 39 |
| database | 35 |
| devops | 24 |
| storage | 23 |
| document | 14 |
| human_input | 13 |
| scraping | 8 |
| calendar | 7 |

### Node Types

| Node Type | Count |
|-----------|-------|
| n8n-nodes-base.stickyNote | 811 |
| n8n-nodes-base.httpRequest | 192 |
| n8n-nodes-base.code | 153 |
| n8n-nodes-base.set | 146 |
| n8n-nodes-base.if | 97 |
| n8n-nodes-base.googleSheets | 84 |
| @n8n/n8n-nodes-langchain.agent | 72 |
| n8n-nodes-base.wait | 58 |
| @n8n/n8n-nodes-langchain.lmChatOpenAi | 41 |
| @blotato/n8n-nodes-blotato.blotato | 37 |
| @n8n/n8n-nodes-langchain.outputParserStructured | 36 |
| n8n-nodes-base.scheduleTrigger | 32 |
| n8n-nodes-base.telegram | 30 |
| n8n-nodes-base.gmail | 30 |
| @n8n/n8n-nodes-langchain.openAi | 28 |
| n8n-nodes-base.executeWorkflow | 26 |
| n8n-nodes-base.merge | 25 |
| n8n-nodes-base.manualTrigger | 25 |
| n8n-nodes-base.filter | 24 |
| n8n-nodes-base.switch | 23 |
*... and 135 more node types (table truncated for readability)*

## Community / Custom / Unclassified Node Types

The following 36 node types are from community packages, custom builds,
or unrecognized sources.
They may have custom cost or risk profiles not covered by built-in rules:

- `@apify/n8n-nodes-apify.apify`
- `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectpro`
- `@bedrijfsdatanl/n8n-nodes-prospectpro.prospectproTrigger`
- `@blotato/n8n-nodes-blotato.blotatoTool`
- `@mendable/n8n-nodes-firecrawl.firecrawlTool`
- `n8n-nodes-base.aiTransform`
- `n8n-nodes-base.asana`
- `n8n-nodes-base.clickUp`
- `n8n-nodes-base.clickUpTrigger`
- `n8n-nodes-base.crypto`
- `n8n-nodes-base.dateTime`
- `n8n-nodes-base.emailSendTool`
- `n8n-nodes-base.executeCommand`
- `n8n-nodes-base.ftp`
- `n8n-nodes-base.linkedIn`
- `n8n-nodes-base.messageBird`
- `n8n-nodes-base.microsoftOneDrive`
- `n8n-nodes-base.odoo`
- `n8n-nodes-base.readBinaryFile`
- `n8n-nodes-base.readWriteFile`
*... and 16 more unclassified node types (table truncated for readability)*

## Connection Inventory

- **Total edges:** 1855
- **Max outgoing edges:** 33
- **High fan-out nodes:** AI Agent, Branch by Intent, Code in JavaScript, Edit Fields, Embeddings OpenAI, Google Gemini Chat Model, Google Gemini Chat Model1, If, Loop Over Items, Merge, Odoo (Create Contact), On form submission, OpenAI, OpenAI Chat Model, OpenAI Chat Model1, Operations, Route Document Types, Route by Draft Type, Route by Performance, Schedule Trigger, Simple Memory, Split Out, Structured Output Parser, Structured Output Parser1, Switch, Telegram Trigger, Think, Upload Video to BLOTATO, Upload Video to Blotato, Wait, When Executed by [trigger workflow], When chat message received, When clicking ‘Execute workflow’, When clicking ‘Test workflow’
- **Isolated nodes:** ## Create THE EYE Session, Answer - Array Access, Answer - Array of Objects, Answer - Basic Access, Answer - Final, Answer - JS Function, Answer - Nested Object, Answer Note - Array Access, Answer Note - Array of Objects, Answer Note - Basic Access, Answer Note - Final, Answer Note - JS Function, Answer Note - Nested Object, Anthropic, Author Message1, Congratulations!, Documentation, Feedback Correct1, Feedback Correct2, Feedback Correct3, Feedback Correct4, Feedback Correct5, Feedback Correct6, Feedback Incorrect1, Feedback Incorrect2, Feedback Incorrect3, Feedback Incorrect4, Feedback Incorrect5, Feedback Incorrect6, Get Results (Apify)1, How It Works, Instruction - Array Access, Instruction - Array of Objects, Instruction - Basic Access, Instruction - Basic Access1, Instruction - Final, Instruction - JS Function, Instruction - Nested Object, Introduction Note, LLM Flow Sticky Note, Main Overview1, Note: AI Ideation, Note: Asset Generation, Note: Distribution, Note: Final Assembly, Output & Next Steps, Post Processing Sticky Note, Post Processing Sticky Note1, Post Processing Sticky Note2, Post Processing Sticky Note4, SUBMISSION GUIDE, Section , Section 6, Section 7, Section 8, Section 9, Section — Critical Suppression Branch, Section — Error Handling Branch, Section — Score, Persist & Report, Section — Setup & Profile Fetch, Section: AI Selection (Gemini), Section: FFmpeg Audio Job Loop, Section: FFmpeg Short Job Loop, Section: Intake & Form, Section: Scheduling, Section: Transcription & Parsing, Setup, Setup Guide - Start Here, Setup Instructions, Step 1 - Prerequisites, Step 1 - Telegram Setup, Step 1 Explanation, Step 2 - API Keys Configuration, Step 2 - Extract Input Data Documentation, Step 2 Explanation, Step 2 Header1, Step 3 - AI Processing, Step 3 - API Keys Configuration, Step 4 - Voice & Video Generation, Step 4 - Workflow Activation, Step 5 - Publishing, Sticky Note, Sticky Note - AI Agent, Sticky Note - Edit Fields, Sticky Note - Example, Sticky Note - Extract, Sticky Note - Generate, Sticky Note - Header, Sticky Note - Notion, Sticky Note - Overview, Sticky Note - Remove BG, Sticky Note - Setup, Sticky Note - Slack, Sticky Note - Transcribe, Sticky Note - Trigger, Sticky Note - Update, Sticky Note – AI Engine1, Sticky Note – AI Intent Agent, Sticky Note – Actions Summary, Sticky Note – Approved Trigger, Sticky Note – Build Report, Sticky Note – Fetch Comments, Sticky Note – Flatten Comments, Sticky Note – Format Reply, Sticky Note – Opportunity Fetch, Sticky Note – Parse & Filter, Sticky Note – Parse Sentiment Output, Sticky Note – Pipeline 2 Header, Sticky Note – Pipeline 3 Header, Sticky Note – Reply Agent, Sticky Note – Save to Sheet, Sticky Note – Schedule & Threshold, Sticky Note – Send Email, Sticky Note – SerpAPI Search, Sticky Note – Sheet Trigger P2, Sticky Note – Trigger, Sticky Note – Workflow Overview, Sticky Note – Write Reply, Sticky Note — DPO Retry Path, Sticky Note — Email Dispatch, Sticky Note — MCTS Draft Generation, Sticky Note — Outcome Logging, Sticky Note — Pick Best Draft, Sticky Note — Reply Decision, Sticky Note — Reply Monitoring, Sticky Note — Self-Critique Rounds, Sticky Note — Slack Notifications, Sticky Note — Trigger, Sticky Note — Validation, Sticky Note — Workflow Overview, Sticky Note1, Sticky Note10, Sticky Note100, Sticky Note101, Sticky Note102, Sticky Note103, Sticky Note104, Sticky Note105, Sticky Note106, Sticky Note107, Sticky Note108, Sticky Note109, Sticky Note11, Sticky Note110, Sticky Note12, Sticky Note13, Sticky Note14, Sticky Note15, Sticky Note16, Sticky Note17, Sticky Note18, Sticky Note19, Sticky Note2, Sticky Note20, Sticky Note21, Sticky Note22, Sticky Note23, Sticky Note24, Sticky Note25, Sticky Note26, Sticky Note27, Sticky Note28, Sticky Note29, Sticky Note3, Sticky Note30, Sticky Note31, Sticky Note32, Sticky Note33, Sticky Note34, Sticky Note35, Sticky Note36, Sticky Note37, Sticky Note38, Sticky Note39, Sticky Note4, Sticky Note40, Sticky Note41, Sticky Note42, Sticky Note43, Sticky Note44, Sticky Note45, Sticky Note46, Sticky Note47, Sticky Note48, Sticky Note49, Sticky Note5, Sticky Note50, Sticky Note51, Sticky Note52, Sticky Note53, Sticky Note54, Sticky Note55, Sticky Note56, Sticky Note57, Sticky Note58, Sticky Note59, Sticky Note6, Sticky Note60, Sticky Note61, Sticky Note62, Sticky Note63, Sticky Note64, Sticky Note65, Sticky Note66, Sticky Note67, Sticky Note68, Sticky Note69, Sticky Note7, Sticky Note70, Sticky Note71, Sticky Note72, Sticky Note73, Sticky Note74, Sticky Note75, Sticky Note76, Sticky Note77, Sticky Note78, Sticky Note79, Sticky Note8, Sticky Note80, Sticky Note81, Sticky Note82, Sticky Note83, Sticky Note84, Sticky Note85, Sticky Note86, Sticky Note87, Sticky Note88, Sticky Note89, Sticky Note9, Sticky Note90, Sticky Note91, Sticky Note92, Sticky Note93, Sticky Note94, Sticky Note95, Sticky Note96, Sticky Note97, Sticky Note98, Sticky Note99, Test, Test Note, Triggers Section Sticky Note, Triggers Section Sticky Note1, Triggers Section Sticky Note2, Try This Example, Usage Instructions, Warning1, Webhook2, Webhook5, What This Does, What this does, Why This Works, Workflow Description, Workflow Overview Documentation, add create_at column, ℹ️ Viewer Tips, ℹ️ Viewer Tips1, ℹ️ Viewer Tips2, ℹ️ Viewer Tips3, ℹ️ Viewer Tips4, ℹ️ Viewer Tips5, ℹ️ Viewer Tips6, ℹ️ Viewer Tips7, ℹ️ Viewer Tips9, ⏱️ Timing Optimization Guide, ⚙️ Setup Notes, ⚠️ Critical Setup, ⚠️ Warning: Azure OpenAI Credentials, ✉️ Welcome Email Best Practices, 💭 Personal Check-in Psychology, 📈 Week 1 Content Strategy, 📉 List Decay Detection — Main, 📊 CRM Integration Guide, 📊 Sheet Structure, 📊 Status Tracking Info, 📋 Overview, 📋 Template Overview, 📋 Webhook Trigger Explanation, 📚 Document Delivery Strategy, 📝 Setup & Instructions, 📤 Section: Output Processing, 📥 Section: Input & Prompt Prep, 🔔 Team Notification Strategy, 🤖 Section: AI Generation

## Top Workflows To Review First

| Rank | Workflow | Overall Risk | Cost Risk | Critical | High | Top Drivers |
|------|----------|-------------|-----------|----------|------|-------------|
| 1 | Workflow Patterns & Boilerplate for Scaling up | 100 | 35 | 1 | 1 | LOOP_HTTP, LARGE_WF, NO_ERROR_HANDLING |
| 2 | Auto WordPress Blog Generator (GPT + Postgres + WP Media) | 100 | 95 | 0 | 2 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 3 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | 100 | 100 | 0 | 1 | LOOP_HTTP, AI_NODE, LARGE_WF |
| 4 | 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | 100 | 100 | 0 | 1 | LOOP_HTTP, AI_NODE, LARGE_WF |
| 5 | 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide | 100 | 95 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 6 | Automate Template Delivery to Customers from Stripe Payments | 100 | 90 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 7 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 8 | Dynamically Selects Models Based on Input Type | 100 | 100 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 9 | LinkedIn AI Content Automation - Agentic Vibe | 100 | 100 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 10 | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | 100 | 95 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 11 | Smart Event Follow-Up & Networking Assistant | 100 | 95 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 12 | AI Error diagnosis system | 100 | 90 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 13 | Autonomous B2B Supplier Price Negotiation Agent | 100 | 90 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 14 | AI Automated TikTok/Youtube Shorts/Reels Generator | 95 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 15 | Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review | 95 | 80 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 16 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | 95 | 80 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 17 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | 95 | 65 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 18 | Generate Shopify product listings from images with Gemini AI and Airtable | 90 | 75 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 19 | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | 90 | 60 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 20 | Track AI agent token usage and estimate costs in Google Sheets | 90 | 75 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 21 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | 90 | 60 | 0 | 0 | AI_NODE, LARGE_WF, NO_ERROR_HANDLING |
| 22 | Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot | 80 | 30 | 0 | 2 | LOOP_HTTP, NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 23 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 80 | 65 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 24 | Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter | 80 | 65 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 25 | Export AI agent conversation logs from Postgres to Google Sheets | 75 | 30 | 0 | 2 | LOOP_HTTP, NO_ERROR_HANDLING, DB_IN_LOOP |
| 26 | AI Lead Machine Agent | 75 | 60 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 27 | 💥 Automate Scrape Google Maps Business Leads (Email, Phone, Website) using Apify -vide II | 75 | 60 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 28 | Auto Generate Descriptive Node Names with AI for Workflow Readability | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 29 | Comment Analyse and Reporter | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 30 | Discover creators among loyalty program contacts on Salesforce and send email | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 31 | Identify Buying-Intent Leads on Twitter & Instagram using GPT-4o-mini with Slack Alerts and Notion CRM | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 32 | Scrape, search and browse the web with a Firecrawl AI agent webhook | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 33 | Turn new Shopify products into SEO blogs with Perplexity, Gemini and Sheets | 75 | 60 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 34 | n8n_fluidx_create_session | 65 | 50 | 0 | 1 | LOOP_HTTP, AI_NODE, NO_ERROR_HANDLING |
| 35 | Wordpress Blog Post Generator for WPML | 65 | 50 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 36 | AI Workflow Generator | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 37 | AI blog generator for Shopify product listings:  Using GPT-4o and Google Sheets | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 38 | Build your first email agent with fall back model | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 39 | CFO forecasting Agent | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 40 | Multi-Agent Evaluation (eval nodes) | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 41 | RAG Starter Template using Simple Vector Stores, Form trigger and OpenAI | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 42 | SaaS Onboarding Template | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 43 | Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | 60 | 45 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 44 | Build your own N8N workflows MCP server | 60 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, HIGH_FAN_OUT |
| 45 | Jarvis template | 60 | 30 | 0 | 0 | AI_NODE, LARGE_WF, NO_ERROR_HANDLING |
| 46 | Triage emails and draft Gmail replies using Gemini and Google Calendar | 60 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, HIGH_FAN_OUT |
| 47 | Reels Trends Watcher | 50 | 35 | 0 | 1 | LOOP_HTTP, NO_ERROR_HANDLING, MANY_HTTP |
| 48 | Fetch live ETF metrics from JustETF to Excel with one-click updates | 50 | 30 | 0 | 1 | LOOP_HTTP, NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 49 | AI Self-Healing Engine & Auto-Patching System | 50 | 35 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 50 | Build a knowledge base chatbot with Jotform, RAG Supabase, Together AI & Gemini | 50 | 35 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 51 | Stock market daily digest with Bright Data scraping & Gemini AI email reports | 50 | 35 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 52 | Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | 50 | 35 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 53 | Veo3 Instagram Agent Workflow | 50 | 35 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 54 | Apply to Jobs from Excel and Track Application Status | 45 | 30 | 0 | 1 | LOOP_HTTP, NO_ERROR_HANDLING |
| 55 | Automated n8n workflow backup to GitHub with deletion tracking | 45 | 30 | 0 | 1 | LOOP_HTTP, NO_ERROR_HANDLING |
| 56 | AI Agent Content | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 57 | Automate email filtering & AI summarization. 100% free & effective, works 7/24 | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 58 | Build your first AI agent | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 59 | E-commerce Product Visual Generator | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 60 | Email_Summarizer | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 61 | Get started with Google Sheets in n8n | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 62 | LeadBot Autopilot: Chat-to-Lead for Salesforce Automation | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 63 | Meeting Notes Automation | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 64 | RAG Pipeline | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 65 | Talk to your Google Sheets using ChatGPT-5 | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 66 | eCommerce Ai Agent ( Telegram Bot ) | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 67 | whats app agent community | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 68 | 🤖 Build an interactive AI agent with chat interface and multiple tools | 45 | 30 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 69 | Create Video with Google Veo3 and Upload to Youtube | 35 | 20 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 70 | Smart Inventory Replenishment & Auto-Purchase Orders | 35 | 20 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, MANY_HTTP |
| 71 | Convert inbound lead data from Webhook to AI-qualified Asana tasks | 35 | 15 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 72 | Create food emoji icons with OpenAI GPT & image generation | 30 | 30 | 0 | 0 | AI_NODE |
| 73 | Email Manager | 30 | 30 | 0 | 0 | AI_NODE |
| 74 | Automate invoice processing with OCR, GPT-4 & Salesforce opportunity creation | 30 | 15 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 75 | Automate stale deal follow-ups in Salesforce with GPT-5.1, email, Slack & tasks | 30 | 15 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 76 | Salesforce lead capture with GPT-4 personalized email & SMS follow-up | 30 | 15 | 0 | 0 | AI_NODE, NO_ERROR_HANDLING |
| 77 | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | 30 | 0 | 0 | 0 | NO_ERROR_HANDLING, HIGH_FAN_OUT |
| 78 | Sync New Shopify Customers to Odoo Contacts with Email, SMS & WhatsApp Notifications | 30 | 0 | 0 | 0 | NO_ERROR_HANDLING, HIGH_FAN_OUT |
| 79 | 🧑‍🎓 Test your data access techniques with progressive expression challenges | 30 | 0 | 0 | 0 | LARGE_WF, NO_ERROR_HANDLING |
| 80 | Apify_lead_generation | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 81 | Automated Stripe Invoicing | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 82 | Building Prospecting Lists | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 83 | Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 84 | Glassdoor Job Finder: Bright Data Scraping + Keyword-Based Automation | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 85 | Loyverse Sales Report Agent | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 86 | Process large documents with OCR using SubworkflowAI and Gemini | 20 | 5 | 0 | 0 | NO_ERROR_HANDLING, MANY_HTTP |
| 87 | Prevent duplicate webhook executions in n8n | 20 | 0 | 0 | 0 | NO_ERROR_HANDLING, WEBHOOK_CHAIN |
| 88 | LinkedIn Post To Personalized Opener | 15 | 15 | 0 | 0 | AI_NODE |
| 89 | Personalized hotel reward emails for high-spenders with Salesforce, Gemini AI & Brevo | 15 | 15 | 0 | 0 | AI_NODE |
| 90 | 💥 AI Email Assistant: Get Actionable Gmail Alerts on Telegram | 15 | 15 | 0 | 0 | AI_NODE |
| 91 | Automated Lead Scraper: Apify to Google Sheets | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 92 | Automated Pharmacy Inventory Alerts for Low Stock & Expiry Dates with Google Sheets | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 93 | Automated daily workflow backup to GitHub | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 94 | Automatic workflow & credentials backup to GitHub with change detection | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 95 | Create HubSpot companies & tasks from Jotform submissions with Google Sheets | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 96 | Daily workflow backup to GitLab with Slack notifications | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 97 | Klaviyo List Decay Detection Deploy | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 98 | Learn Customer Onboarding Automation with n8n | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 99 | Learn secure webhook APIs with authentication and Supabase integration | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 100 | New Appointment → Welcome SMS | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 101 | Physician Profile Enricher | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 102 | 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 103 | 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 104 | 🚀 Automated Stripe payment recovery: track failures & follow-up emails | 15 | 0 | 0 | 0 | NO_ERROR_HANDLING |
| 105 | Automatic FTP file backup to Google Drive with scheduled sync | 0 | 0 | 0 | 0 | — |
| 106 | Email new leads from Google Sheets via Outlook on a schedule | 0 | 0 | 0 | 0 | — |
| 107 | How to automatically import CSV files into postgres | 0 | 0 | 0 | 0 | — |

## Workflow Inventory

| # | Workflow | Active | Nodes | Triggers | Risk Score |
|---|----------|--------|-------|----------|------------|
| 1 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ❌ | 35 | n8n-nodes-base.telegramTrigger | 100 |
| 2 | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | ❌ | 25 | n8n-nodes-base.googleSheetsTrigger | 90 |
| 3 | n8n_fluidx_create_session | ❌ | 50 | n8n-nodes-base.formTrigger | 65 |
| 4 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | ❌ | 28 | n8n-nodes-base.telegramTrigger | 80 |
| 5 | eCommerce Ai Agent ( Telegram Bot ) | ❌ | 16 | n8n-nodes-base.telegramTrigger | 45 |
| 6 | Triage emails and draft Gmail replies using Gemini and Google Calendar | ❌ | 25 | n8n-nodes-base.gmailTrigger | 60 |
| 7 | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | ❌ | 35 | n8n-nodes-base.manualTrigger, n8n-nodes-base.whatsAppTrigger | 100 |
| 8 | Create Video with Google Veo3 and Upload to Youtube | ❌ | 23 | n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger | 35 |
| 9 | LinkedIn AI Content Automation - Agentic Vibe | ❌ | 13 | n8n-nodes-base.scheduleTrigger | 100 |
| 10 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | ❌ | 29 | n8n-nodes-base.scheduleTrigger | 95 |
| 11 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | ❌ | 32 | n8n-nodes-base.scheduleTrigger | 95 |
| 12 | RAG Pipeline | ❌ | 13 | @n8n/n8n-nodes-langchain.chatTrigger, n8n-nodes-base.formTrigger | 45 |
| 13 | 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide | ❌ | 40 | n8n-nodes-base.scheduleTrigger | 100 |
| 14 | Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | ❌ | 19 | n8n-nodes-base.formTrigger | 20 |
| 15 | 🤖 Build an interactive AI agent with chat interface and multiple tools | ❌ | 17 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 16 | Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | ❌ | 16 | n8n-nodes-base.scheduleTrigger | 60 |
| 17 | Build your first AI agent | ❌ | 13 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 18 | Build your first email agent with fall back model | ❌ | 11 | n8n-nodes-base.gmailTrigger | 60 |
| 19 | Talk to your Google Sheets using ChatGPT-5 | ❌ | 11 | @n8n/n8n-nodes-langchain.chatTrigger | 45 |
| 20 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | ❌ | 63 | n8n-nodes-base.executeWorkflowTrigger, n8n-nodes-base.telegramTrigger | 90 |
| 21 | Jarvis template | ❌ | 52 | @n8n/n8n-nodes-langchain.mcpTrigger, n8n-nodes-base.telegramTrigger | 60 |
| 22 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | ❌ | 63 | n8n-nodes-base.scheduleTrigger, n8n-nodes-base.telegramTrigger | 100 |
| 23 | 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | ❌ | 63 | n8n-nodes-base.telegramTrigger | 100 |
| 24 | Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | ❌ | 26 | n8n-nodes-base.formTrigger | 50 |
| 25 | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | ❌ | 23 | n8n-nodes-base.scheduleTrigger | 30 |
| 26 | Loyverse Sales Report Agent | ❌ | 21 | n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger | 20 |
| 27 | Smart Inventory Replenishment & Auto-Purchase Orders | ❌ | 24 | n8n-nodes-base.scheduleTrigger | 35 |
| 28 | Process large documents with OCR using SubworkflowAI and Gemini | ❌ | 16 | n8n-nodes-base.manualTrigger | 20 |
| 29 | Meeting Notes Automation | ❌ | 16 | n8n-nodes-base.rssFeedReadTrigger | 45 |
| 30 | Automated Pharmacy Inventory Alerts for Low Stock & Expiry Dates with Google Sheets | ❌ | 7 | none | 15 |
*... and 77 more workflows (table truncated for readability)*

## Quick Wins

1. Add rate limits and concurrency controls around the HTTP loop in '💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide'.
2. Add rate limits and concurrency controls around the HTTP loop in '💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide'.
3. Add rate limits and concurrency controls around the HTTP loop in 'n8n_fluidx_create_session'.
4. Add rate limits and concurrency controls around the HTTP loop in 'Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini'.
5. Add rate limits and concurrency controls around the HTTP loop in '💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide'.

## Top Risks

| Severity | Category | Workflow | Message |
|----------|----------|----------|---------|
| CRITICAL | complexity | Workflow Patterns & Boilerplate for Scaling up | Workflow has 240 nodes, making it very complex to maintain and debug |
| HIGH | cost | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | n8n_fluidx_create_session | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Workflow Patterns & Boilerplate for Scaling up | HTTP Request node inside a loop/batch can multiply API calls and costs |
| HIGH | cost | Fetch live ETF metrics from JustETF to Excel with one-click updates | HTTP Request node inside a loop/batch can multiply API calls and costs |

## Cost Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| HIGH | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Merge1, ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Search Trends with Perplexity | AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Script with GPT-4 | AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate |
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Generate Caption with GPT-4 | AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate |
| LOW | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | ElevenLabs Voice Synthesis, FAL.ai Video Generation, Upload Audio to Public URL, Build Public Image URL, Download VEED Video | Workflow has 5 HTTP Request nodes, increasing external dependency and cost |
| HIGH | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | Merge1, Download Video, Veo Generation1 | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | Parse GPT Response | AI/LLM node 'Parse GPT Response' has variable token-based cost that can escalate |
| MEDIUM | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | GPT-4 API Call | AI/LLM node 'GPT-4 API Call' has variable token-based cost that can escalate |
| HIGH | n8n_fluidx_create_session | Split photoRefs (Item Lists), Merge Analyze + URL, Merge photoRefs, Merge, fluidX API - Media Info HTTP Request GET, fluidX API - Create Session, fluidX API - Send SMS User, fluidX API - Get Session Info, fluidX API - Download Photo THEEYE Session, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | n8n_fluidx_create_session | Analyze image | AI/LLM node 'Analyze image' has variable token-based cost that can escalate |
| LOW | n8n_fluidx_create_session | fluidX API - Media Info HTTP Request GET, fluidX API - Create Session, fluidX API - Send SMS User, fluidX API - Get Session Info, fluidX API - Download Photo THEEYE Session, fluidX API - Media Info HTTP Request POST, fluidX API - Media Summary | Workflow has 7 HTTP Request nodes, increasing external dependency and cost |
| HIGH | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Merge, Merge1, 1 hour, 15 min, 1 day, News | HTTP Request node inside a loop/batch can multiply API calls and costs |
| MEDIUM | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Google Gemini Chat Model1 | AI/LLM node 'Google Gemini Chat Model1' has variable token-based cost that can escalate |
| MEDIUM | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | Crypto Agent | AI/LLM node 'Crypto Agent' has variable token-based cost that can escalate |
| LOW | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 1 hour, 15 min, 1 day, News | Workflow has 4 HTTP Request nodes, increasing external dependency and cost |
| MEDIUM | eCommerce Ai Agent ( Telegram Bot ) | AI Agent | AI/LLM node 'AI Agent' has variable token-based cost that can escalate |
| MEDIUM | eCommerce Ai Agent ( Telegram Bot ) | OpenRouter Chat Model | AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate |
| MEDIUM | Triage emails and draft Gmail replies using Gemini and Google Calendar | Draft and Label Agent | AI/LLM node 'Draft and Label Agent' has variable token-based cost that can escalate |
| MEDIUM | Triage emails and draft Gmail replies using Gemini and Google Calendar | Gemini Chat Model | AI/LLM node 'Gemini Chat Model' has variable token-based cost that can escalate |
| MEDIUM | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | Knowledge Base Agent | AI/LLM node 'Knowledge Base Agent' has variable token-based cost that can escalate |
*... and 246 more findings (table truncated for readability)*

## Estimated Cost Exposure

- **💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Search Trends with Perplexity' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Script with GPT-4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Caption with GPT-4' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Parse GPT Response' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'GPT-4 API Call' has variable token-based cost that can escalate
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
- **eCommerce Ai Agent ( Telegram Bot ):** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
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
- **Create Video with Google Veo3 and Upload to Youtube:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Generate title' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **LinkedIn AI Content Automation - Agentic Vibe:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Content topic generator2' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Content creator' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Hashtag generator /SEO' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model2' has variable token-based cost that can escalate
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
- **💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'LLM: Draft Video Prompt Details (GPT-4.1)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Creative Video Idea' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Detailed Video Prompts' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM: Generate Raw Idea (GPT-5)' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 6 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 8 HTTP Request nodes, increasing external dependency and cost
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
- **Build your first email agent with fall back model:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI  Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gemini Chat Model' has variable token-based cost that can escalate
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
- **💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Generate Image Prompt' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Message a model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent: Generate Video Script' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate 4o Image（GPT IMAG 1）' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'ChatGPT Image – fetch generated image' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 10 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent - Select Viral Clips' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **PPC campaign intelligence & optimization with Google Ads, Sheets & Slack:** 🟢 LOW — minimal (heuristic)
- **Loyverse Sales Report Agent:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
- **Smart Inventory Replenishment & Auto-Purchase Orders:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'AI Demand Forecasting' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Process large documents with OCR using SubworkflowAI and Gemini:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
- **Meeting Notes Automation:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Anthropic Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Automated Pharmacy Inventory Alerts for Low Stock & Expiry Dates with Google Sheets:** 🟢 LOW — minimal (heuristic)
- **Auto Generate Descriptive Node Names with AI for Workflow Readability:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Prepare LLM Validation Data' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Node Rename Mapping' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM Flow Sticky Note' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Workflow Patterns & Boilerplate for Scaling up:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: MANY_HTTP: Workflow has 7 HTTP Request nodes, increasing external dependency and cost
- **AI Self-Healing Engine & Auto-Patching System:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Azure OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Diagnose Error' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **AI Error diagnosis system:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Claude Scoring Judge' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Claude Diagnosis' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Haiku 4.5 fallback 2' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Haiku 4.5 fallback 1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Sonnet 4.6 - 2' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Sonnet 4.6 - 1' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Build your own N8N workflows MCP server:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
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
- **Dynamically Selects Models Based on Input Type:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Model Selector' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Request Type' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Opus 4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gemini Thinking Pro' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'GPT 4.1 mini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Perplexity' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Learn secure webhook APIs with authentication and Supabase integration:** 🟢 LOW — minimal (heuristic)
- **Fetch live ETF metrics from JustETF to Excel with one-click updates:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **Apply to Jobs from Excel and Track Application Status:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **💥 Automate Scrape Google Maps Business Leads (Email, Phone, Website) using Apify -vide II:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Extract Business Email from Website HTML (GPT-4)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Company Description Generator' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Physician Profile Enricher:** 🟢 LOW — minimal (heuristic)
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
- **LinkedIn Post To Personalized Opener:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'AI Magic' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **AI Lead Machine Agent:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **LeadBot Autopilot: Chat-to-Lead for Salesforce Automation:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Email new leads from Google Sheets via Outlook on a schedule:** ⚪ UNKNOWN — unknown
- **Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Agent One' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Judge Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 6 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Email Manager:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Anthropic Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **whats app agent community:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **RAG Starter Template using Simple Vector Stores, Form trigger and OpenAI:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Embeddings OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Automate email filtering & AI summarization. 100% free & effective, works 7/24:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Groq Chat Model1' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Automated daily workflow backup to GitHub:** 🟢 LOW — minimal (heuristic)
- **Automatic workflow & credentials backup to GitHub with change detection:** 🟢 LOW — minimal (heuristic)
- **Automated n8n workflow backup to GitHub with deletion tracking:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **Automatic FTP file backup to Google Drive with scheduled sync:** ⚪ UNKNOWN — unknown
- **Daily workflow backup to GitLab with Slack notifications:** 🟢 LOW — minimal (heuristic)
- **Email_Summarizer:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Get started with Google Sheets in n8n:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Write description' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Smart Event Follow-Up & Networking Assistant:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Analyze Profile' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Email' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate LinkedIn Msg' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent2' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Learn Customer Onboarding Automation with n8n:** 🟢 LOW — minimal (heuristic)
- **Building Prospecting Lists:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
- **Create HubSpot companies & tasks from Jotform submissions with Google Sheets:** 🟢 LOW — minimal (heuristic)
- **Identify Buying-Intent Leads on Twitter & Instagram using GPT-4o-mini with Slack Alerts and Notion CRM:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Discover Buying-Intent Leads from Social Platforms (AI)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM Reasoning Engine for Lead Qualification' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Slack & Notion Lead Insight Summary (AI)' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'LLM Reasoning Engine for Insight Structuring' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Reels Trends Watcher:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
- **💥 AI Email Assistant: Get Actionable Gmail Alerts on Telegram:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'AI – Analyze & Classify Emails' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Wordpress Blog Post Generator for WPML:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI GPT-5 Mini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Article Text' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Create Featured Image with AI' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 6 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **AI Automated TikTok/Youtube Shorts/Reels Generator:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Generate Image Prompts' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Video Captions' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Generate Script' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 8 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Veo3 Instagram Agent Workflow:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Video Prompt Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Caption Agent' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Create food emoji icons with OpenAI GPT & image generation:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'LLM: Generate Style‑JSON' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Image‑Gen: Render Food Emoji Icon' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **Klaviyo List Decay Detection Deploy:** 🟢 LOW — minimal (heuristic)
- **How to automatically import CSV files into postgres:** ⚪ UNKNOWN — unknown
- **Auto WordPress Blog Generator (GPT + Postgres + WP Media):** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent SEO Headings' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent SEO writer' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 4 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Export AI agent conversation logs from Postgres to Google Sheets:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
- **Build a knowledge base chatbot with Jotform, RAG Supabase, Together AI & Gemini:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 5 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Automate invoice processing with OCR, GPT-4 & Salesforce opportunity creation:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Message a model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Automate stale deal follow-ups in Salesforce with GPT-5.1, email, Slack & tasks:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Message a model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Discover creators among loyalty program contacts on Salesforce and send email:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Classifier Model4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Creator Classification Agent4' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Creator Classification Agent5' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Classifier Model5' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Personalized hotel reward emails for high-spenders with Salesforce, Gemini AI & Brevo:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'Basic LLM Chain' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Salesforce lead capture with GPT-4 personalized email & SMS follow-up:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Automated Lead Scraper: Apify to Google Sheets:** 🟢 LOW — minimal (heuristic)
- **Glassdoor Job Finder: Bright Data Scraping + Keyword-Based Automation:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
- **Stock market daily digest with Bright Data scraping & Gemini AI email reports:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Google Gemini Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'create summary' has variable token-based cost that can escalate
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
  - Note: AI node costs depend on token usage, not execution count
- **Apify_lead_generation:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
- **Generate Shopify product listings from images with Gemini AI and Airtable:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'analyze_image' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Basic LLM Chain' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gimini Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Turn new Shopify products into SEO blogs with Perplexity, Gemini and Sheets:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Gemini' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'web search' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'content generator' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gemini3' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **E-commerce Product Visual Generator:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Anthropic Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Sync New Shopify Customers to Odoo Contacts with Email, SMS & WhatsApp Notifications:** 🟢 LOW — minimal (heuristic)
- **AI blog generator for Shopify product listings:  Using GPT-4o and Google Sheets:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Blog Poster' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Automate Template Delivery to Customers from Stripe Payments:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
  - Driver: AI_NODE: AI/LLM node 'Azure OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Azure OpenAI Chat Model1' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent  → Google Sheets Lookup' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'AI Agent – Email Composer' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **SaaS Onboarding Template:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'GPT-4o' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'OpenAI Embeddings' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **CFO forecasting Agent:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Embeddings OpenAI' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Forecaster agent' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **🚀 Automated Stripe payment recovery: track failures & follow-up emails:** 🟢 LOW — minimal (heuristic)
- **Automated Stripe Invoicing:** 🟢 LOW — minimal (heuristic)
  - Driver: MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
- **AI Agent Content:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'AI Content Orchestrator' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Gemini Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Convert inbound lead data from Webhook to AI-qualified Asana tasks:** 🟢 LOW — minimal (heuristic)
  - Driver: AI_NODE: AI/LLM node 'AI Lead Scoring' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **AI Workflow Generator:** 🟡 MEDIUM — moderate (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Generate Workflow via AI Agent' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node '⚠️ Warning: Azure OpenAI Credentials' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Azure OpenAI Chat Model1' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count
- **Prevent duplicate webhook executions in n8n:** 🟢 LOW — minimal (heuristic)
- **Scrape, search and browse the web with a Firecrawl AI agent webhook:** 🔴 HIGH — significant (heuristic — review manually)
  - Driver: AI_NODE: AI/LLM node 'Research & Extract Web Data' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Primary Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Fallback Chat Model' has variable token-based cost that can escalate
  - Driver: AI_NODE: AI/LLM node 'Parser Chat Model' has variable token-based cost that can escalate
  - Note: AI node costs depend on token usage, not execution count

*Cost estimates are heuristic — based on static analysis, not actual financial quotes.*

## Operational Risk Findings

| Severity | Workflow | Node(s) | Finding |
|----------|----------|---------|---------|
| LOW | Workflow Patterns & Boilerplate for Scaling up | Webhook | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |
| LOW | Fetch live ETF metrics from JustETF to Excel with one-click updates | When called by Excel Macro | Webhook 'When called by Excel Macro' triggers external HTTP calls — cascading chain risk |
| LOW | Smart Event Follow-Up & Networking Assistant | Webhook Trigger | Webhook 'Webhook Trigger' triggers external HTTP calls — cascading chain risk |
| LOW | Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot | Webhook | Webhook 'Webhook' triggers external HTTP calls — cascading chain risk |
| HIGH | Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot | Loop Over Items, Loop Over Items1, Select rows from a table, Update rows in a table, Select rows from a table1, Update rows in a table1, Update rows in a table2 | Database operation inside a loop can cause performance issues and unexpected costs |
| HIGH | Auto WordPress Blog Generator (GPT + Postgres + WP Media) | Merge, Merge heading, Selecting recent, 10 latest headlines, Updating posts DB | Database operation inside a loop can cause performance issues and unexpected costs |
| HIGH | Export AI agent conversation logs from Postgres to Google Sheets | Loop Over Session IDs, add create_at column, Get conversations by sessionId, Postgres - Get session ids | Database operation inside a loop can cause performance issues and unexpected costs |
| LOW | Convert inbound lead data from Webhook to AI-qualified Asana tasks | Webhook Trigger | Webhook 'Webhook Trigger' triggers external HTTP calls — cascading chain risk |
| LOW | Prevent duplicate webhook executions in n8n | Incoming webhook event | Webhook 'Incoming webhook event' triggers external HTTP calls — cascading chain risk |

## Complexity Findings

| Severity | Workflow | Finding |
|----------|----------|---------|
| MEDIUM | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |
| MEDIUM | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | Node 'Upload Video to BLOTATO' has 6 outgoing connections (high fan-out) |
| MEDIUM | Triage emails and draft Gmail replies using Gemini and Google Calendar | Node 'Route by Draft Type' has 6 outgoing connections (high fan-out) |
| MEDIUM | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | Node 'Route Document Types' has 11 outgoing connections (high fan-out) |
| MEDIUM | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | Node 'Upload Video to Blotato' has 10 outgoing connections (high fan-out) |
| MEDIUM | 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |
| MEDIUM | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | Workflow has 63 nodes, which increases complexity |
| MEDIUM | Jarvis template | Workflow has 52 nodes, which increases complexity |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Workflow has 63 nodes, which increases complexity |
| MEDIUM | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | Node 'Branch by Intent' has 6 outgoing connections (high fan-out) |
| MEDIUM | 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | Workflow has 63 nodes, which increases complexity |
| MEDIUM | 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | Node 'Upload Video to BLOTATO' has 9 outgoing connections (high fan-out) |
| MEDIUM | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | Node 'Route by Performance' has 8 outgoing connections (high fan-out) |
| CRITICAL | Workflow Patterns & Boilerplate for Scaling up | Workflow has 240 nodes, making it very complex to maintain and debug |
| MEDIUM | Workflow Patterns & Boilerplate for Scaling up | Node 'When Executed by [trigger workflow]' has 5 outgoing connections (high fan-out) |
| MEDIUM | Build your own N8N workflows MCP server | Node 'Operations' has 5 outgoing connections (high fan-out) |
| MEDIUM | 🧑‍🎓 Test your data access techniques with progressive expression challenges | Workflow has 62 nodes, which increases complexity |
| MEDIUM | Sync New Shopify Customers to Odoo Contacts with Email, SMS & WhatsApp Notifications | Node 'Odoo (Create Contact)' has 6 outgoing connections (high fan-out) |

## Recommendations

1. Add guardrails, rate limits, and concurrency controls around loops with HTTP to prevent runaway API costs.
2. Estimate token/API cost before moving AI nodes to production. Set usage limits and monitor spend regularly.
3. Configure error workflow/handling on critical workflows to ensure failures are caught and notified.
4. Review if all external HTTP calls are necessary. Consider caching or batching to reduce dependency costs.
5. Split large workflows into smaller focused workflows to improve maintainability and reduce blast radius.
6. Review webhook chain depth and add idempotency keys to prevent duplicate processing.
7. Move database operations outside loops or batch them to avoid performance degradation and unexpected costs.

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

### 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide

- **ID:** Zwz315okMu0UwtRQ
- **Active:** ❌
- **Nodes:** 25
- **Triggers:** n8n-nodes-base.googleSheetsTrigger
- **Scores:** Cost=60 | Ops=0 | Complexity=15 | Overall=90

**Findings:**
  - [HIGH] [cost] LOOP_HTTP: HTTP Request node inside a loop/batch can multiply API calls and costs
    - Nodes: Merge1, Download Video, Veo Generation1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Parse GPT Response' has variable token-based cost that can escalate
    - Nodes: Parse GPT Response
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'GPT-4 API Call' has variable token-based cost that can escalate
    - Nodes: GPT-4 API Call
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Upload Video to BLOTATO' has 6 outgoing connections (high fan-out)
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

### eCommerce Ai Agent ( Telegram Bot )

- **ID:** 7O58hqKnq3tiUEoy
- **Active:** ❌
- **Nodes:** 16
- **Triggers:** n8n-nodes-base.telegramTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=0 | Overall=45

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'AI Agent' has variable token-based cost that can escalate
    - Nodes: AI Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenRouter Chat Model' has variable token-based cost that can escalate
    - Nodes: OpenRouter Chat Model
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

### Triage emails and draft Gmail replies using Gemini and Google Calendar

- **ID:** 15369
- **Active:** N/A
- **Nodes:** 25
- **Triggers:** n8n-nodes-base.gmailTrigger
- **Scores:** Cost=30 | Ops=0 | Complexity=15 | Overall=60

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Draft and Label Agent' has variable token-based cost that can escalate
    - Nodes: Draft and Label Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Gemini Chat Model' has variable token-based cost that can escalate
    - Nodes: Gemini Chat Model
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Route by Draft Type' has 6 outgoing connections (high fan-out)
    - Nodes: Route by Draft Type

### AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG

- **ID:** 4827
- **Active:** N/A
- **Nodes:** 35
- **Triggers:** n8n-nodes-base.manualTrigger, n8n-nodes-base.whatsAppTrigger
- **Scores:** Cost=95 | Ops=0 | Complexity=15 | Overall=100

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Knowledge Base Agent' has variable token-based cost that can escalate
    - Nodes: Knowledge Base Agent
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Embeddings OpenAI' has variable token-based cost that can escalate
    - Nodes: Embeddings OpenAI
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Embeddings Generator' has variable token-based cost that can escalate
    - Nodes: OpenAI Embeddings Generator
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
    - Nodes: OpenAI
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI1' has variable token-based cost that can escalate
    - Nodes: OpenAI1
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured
  - [LOW] [cost] MANY_HTTP: Workflow has 3 HTTP Request nodes, increasing external dependency and cost
    - Nodes: Download Voicemail, Download Image, Download Document
  - [MEDIUM] [complexity] HIGH_FAN_OUT: Node 'Route Document Types' has 11 outgoing connections (high fan-out)
    - Nodes: Route Document Types

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

### LinkedIn AI Content Automation - Agentic Vibe

- **ID:** 4968
- **Active:** ❌
- **Nodes:** 13
- **Triggers:** n8n-nodes-base.scheduleTrigger
- **Scores:** Cost=100 | Ops=0 | Complexity=0 | Overall=100

**Findings:**
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Content topic generator2' has variable token-based cost that can escalate
    - Nodes: Content topic generator2
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Content creator' has variable token-based cost that can escalate
    - Nodes: Content creator
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model1' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model1
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI' has variable token-based cost that can escalate
    - Nodes: OpenAI
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'Hashtag generator /SEO' has variable token-based cost that can escalate
    - Nodes: Hashtag generator /SEO
  - [MEDIUM] [cost] AI_NODE: AI/LLM node 'OpenAI Chat Model2' has variable token-based cost that can escalate
    - Nodes: OpenAI Chat Model2
  - [MEDIUM] [reliability] NO_ERROR_HANDLING: Workflow has no error workflow configured

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

*... and 97 more workflows with hidden details (table truncated for readability)*

## Workflow Risk Ranking

| Rank | Workflow | Overall | Cost | Ops | Complexity | Findings |
|------|----------|---------|------|-----|------------|----------|
| 1 | Workflow Patterns & Boilerplate for Scaling up | 100 | 35 | 5 | 65 | 6 |
| 2 | Auto WordPress Blog Generator (GPT + Postgres + WP Media) | 100 | 95 | 30 | 0 | 8 |
| 3 | Monitor n8n community and Reddit discussions in Telegram with Gemini and Groq | 100 | 100 | 0 | 30 | 13 |
| 4 | 💥 Automate video ads with NanoBanana, Seedream 4, ChatGPT Image and Veo 3 - VIDE | 100 | 100 | 0 | 30 | 12 |
| 5 | 💥 Generate AI Videos with Seedance & Blotato and Upload to TikTok, YouTube & Instagram - version II - vide | 100 | 95 | 0 | 15 | 8 |
| 6 | Automate Template Delivery to Customers from Stripe Payments | 100 | 90 | 0 | 0 | 6 |
| 7 | 💥 Viral TikTok Video Machine: Auto-Create UGC with VEED Avatars -vide | 100 | 80 | 0 | 15 | 7 |
| 8 | Dynamically Selects Models Based on Input Type | 100 | 100 | 0 | 0 | 9 |
| 9 | LinkedIn AI Content Automation - Agentic Vibe | 100 | 100 | 0 | 0 | 8 |
| 10 | AI-powered WhatsApp chatbot for text, voice, images, and PDF with RAG | 100 | 95 | 0 | 15 | 9 |
| 11 | Smart Event Follow-Up & Networking Assistant | 100 | 95 | 5 | 0 | 9 |
| 12 | AI Error diagnosis system | 100 | 90 | 0 | 0 | 7 |
| 13 | Autonomous B2B Supplier Price Negotiation Agent | 100 | 90 | 0 | 0 | 7 |
| 14 | AI Automated TikTok/Youtube Shorts/Reels Generator | 95 | 80 | 0 | 0 | 6 |
| 15 | Personalized email outreach with LinkedIn & Crunchbase data and Gemini AI review | 95 | 80 | 0 | 0 | 6 |
| 16 | Automated AI YouTube Shorts Factory for ASMR (Seedance) | 95 | 80 | 0 | 0 | 7 |
| 17 | Automate video creation with Veo3 and auto-post to Instagram, TikTok via Blotato - vide | 95 | 65 | 0 | 15 | 7 |
| 18 | Generate Shopify product listings from images with Gemini AI and Airtable | 90 | 75 | 0 | 0 | 5 |
| 19 | 💥 Automate AI Video Creation & Multi-Platform Publishing with Veo 3.1 & Blotato - vide | 90 | 60 | 0 | 15 | 5 |
| 20 | Track AI agent token usage and estimate costs in Google Sheets | 90 | 75 | 0 | 0 | 6 |
| 21 | Nutrition tracker & meal logger with Telegram, Gemini AI and Google Sheets | 90 | 60 | 0 | 15 | 6 |
| 22 | Send cold outreach emails and follow-ups with Resend, Postgres and HubSpot | 80 | 30 | 35 | 0 | 4 |
| 23 | Analyze crypto markets via Telegram with KuCoin, NewsAPI and Gemini | 80 | 65 | 0 | 0 | 5 |
| 24 | Generate personalized sales emails with LinkedIn data & Claude 3.7 via OpenRouter | 80 | 65 | 0 | 0 | 5 |
| 25 | Export AI agent conversation logs from Postgres to Google Sheets | 75 | 30 | 30 | 0 | 3 |
| 26 | AI Lead Machine Agent | 75 | 60 | 0 | 0 | 4 |
| 27 | 💥 Automate Scrape Google Maps Business Leads (Email, Phone, Website) using Apify -vide II | 75 | 60 | 0 | 0 | 4 |
| 28 | Auto Generate Descriptive Node Names with AI for Workflow Readability | 75 | 60 | 0 | 0 | 5 |
| 29 | Comment Analyse and Reporter | 75 | 60 | 0 | 0 | 5 |
| 30 | Discover creators among loyalty program contacts on Salesforce and send email | 75 | 60 | 0 | 0 | 5 |
| 31 | Identify Buying-Intent Leads on Twitter & Instagram using GPT-4o-mini with Slack Alerts and Notion CRM | 75 | 60 | 0 | 0 | 5 |
| 32 | Scrape, search and browse the web with a Firecrawl AI agent webhook | 75 | 60 | 0 | 0 | 5 |
| 33 | Turn new Shopify products into SEO blogs with Perplexity, Gemini and Sheets | 75 | 60 | 0 | 0 | 5 |
| 34 | n8n_fluidx_create_session | 65 | 50 | 0 | 0 | 4 |
| 35 | Wordpress Blog Post Generator for WPML | 65 | 50 | 0 | 0 | 5 |
| 36 | AI Workflow Generator | 60 | 45 | 0 | 0 | 4 |
| 37 | AI blog generator for Shopify product listings:  Using GPT-4o and Google Sheets | 60 | 45 | 0 | 0 | 4 |
| 38 | Build your first email agent with fall back model | 60 | 45 | 0 | 0 | 4 |
| 39 | CFO forecasting Agent | 60 | 45 | 0 | 0 | 4 |
| 40 | Multi-Agent Evaluation (eval nodes) | 60 | 45 | 0 | 0 | 4 |
| 41 | RAG Starter Template using Simple Vector Stores, Form trigger and OpenAI | 60 | 45 | 0 | 0 | 4 |
| 42 | SaaS Onboarding Template | 60 | 45 | 0 | 0 | 4 |
| 43 | Track SEO keyword rankings with Bright Data MCP and GPT-5.2 AI analysis | 60 | 45 | 0 | 0 | 4 |
| 44 | Build your own N8N workflows MCP server | 60 | 30 | 0 | 15 | 4 |
| 45 | Jarvis template | 60 | 30 | 0 | 15 | 4 |
| 46 | Triage emails and draft Gmail replies using Gemini and Google Calendar | 60 | 30 | 0 | 15 | 4 |
| 47 | Reels Trends Watcher | 50 | 35 | 0 | 0 | 3 |
| 48 | Fetch live ETF metrics from JustETF to Excel with one-click updates | 50 | 30 | 5 | 0 | 3 |
| 49 | AI Self-Healing Engine & Auto-Patching System | 50 | 35 | 0 | 0 | 4 |
| 50 | Build a knowledge base chatbot with Jotform, RAG Supabase, Together AI & Gemini | 50 | 35 | 0 | 0 | 4 |
| 51 | Stock market daily digest with Bright Data scraping & Gemini AI email reports | 50 | 35 | 0 | 0 | 4 |
| 52 | Transform long videos into viral shorts with AI and schedule to social media using Whisper & Gemini | 50 | 35 | 0 | 0 | 4 |
| 53 | Veo3 Instagram Agent Workflow | 50 | 35 | 0 | 0 | 4 |
| 54 | Apply to Jobs from Excel and Track Application Status | 45 | 30 | 0 | 0 | 2 |
| 55 | Automated n8n workflow backup to GitHub with deletion tracking | 45 | 30 | 0 | 0 | 2 |
| 56 | AI Agent Content | 45 | 30 | 0 | 0 | 3 |
| 57 | Automate email filtering & AI summarization. 100% free & effective, works 7/24 | 45 | 30 | 0 | 0 | 3 |
| 58 | Build your first AI agent | 45 | 30 | 0 | 0 | 3 |
| 59 | E-commerce Product Visual Generator | 45 | 30 | 0 | 0 | 3 |
| 60 | Email_Summarizer | 45 | 30 | 0 | 0 | 3 |
| 61 | Get started with Google Sheets in n8n | 45 | 30 | 0 | 0 | 3 |
| 62 | LeadBot Autopilot: Chat-to-Lead for Salesforce Automation | 45 | 30 | 0 | 0 | 3 |
| 63 | Meeting Notes Automation | 45 | 30 | 0 | 0 | 3 |
| 64 | RAG Pipeline | 45 | 30 | 0 | 0 | 3 |
| 65 | Talk to your Google Sheets using ChatGPT-5 | 45 | 30 | 0 | 0 | 3 |
| 66 | eCommerce Ai Agent ( Telegram Bot ) | 45 | 30 | 0 | 0 | 3 |
| 67 | whats app agent community | 45 | 30 | 0 | 0 | 3 |
| 68 | 🤖 Build an interactive AI agent with chat interface and multiple tools | 45 | 30 | 0 | 0 | 3 |
| 69 | Create Video with Google Veo3 and Upload to Youtube | 35 | 20 | 0 | 0 | 3 |
| 70 | Smart Inventory Replenishment & Auto-Purchase Orders | 35 | 20 | 0 | 0 | 3 |
| 71 | Convert inbound lead data from Webhook to AI-qualified Asana tasks | 35 | 15 | 5 | 0 | 3 |
| 72 | Create food emoji icons with OpenAI GPT & image generation | 30 | 30 | 0 | 0 | 2 |
| 73 | Email Manager | 30 | 30 | 0 | 0 | 2 |
| 74 | Automate invoice processing with OCR, GPT-4 & Salesforce opportunity creation | 30 | 15 | 0 | 0 | 2 |
| 75 | Automate stale deal follow-ups in Salesforce with GPT-5.1, email, Slack & tasks | 30 | 15 | 0 | 0 | 2 |
| 76 | Salesforce lead capture with GPT-4 personalized email & SMS follow-up | 30 | 15 | 0 | 0 | 2 |
| 77 | PPC campaign intelligence & optimization with Google Ads, Sheets & Slack | 30 | 0 | 0 | 15 | 2 |
| 78 | Sync New Shopify Customers to Odoo Contacts with Email, SMS & WhatsApp Notifications | 30 | 0 | 0 | 15 | 2 |
| 79 | 🧑‍🎓 Test your data access techniques with progressive expression challenges | 30 | 0 | 0 | 15 | 2 |
| 80 | Apify_lead_generation | 20 | 5 | 0 | 0 | 2 |
| 81 | Automated Stripe Invoicing | 20 | 5 | 0 | 0 | 2 |
| 82 | Building Prospecting Lists | 20 | 5 | 0 | 0 | 2 |
| 83 | Convert Old Photos to AI Videos And Auto-Publish in FB, IG, YT & X | 20 | 5 | 0 | 0 | 2 |
| 84 | Glassdoor Job Finder: Bright Data Scraping + Keyword-Based Automation | 20 | 5 | 0 | 0 | 2 |
| 85 | Loyverse Sales Report Agent | 20 | 5 | 0 | 0 | 2 |
| 86 | Process large documents with OCR using SubworkflowAI and Gemini | 20 | 5 | 0 | 0 | 2 |
| 87 | Prevent duplicate webhook executions in n8n | 20 | 0 | 5 | 0 | 2 |
| 88 | LinkedIn Post To Personalized Opener | 15 | 15 | 0 | 0 | 1 |
| 89 | Personalized hotel reward emails for high-spenders with Salesforce, Gemini AI & Brevo | 15 | 15 | 0 | 0 | 1 |
| 90 | 💥 AI Email Assistant: Get Actionable Gmail Alerts on Telegram | 15 | 15 | 0 | 0 | 1 |
| 91 | Automated Lead Scraper: Apify to Google Sheets | 15 | 0 | 0 | 0 | 1 |
| 92 | Automated Pharmacy Inventory Alerts for Low Stock & Expiry Dates with Google Sheets | 15 | 0 | 0 | 0 | 1 |
| 93 | Automated daily workflow backup to GitHub | 15 | 0 | 0 | 0 | 1 |
| 94 | Automatic workflow & credentials backup to GitHub with change detection | 15 | 0 | 0 | 0 | 1 |
| 95 | Create HubSpot companies & tasks from Jotform submissions with Google Sheets | 15 | 0 | 0 | 0 | 1 |
| 96 | Daily workflow backup to GitLab with Slack notifications | 15 | 0 | 0 | 0 | 1 |
| 97 | Klaviyo List Decay Detection Deploy | 15 | 0 | 0 | 0 | 1 |
| 98 | Learn Customer Onboarding Automation with n8n | 15 | 0 | 0 | 0 | 1 |
| 99 | Learn secure webhook APIs with authentication and Supabase integration | 15 | 0 | 0 | 0 | 1 |
| 100 | New Appointment → Welcome SMS | 15 | 0 | 0 | 0 | 1 |
| 101 | Physician Profile Enricher | 15 | 0 | 0 | 0 | 1 |
| 102 | 🎓 Learn JSON basics with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | 1 |
| 103 | 🎓 Learn n8n expressions with an interactive step-by-step tutorial for beginners | 15 | 0 | 0 | 0 | 1 |
| 104 | 🚀 Automated Stripe payment recovery: track failures & follow-up emails | 15 | 0 | 0 | 0 | 1 |
| 105 | Automatic FTP file backup to Google Drive with scheduled sync | 0 | 0 | 0 | 0 | 0 |
| 106 | Email new leads from Google Sheets via Outlook on a schedule | 0 | 0 | 0 | 0 | 0 |
| 107 | How to automatically import CSV files into postgres | 0 | 0 | 0 | 0 | 0 |

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