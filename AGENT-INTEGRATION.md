# Portable agent integration

This folder is intentionally plain Markdown plus one standard-library Python script. Any AI agent that supports instruction files can load `SKILL.md` as its system/project skill.

## Recommended loading order

1. Load `SKILL.md`.
2. Load `references/rea-workflows.md` when routing a target or interpreting evidence.
3. Copy `templates/investigation-report.md` for each investigation.
4. Run `scripts/create_manifest.py TARGET -o rea-manifest.json` before analysis when a local file or directory is available.

## REA connection

The instruction package does not pretend to provide the REA MCP server. If the agent supports MCP, register the official REA server through the upstream setup workflow. If the agent only supports shell commands, use the official CLI after reviewing its setup plan:

```bash
npx rea-agents@latest setup
npx -y rea-agents@latest doctor --json
```

Use the actual tool list and schemas advertised by the connected server. Do not copy credentials into prompts or reports.

## Minimal prompt

"Use the REA reverse-engineering skill. Analyze this authorized target: `/absolute/path`. Start with a manifest and static summary. Answer: `[question]`. Cite Evidence IDs, separate observed/inferred/unknown facts, avoid runtime/network/device actions unless explicitly scoped, and fill the investigation report template."
