# Weekly Planning

## What this workflow is

Produces Bryan's weekly plan across all areas — classes, PBL/clubs, financial opportunities, jobs, personal projects (including [[sycamore]]), and daily organization. Run at the start of each week, or whenever Bryan says "plan my week." This is also the system's heartbeat: it is when open placeholders get answered and stale items get flagged.

## Prerequisites

- `context/owner.md` (areas of activity)
- `brain/INDEX.md` + recent notes in `brain/notes/`
- Last week's plan in `brain/notes/` (filename `YYYY-MM-DD_weekly-plan.md`), if one exists
- Each active project's `history.md`

## Inputs

| Field | Required | Description |
|---|---|---|
| Fixed commitments | Yes | Classes, work shifts, club meetings, deadlines this week — from Bryan (or calendar, once connected) |
| Carry-overs | No | Auto-pulled from last week's plan: anything not marked done |
| Energy/notes | No | Anything unusual this week (exams, travel, low capacity) |

## Process

### Step 1: Review before planning
Read last week's plan. List what got done, what did not, and what keeps not getting done (three misses in a row = the task is wrong, not the discipline — flag it for redesign or deletion).

### Step 2: Gather this week's reality
Ask Bryan for fixed commitments and deadlines. Do not invent a schedule.

### Step 3: Draft the plan
- At most **3 priorities** for the week, each tied to an area or project. A priority states its definition-of-done, not an activity ("send Sycamore mockup to 2 people," not "work on Sycamore").
- Under the priorities: the fixed commitments, then a short everything-else list.
- Each active project gets at minimum one visible next action or an explicit "paused this week."

### Step 4: Surface system maintenance
Include any open `[PLACEHOLDER]` questions from context/project files (max 2 per week, oldest first) so the brain's gaps close as a side effect of planning.

### Step 5: File and gate
Save as `brain/notes/YYYY-MM-DD_weekly-plan.md`, add to INDEX, run `python3 execution/check_brain_index.py`, commit.

### Step 6: Close the loop (end of week or next run)
Mark done/not-done on the old plan before writing the new one. Wins and lessons worth keeping get their own brain notes.

## Quality gates

- [ ] No more than 3 priorities, each with a definition-of-done
- [ ] Every fixed commitment came from Bryan, none invented
- [ ] Last week's plan reviewed and reconciled before this week's exists
- [ ] Plan filed as a dated brain note and indexed

## Edge cases

- No last-week plan exists (first run) → skip Step 1, note it, start clean.
- Bryan gives more than 3 priorities → make him rank; record the cut ones in `brain/ideas/` or the plan's everything-else list, not as priorities.
- Mid-week replan requested → edit the existing week's note with a dated addendum; do not create a second plan file for the same week.
- A week with an exam or major deadline → that is automatically priority #1; challenge anything else that competes with it.
