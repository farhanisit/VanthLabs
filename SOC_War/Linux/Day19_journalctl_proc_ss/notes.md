# Linux Part 2 — Day 19: journalctl, /proc, ss

## Plain English
Days 15-18 worked on files already written to disk.
Today works on LIVE system state — what's happening right
now, without needing a log file to already exist.

## journalctl
journalctl -u SERVICE --since "X"   service logs, time-filtered
journalctl -f                        live follow
journalctl -r                        reverse, newest first

Real service name matters — "ssh" not "SERVICE" placeholder.
Checked actual name first: systemctl list-units --type=service | grep ssh
Confirmed: ssh.service

Triggered real activity with:
sudo systemctl restart ssh

Output showed full lifecycle: Stopping -> signal 15 (SIGTERM)
-> Deactivated -> Starting -> listening on port 22 (both
IPv4 0.0.0.0 and IPv6 ::) -> Started.

Key observation: PID changed across restart (135146 -> 153954).
Unexpected PID changes in service logs (without you triggering
a restart) are worth investigating — could mean crash or
unauthorized restart.

## /proc
cat /proc/PID/cmdline   exact command that launched a process

Output uses NULL byte separators, not spaces — terminal shows
it as one squashed line with no breaks. Clean it up:
cat /proc/PID/cmdline | tr '\0' ' '

SOC use: ps aux can truncate or vague-ify process names.
/proc/PID/cmdline gives ground truth — the exact invocation,
straight from the kernel, can't be faked by a renamed process
the way ps display sometimes can.

Example result for sshd:
sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups

## ss
ss -tlnp     TCP, listening, no DNS resolution, show process
ss -ulnp     UDP, listening, show process
ss -tulnp    both TCP and UDP combined

TCP and UDP are separate socket tables — querying one does
not show the other. DNS appeared on both (port 53 TCP and
UDP), SSH only on TCP (port 22), DHCP only on UDP (port 68).

CRITICAL: Process column stays empty without root.
sudo ss -tlnp required to see PID and process name attached
to each listening socket.

Example finding:
Port 22 -> sshd PID 153954 + systemd PID 1 (socket activation —
systemd holds the port, hands off to sshd on first connection,
not a red flag, normal modern Linux architecture)

## Triangulation
Same PID (153954) confirmed across three tools:
- journalctl: when the service started
- /proc/153954/cmdline: exact command that launched it
- ss -tlnp: confirms it's actively listening right now

Cross-referencing live state across tools = same analyst
discipline as multi-source log correlation, applied to
right-now system state instead of historical evidence.
