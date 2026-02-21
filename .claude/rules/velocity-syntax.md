# Velocity & YML Technical Reference

Each scene in Newlife consists of two files with the same base name: a `.yml` structure file and a `.vm` prose file. This document is the technical reference for both.

---

## VM File Format

The `.vm` file contains Velocity template text organized into named sections using XML-style tags:

```xml
<introText>
Your intro text here. Can contain any Velocity syntax.
</introText>

<someActionText>
Text shown when the player takes this action.
</someActionText>

<sceneDescriptionText>
Short static description. DO NOT put game-state-changing effects here — this renders multiple times per session.
</sceneDescriptionText>

<empty></empty>
```

Tag names correspond exactly to `textId` values in the `.yml` file. Every `textId` referenced in the YML **must** have a matching tag in the VM. The `<empty>` tag must be present if any NPC actions reference `textId: empty`.

---

## Core Velocity Syntax

### Variables
```velocity
$w.name              ## Player's name
$m.getName()         ## NPC's name (method call)
$w.figure            ## Returns enum string: "WOMANLY", "SLIM", "TONED"
$m.behaviour         ## Returns: "ROM", "MEAN", "COLD", "NEUTRAL"
```

### Conditionals
```velocity
#if ($w.hasTrait("POSH"))
    Posh path text.
#elseif ($w.hasTrait("CUTE"))
    Cute path text.
#else
    Default path text.
#end
```

### Setting variables
```velocity
#set($myVar = true)
#set($count = 0)
#set($label = "something")
```

### Newline suppression (critical)
Velocity inserts a newline after every directive. Use `##` at line end to suppress:
```velocity
He looks at you##
#if ($w.hasTrait("SHY")) and you look away.##
#else and you hold his gaze.##
#end
```
Without `##`, there would be blank lines around the conditional text.

### Comments
```velocity
## Single line comment (also suppresses the newline)
#*
   Multi-line block comment.
   Nothing here is output.
*#
```

### Random helpers
```velocity
$scene.randomBoolean()
## → Returns true or false randomly

$scene.pickFromList(["option A", "option B", "option C"])
## → Returns one item from the list at random
```

### Game effects in VM text
Effects can go directly in VM text:
```velocity
$m.addArousalTiny()
$w.addArousalSmall()
$gd.addStat("ACTS_OF_EVIL")
$gd.setGameFlag("FLAG_NAME")
```
These are evaluated when the text section renders. Do not put state-changing effects in `<sceneDescriptionText>`.

---

## Context Object Methods

### Player Character ($w)
```
$w.name / $w.getName()
$w.figure                       → WOMANLY / SLIM / TONED
$w.eyeColour / $w.eyeAdj
$w.breastsDesc / $w.stomachDesc
$w.hasTrait("TRAIT_NAME")       → boolean
$w.getSkill("FITNESS")          → integer (0-100+)
$w.getSkill("FEMININITY")       → integer (see Transformation section below)
$w.isVeryDrunk() / $w.isMaxDrunk() / $w.isDrunk()
$w.virgin                       → boolean
$w.pregnancyStage               → FLAT / etc.
$w.addArousalTiny() / $w.addArousalSmall() / $w.addArousalMedium()
$w.reduceArousalTiny()
$w.girlOrWoman                  → "girl" or "woman"
$w.isAnxious() / $w.isHighStress()
$w.getTop().getBasicDesc()      → clothing description
$w.getBra().getBasicDesc()
$w.getTop().isAlsoLowerBody()   → boolean (e.g. dress)
$w.getTop().hasFlag("LOWCUT")   → boolean
```

### Transformation Status API

The PC may have been transformed from male to female. This is the game's core premise and must be handled correctly.

**Three PC types:**

| Trait combination | Meaning |
|---|---|
| `!$w.hasTrait("ALWAYS_FEMALE")` | Male-start: definitively transformed from male. The primary transformation check. |
| `$w.hasTrait("ALWAYS_FEMALE") && !$w.hasTrait("NOT_TRANSFORMED")` | Female-start with some transformation element |
| `$w.hasTrait("ALWAYS_FEMALE") && $w.hasTrait("NOT_TRANSFORMED")` | Quickstart female: never transformed at all |

**`$w.getSkill("FEMININITY")` — the adaptation dial:**

