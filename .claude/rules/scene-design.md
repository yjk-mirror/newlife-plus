# Scene Design Principles

This document defines what a good scene looks like for this project — not technically, but structurally and philosophically. Read before designing any new scene.

---

## The Core Question

Ask of every scene: **does this feel like something that happens TO the player, or something the player does?**

We want the first. The world should interrupt. Events should have consequences the player didn't choose. NPCs should feel like people with their own agendas. The player is a person in a city that has its own life — not a protagonist that the world orbits.

---

## Anatomy of a Good Solo Event

A solo event needs all four of these:

### 1. An inciting situation (before any player choice)
Something happens before the player decides anything. The world moves first. She must respond to it — she does not initiate it.

### 2. 1-3 genuine choices
Not cosmetic choices. The path taken must change what the player experiences and what follows. "Do you want to leave?" with identical consequences is not a choice.

### 3. At least one lasting consequence
A game flag, an NPC stat change, or a PC stat change. Something that means this moment existed. The world must be able to remember.

### 4. Trait coverage that changes the situation
2-4 player traits that genuinely alter what happens — not what adjective describes it. See writing-style.md for examples of the difference.

---

## Consequence Persistence

**Every scene must change at least one of:**
- A game flag (`$gd.setGameFlag("FLAG")`) — world memory, persistent across sessions
- An NPC stat (liking, love, enjoy) — relationship memory
- A PC stat (`$gd.addStat("STAT")`) — character history
- A scene flag (`$scene.setFlag("FLAG")`) — within-scene state only

Scenes that leave no trace did not happen. The world cannot feel real if it has amnesia.

### Repeat-visit variation
If a player might encounter the same location, type of encounter, or named NPC twice, use a game flag to vary the text on return:

```velocity
#if (!$gd.hasGameFlag("SEEN_BAKERY_MAN"))
    $gd.setGameFlag("SEEN_BAKERY_MAN")
    Describe him fully — this is the first time.
#else
    He's there again. Brief acknowledgement.
#end
```

This costs almost nothing to write and makes the world feel continuous.

---

## The Weight System and Rarity

Use `weightDivisorConditions` in NPC action selectors to control how often events fire. A surprise that fires every session is furniture — not a surprise.

```yaml
- id: strangeEncounter
  weightDivisorConditions:
    - true    # ÷2
    - true    # ÷4
    - true    # ÷8 — genuinely rare
```

**Guidelines:**
- Common events (every few sessions): no weight modification or 1 multiplier condition
- Uncommon events (occasional): 1-2 divisors
- Rare events (memorable, singular): 3+ divisors
- Very rare (once-in-a-playthrough feel): 4+ divisors, or gate behind a specific game flag that is then cleared

Reserve genuine rarity for moments that are worth waiting for. Not every event needs to be rare, but the ones that are make the world feel larger.

---

## NPC Agency

The most powerful tool for making the world feel alive is **NPC-initiated events**: situations where the NPC does something the player didn't ask for, and the player responds rather than initiates.

**This is already the engine's architecture.** The `minievent.yml` dispatcher uses NPC actions to select what happens. We should push this pattern further:

- NPCs can initiate things unrelated to romantic interest
- NPCs can initiate things that are inconvenient, unwanted, or uncomfortable
- NPCs can do things that reference their own traits and relationships, independent of the PC's choices

When writing NPC-initiated events, the player should feel that she walked into something already in motion — not that the world staged something for her to encounter.

---

## Scene Taxonomy: What We Are Building

### Priority 1: Solo events (PC alone, world intrudes)

The city has a life. The PC encounters it.

