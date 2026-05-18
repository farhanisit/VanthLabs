# Lesson 12 — Advanced Attack Attribution

## Core Concept
Detection = What happened
Analysis = How it happened
Attribution = WHO did it and WHY

## Three Levels of Attribution

### Layer 1: Tactical Attribution (Tools & Techniques)
What tools and techniques did the attacker use?

**Process:**
- Identify tools used (SSH, mysqldump, reverse shell, etc.)
- Map to MITRE ATT&CK framework
- Assess sophistication level (Low/Medium/High)

**Questions to ask:**
- What tools are visible in the attack?
- Are they custom or standard?
- Do they require special knowledge?

**Example: web-app-prod-03 incident**
Tools:

SSH key injection (T1098.004)
SQL injection (T1190)
mysqldump data extraction (T1005)
Systemd reverse shell (T1543.002)
Track covering (T1070.004)

Sophistication: MEDIUM
Why: Standard tools + basic log cleanup awareness

### Layer 2: Strategic Attribution (Intent & Pattern)
What was the attacker's goal? What does the attack pattern reveal?

**Process:**
- Identify target (what asset was targeted and why)
- Analyze attack speed, noise level, method
- Infer possible motivations
- Assess sophistication of planning

**Questions to ask:**
- Why this target specifically?
- How fast was the attack executed? (rushed vs. practiced)
- Did they clean up tracks? (aware vs. careless)
- What was the end goal? (data, access, disruption)

**Possible Motivations:**
1. Financial (data sale on dark web)
2. Espionage (competitive intelligence)
3. Mass compromise (future exploitation)
4. Disruption (denial of service)
5. Insider threat (pre-existing access)

**Example: web-app-prod-03 incident**
Goal: Customer payment data theft
Method: SQL injection + reverse shell persistence
Pattern: Opportunistic but practiced (10 min to exfil)
Track covering: Removed SSH key (operational security awareness)
No lateral movement: Smash & grab mentality
Motivation Assessment:

PRIMARY: Financial (50k customer records = dark web sale)
SECONDARY: Mass compromise (reverse shell allows long-term access)
LOW: Insider threat (would use internal access, not brute force)


### Layer 3: Operational Attribution (Known Actors)
Does this attack match known threat groups?

**Process:**
- Compare attack signatures to known actor profiles
- Check for unique malware, infrastructure, or methods
- Cross-reference with threat intelligence
- Assign confidence level based on evidence

**Confidence Levels:**
- **High Confidence:** Multiple unique indicators matching one actor
- **Medium Confidence:** Consistent with known actor, but indicators not unique
- **Low Confidence:** Could match multiple actors or generic attack
- **Unattributable:** No clear match to known actors

**Example: web-app-prod-03 incident**

Known Actor Comparison:
Carbanak:

Signature: Custom malware, advanced persistence
This attack: DOESN'T MATCH (no custom malware)

FIN6:

Signature: POS attacks, Metasploit reverse shells, SQL injection
This attack: MATCHES tools and targets
Confidence: Medium-High

Scattered Spider:

Signature: Smash & grab, brute force, standard tools
This attack: MATCHES pattern and simplicity
Confidence: Medium

Random Cybercriminal:

Signature: Opportunistic, standard tools, generic attacks
This attack: MATCHES everything generically
Confidence: Cannot distinguish

FINAL ASSESSMENT:
Attribution: LOW CONFIDENCE
Likely actor: Opportunistic cybercriminal or Scattered Spider
Why: No unique TTPs. Could be multiple groups using standard toolkit.

## Attribution Confidence Framework

| Confidence Level | Characteristics | Example |
|------------------|-----------------|---------|
| High | Multiple unique indicators, custom malware, known signatures | Carbanak trojan + known infrastructure |
| Medium | Consistent with actor, but non-unique tools | FIN6-style reverse shell + SQL injection |
| Low | Generic attack, standard tools, no unique markers | SSH brute force + mysqldump (could be anyone) |
| Unattributable | No clear match, insufficient evidence | Random attack with no signature |

## Key Principles

1. **Most attacks are NOT uniquely attributable**
   - 80% of attacks use common, public tools
   - Attribution requires rare, unique signatures
   - Confidence is probabilistic, not definitive

2. **Attribution is a team effort**
   - L1: Tactical + strategic analysis
   - L2/L3 + Threat Intel: Operational analysis with databases
   - Intelligence feeds back to analysts

3. **Multiple indicators = Higher confidence**
   - One unique signature = medium confidence
   - Three unique signatures = high confidence
   - Generic attack = low confidence

4. **Attacker behavior matters**
   - Speed, noise level, sophistication indicate maturity
   - Persistence method reveals intent (long-term vs. quick exfil)
   - Track covering shows operational security awareness

## Lesson 12 Summary

You can now:
- ✅ Do tactical analysis (tools + MITRE mapping)
- ✅ Do strategic analysis (intent + motivation + pattern)
- ✅ Do operational analysis (known actors + confidence level)
- ✅ Understand attribution limitations (most attacks are generic)
- ✅ Brief L2 on attribution findings with confidence levels

**Remember:** Attribution is art + science. Evidence-based assessment, not assumption.
