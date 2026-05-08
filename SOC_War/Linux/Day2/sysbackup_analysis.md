# Day 2 — Account Investigation: sysbackup

## Findings

**Account:** sysbackup (UID 1001)
**Shell:** /bin/bash (real login access)
**Home Dir:** /home/sysbackup (exists)
**Creation Date:** Apr 3 20:33
**System Install Date:** Mar 21 2026
**Gap:** 13 days post-install

**Auth Log Activity:** None found

## Assessment
- Account exists with legitimate configuration
- No recorded login attempts
- Created post-install, not part of original system
- **Risk Level:** Medium — potential persistence account

## Next Steps
- Check sudo access: `sudo -l -U sysbackup`
- Review cron jobs: `crontab -u sysbackup -l`
- Check SSH keys: `ls -la /home/sysbackup/.ssh/`
