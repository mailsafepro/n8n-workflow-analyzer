from __future__ import annotations

from typing import Final

NODE_CATEGORIES: Final[dict[str, str]] = {
    # trigger
    "n8n-nodes-base.manualTrigger": "trigger",
    "n8n-nodes-base.webhook": "trigger",
    "n8n-nodes-base.respondToWebhook": "trigger",
    "n8n-nodes-base.scheduleTrigger": "trigger",
    "n8n-nodes-base.cron": "trigger",
    "n8n-nodes-base.interval": "trigger",
    "n8n-nodes-base.telegramTrigger": "trigger",
    "n8n-nodes-base.gmailTrigger": "trigger",
    "n8n-nodes-base.emailSendTrigger": "trigger",
    "n8n-nodes-base.httpTrigger": "trigger",
    "n8n-nodes-base.sseTrigger": "trigger",
    "n8n-nodes-base.timerTrigger": "trigger",
    "n8n-nodes-base.start": "trigger",
    "n8n-nodes-base.chatTrigger": "trigger",
    "@n8n/n8n-nodes-langchain.chatTrigger": "trigger",
    "n8n-nodes-base.googleDriveTrigger": "trigger",
    "n8n-nodes-base.googleSheetsTrigger": "trigger",
    # ai
    "n8n-nodes-base.openAi": "ai",
    "n8n-nodes-base.anthropicAi": "ai",
    "@n8n/n8n-nodes-langchain.openAi": "ai",
    "@n8n/n8n-nodes-langchain.lmChatOpenAi": "ai",
    "@n8n/n8n-nodes-langchain.lmChatGoogleGemini": "ai",
    "@n8n/n8n-nodes-langchain.lmChatOpenRouter": "ai",
    "@n8n/n8n-nodes-langchain.agent": "ai",
    "@n8n/n8n-nodes-langchain.chainLlm": "ai",
    "@n8n/n8n-nodes-langchain.memoryBufferWindow": "ai",
    "@n8n/n8n-nodes-langchain.vectorStorePinecone": "ai",
    "@n8n/n8n-nodes-langchain.embeddingsGoogleGemini": "ai",
    "@n8n/n8n-nodes-langchain.toolVectorStore": "ai",
    "@n8n/n8n-nodes-langchain.documentDefaultDataLoader": "ai",
    "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter": "ai",
    "@n8n/n8n-nodes-langchain.outputParserAutofixing": "ai",
    "@n8n/n8n-nodes-langchain.outputParserStructured": "ai",
    "n8n-nodes-base.perplexity": "ai",
    # email
    "n8n-nodes-base.gmail": "email",
    "n8n-nodes-base.gmailTool": "email",
    "n8n-nodes-base.emailSend": "email",
    "n8n-nodes-base.emailRead": "email",
    "n8n-nodes-base.imap": "email",
    "n8n-nodes-base.smtp": "email",
    "n8n-nodes-base.outlook": "email",
    "n8n-nodes-base.microsoftToDo": "email",
    # communication
    "n8n-nodes-base.telegram": "communication",
    "n8n-nodes-base.slack": "communication",
    "n8n-nodes-base.discord": "communication",
    "n8n-nodes-base.microsoftTeams": "communication",
    "n8n-nodes-base.whatsapp": "communication",
    "n8n-nodes-base.mattermost": "communication",
    "n8n-nodes-base.twilio": "communication",
    # database
    "n8n-nodes-base.postgres": "database",
    "n8n-nodes-base.mySql": "database",
    "n8n-nodes-base.microsoftSql": "database",
    "n8n-nodes-base.snowflake": "database",
    "n8n-nodes-base.mongoDb": "database",
    "n8n-nodes-base.redis": "database",
    "n8n-nodes-base.supabase": "database",
    "n8n-nodes-base.elasticsearch": "database",
    "n8n-nodes-base.couchbase": "database",
    "n8n-nodes-base.dynamoDb": "database",
    "n8n-nodes-base.arangoDb": "database",
    # spreadsheet
    "n8n-nodes-base.googleSheets": "spreadsheet",
    "n8n-nodes-base.airtable": "spreadsheet",
    "n8n-nodes-base.microsoftExcel": "spreadsheet",
    # storage
    "n8n-nodes-base.googleDrive": "storage",
    "n8n-nodes-base.s3": "storage",
    "n8n-nodes-base.dropbox": "storage",
    "n8n-nodes-base.box": "storage",
    "n8n-nodes-base.oneDrive": "storage",
    "n8n-nodes-base.convertToFile": "storage",
    # crm
    "n8n-nodes-base.salesforce": "crm",
    "n8n-nodes-base.hubspot": "crm",
    "n8n-nodes-base.pipedrive": "crm",
    "n8n-nodes-base.zoho": "crm",
    # marketing
    "n8n-nodes-base.mailchimp": "marketing",
    "n8n-nodes-base.activeCampaign": "marketing",
    "n8n-nodes-base.sendgrid": "marketing",
    "n8n-nodes-base.facebook": "marketing",
    "n8n-nodes-base.facebookGraph": "marketing",
    # http / api
    "n8n-nodes-base.httpRequest": "http_api",
    "n8n-nodes-base.graphql": "http_api",
    "n8n-nodes-base.awsLambda": "http_api",
    # transform
    "n8n-nodes-base.set": "transform",
    "n8n-nodes-base.editFields": "transform",
    "n8n-nodes-base.itemLists": "transform",
    "n8n-nodes-base.aggregate": "transform",
    "n8n-nodes-base.summarize": "transform",
    "n8n-nodes-base.sort": "transform",
    "n8n-nodes-base.filter": "transform",
    "n8n-nodes-base.removeDuplicates": "transform",
    "n8n-nodes-base.renameKeys": "transform",
    "n8n-nodes-base.limit": "transform",
    "n8n-nodes-base.splitOut": "transform",
    "n8n-nodes-base.code": "transform",
    "n8n-nodes-base.function": "transform",
    "n8n-nodes-base.functionItem": "transform",
    "n8n-nodes-base.noOp": "transform",
    "n8n-nodes-base.stopAndError": "transform",
    # control_flow
    "n8n-nodes-base.if": "control_flow",
    "n8n-nodes-base.switch": "control_flow",
    "n8n-nodes-base.merge": "control_flow",
    "n8n-nodes-base.splitInBatches": "control_flow",
    "n8n-nodes-base.loop": "control_flow",
    "n8n-nodes-base.wait": "control_flow",
    "n8n-nodes-base.compareDatasets": "control_flow",
    "n8n-nodes-base.executeWorkflow": "control_flow",
    "n8n-nodes-base.stickyNote": "control_flow",
    # human_input
    "n8n-nodes-base.form": "human_input",
    "n8n-nodes-base.formTrigger": "human_input",
    "n8n-nodes-base.waitForWebhook": "human_input",
    # devops
    "n8n-nodes-base.ssh": "devops",
    "n8n-nodes-base.docker": "devops",
    "n8n-nodes-base.github": "devops",
    "n8n-nodes-base.gitlab": "devops",
    "n8n-nodes-base.jira": "devops",
    "n8n-nodes-base.jiraSoftware": "devops",
    "n8n-nodes-base.n8n": "devops",
    # observability
    "n8n-nodes-base.sentry": "observability",
    "n8n-nodes-base.datadog": "observability",
    # calendar
    "n8n-nodes-base.googleCalendar": "calendar",
    "n8n-nodes-base.googleCalendarTool": "calendar",
    "n8n-nodes-base.calendly": "calendar",
    "n8n-nodes-base.calendarTrigger": "trigger",
    # scraping
    "n8n-nodes-base.html": "scraping",
    "n8n-nodes-base.htmlExtract": "scraping",
    "n8n-nodes-base.readPdf": "document",
    # baserow / no-code DB
    "n8n-nodes-base.baserowTool": "spreadsheet",
    "n8n-nodes-base.nocoDb": "database",
    # document
    "n8n-nodes-base.googleDocs": "document",
    "n8n-nodes-base.extractFromFile": "document",
    # transform (utility / data tools)
    "n8n-nodes-base.cryptoTool": "transform",
    "n8n-nodes-base.dataTable": "transform",
    "n8n-nodes-base.dateTimeTool": "transform",
    # crm
    "n8n-nodes-base.notion": "crm",
    "n8n-nodes-base.wooCommerceTool": "crm",
    "n8n-nodes-base.googleContactsTool": "crm",
    "n8n-nodes-base.googleTasksTool": "crm",
    # marketing
    "n8n-nodes-base.googleAds": "marketing",
    "n8n-nodes-base.youTube": "marketing",
    # triggers (missing from exact list)
    "n8n-nodes-base.twilioTrigger": "trigger",
    "n8n-nodes-base.typeformTrigger": "trigger",
    "n8n-nodes-base.errorTrigger": "trigger",
    "n8n-nodes-base.evaluationTrigger": "trigger",
    "n8n-nodes-base.executeWorkflowTrigger": "trigger",
    # scraping
    "n8n-nodes-base.rssFeedReadTool": "scraping",
    # control_flow
    "n8n-nodes-base.evaluation": "control_flow",
    # community / custom
    "n8n-nodes-mcp.mcpClientTool": "devops",
    "@blotato/n8n-nodes-blotato.blotato": "marketing",
    "@tavily/n8n-nodes-tavily.tavilyTool": "ai",
    "@elevenlabs/n8n-nodes-elevenlabs.elevenLabs": "ai",
    "CUSTOM.scrapeNinja": "scraping",
}