| Range | What it means | How to write it |
|-------|--------------|-----------------|
| < 20 | Barely adjusted; still thinking like a man | Strong male-self-concept; female experiences feel like thresholds ("becoming a woman") |
| < 50 | "Still a guy at heart" | Conflicted; recognises female feelings but doesn't fully own them |
| 50–74 | Adapted but past is real | Occasional flicker of former self; mostly inhabits her female life |
| ≥ 75 | Fully adapted | Transformation content absent or distant-memory; feels strange to imagine being male |

Female-start characters begin at **75**. Male-start characters begin low (can be negative).

**Standard guard patterns:**

```velocity
## "Still adjusting" content — the richest transformation zone
#if (!$w.hasTrait("ALWAYS_FEMALE") && $w.getSkill("FEMININITY") < 50)
    She hasn't been doing this long enough to have stopped noticing it.
#end

## Fully adapted male-start — barely remembers
#if (!$w.hasTrait("ALWAYS_FEMALE") && $w.getSkill("FEMININITY") >= 75)
    It would feel strange to be male again now. That's not quite the same as forgetting.
#end

## Never transformed — skip transformation content entirely
#if ($w.hasTrait("NOT_TRANSFORMED"))
    No transformation content here. This player always was female.
#end

## Three-level transformation gradient
#if (!$w.hasTrait("ALWAYS_FEMALE") && $w.getSkill("FEMININITY") < 50)
    The version that's still working out what this means for her.
#elseif (!$w.hasTrait("ALWAYS_FEMALE"))
    The fully adapted version — the past is distant but real.
#else
    The always-female version — no transformation frame at all.
#end
```

**Male-start virginity:** The game assumes male-start PCs were heterosexual before transformation. `$w.virgin` is always true for male-start at game start. First-time flags (`$gd.hasGameFlag("FIRST_TIME_MISSIONARY")` etc.) track their first in-game sexual experiences as a woman.

### Male NPC ($m / $bf / $npc)
```
$m.name / $m.getName()
$m.getPersonality()             → JERK / SELFISH / AVERAGE / ROMANTIC / CARING
$m.hasTrait("TRAIT_NAME")       → boolean
$m.behaviour                    → ROM / MEAN / COLD / NEUTRAL
$m.eyeColour / $m.handAdj / $m.torsoDesc
$m.figure                       → AVERAGE / SKINNY / TONED / MUSCULAR / THICKSET / PAUNCHY / FAT
$m.isPartner()                  → boolean
$m.isNpcAttractionOk()          → boolean
$m.isWAttractionLust()          → boolean
$m.isWLoveCrush() / $m.isNpcLoveSome() / $m.isNpcLoveCrush()
$m.wLoveCrush / $m.wLoveConfused
$m.wAttractionOk / $m.wAttractionUnattracted
$m.hadOrgasm                    → boolean
$m.addArousalTiny()
$m.addNpcLikingTiny() / $m.addNpcLikingMedium()
$m.addNpcLoveSmall() / $m.addNpcLoveTiny()
$m.addWLikingTiny() / $m.addEnjoyTiny()
$m.reduceWEnjoyTiny()
$m.addTrait("TRAIT_NAME")       ## Adds a hidden tracking trait
$m.increaseKnowledge(min, max)
$m.hasDoneSexualActivity("SEX") / ("ORAL") / ("ANAL")
$m.hasRelationshipFlag("FLAG")
$m.strength                     → integer
```

### Female NPC ($f / $gf / $femaleFriend)
```
$f.name / $f.getName()
$f.getCharType()                → PARTY_GIRL / INNOCENT / SOPHISTICATED
$f.addEnjoyTiny() / $f.addNpcLikingTiny() / $f.addWLikingTiny()
```

### Game Data ($gd)
```
$gd.hasGameFlag("FLAG_NAME")    → boolean (persists across sessions)
$gd.setGameFlag("FLAG_NAME")    ## Sets a permanent flag
$gd.removeGameFlag("FLAG_NAME")
$gd.addStat("STAT_NAME")        ## Increments a game statistic
```

### Scene Control ($scene)
```
$scene.hideNpc($npc)            ## Hides NPC from scene (still accessible via variable)
$scene.unHideNpc($npc)          ## Makes hidden NPC visible
$scene.setActiveMaleNpc($m)     ## Sets the 'active' male NPC
$scene.removeFlag("FLAG")       ## Removes a scene-local flag
$scene.hasFlag("FLAG")          → boolean (scene-local only, not persistent)
$scene.randomBoolean()          → boolean
$scene.pickFromList([...])      → String
```

---

## YML Scene Structure

