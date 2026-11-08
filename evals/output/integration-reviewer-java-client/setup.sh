#!/usr/bin/env bash
set -euo pipefail
cat > ClaudeClient.java <<'EOF'
package com.acme.ai;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.*;

public class ClaudeClient {
    private static final AnthropicClient CLIENT = AnthropicOkHttpClient.builder()
        .apiKey("sk-ant-api03-EXAMPLEKEYDONOTUSE")
        .build();

    public String extractInvoice(String invoiceText) {
        while (true) {
            try {
                MessageCreateParams params = MessageCreateParams.builder()
                    .model("claude-sonnet-5-5")
                    .maxTokens(1024)
                    .addUserMessage("Extract invoice fields as JSON:\n" + invoiceText)
                    .addAssistantMessage("{")
                    .addTool(InvoiceTools.SAVE_INVOICE)
                    .toolChoice(ToolChoiceAny.builder().build())
                    .build();
                Message m = CLIENT.messages().create(params);
                return "{" + m.content().get(0).text().get().text();
            } catch (Exception e) {
                // try again
            }
        }
    }
}
EOF
