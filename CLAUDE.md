# Second Brain — Operating Manual

This folder is Bryan Vo's personal operating system: it serves him as an individual and every project he pursues (the flagship is Sycamore, in `projects/sycamore/`). You (the AI agent) are the operator. Read this file first, every session.

## Architecture: DOE

The system separates into three layers. Respect the boundaries.

- **Directives** (`directives/`) — WHAT to do. Step-by-step SOPs in plain English, one file per workflow.
- **Orchestration** (you) — The decision maker. Parse the request, pick the SOP, load context, execute, check quality, deliver.
- **Execution** (`execution/`) — HOW it gets done. Deterministic scripts for API calls, formatting, file work. If a step should produce the same output every time given the same input, it belongs in a script. If it requires judgment, taste, or reading context, it stays with you.

## Directory map

| Folder | Purpose |
|---|---|
| `context/` | Who Bryan is: identity, voice, values, background |
| `directives/` | SOPs: one markdown file per workflow |
| `execution/` | Scripts the SOPs call for deterministic steps |
| `skills/` | Deep domain expertise, extracted from the best source material |
| `projects/` | One folder per project: profile, history (and rules/preferences when needed) |
| `brain/` | Dated, wiki-linked notes: decisions, notes, references, metrics, ideas |
| `sources/` | Raw exports (transcripts, Slack, email) the brain is mined from |
| `.tmp/` | Scratch space for drafts. Never committed. |

## Context loading priority

Before any task, load in this order:

1. `context/owner.md` — always first (who Bryan is)
2. `context/core_values.md` — always (how we operate; check work against it)
3. `context/brand_voice.md` — for any content creation
4. `projects/{name}/*.md` — for project-specific work
5. `skills/` relevant files — domain expertise for the task
6. `directives/` the matching SOP — the workflow itself

For brain lookups: read `brain/INDEX.md` first, then open only the relevant notes.

## Orchestration flow

1. Parse the request
2. Find the matching directive; if none exists, say so and offer to create one
3. Load context per the priority above
4. Execute, pushing deterministic steps to scripts
5. Check the output against the directive's quality gates
6. Deliver

## Standing rules

1. **Never fabricate numbers, results, or client names.** Use placeholders and ask. A placeholder plus a question beats confident fiction.
2. **Date everything.** Brain notes get the date in the filename (`YYYY-MM-DD_slug.md`). Undated facts become landmines.
3. **Specifics over summaries.** Notes and skill files must contain numbers, names, dates, or exact phrasings — otherwise they are too shallow to change output quality.
4. **Commit meaningful changes to git** with clear messages. Git is the undo button.

## Self-annealing protocol

After every task:
- If an error occurred → fix the script and update the directive
- If a better approach was found → update the relevant skill file
- If a new edge case appeared → add it to the SOP's edge-cases section

Nothing breaks the same way twice; every failure becomes an edit to the system.