### Minimal complete skeleton
```yaml
textFileName: sceneName.vm
sceneDescriptionTextId: sceneDescriptionText

testingInfo:
  playerOutfit: CASUAL
  maleNpcs:
    - id: m
      outfit: CASUAL
  location:
    wall: wall
    floor: floor
    hasBed: false
    isOutside: false

intro:
  textId: introText
  effects:
    - effect: $scene.hideNpc($m)
      condition: $m
  followUpActions:
    firstAction:

actions:
  - id: firstAction
    shortDesc: Do the thing
    longDesc: A longer description of this action
    textId: firstActionText
    effects:
      - effect: $gd.setGameFlag("DID_THE_THING")
        condition: "!$gd.hasGameFlag('DID_THE_THING')"
    followUpActions:
      secondAction:
      finishScene: "$someCondition"

  - id: secondAction
    shortDesc: Something else
    longDesc: Do something else
    textId: secondActionText
    finishScene: true

  - id: finishScene
    shortDesc: End Scene
    longDesc: Leave
    textId: finishSceneText
    finishScene: true

defaultActions:
  firstAction: true

maleNpcActions:
  - id: npcChoiceOne
    textId: empty
    condition: true
    weightMultiplierConditions:
      - $m.hasTrait("BOASTFUL")
    sceneTransition:
      condition: true
      type: CUSTOM
      maleNpcs:
        - id: m
          npc: m
      transitionInfo:
        ymlFile: otherScene.yml
      location:
        useCurrentLocation: true
```

### Key YML rules

**Conditions with `!` must be in quotes** (YAML special character):
```yaml
condition: "!$m.hadOrgasm"
condition: '$eventType=="SOLO" && $w.getSkill("FITNESS") > 20'
```

**Empty condition = always available** (same as `condition: true`)

**Action termination:** Every action chain must eventually reach:
- `finishScene: true` — ends the scene
- `returnToParent: true` — returns to parent scene (sub-scenes only)
- A scene transition

**`allowNpcActions: true`** on a player action means the engine picks an NPC action after the player acts. You must have a `maleNpcActions:` section.

**`useBehaviourActions: true`** shows the standard behaviour-change UI. Requires a `behaviourChange:` section.

**`useDefaultActions: true`** uses the `defaultActions:` map instead of action-specific followups.

### Scene Transition Syntax
```yaml
sceneTransition:
  condition: true
  type: HOME_DATE          # 1-way, always uses player's home. No returningId needed.
  type: STANDING_MAKEOUT   # Returns to parent. Set returningId.
  type: CUSTOM             # Custom scene. Set transitionInfo.ymlFile.
  maleNpcs:
    - id: m                # ID that target scene will use
      npc: m               # ID of the NPC in current scene context
  femaleNpcs:
    - id: f
      npc: femaleFriend
  transitionInfo:
    ymlFile: targetScene.yml
  returningId: returnSectionId    # Only for RETURNING transitions (not 1-way)
  location:
    useCurrentLocation: true      # Use this scene's location
    usePlayerHome: true           # Use player's home
    wall: "cream-painted wall"    # Define manually
    floor: "hardwood floor"
    hasBed: true
    isOutside: false
```

### NPC Action Weight System

Default weight = 1. Conditions are evaluated at runtime; each true entry multiplies or divides.

```yaml
maleNpcActions:
  - id: rareEvent
    textId: empty
    condition: true
    weightDivisorConditions:
      - true    # /2
      - true    # /4
      - true    # /8 total — genuinely rare

  - id: commonEvent
    textId: empty
    condition: true
    weightMultiplierConditions:
      - $m.hasTrait("BOASTFUL")    # x2 if boastful
      - $m.isPartner()             # x2 again if partner → x4
```

Use `weightDivisorConditions: [true, true, true]` for truly rare events — surprising moments that feel special precisely because they don't happen every session.

### Outfit Types (valid values)
`CASUAL` · `BUSINESS` · `GOING_OUT` · `NIGHTWEAR` · `SWIMWEAR`

### Figure Values (Male)
`AVERAGE` · `SKINNY` · `TONED` · `MUSCULAR` · `THICKSET` · `PAUNCHY` · `FAT`

### Figure Values (Female PC)
`SLIM` · `TONED` · `WOMANLY`

---

## Game Flag Naming Convention

