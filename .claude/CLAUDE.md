# Newlife — Project Overview

## What This Is

Newlife is a British life-simulation adult text game by Splendid Ostrich Games. The player character (PC) is a young woman navigating relationships, work, and social life in a contemporary UK city. The game runs in Java; all custom content is authored as paired `.yml` + `.vm` files using Apache Velocity for templating. The Java engine handles scheduling, NPC spawning, scene dispatch, and game state — writers only touch the content files.

## Our Creative Goal

We are expanding the game to make the world feel **alive, unpredictable, and beyond the player's control.** The player controls only herself — her choices, responses, attitudes. The world around her should happen regardless: NPCs have their own lives, the city has its own rhythm, and random events should feel genuinely surprising rather than scripted. Replays should feel like different lives, not different routes through the same map.

**The core problem with the existing content:** most solo events are passive, one-paragraph read-throughs with no real player choice and no lasting consequence. Five solo events exist. They have no world memory. NPCs only act when the player is present. This is what we are fixing.

## Content Location

- `additional_scenes/official_content/` — all game content (.yml + .vm pairs)
- `additional_scenes/documentation/` — engine reference documentation
- `custom_npc_guides/` — NPC creation reference
- **New scenes go in:** `additional_scenes/official_content/`

## Technical Stack

Each scene = two files with the same base name:
- **`sceneName.yml`** — Scene structure: actions, conditions, effects, NPC actions, scene transitions
- **`sceneName.vm`** — Prose text: Velocity templates wrapped in `<tagName>` XML tags

See @.claude/rules/velocity-syntax.md for full technical reference.

## Key Velocity Context Objects

| Object | What it is | Common uses |
|--------|------------|-------------|
| `$w` | Player character | `$w.hasTrait("TRAIT")`, `$w.name`, `$w.figure`, `$w.eyeColour`, `$w.getSkill("FITNESS")`, `$w.isVeryDrunk()` |
| `$m` / `$bf` / `$npc` | Male NPC | `$m.name`, `$m.getName()`, `$m.getPersonality()`, `$m.hasTrait("TRAIT")`, `$m.behaviour` |
| `$f` / `$gf` / `$femaleFriend` | Female NPC | `$f.name`, `$f.getName()`, `$f.getCharType()` |
| `$gd` | Game data | `$gd.hasGameFlag("FLAG")`, `$gd.setGameFlag("FLAG")`, `$gd.addStat("STAT")` |
| `$scene` | Scene control | `$scene.hideNpc($npc)`, `$scene.unHideNpc($npc)`, `$scene.randomBoolean()`, `$scene.pickFromList([...])` |

## Player Traits (for text branching)

`POSH` · `CUTE` · `SULTRY` · `DOWN_TO_EARTH` · `BITCHY` · `SHY` · `REFINED` · `ROMANTIC` · `FLIRTY` · `AMBITIOUS` · `OVERACTIVE_IMAGINATION` · `PLAIN`

## NPC Personalities & Key Traits

Personality: `JERK` · `SELFISH` · `AVERAGE` · `ROMANTIC` · `CARING`
Traits: `SLEAZY` · `CHARMING` · `BOASTFUL` · `CRUDE` · `TACITURN` · `INTERESTING` · `DULL` · `HATES_CONDOMS` · `CONSCIENTIOUS` · `WANTS_KIDS` · `DOESNT_WANT_KIDS` · `IMPREGNATOR` · `CHEATER`

## Scene Types

| Type | When it fires | NPC required |
|------|--------------|--------------|
| Solo minievent | PC's free time | No |
| Friend minievent | PC has friends | Male or female friend |
| Partner minidate | PC has a BF/GF | BF or GF |
| Walk home | After clubbing | Lowlife / random |
| Work event | Career timeslot | Boss / colleague |
| Special scene | Storyline trigger | Varies |

## What We Are Building (Priority Order)

1. **Solo events** — currently only 5 exist, all thin. Target: 20+ richly varied events with real player choice and persistent world state
2. **NPC-initiated intrusions** — events that fire because an NPC did something, not because the player engaged them
3. **Consequence chains** — later events that reference what happened in earlier ones via game flags

## Rules Reference

- Prose style, anti-patterns, and tone: @.claude/rules/writing-style.md
- YML/Velocity technical syntax: @.claude/rules/velocity-syntax.md
- Scene design principles: @.claude/rules/scene-design.md
