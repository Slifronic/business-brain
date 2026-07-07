# Brain Dump Capture

## What this workflow is

Turns a raw brain dump from Bryant (voice transcript, typed stream-of-consciousness, or pasted notes) into properly filed second-brain content: updated context/project files, dated brain notes, and INDEX.md entries. Use whenever Bryant shares unstructured thoughts about himself, a project, a decision, or a lesson. This is the intake valve for the whole system.

## Prerequisites

- Context files: `context/owner.md`, `context/core_values.md`
- `brain/INDEX.md` (read before filing, to avoid duplicates)
- Script: `execution/check_brain_index.py` (quality gate)

## Inputs

| Field | Required | Description |
|---|---|---|
| Dump text | Yes | The raw transcript or typed dump |
| Source type | Yes | Voice or typed — voice gets the mishear treatment (see Step 2) |
| Topic hint | No | Which project/area it concerns, if Bryant says |

## Process

### Step 1: Read before writing
Load `brain/INDEX.md` and any context/project files the dump touches. New information updates existing files; it does not create parallel copies.

### Step 2: Flag transcription artifacts (voice dumps)
Voice transcripts mishear proper nouns. Do not silently "fix" them — resolve or flag:
- If the intended word is obvious from context, use it and note the original in a placeholder for confirmation (e.g., "the Anza" → De Anza [confirm]).
- If not resolvable, keep the transcribed form in a `[PLACEHOLDER — verify]` marker. Never let an unverified proper noun flow into a bio, pitch, or claim.

### Step 3: Sort the content into layers
Each fact goes to exactly one home:
- About Bryant (background, involvements, results) → `context/owner.md`
- How Bryant sounds / operates → `context/brand_voice.md` / `context/core_values.md`
- Project facts (product, buyers, positioning) → `projects/{name}/profile.md`
- A decision with reasoning → `brain/decisions/YYYY-MM-DD_slug.md` ("We decided X because Y" + implication)
- Durable reference facts → `brain/references/`
- Lessons, events, narrative → `brain/notes/`
- Numbers snapshots → `brain/metrics/`
- Ideas that are not commitments → `brain/ideas/`

### Step 4: Write with the conventions
- Dates in note filenames: `YYYY-MM-DD_slug.md`
- Wikilinks (`[[note-name]]`) between genuinely related notes — relationships, not keyword matches
- Specifics over summaries: keep the numbers, names, and exact phrasings from the dump
- Anything the dump did not say gets a `[PLACEHOLDER — question]`, never an invented fact
- Update the project's `history.md` with a dated entry if the dump advanced a project

### Step 5: Update INDEX.md
One line per new note, under the right category.

### Step 6: Run the quality-gate script
`python3 execution/check_brain_index.py` — verifies filename conventions and that every note is indexed.

### Step 7: Report back and commit
Tell Bryant: what was filed where, what placeholders need his answer (as numbered questions), and what was inferred vs. stated. Commit with a message summarizing the dump's content.

## Quality gates

- [ ] `check_brain_index.py` passes (all notes indexed, filenames dated)
- [ ] Zero invented facts: every claim traces to the dump or an existing file
- [ ] Every unresolved proper noun or ambiguity carries a `[PLACEHOLDER]`
- [ ] Decisions captured with reasoning attached, not just the outcome
- [ ] Open questions surfaced to Bryant as a numbered list, not buried in files

## Edge cases

- Dump contradicts an existing file → the new dump usually wins (it is newer), but flag the change to Bryant explicitly and keep the old value in the git history.
- Dump mentions a new project → create `projects/{name}/profile.md` with what was said; ask before assuming it is a commitment (it may belong in `brain/ideas/`).
- Dump is ambiguous about whether something exists or is planned (e.g., "I have a dashboard") → record as planned/spec and add a placeholder asking which it is.
- Tiny dump (one fact) → skip ceremony; file the one fact, update INDEX if a note was created, done.
