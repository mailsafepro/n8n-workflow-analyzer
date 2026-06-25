from __future__ import annotations

from n8n_cost_analyzer.node_classifier import NODE_CATEGORIES, classify_node_type


def test_classifies_common_triggers():
    assert classify_node_type("n8n-nodes-base.webhook") == "trigger"
    assert classify_node_type("n8n-nodes-base.scheduleTrigger") == "trigger"
    assert classify_node_type("n8n-nodes-base.cron") == "trigger"
    assert classify_node_type("n8n-nodes-base.manualTrigger") == "trigger"
    assert classify_node_type("n8n-nodes-base.telegramTrigger") == "trigger"
    assert classify_node_type("n8n-nodes-base.gmailTrigger") == "trigger"
    assert classify_node_type("@n8n/n8n-nodes-langchain.chatTrigger") == "trigger"


def test_classifies_gmail_as_email_not_ai():
    assert classify_node_type("n8n-nodes-base.gmail") == "email"
    assert classify_node_type("n8n-nodes-base.gmailTool") == "email"
    assert classify_node_type("n8n-nodes-base.gmailTrigger") == "trigger"


def test_classifies_wait_as_control_flow_not_ai():
    assert classify_node_type("n8n-nodes-base.wait") == "control_flow"


def test_classifies_if_as_control_flow():
    assert classify_node_type("n8n-nodes-base.if") == "control_flow"
    assert classify_node_type("n8n-nodes-base.merge") == "control_flow"
    assert classify_node_type("n8n-nodes-base.splitInBatches") == "control_flow"
    assert classify_node_type("n8n-nodes-base.switch") == "control_flow"


def test_classifies_langchain_openai_as_ai():
    assert classify_node_type("@n8n/n8n-nodes-langchain.openAi") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.lmChatOpenAi") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.lmChatGoogleGemini") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.agent") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.vectorStorePinecone") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.embeddingsGoogleGemini") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.chainLlm") == "ai"
    assert classify_node_type("@n8n/n8n-nodes-langchain.memoryBufferWindow") == "ai"


def test_classifies_salesforce_as_crm():
    assert classify_node_type("n8n-nodes-base.salesforce") == "crm"
    assert classify_node_type("n8n-nodes-base.hubspot") == "crm"


def test_classifies_google_sheets_as_spreadsheet():
    assert classify_node_type("n8n-nodes-base.googleSheets") == "spreadsheet"
    assert classify_node_type("n8n-nodes-base.airtable") == "spreadsheet"


def test_classifies_http_request_as_http_api():
    assert classify_node_type("n8n-nodes-base.httpRequest") == "http_api"


def test_unknown_remains_unknown():
    assert classify_node_type("completely.random.node") == "unknown"


def test_all_node_categories_are_nonempty():
    for node_type, cat in NODE_CATEGORIES.items():
        assert cat, f"Empty category for {node_type}"
        assert isinstance(cat, str), f"Non-string category for {node_type}"


def test_classifies_blotato_as_marketing():
    assert classify_node_type("@blotato/n8n-nodes-blotato.blotato") == "marketing"


def test_classifies_tavily_as_ai():
    assert classify_node_type("@tavily/n8n-nodes-tavily.tavilyTool") == "ai"


def test_classifies_scrape_ninja_as_scraping():
    assert classify_node_type("CUSTOM.scrapeNinja") == "scraping"


def test_classifies_mcp_as_devops():
    assert classify_node_type("n8n-nodes-mcp.mcpClientTool") == "devops"


def test_keyword_fallback_does_not_false_positive_ai():
    assert classify_node_type("n8n-nodes-base.gmailTool") == "email"
    assert classify_node_type("n8n-nodes-base.wait") == "control_flow"
    assert classify_node_type("n8n-nodes-base.telegram") == "communication"
    assert classify_node_type("n8n-nodes-base.scheduleTrigger") == "trigger"


def test_classifies_http_request_tool():
    assert classify_node_type("n8n-nodes-base.httpRequestTool") == "http_api"


def test_classifies_google_sheets_tool():
    assert classify_node_type("n8n-nodes-base.googleSheetsTool") == "spreadsheet"


def test_classifies_google_sheets_trigger_as_trigger():
    assert classify_node_type("n8n-nodes-base.googleSheetsTrigger") == "trigger"


def test_classifies_google_docs():
    assert classify_node_type("n8n-nodes-base.googleDocs") == "document"


def test_classifies_crypto_tool():
    assert classify_node_type("n8n-nodes-base.cryptoTool") == "transform"


def test_classifies_data_table():
    assert classify_node_type("n8n-nodes-base.dataTable") == "transform"


def test_classifies_date_time_tool():
    assert classify_node_type("n8n-nodes-base.dateTimeTool") == "transform"


def test_classifies_notion():
    assert classify_node_type("n8n-nodes-base.notion") == "crm"


def test_classifies_rss_feed_tool():
    assert classify_node_type("n8n-nodes-base.rssFeedReadTool") == "scraping"


def test_classifies_woo_commerce_tool():
    assert classify_node_type("n8n-nodes-base.wooCommerceTool") == "crm"


def test_classifies_youtube():
    assert classify_node_type("n8n-nodes-base.youTube") == "marketing"


def test_classifies_twilio_trigger():
    assert classify_node_type("n8n-nodes-base.twilioTrigger") == "trigger"


def test_classifies_typeform_trigger():
    assert classify_node_type("n8n-nodes-base.typeformTrigger") == "trigger"


def test_classifies_error_trigger():
    assert classify_node_type("n8n-nodes-base.errorTrigger") == "trigger"


def test_classifies_evaluation():
    assert classify_node_type("n8n-nodes-base.evaluation") == "control_flow"


def test_classifies_evaluation_trigger():
    assert classify_node_type("n8n-nodes-base.evaluationTrigger") == "trigger"


def test_classifies_execute_workflow_trigger():
    assert classify_node_type("n8n-nodes-base.executeWorkflowTrigger") == "trigger"


def test_classifies_extract_from_file():
    assert classify_node_type("n8n-nodes-base.extractFromFile") == "document"


def test_classifies_google_ads():
    assert classify_node_type("n8n-nodes-base.googleAds") == "marketing"


def test_classifies_google_contacts_tool():
    assert classify_node_type("n8n-nodes-base.googleContactsTool") == "crm"


def test_classifies_google_tasks_tool():
    assert classify_node_type("n8n-nodes-base.googleTasksTool") == "crm"


def test_classifies_elevenlabs_ai():
    assert classify_node_type("@elevenlabs/n8n-nodes-elevenlabs.elevenLabs") == "ai"


def test_keyword_fallback_matches_case_insensitively():
    assert classify_node_type("n8n-nodes-base.httpRequestTool") == "http_api"
    assert classify_node_type("n8n-nodes-base.googleSheetsTool") == "spreadsheet"
