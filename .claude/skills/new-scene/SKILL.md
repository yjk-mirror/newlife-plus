---
name: new-scene
description: Generate a complete new scene pair (.yml + .vm) for the Newlife game. Use when asked to create a new scene, event, or encounter.
argument-hint: "[scene concept description]"
allowed-tools: Read, Write, Glob, Grep
---

You are generating a new scene for the Newlife game.

**Concept:** $ARGUMENTS

Work through these four steps in order. Do not skip steps or combine them.

---

## Step 1: Scene Brief

Before writing any files, produce a structured brief and present it for review.

```
SCENE NAME:        (snake_case filename, e.g. minievent_solo_charitymugger)
SCENE TYPE:        (solo / friend / partner / walkHome / work / special)
TRIGGER:           (what game state must be true for this to fire)
INCITING SITUATION:(what happens before the player makes any choice)
PLAYER CHOICES:    (2-4 choices, each with a different outcome)
TRAIT BRANCHES:    (2-4 player traits that meaningfully change the experience)
NPC INVOLVEMENT:   (if any — which NPC, which traits/personality matter)
LASTING CONSEQUENCES: (game flags set, NPC stats changed, or PC stats changed)
CONTENT TAGS:      (VANILLA / SEXUAL / ROUGH / DUBCON / NONCON / TRANSFORMATION — list all that apply; note which paths require BLOCK_ROUGH gating and which femininity ranges the transformation branch targets)
RARITY:            (common / uncommon / rare — guides weight conditions)
WORLD-ALIVE QUALITY: (one sentence: why does this make the world feel like it has its own life?)
```

Do not proceed to Step 2 until this brief is confirmed.

---

## Step 2: Write the YML File

Delegate this to the **scene-architect** agent or write it directly, following @.claude/rules/velocity-syntax.md.

File path: `additional_scenes/official_content/[SCENE NAME].yml`

Requirements:
- Every player choice from the brief → a distinct action with its own `id`, `shortDesc`, `longDesc`, and `textId`
- Every lasting consequence → an `effects` entry with appropriate condition
- Trait gates and conditions → correct Velocity expressions (quote conditions containing `!`)
- Rare events → `weightDivisorConditions` on the NPC action dispatcher
- `testingInfo` must include realistic outfit, NPC list, and location

At the end of the YML, produce a **TEXTID LIST** — every `textId` used in the file. The prose writer needs this exact list.

---

## Step 3: Write the VM File

Delegate this to the **prose-writer** agent or write it directly, following @.claude/rules/writing-style.md.

File path: `additional_scenes/official_content/[SCENE NAME].vm`

Requirements:
- Every `textId` from the TEXTID LIST → a matching `<tag>` in the VM
- `<empty></empty>` present if any NPC actions use `textId: empty`
- Trait branches must be **structurally different** — different situations, not different adjectives
- British English, second-person, present tense throughout
- No emotion announcements, no heart/pulse clichés, no generic NPC dialogue
- `<sceneDescriptionText>` must be static — no game-state effects
- Game flags and repeat-visit variation handled if the scene can fire more than once

---

## Step 4: Self-Review

After both files are written, check every item:

**Structural:**
- [ ] Every `textId` in the YML has a matching `<tag>` in the VM
- [ ] Every `<tag>` in the VM has a corresponding `textId` in the YML
- [ ] All conditions containing `!` are in quotes in the YML
- [ ] All terminal actions have `finishScene: true` or `returnToParent: true`
- [ ] `<empty>` tag is present if any NPC actions use `textId: empty`

**Design:**
- [ ] At least one lasting consequence is set (game flag, NPC stat, or PC stat)
- [ ] If the scene can repeat, a game flag gates variation on the second visit
- [ ] Rare/uncommon events have appropriate `weightDivisorConditions`
- [ ] Every player choice leads to a genuinely different outcome

**Content gating:**
- [ ] Scene content level is tagged (VANILLA / SEXUAL / ROUGH / DUBCON / NONCON / TRANSFORMATION)
- [ ] All ROUGH/DUBCON/NONCON actions in YML have `condition: '!$w.hasTrait("BLOCK_ROUGH")'`
- [ ] All ROUGH/DUBCON/NONCON prose branches in VM have `#if (!$w.hasTrait("BLOCK_ROUGH"))`
- [ ] Every rough `#if` has an `#else` — `BLOCK_ROUGH` players must never hit a blank section
- [ ] If the scene is entirely ROUGH/DUBCON/NONCON, it is gated at the dispatcher/approach level
- [ ] If tagged TRANSFORMATION: `!$w.hasTrait("ALWAYS_FEMALE")` branches exist at appropriate FEMININITY ranges
- [ ] `ALWAYS_FEMALE` players have a complete path that doesn't feel like a missing branch

**Prose:**
- [ ] All trait branches are structurally different (not adjective swaps)
- [ ] British English throughout
- [ ] Second-person present tense throughout
- [ ] No emotion announcements or heart/pulse clichés
- [ ] `<sceneDescriptionText>` has no game-state effects

Fix any issues before presenting the final output.