# Category keywords for heuristic matching (type-based, not name-based)
# Only used as fallback when exact type not found.
# Each keyword maps to a category. Keywords must be 3+ chars and not cause false positives.
_TYPE_KEYWORD_CATEGORIES: Final[list[tuple[str, str]]] = [
    ("sentry", "observability"),
    ("datadog", "observability"),
    ("grafana", "observability"),
    ("slack", "communication"),
    ("discord", "communication"),
    ("telegram", "communication"),
    ("whatsapp", "communication"),
    ("outlook", "email"),
    ("imap", "email"),
    ("smtp", "email"),
    ("gmail", "email"),
    ("postgres", "database"),
    ("mysql", "database"),
    ("mongo", "database"),
    ("redis", "database"),
    ("supabase", "database"),
    ("sqlite", "database"),
    ("snowflake", "database"),
    ("airtable", "spreadsheet"),
    ("googleSheets", "spreadsheet"),
    ("googleDrive", "storage"),
    ("salesforce", "crm"),
    ("hubspot", "crm"),
    ("pipedrive", "crm"),
    ("zoho", "crm"),
    ("mailchimp", "marketing"),
    ("sendgrid", "marketing"),
    ("github", "devops"),
    ("gitlab", "devops"),
    ("jira", "devops"),
    ("docker", "devops"),
    ("ssh", "devops"),
    ("httpRequest", "http_api"),
    ("graphql", "http_api"),
    ("stickyNote", "control_flow"),
    ("scheduleTrigger", "trigger"),
    ("cron", "trigger"),
    ("timerTrigger", "trigger"),
    ("webhook", "trigger"),
    ("manualTrigger", "trigger"),
    ("formTrigger", "trigger"),
    ("googleDriveTrigger", "trigger"),
    # langchain
    ("langchain", "ai"),
    ("lmChat", "ai"),
    ("openAi", "ai"),
    ("anthropic", "ai"),
    ("embeddings", "ai"),
    ("vectorStore", "ai"),
    ("chainLlm", "ai"),
    ("outputParser", "ai"),
]


def classify_node_type(node_type: str, node_name: str = "") -> str:
    """Classify an n8n node type into a category string.

    Uses an explicit dict lookup first, then falls back to keyword matching
    on the node type string. If still unknown, returns 'unknown'.
    """
    exact = NODE_CATEGORIES.get(node_type)
    if exact is not None:
        return exact

    lower = node_type.lower()
    for keyword, category in _TYPE_KEYWORD_CATEGORIES:
        if keyword.lower() in lower:
            return category

    return "unknown"
