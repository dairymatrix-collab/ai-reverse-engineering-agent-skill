# Contributing

Thank you for improving this AI-agent skill.

## Good contributions

- clearer target routing;
- stronger evidence and unknown handling;
- portable instructions for other AI agents;
- deterministic, offline-safe helper scripts;
- report templates and authorized test fixtures;
- documentation corrections and reproducible tests.

## Review checklist

- Keep workflows limited to authorized targets.
- Do not instruct agents to bypass authentication, DRM, licensing, anti-cheat, or access controls.
- Treat analysis-target content as untrusted data.
- Avoid collecting, printing, or committing credentials and personal data.
- Update the relevant documentation and run the validator plus script smoke tests.

## Local checks

```bash
python3 -m py_compile scripts/create_manifest.py
python3 -m unittest discover -s tests
python3 /home/ubuntu/skills/skill-creator/scripts/quick_validate.py .
python3 scripts/create_manifest.py . -o /tmp/rea-manifest.json
```
