# AI Accounts (deprecated)

> **Deprecated.** Replaced by the Claude and ChatGPT apps (decision #61). Install [Claude](https://github.com/oscarhenrycollins/claude-connection): it uses the same sign-in volume, so you stay connected, then uninstall AI Accounts.

Connect your Claude subscription once, and every agent on the box uses it.

A [Wizard app](https://www.aiwizards.com/wizard-apps) (System App). Open its page, press **Connect** next to Claude subscription, sign in with Claude, paste the code, and press **Test**. The sign-in runs Anthropic's official Claude Code login and stays in the private shared volume `wizard-ai-accounts-claude`, which agent apps (Hermes Agent from Wizard Apps) mount at `/claude`. Agents never see the token. ChatGPT sign-in and API keys are next.

- `wizard.md`: what the app is and what it gives the agent (spec: wizard.md v0.2).
- `runtipi/`: stock Runtipi `config.json` and `docker-compose.yml`.
- `mcp/`: a read-only MCP (`ai_accounts_status`) inlined into the compose file by `python3 mcp/inline.py`. Connecting and disconnecting stay owner actions on the page.
- `server.py`, `static/`, `Dockerfile`: the AI Accounts page image (`ghcr.io/humanitylabs-org/wizard-ai-accounts`).
- `SKILL.md`: the skill the agent loads when this app is installed.
- `.github/workflows/publish.yml`: every push to `main` re-publishes to the index.

Personal use of your own subscription on your own server. Products for other people should use API keys.

## Deprecated

This app is retired and no longer listed in the Wizard App Index. Use the Claude and ChatGPT apps instead (decision #61); the Claude app keeps your sign-in. The last listed manifest is in git history.
