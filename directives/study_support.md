# Study Support

## What this workflow is

Turns any studying request into structured output: class prep before a lecture or exam, learning a new topic for educational growth, or transfer-prep work (requirements tracking, application materials). Use whenever Bryan asks for help studying, understanding a topic, or preparing for a class, exam, or transfer milestone.

## Prerequisites

- `context/owner.md` (current classes, transfer targets — check the placeholders there)
- `brain/references/` — durable study facts already captured (check INDEX first)
- For transfer prep: official sources only (assist.org for CA community-college articulation, the target school's own pages)

## Inputs

| Field | Required | Description |
|---|---|---|
| Mode | Yes | Class prep / new topic / transfer prep |
| Subject & goal | Yes | What class or topic, and what outcome (exam date, concept mastery, application deadline) |
| Materials | No | Syllabus, notes, slides, problem sets — dropped in `sources/` or linked from Drive |

## Process

### Step 1: Load context
Read INDEX.md and any existing brain references on the subject. Never rebuild what is already captured.

### Step 2: Branch by mode
- **Class prep:** work from Bryan's actual materials, not generic knowledge. Produce: a one-page summary of the material, a list of the concepts most likely to be tested (with why), and practice questions Bryan answers before seeing solutions. Active recall over rereading.
- **New topic:** establish why Bryan is learning it (ties to which area — PBL, Sycamore, finances, career), then build a learning path: core concepts in dependency order, one good exercise per concept, and a definition-of-done.
- **Transfer prep:** requirements and deadlines come only from official sources, each cited with URL and date checked. File them in `brain/references/` as dated notes so stale requirements are detectable.

### Step 3: Capture the durable residue
A study session usually produces one durable fact worth keeping (a requirement, a framework, a recurring weak spot). File it per [[brain_dump_capture]] conventions. Session-specific scratch (practice questions, drafts) goes to `.tmp/`, not the brain.

### Step 4: Quality-gate and deliver
Run `python3 execution/check_brain_index.py` if brain notes were touched.

## Quality gates

- [ ] Transfer requirements/deadlines carry a source URL and date-checked; zero from memory
- [ ] Class-prep output is grounded in Bryan's materials when provided, and says so when not
- [ ] Practice questions come before their answers (recall, not recognition)
- [ ] Durable facts filed to brain/; scratch kept in `.tmp/`

## Edge cases

- No materials provided for class prep → say the output is from general knowledge of the subject, not the actual course, and ask for the syllabus/notes once.
- Transfer rules ambiguous or conflicting between sources → present both with citations; never pick silently.
- Bryan asks for answers to graded work → help him understand and practice the method; don't produce work meant to be submitted as his own.