**Target situation types:**
- **Social friction** — someone in her space, unwanted conversation, overheard argument, being ignored, being noticed when she'd rather not be
- **Small moral choices** — found wallet, witnessed something questionable, asked for help she can refuse
- **Physical world interruptions** — weather change, delayed transport, broken thing, unexpected obstacle
- **Unexpected recognition** — someone from her past who she has (or hasn't) a history with via game flags
- **Economic texture** — unexpected expense, found money, something she needs is unavailable
- **Background world events** — things happening in the city that don't involve her but that she witnesses

**What makes solo events weak** (existing codebase problems to avoid):
- One paragraph, no player choice, no consequence → read-only anecdote
- Player trait branches that swap one adjective
- No game flag set → the world has no memory of this happening
- Too pleasant → the world never pushes back or makes demands

### Priority 2: NPC-initiated intrusions (NPC acts, world changes)

People in her life do things without her direction:
- Ex contacts her unexpectedly (text varies based on how they parted)
- Friend creates an obligation, needs something, involves her in drama
- Someone else's situation lands on her doorstep
- A rumour about her has been spreading (only fires if she's done flag-generating things)

### Priority 3: Consequence chains (earlier choices surface later)

Use game flags from earlier scenes to create moments that reference what happened:
- She flashed the pub crowd → someone recognises her later
- She helped a stranger → they reappear in a different context with established warmth
- She made an enemy → they cause a problem weeks later

---

## What Makes a Moment Memorable

A scene that has three of these five qualities is a good scene:

1. **Specificity** — A particular detail that couldn't be about anyone else or anywhere else. A general pharmacy visit is nothing. A pharmacy visit where the same woman who judged her for buying something last time now watches her buy something more judgeable is something.

2. **Consequence** — Something changed. The world is different after this moment than before it.

3. **Unpredictability** — It wasn't the obvious thing to happen. The world surprised her. She had to respond to something she didn't expect.

4. **Character revelation** — The player learns something about who she is through how she responds. Different traits lead to genuinely different self-knowledge.

5. **World texture** — The world around her was doing something independent. The scene is set inside a city that has its own concerns.

---

## Pacing and Length

**Solo events:** 150–400 words of prose total across all paths. Short enough to feel light; long enough to feel specific.

**Multi-action scenes:** longer is appropriate if each action earns its length. Don't add actions to add length — add them when the choice genuinely matters.

**NPC-initiated events:** keep NPC-initiated text brief. The player should be responding, not reading.

**Intro text:** sets up the situation quickly. One or two paragraphs. No extended scene-setting. The inciting situation, then stop — let the choices carry the scene.

---

## The Transformation Dimension

Every scene should be asked: **does this moment feel different for a woman who used to be a man?**

If the answer is yes — and for many scenes involving male attention, desire, vulnerability, or gendered social dynamics it will be — write the branch. If the answer is genuinely no, don't force it.

### The design question

Transformation content isn't just about adding a branch. It's about identifying scenes where the transformation backstory changes the **stakes**, the **irony**, or the **erotic charge** of what's happening:

- A catcall: she knows exactly what's behind it. She used to be on that side.
- Being talked over in a meeting: she used to be the one who didn't notice doing this.
- Being physically protected by a man: the specific reversal of that role.
- Attraction to a man at low femininity: genuinely unfamiliar, not just desire but *surprise at desire*.
- Her reflection, unexpectedly: still occasionally new.

### How to tag transformation in a brief

Add `TRANSFORMATION` to content tags when the scene has at least one branch specifically for the transformed PC experience. Note the relevant femininity range:

```
Content tags: VANILLA, TRANSFORMATION (< 50 branch for male-start PC)
```

### Checklist addition

When designing trait branches for a scene: ask whether `!$w.hasTrait("ALWAYS_FEMALE")` earns its own branch *before* you pick player traits. The transformation axis is separate from (and often more powerful than) the personality trait axis.

---

## Content Classification

Every scene has a content level. Classify it before writing — it determines what gating is required.

| Level | Description | Gate |
|-------|-------------|------|
| `VANILLA` | No sexual content | None |
| `SEXUAL` | Consensual sex or explicit content, not rough | None |
| `ROUGH` | Consensual rough/BDSM elements | `!$w.hasTrait("BLOCK_ROUGH")` |
| `DUBCON` | Ambiguous consent — drunk, pressure, situational coercion | `!$w.hasTrait("BLOCK_ROUGH")` |
| `NONCON` | Non-consensual | `!$w.hasTrait("BLOCK_ROUGH")` |

A single scene can contain multiple levels across different paths. A SEXUAL scene might have a ROUGH branch that requires `BLOCK_ROUGH` gating. Tag the scene by its maximum level and note which paths require gating.

See `velocity-syntax.md` → "Content Gating" for the exact patterns.

---

## Checklist Before Writing Any Scene

- [ ] Does something happen before the player makes any choice?
- [ ] Are there 1-3 choices where different paths produce genuinely different outcomes?
- [ ] Does at least one path set a lasting game flag or NPC/PC stat?
- [ ] Are the trait branches structurally different (not adjective swaps)?
- [ ] If this could repeat, does it check a game flag for variation?
- [ ] Is the inciting situation something that happens TO her, not something she chose to pursue?
- [ ] Does the world behave as if it has its own life, independent of her?
- [ ] Is the content level tagged, and are all ROUGH/DUBCON/NONCON paths gated correctly?
- [ ] Does this scene earn a transformation branch? If yes, is it written and tagged TRANSFORMATION?
