---
wizard: 0.2
id: wizard-ai-accounts
name: AI Accounts
type: external
category: system
tags: [security]
version: 0.1.1
summary: "Deprecated: replaced by the Claude and ChatGPT apps (decision #61). Install Claude instead; it keeps your sign-in."
icon: icon.png
license: MIT
source: https://github.com/oscarhenrycollins/ai-accounts
runtime:
  kind: runtipi
  config: runtipi/config.json
  compose: runtipi/docker-compose.yml
mcp:
  path: /mcp
  port: 8795
  transport: streamable-http
skill: SKILL.md
view:
  path: /
  port: 8795
provides:
- ai-accounts
- claude-subscription
health: /health
---

# AI Accounts

**Deprecated.** Replaced by the Claude and ChatGPT apps (decision #61). Install Claude (`wizard-claude`): it uses the same sign-in volume, so you stay connected.

Connect your Claude subscription once on the AI Accounts page, and every agent on this Wizard uses it. The sign-in runs Anthropic's official Claude Code login and stays in a private shared volume; agents never see the token. ChatGPT sign-in and API keys come later.
