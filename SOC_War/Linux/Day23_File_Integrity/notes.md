# Linux Part 2 — Day 23: File Integrity

## Plain English
A file can be modified without changing its name, size, or
timestamp. File integrity checking detects this by taking a
FINGERPRINT (hash) of the file's contents. If the fingerprint
changes, the contents changed. No argument possible.

## The Two Tools
md5sum    = fast, 128-bit, cryptographically weak (known
            collisions demonstrated). Use for convenience/
            speed only, NOT for security-critical verification.
sha256sum = strong, 256-bit, no known practical collisions.
            Use for everything security-related.

Rule: when in doubt, always sha256sum.

## Commands
sha256sum filename              generate hash
sha256sum filename > file.sha256   save hash to file
sha256sum -c file.sha256        verify file against saved hash
sha256sum filename              hash any file, including .sha256
                                files themselves (meta-integrity)

## Lab Results
Generated hash of auth_sample.log:
420246efd88197beb06b0519c772770393f33ce6dd1e9ab21dc8a65b16c49eba

Verified clean: auth_sample.log: OK
Modified file (appended lines), re-verified:
auth_sample.log: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match

FAILED detection confirmed: one changed character (or added
lines) = completely different hash = immediate detection.

## Key Observations
- sha256sum on a .sha256 file hashes the HASH FILE ITSELF,
  not the file it references. Use -c flag to verify properly.
- >> appends to a file without overwriting. Even one appended
  line completely changes the hash output.
- rm with wrong arguments can delete unintended files. Always
  double-check rm commands, especially on investigation machines
  where files are evidence.

## SOC Use Cases
Evidence preservation: sha256sum disk_image.dd > disk_image.sha256
Baseline checking: hash known-good binaries, compare after incident
Download verification: compare vendor-published hash against local

## Day 24 — Capstone Format
Three evidence sources, one scenario, cold investigation.
Tools in scope: all of Part 2 (awk, sed, find, journalctl,
/proc, ss, Python, sha256sum, SSH hardening knowledge).
Output: unified timeline + 5-layer classification + L2 brief
+ "what Part 2 tools catch this" section.
Decision pending: purely Linux-side vs cross-telemetry surfaces.
