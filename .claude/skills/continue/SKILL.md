---
name: continue
description: Resume the Newlife expansion project. Reads PROGRESS.md, takes scenes from the backlog, and generates them in parallel batches. Use when the user says "continue", "pick up where we left off", or similar.
disable-model-invocation: true
allowed-tools: Read, Write, Glob, Grep, Bash, Task
---

Resume the project. Work autonomously. Generate scenes in parallel batches. Do not ask the user which scene to work on unless the backlog is completely empty.

---

## Step 1: Orient

Read `PROGRESS.md` completely.

Then run:
```
ls additional_scenes/official_content/*.yml | xargs -I{} basename {} .yml | sort
```

Compare against **Completed Scenes** in PROGRESS.md. Add any scenes that exist in the filesystem but not in Completed — they were written in a previous session. Remove them from the Backlog before proceeding.

---

## Step 2: Report State

Present briefly:
- Scenes completed so far (count + names)
- How many READY items remain in the Backlog
- Batch plan for this session ("Running in batches of 5 — estimated X batches")

Then proceed immediately.

---

## Step 3: Parallel Batch Generation

### Batch size: 5 scenes at a time

Take the **first 5 READY items** from the Backlog. If fewer than 5 remain, take all of them.

For each scene in the batch, spawn a **Task agent** using the `scene-generator` agent. Pass the **complete scene brief** from PROGRESS.md as the agent's prompt. Spawn all 5 simultaneously — do not wait for one to finish before starting the next.

**Agent prompt template for each scene:**

```
You are the scene-generator agent. Generate one complete Newlife scene.

SCENE NAME: [scene name from brief]

BRIEF:
[paste the complete brief text here — all fields]

Write both files:
- additional_scenes/official_content/[name].yml
- additional_scenes/official_content/[name].vm

Follow all rules in your agent file. Report SCENE COMPLETE when done.
```

Wait for all 5 agents in the batch to complete before proceeding.

---

## Step 4: Update PROGRESS.md

After each batch completes:
- Move all completed scenes from **Backlog** to **Completed Scenes**
- Update **Last Worked On** with the scene names and today's date
- Update **Next:** to point to the next Backlog item

---

## Step 5: Auto-Generate More Briefs (when backlog runs low)

If the Backlog has fewer than **10 READY items** after a batch, generate more briefs before continuing:

1. Review what's already been written (scene types, tones, content levels)
2. Identify gaps: categories underrepresented, content levels not yet covered, consequence chains not yet written
3. Generate 10 new complete briefs in the PROGRESS.md format
4. Append them to the Backlog in PROGRESS.md

Target mix for new briefs: 60% VANILLA/everyday, 25% SEXUAL/suggestive, 15% ROUGH/DUBCON (tagged and gated).

Continue batching from the expanded backlog.

---

## Step 6: Continue

Without pausing, take the next batch and repeat from Step 3.

Stop when:
- The user says stop
- The Backlog is empty and no new briefs can be meaningfully generated (then report and suggest `/scene-concept` for fresh concept work)
- A scene is repeatedly failing and needs user input to resolve

---

## Quality Gate

Every scene in this session must:
- Pass the scene-generator's self-review without critical issues
- Have at least one lasting game flag or stat consequence
- Have trait branches that are structurally different (not adjective swaps)
- Be written in British English, second-person, present tense
- Have all ROUGH/DUBCON/NONCON paths correctly gated behind `!$w.hasTrait("BLOCK_ROUGH")`

If a scene-generator agent reports critical issues it cannot fix, skip that scene, note it in PROGRESS.md as BLOCKED with the issue, and continue to the next.

---

## Agent Teams Mode

If Agent Teams are active (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 is set):

You can spawn **teammates** instead of Task subagents for sustained parallel work:

1. Create shared tasks in the task list — one task per scene, status pending
2. Spawn 5-10 teammates with this instruction: "You are a Newlife scene generator. Claim tasks from the task list. For each task, read the scene brief from PROGRESS.md, generate the complete scene pair (YML + VM), mark the task complete. Continue claiming tasks until the list is empty."
3. Monitor teammates' progress via the task list
4. When all teammates are idle and the task list is empty, update PROGRESS.md and report

This mode is more efficient for very long runs (50+ scenes). For shorter sessions, Task subagents are simpler.