Use SCREAMING_SNAKE_CASE. Be specific and descriptive:
- `"MET_BAKERY_MAN"` — a specific person encountered
- `"FLASHED_PUB_CROWD"` — an action taken
- `"REFUSED_CHARITY_MUGGER"` — a choice made
- `"SEEN_WEIRD_ARGUMENT_CAFE"` — a world event witnessed

Prefix solo events with `"SOLO_"` and named NPC events with the NPC identifier for clarity.

---

## Content Gating

Newlife uses a three-state rough content system driven by player character traits. All new content must respect this system.

### The Three States

| Trait | What it means | What you must do |
|-------|--------------|------------------|
| `$w.hasTrait("BLOCK_ROUGH")` | Player disabled rough/noncon content | Exclude all rough, dubcon, and noncon paths — no hints, no softer versions of the same thing |
| `$w.hasTrait("LIKES_ROUGH")` | Player actively wants rough content | Add extra paths and weight multipliers where appropriate |
| Neither | Default player | Mild content fine; hard rough or noncon excluded |

### Content Categories

Label each scene and each branching path with one of these:

| Tag | What it includes | Gate required |
|-----|-----------------|---------------|
| `VANILLA` | No sexual content | None — always safe |
| `SEXUAL` | Consensual sex, non-rough | None — always safe in this adult game |
| `ROUGH` | Consensual rough/BDSM | `!$w.hasTrait("BLOCK_ROUGH")` |
| `DUBCON` | Ambiguous consent — drunk, pressure, power imbalance | `!$w.hasTrait("BLOCK_ROUGH")` |
| `NONCON` | Non-consensual | `!$w.hasTrait("BLOCK_ROUGH")` |

### Gating Patterns

**VM — rough path within a scene:**
```velocity
#if (!$w.hasTrait("BLOCK_ROUGH"))
He doesn't ask. She finds herself not stopping him.
#else
He glances over and seems to think better of it.
#end
```

**VM — three-level rough gradient:**
```velocity
#if ($w.hasTrait("LIKES_ROUGH"))
He's more forceful than she expected. That's the thing — she expected it.
#elseif (!$w.hasTrait("BLOCK_ROUGH"))
He pushes a little. She lets it happen without quite deciding to.
#else
He keeps it slow. She doesn't have to think about it.
#end
```

**YML — gate an entire action:**
```yaml
- id: letHim
  condition: '!$w.hasTrait("BLOCK_ROUGH")'
  shortDesc: Don't stop him
  longDesc: See where this goes.
  textId: letHimText
  finishScene: true
```

**YML — weight boost for LIKES_ROUGH:**
```yaml
- id: roughApproach
  condition: '!$w.hasTrait("BLOCK_ROUGH")'
  textId: empty
  weightMultiplierConditions:
    - $w.hasTrait("LIKES_ROUGH")    ## x2 if she wants rough
```

**YML — whole-scene gating (scene is entirely NONCON or DUBCON):**

Gate at the NPC action level in the dispatcher scene:
```yaml
menApproach: '!$w.hasTrait("BLOCK_ROUGH")'
```

Or in `weight_modifiers.properties`, set the scene to 0 (disabled entirely).

### Rules

- **Always provide an `#else`** for rough branches — `BLOCK_ROUGH` players must get alternative text, never a blank
- **Never hint at rough content** for `BLOCK_ROUGH` players — not even "you feel like something was about to happen"
- **`LIKES_ROUGH` is preference, not blanket consent** — use it to add paths and weight, not to skip player choice
- **Every rough-content action in YML** must have `condition: '!$w.hasTrait("BLOCK_ROUGH")'`

---

## Common Patterns

### Repeat-visit variation
```velocity
#if (!$gd.hasGameFlag("FIRST_PHARMACY_VISIT"))
    $gd.setGameFlag("FIRST_PHARMACY_VISIT")##
    The woman at the counter glances up, sizing you up in the way pharmacists do.
#else
    The woman at the counter gives you a brief nod — she's served you before.
#end
```

### Revealing an NPC mid-scene
```yaml
effects:
  - effect: $scene.unHideNpc($helper)
  - effect: $helper.addNpcLikingMedium()
  - effect: $helper.addTrait("WALK_HOME_ALONE_HELPER")
```
NPCs are hidden at scene start and revealed when the player's actions bring them into the scene.

### Blocking a transition if already done
```yaml
returningTransition: "!$m.hadOrgasm"
```

### Stat check conditions
```yaml
condition: '$w.getSkill("FITNESS") > 20 && !$w.hasTrait("PLAIN")'
```
