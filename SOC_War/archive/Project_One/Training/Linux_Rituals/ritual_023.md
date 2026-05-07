# CLI_RITUAL_023 — Case Study: Broken Flask Script
📅 Date: 2025-05-24
🧠 Mode: Scenario + Debug Logic

## Scenario:
Deployment script fails. Turns out:
- `chmod +x` missing
- `chown` misconfigured (root-owned venv)

## Commands:
- `ls -l`
- `chmod +x start_app.sh`
- `chown -R vanth:vanth venv/`
- `./start_app.sh`

## Real-World Value:
Understanding permission layers helps in **live bug fixing**, **CTF privilege escalations**, and **automation failures**.

## Next Actions:
- Save this to `CaseStudy_PermissionBreaks.md`
- Try a THM machine where broken perms are part of the challenge

