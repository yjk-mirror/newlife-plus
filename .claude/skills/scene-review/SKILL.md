---
name: scene-review
description: Review an existing scene pair (.yml + .vm) for quality, consistency, and alignment with project goals.
argument-hint: "[scene base name, e.g. minievent_solo_parkjog]"
allowed-tools: Read, Glob, Grep
---

Review the scene: **$ARGUMENTS**

Read both files:
- `additional_scenes/official_content/$ARGUMENTS.yml`
- `additional_scenes/official_content/$ARGUMENTS.vm`

Evaluate against every criterion below. For each issue found, quote the relevant text, explain the problem, and suggest the fix.

---

## Structural Checks

- [ ] Does every `textId` in the YML have a matching `<tag>` in the VM?
- [ ] Does every `<tag>` in the VM have a corresponding `textId` reference in the YML?
- [ ] Are all Velocity conditions syntactically valid (method calls correct, quotes around `!` conditions)?
- [ ] Do all terminal actions have `finishScene: true` or `returnToParent: true`?
- [ ] If any NPC actions use `textId: empty`, is the `<empty>` tag present in the VM?
- [ ] Does any action with `allowNpcActions: true` have a corresponding `maleNpcActions:` section?
- [ ] Are all scene transitions correctly typed (1-way vs returning, `returningId` set/unset appropriately)?

---

## Design Checks

- [ ] Does something happen in the intro before the player makes any choice?
- [ ] Does the scene have at least one genuine player choice (not cosmetic)?
- [ ] Do different choices lead to genuinely different outcomes?
- [ ] Does the scene have at least one lasting consequence (game flag, NPC stat, or PC stat)?
- [ ] If the scene can repeat, does it check a game flag for variation on return?
- [ ] Are rare or surprising moments weighted with `weightDivisorConditions`?
- [ ] Is the inciting situation something that happens TO the player (world initiates) rather than something the player chose to do?

---

## Prose Checks

- [ ] British English throughout (pub not bar, pavement not sidewalk, etc.)?
- [ ] Second-person present tense throughout?
- [ ] Trait branches are structurally different (not adjective swaps)?
- [ ] No emotion announcements ("You feel embarrassed", "You're nervous")?
- [ ] No heart/pulse clichés ("your heart skips a beat", "your pulse quickens")?
- [ ] No generic NPC dialogue ("You look beautiful", "Want to get out of here?")?
- [ ] `<sceneDescriptionText>` has no game-state-changing effects?
- [ ] Sentence structure varies (not every line starting with "You")?
- [ ] Specific sensory detail rather than generic atmosphere?
- [ ] NPC voice reflects their personality and traits (not a generic pleasant/unpleasant switch)?

---

## Summary Report

After completing all checks, produce:

### Critical Issues (must fix — broken functionality)
List any structural problems that would cause runtime errors or missing content.

### Quality Issues (should fix — against project standards)
List any prose anti-patterns, missing consequences, or design failures.

### Suggestions (consider improving)
Optional improvements: additional trait branches worth adding, richer text, rarity adjustment.

### Overall Rating
- **Complete** — ready to use as-is
- **Needs Work** — quality issues present, functional but below standard
- **Needs Significant Revision** — design or structural problems that require rethinking
