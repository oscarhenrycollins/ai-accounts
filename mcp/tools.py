# Read-only by design: connecting, disconnecting and the test call are owner actions on the AI Accounts
# page. The MCP only reports status (plan and account label), never a token.


@tool("ai_accounts_status", "Which AI subscriptions are connected on this Wizard (Claude now; ChatGPT and API keys later), "
      "and what the owner should do if one is not connected.")
def ai_accounts_status():
    headers = {}
    auth = REQUEST.get().get("authorization")
    if auth:
        headers["Authorization"] = auth  # the page password (Basic), forwarded unchanged
    _, raw = http("GET", "/api/accounts", None, headers, timeout=30)
    d = json.loads(raw)
    rows = [{k: a.get(k) for k in ("id", "name", "status", "plan", "account", "signing_in") if a.get(k) is not None}
            for a in d.get("accounts") or []]
    return {"accounts": rows, "version": d.get("version"),
            "if_not_connected": "Ask the owner to open AI Accounts, press Connect next to Claude subscription, sign in, "
                                "paste the code, then press Test. Never ask for the code or a token in chat."}
