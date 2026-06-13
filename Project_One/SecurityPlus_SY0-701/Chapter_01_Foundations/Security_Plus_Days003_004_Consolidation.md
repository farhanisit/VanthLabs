# Security+ SY0-701 — Days 003 & 004 Consolidation
## Lessons 011–020

---

## Lesson 011: Change Management I

**Core idea:** Controlled changes, not random changes.

**Key steps:**
Request → Assess → Approve → Test → Schedule → Implement → Document → Review

**Exam keywords:** Change request, impact analysis, maintenance window, backout plan, rollback

**Final memory line:** Change management = controlled changes, not random changes.

---

## Lesson 012: Change Management II

**Core idea:** Recognise which part of change management failed.

| Scenario | What failed |
|---|---|
| No permission obtained | Approval |
| No way to undo the change | Backout/rollback plan |
| Effects not understood | Impact analysis |
| No record of change | Documentation / version control |
| Users not warned | Stakeholder notification |
| Changed during business hours causing disruption | Maintenance window |

**Final memory line:** Request → Assess → Approve → Test → Schedule → Implement → Document → Review

---

## Lesson 013: Risk Basics

**Core idea:** Risk = the chance a threat exploits a vulnerability and causes harm.

| Term | Meaning |
|---|---|
| Asset | Something valuable |
| Threat | Something that can cause harm |
| Vulnerability | A weakness |
| Impact | Damage if it happens |
| Likelihood | Chance of it happening |
| Risk | Likelihood × Impact |

**Final memory line:** Risk = bad thing could happen and cause damage.

---

## Lesson 014: Threat vs Vulnerability vs Risk

| Term | Meaning | Example |
|---|---|---|
| Threat | Who/what attacks | Ransomware group, attacker, fire |
| Vulnerability | The weakness | Missing patch, weak password, open port |
| Risk | Possible damage scenario | Attacker exploits weak login and steals data |

**Analogy:** Bike (asset) + unlocked gate (vulnerability) + thief (threat) = risk of theft.

**Final memory line:** Threat = who attacks. Vulnerability = the weakness. Risk = the damage scenario.

---

## Lesson 015: Exposure vs Impact vs Likelihood

| Term | Meaning | Example |
|---|---|---|
| Exposure | How open/vulnerable something is | Database directly on internet |
| Likelihood | How probable the event is | Weekly phishing campaigns |
| Impact | How much damage if it occurs | Ransomware stopping emergency admissions |

**Exam trap:** High impact ≠ high likelihood. High likelihood ≠ high impact. They are independent variables.

**Final memory line:** Exposure = how open. Likelihood = how probable. Impact = how bad.

---

## Lesson 016: Encryption vs Hashing vs Encoding

| Method | Purpose | Reversible? | Security use |
|---|---|---|---|
| Encryption | Hide data | Yes, with key | Confidentiality |
| Hashing | Fingerprint data | No | Integrity |
| Encoding | Reformat data | Yes, easily | Not a security control |

**Exam traps:**
- Base64 is encoding, not encryption.
- Hashing does not provide confidentiality.
- Encryption protects secrecy; hashing checks integrity.

**Final memory line:** Encrypt = hide. Hash = fingerprint. Encode = reformat.

---

## Lesson 017: Hashing, Salting, and Password Storage

**Core idea:** Passwords must be stored as salted hashes, never plaintext.

**Login verification flow:**
1. User enters password
2. System adds stored salt
3. System hashes the result
4. Compare new hash with stored hash
5. Match = login success

**Why salting matters:** Same password + different salt = different hash. Defeats rainbow table attacks.

**Exam trap:** You do not decrypt a password hash. You compare hashes.

**Final memory line:** Password + salt → hash stored.

---

## Lesson 018: Digital Signatures

**Core idea:** A digital signature proves who signed something and that data was not altered.

**What it provides:** Integrity + Authentication + Non-repudiation

**Key rule:** Sign with private key. Verify with public key.

**How integrity is proven:**
1. Sender hashes the file/message
2. Sender signs that hash with private key
3. Receiver recalculates the hash
4. Receiver verifies signed hash using sender's public key
5. If hashes match → data unchanged

**Exam trap:** Digital signature does not hide the message. Encryption hides. Signature proves.

**Final memory line:** Sign with private key, verify with public key. Signature protects integrity by signing the hash.

---

## Lesson 019: Symmetric vs Asymmetric Encryption

| Type | Keys | Speed | Use case |
|---|---|---|---|
| Symmetric | One shared secret key | Fast | Bulk data encryption |
| Asymmetric | Public + private key pair | Slower | Trust, signatures, key exchange |

**TLS flow (simplified):**
- Asymmetric = identity verification + establishing the session key
- Symmetric = fast encryption of actual session traffic

**Exam trap:** Sharing the symmetric key securely is the main problem. Asymmetric solves that problem.

**Final memory line:** Symmetric = one key, fast. Asymmetric = key pair, trust and exchange.

---

## Lesson 020: PKI and Certificates Intro

**Core idea:** PKI is the system of certificates, keys, and trusted authorities that proves identity and enables secure communication.

| Term | Meaning |
|---|---|
| PKI | Public Key Infrastructure |
| Certificate | Digital ID card |
| CA | Certificate Authority — trusted issuer |
| Public key | Shared openly |
| Private key | Never shared |

**What a certificate contains:** Identity info + public key + issuer + validity dates + CA digital signature

**Exam trap:** A certificate contains the public key, not the private key.

**Lab verified:** openssl s_client → google.com certificate showed subject, issuer, notBefore, notAfter in terminal.

**HTTPS reminder:** Encrypted connection ≠ safe website. Phishing sites can also use HTTPS.

**Final memory line:** Certificate = digital ID card issued by a trusted CA. Contains public key, not private key.

---

## Combined Scores

| Day | Lessons | Score |
|---|---|---|
| Day 003 | 011–013 | 9/9 |
| Day 004 | 014–020 | 21/21 |
| **Total** | **10 lessons** | **30/30** |

---

## Next Session

021: Certificate Problems - Expired, Revoked, Self-Signed, Name Mismatch
022: Secure Protocols Intro
023: TLS / HTTPS
