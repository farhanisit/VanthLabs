# Lesson 15 — Incident Command & Crisis Management

## Core Idea
Lessons 7-14 = how ONE analyst investigates.
Lesson 15 = how MANY people coordinate when an incident is too big
for one analyst. A real breach is a TEAM operation under pressure.

Analyst question:   "What happened on this host?"
Commander question: "Who is doing what right now, and do we have ONE
                     coherent response or five people colliding?"

A major incident fails for ORGANIZATIONAL reasons more often than
technical ones. Incident command exists to fix human chaos, not malware.

## Why It Exists (chaos without structure)
- two people isolate the same host; nobody scopes the spread
- management interrupts 5 analysts; investigation stops
- evidence destroyed because nobody owned preservation
- fix deployed before entry vector known -> reinfection

## Key Roles (NIST / ICS-derived)
1. Incident Commander (IC) - OWNS the response, single decision-maker,
   coordinates (does NOT do the technical work).
2. Investigation/Analysis lead - scope, root cause, IOCs. (L1/L2 sits here.)
3. Containment/Remediation lead - isolation, blocks, resets, eradication.
4. Communications lead - management/legal/customers; SHIELDS analysts.
5. Scribe/Recorder - documents every decision + time (COC, PIR depend on it).
Small org: one person, many hats. Big incident: all staffed separately.

## Golden Rule of Comms
Analysts do NOT report to management directly during a live incident.
Everything flows through IC / Comms lead.
-> protects the investigation + management hears ONE coherent story.
(Scaled-up version of L11 "notify management WITH facts.")

## Severity -> Response Scale
- SEV3 (Low): single analyst, normal workflow.
- SEV2 (High): small team, IC named, comms managed.
- SEV1 (Critical): full command, all roles, exec involvement.
Declaring SEV1 too late = classic failure. SEV1 for everything = burnout.

## Lifecycle
Prepare -> Detect -> [DECLARE] -> Respond (command active)
        -> Recover -> Post-Incident Review.
"Declare" flips "an analyst on an alert" into "an owned incident."

## Where L1 Sits
Usually Investigation/Analysis, feeding facts UP to the IC:
- findings as proof vs impact (L13)
- no freelancing (no isolate/eradicate/block without coordination - L11)
- flat updates to the IC, NOT to management directly
- document everything touched

## Reflex: the stakeholder demand
A C-level demanding an answer you don't have yet:
Do NOT answer (guessing), do NOT ignore (unprofessional).
REDIRECT: "Can't confirm yet, still scoping; the IC owns the full
picture and comms - let me point you to them."
"I don't know yet + here's who owns it" beats any confident guess.

## Post-Incident Review (PIR)
BLAMELESS is the core principle: assume everyone acted reasonably given
what they knew at the time; hindsight banned.
- Blame culture -> people hide mistakes -> same breach next quarter.
- Blameless -> truth -> fix the real gap -> org gets stronger.

Four questions: 1) What happened (timeline) 2) What went well
3) What went badly 4) What changes — each action item OWNED + DATED.
"Improve monitoring" = theater. "Priya adds mass-encryption Sysmon
rule by Friday" = real.

Key question: "What signal would have caught this EARLIER?"
-> becomes a new detection rule -> feeds threat hunting (L14).

## The Loop (closes the arc)
An incident is a detection that came too late.
Detect -> Respond -> Review -> better Detection -> repeat.
Every survived incident should make the next easier to catch.

## Key Learnings (Lesson 15)
1. Big incidents fail organizationally, not technically.
2. One owner (IC), one coherent picture.
3. Comms flow through the IC - even verbal, even under pressure.
4. L1 = investigation seat: facts up, no freelancing.
5. "I don't know yet + who owns it" > a confident guess to a stakeholder.
6. PIR is blameless or it's worthless.
7. Action items without an owner and date are theater.
8. Incidents feed detections; the lifecycle is a circle.
