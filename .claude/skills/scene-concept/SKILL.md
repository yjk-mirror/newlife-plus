---
name: scene-concept
description: Brainstorm new scene concepts for the Newlife game. Produces structured briefs for review before any code is written. Use at the start of a scene generation session.
allowed-tools: Read, Glob, Grep
---

Brainstorm new scene concepts for the Newlife game.

## Step 1: Survey What Exists

Scan `additional_scenes/official_content/` and list all `.yml` files by type:
- Solo minievents (prefix: `minievent_solo_`)
- Friend minievents (`minievent_m_`, `minievent_f_`)
- Partner dates (`minidate_`)
- Walk home events (`walkHomeAlone_`)
- Work events (`officeHarass`, etc.)
- Special scenes (everything else)

Note which categories are underrepresented. The immediate priority is **solo events** — currently only five exist.

## Step 2: Generate 5 Concepts

Produce five new scene concepts. Prioritise:
- **The world initiates** — something happens before the player chooses
- **Negative or uncomfortable possibilities** — not everything is pleasant
- **Consequence that persists** — the world remembers
- **NPC behaviour the player cannot predict or control**
- **Genuine player choice** — paths that lead somewhere different

For each concept:

```
CONCEPT:       [Evocative title, 3-6 words]
TYPE:          [solo / friend / partner / walkHome / work / special]
PREMISE:       [1-2 sentences: what situation does the player walk into?
                The world should be doing something — she enters mid-action.]
CHOICES:       [2-4 bullet points: what can she actually do?
                Each should lead somewhere genuinely different.]
TRAIT HOOKS:   [2-3 player traits that meaningfully change this situation.
                Not adjective swaps — structural differences.]
CONSEQUENCE:   [What game flag or stat change persists after the scene?]
RARITY:        [common / uncommon / rare]
WORLD-ALIVE:   [One sentence: why does this feel like the world has its own life?]
```

## Step 3: Present and Refine

After presenting all five concepts, note which are strongest and why.

Ask which concept (or which combination of elements) to develop into a full scene, then hand off to `/new-scene` with the confirmed concept as the argument.

---

## Quality bar for concepts

Reject any concept where:
- The player initiates the entire situation herself (she chose to go shopping → she shops → she leaves)
- There is no lasting consequence
- The trait branches are obviously just adjective swaps
- Every possible outcome is pleasant or neutral
- The world is passive backdrop rather than active participant
