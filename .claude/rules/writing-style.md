# Writing Style Guide

This is the prose standard for all content added to this project. Read it before writing a single line of text.

---

## Voice and Register

The game's narrator is a slightly detached second-person voice — dry, observational, British, with occasional dark humour. It is **not**:
- Literary or self-consciously artistic
- Pornographic in euphemism ("his throbbing manhood")
- Clinical or mechanical
- Chipper and upbeat ("What a fun adventure!")

It sits somewhere between a wry novel and someone telling you what happened to them. The narrator notices things. It has opinions but doesn't editorialize directly. The tone is casual-to-conversational without being sloppy.

---

## POV and Tense

- Always second-person: "You go...", "You see...", "He says..."
- Always present tense: "You walk home" not "You walked home"
- Vary sentence starters — don't open every sentence with "You"

---

## British English (Non-Negotiable)

The setting is a contemporary UK city. Use British spellings and references throughout.

| Use | Not |
|-----|-----|
| Boots / Superdrug | CVS / Walgreens |
| Greggs | generic "bakery" |
| pub | bar |
| pavement | sidewalk |
| flat | apartment |
| quid / fiver / tenner | dollar amounts |
| mobile | cell phone |
| sloshed / pissed (drunk) | wasted, hammered |
| yobs | thugs / punks |
| queue | line |
| rubbish | trash / garbage |
| brilliant / rubbish | awesome / terrible |

Shops and brands that exist in this world: Aldi, Lidl, Greggs, Boots, Superdrug, Costa, Pret, Waitrose (posh), Wetherspoons (cheap pubs), Primark.

---

## Trait Branching: The Fundamental Rule

**Trait branches must change what happens — not what adjective is used.**

### Bad (adjective-swap — do not do this):

```velocity
#if ($w.hasTrait("POSH"))
You smile gracefully at him.
#elseif ($w.hasTrait("CUTE"))
You smile cheerily at him.
#elseif ($w.hasTrait("SULTRY"))
You smile alluringly at him.
#else
You smile at him.
#end
```

This is the most common failure in the existing codebase. Every path is structurally identical. The player experiences exactly the same scene regardless of who she is.

### Good (situational — what actually changes):

```velocity
#if ($w.hasTrait("POSH"))
You give him the slight, closed-lip smile you reserve for situations that require acknowledgement but not encouragement. He seems to take it as an invitation anyway.
#elseif ($w.hasTrait("CUTE"))
You beam at him before you can stop yourself. He looks pleased in a way that makes you feel vaguely responsible for his mood.
#elseif ($w.hasTrait("BITCHY"))
You don't smile. He gets the message and finds somewhere else to be.
#else
You catch his eye by accident. The moment stretches until one of you looks away.
#end
```

The scene itself changes. The outcome changes. The tone changes. The character is present in what happens, not just how one word is coloured.

---

## Trait Quick Reference

Use 2-4 player traits per scene. Pick the ones that genuinely change whether this situation is comfortable, awkward, desirable, or infuriating for that person. A strong `#else` handles everyone else.

- **POSH**: Notices class signals. Faintly superior. Avoids anything "slovenly". Prioritises presentation. Goes to Boots, not Superdrug.
- **CUTE**: Genuine enthusiasm, easily delighted, occasionally oblivious to social dynamics. Can be taken advantage of through naivety.
- **SULTRY**: Aware of her effect on people. Comfortable with attention and attraction. Operates with deliberate ease.
- **DOWN_TO_EARTH**: Practical, unselfconscious. Good deals matter. No pretension. Prefers Superdrug, stocks up on Aldi wine.
- **BITCHY**: Notices what's annoying and says so, or thinks it loudly. Often right. Low tolerance for nonsense.
- **SHY**: Avoids eye contact, defers, gets flustered. Actions cost more than they look. May fail to do what she wants to do.
- **REFINED**: Sensitive to vulgarity. Dislikes crudeness. Has opinions about quality and presentation.
- **ROMANTIC**: Takes everything slightly more seriously than is warranted. Notices possibility in small moments.
- **FLIRTY**: Can't entirely help it. The context doesn't always matter.
- **AMBITIOUS**: Goal-focused. Impatient with things that don't advance anything. Evaluates everything.
- **OVERACTIVE_IMAGINATION**: Takes situations to their logical (and sometimes absurd) conclusion. Gets ahead of herself.

---

## NPC Voice by Personality

NPCs must sound distinct. Every line of NPC dialogue should reflect who that NPC is and what they want from this interaction.

- **JERK**: Transactional, contemptuous, self-serving. Performs warmth when he wants something. Drops it fast.
- **SELFISH**: Self-absorbed. Relates everything to himself. Oblivious to what others need.
- **AVERAGE**: Ordinary, predictable. No particular edge or warmth. The baseline of humanity.
- **ROMANTIC**: Earnest, attentive, occasionally overwrought. Notices small things about you and says so.
- **CARING**: Actively interested. Asks follow-up questions. Adjusts to what you need. Remembers.

Modify with traits:
- **SLEAZY** (any personality): more sexually forward, less tactful, pushes past comfort faster
- **CHARMING**: reads the room well, can fake warmth convincingly
- **BOASTFUL**: redirects to himself, misses signals, needs an audience
- **CRUDE**: swears more, less filter between thought and mouth
- **TACITURN**: minimal dialogue, communicates through gesture, presence, and implication

---

## Anti-Patterns (Never Write These)

### 1. Emotion announcement
- ❌ "You feel a wave of embarrassment."
- ❌ "You're nervous."
- ❌ "A shiver runs down your spine."
- ✅ Show the physical or behavioural evidence. Let the reader feel it.

### 2. Heart/pulse clichés
- ❌ "Your heart skips a beat."
- ❌ "Your pulse quickens."
- ❌ "Your heart races."

### 3. Generic NPC dialogue
- ❌ "You look beautiful tonight."
- ❌ "Want to get out of here?"
- ❌ "You're amazing, you know that?"
- ✅ Dialogue should reflect the NPC's personality, their current goal, and the specific situation.

### 4. Passive observation chains
- ❌ "You notice a man. You see that he is tall. You observe that he is looking at you."
- ✅ Enter mid-action. Pick one detail that matters. Let it mean something.

### 5. Step-by-step narration without texture
- ❌ "You walk to the counter. You order a coffee. You pay. You wait. Your coffee arrives."
- ✅ Skip the mechanical steps. Write what's actually interesting about this moment for this character.

### 6. Perfect structural symmetry
Every scene doesn't need the same number of branches or the same beats. Real situations are asymmetric. A POSH branch might be two sentences. A SHY branch might run longer and end worse.

### 7. Resolving everything neatly
Not every encounter ends with resolution. The man can just walk away. The awkward moment can stay awkward. The world doesn't owe the player a tidy conclusion.

---

## What "The World Has Its Own Life" Looks Like in Prose

The narrator should occasionally notice things that have nothing to do with the player's choices. The city has weather. The park has other people doing things. Background events can interrupt. Not everything resolves because of what the player chose — sometimes it resolves because of what someone else did.

**Small specific details over sweeping atmosphere:**
- ❌ "The park is beautiful and peaceful."
- ✅ "A kid is being dragged away from the fountain by her dad while her ice cream melts down her wrist."

**The player is a person in a world, not the centre of that world.** The world was happening before she arrived, and it continues after.

---

---

## The Transformation Fantasy

This is the game's deepest and most distinctive creative territory. The player character was transformed from male to female. Most solo content ignores this entirely, treating her as if she always was a woman. That is a missed opportunity of the first order.

The transformation is not a premise to be acknowledged once and forgotten. It is a lens that changes how *every* socially-gendered experience lands. A catcall, a hand held open, being talked over, being protected, feeling desire for a man — these things mean something *different* for a woman who remembers being a man. The game's erotic logic (the world happening to her, loss of control, things she didn't plan for) is deepened enormously by the specific position she's in: she *knows* how men think. She's about to find out what that means from the other side.

**Use this. It is what makes this game specific.**

---

### The Three PC Types

Always write a path for each:

```velocity
#if (!$w.hasTrait("ALWAYS_FEMALE") && $w.getSkill("FEMININITY") < 50)
    ## Transformed, still adjusting — the richest zone for transformation content
#elseif (!$w.hasTrait("ALWAYS_FEMALE"))
    ## Transformed, fully adapted — past is distant but real
#else
    ## Always female — no transformation frame; write her as a woman who has always been one
#end
```

If a scene has no meaningful transformation angle, skip the check entirely and write normally. Not every scene needs a transformation branch — only the ones where it genuinely changes the texture of what happens.

---

### FEMININITY as a Writing Dial

`$w.getSkill("FEMININITY")` tracks adaptation. It is not binary.

| Range | What she's like | Example texture |
|-------|----------------|-----------------|
| < 20 | Strongly male-identified | Female experiences feel like thresholds. "This is becoming a woman." Sex with a man is conceptually enormous. |
| 20–49 | Conflicted | Recognises female feelings, doesn't fully own them. "You're really a guy at heart, right?" — but less certainly than before. |
| 50–74 | Adapted, not erased | Mostly inhabits female life. Occasional flicker of the former self. The past is real but not dominant. |
| ≥ 75 | Fully adapted | Barely remembers being male. The transformation is distant. Don't impose transformation content here unless it's earned. |

---

### Four Transformation Textures

**1. Insider knowledge**
She knows how men think because she was one. This gives her unusual clarity about male behaviour — she can read what a man wants, what he's performing, what he actually means. This is not magic powers; it is the specific advantage of having been on that side. It can be erotic (she knows exactly how much trouble she's in), uncomfortable (she recognises the gap between what he's saying and what he's doing), or simply wry (she's watched this play out before, from the other side).

```velocity
#if (!$w.hasTrait("ALWAYS_FEMALE") && $w.getSkill("FEMININITY") < 50)
She knows that look. She used to wear it.
#end
```

**2. Body unfamiliarity**
She is still, at some level, learning what this body does and how it works. Not in an exaggerated way — not constant commentary — but in specific moments where something about being in this body is genuinely new. The weight of breasts. The specific vulnerability of being smaller. Her own reflection after a year of this. Having to learn her own anatomy the way someone else would learn a foreign language.

```velocity
#if (!$w.hasTrait("ALWAYS_FEMALE") && $w.getSkill("FEMININITY") < 50)
There's still the occasional moment where her own reflection takes her slightly by surprise. This is one of them.
#end
```

**3. Social reversal**
She used to be on the side that holds doors, pays, interrupts, takes up space. Now she's on the other side of all of it. This can be:
- Dissonance (being talked over when she used to do the interrupting)
- Revelation (being protected when she used to be the one offering protection)
- Irony (experiencing exactly what she used to dish out)
- Charged eroticism (being the object of male desire when she used to be the one desiring)

**4. Desire crossover**
The game assumes male-start PCs were heterosexual before transformation. Attraction to men is genuinely new. For low-femininity PCs this can be destabilising — finding herself responding to a man physically, and not knowing what to do with that. For high-femininity PCs it's simply desire, unqualified. Calibrate by FEMININITY level.

---

### Anti-Patterns (Transformation-Specific)

| Don't write | Why |
|---|---|
| Transformation reference in every scene | Becomes noise. Reserve it for scenes where it changes something. |
| "As a former man, you..." | Clunky. Show the transformation through experience, not announcement. |
| Same transformation branch at all femininity levels | A FEMININITY 15 PC and a FEMININITY 60 PC are different people. |
| ALWAYS_FEMALE players left with a blank or a gap | They must always get a complete, valid path. |
| Transformation as comedy | It's not a gag. It's serious creative territory. Wry is fine; slapstick is not. |
| Ignoring it when it would genuinely change the scene | The biggest failure mode — treating her as if she has no history. |

---

### When Transformation Content Is Earned

A scene earns transformation content when the gendered nature of the experience is part of its charge. Ask: **would this moment feel different to a woman who used to be a man than to a woman who always was one?**

If yes: write the branch.

Scenes that almost always earn it: male attention scenes; body-awareness moments; being treated as a woman in a way she'd have been invisible to before; desire for a man; first-time sexual experiences; social situations where gender dynamics are active.

Scenes that often don't need it: buying groceries, choosing a film, dealing with a broken appliance. Include it if it feels genuinely earned, not as a quota.

---

### Content Tag: `TRANSFORMATION`

Add `TRANSFORMATION` to a scene's content tags when the scene has at least one branch specifically written for the transformed PC. This allows future agents to identify and audit transformation coverage.

---

## Adult and Erotic Content

This is an adult game. Sexual content should be genuinely arousing — not mechanically explicit, not clinically descriptive, and not the generic AI version of eroticism.

### What makes it work

**Tension over description.** What hasn't happened yet is more powerful than what has. The moment before is more erotic than the moment of. The look across a room, the hand that stops just short, the decision not yet made — these carry more charge than a catalogue of actions.

**Desire is specific.** Not "she wants him" — what specifically does she want, in what way, and how is that complicated by who she is and who he is? A SHY PC wants things she won't say. A SULTRY PC wants things she'll say too easily. A ROMANTIC PC wants things wrapped in meanings that might not be there. The desire is character.

**The PC's traits are present during sex.** A REFINED woman experiencing something she finds crude doesn't stop being refined — the friction is the content. A CUTE woman in over her head is still herself. The erotic charge often comes from the gap between who she is and what's happening to her.

**NPC desire is specific too.** A ROMANTIC man and a JERK man both want the PC — but what they want from her, how they show it, and what satisfies them are completely different. The ROMANTIC notices her. The JERK wants to use her. These are not interchangeable. The texture of their desire matters.

**The game's core erotic logic is loss of control.** The world happens to her. She responds. Unpredictability, the world exceeding her choices, situations she didn't invite — this is baked into the game's design. Erotic content that leans into this (things happening faster than she planned, finding herself wanting something she hadn't intended to want, NPC agency overriding her expectations) is more aligned with the game than content where she's in full control of a scripted sequence.

### The arousal system
The game tracks arousal via `$w.addArousalTiny()`, `$w.addArousalSmall()`, `$w.addArousalMedium()`, and `$m.addArousalTiny()`. Use these in the VM text near the prose that earns them — not in batches at the end. If the text describes something that would actually affect arousal, the effect call should sit there.

### Vocabulary register
The game uses direct, non-euphemistic vocabulary for bodies and sex without being clinical. Look at the existing explicit scenes for calibration — they use plain English. Avoid:
- Purple prose ("his throbbing need", "her feminine core")
- Clinical detachment ("the penis", "vaginal area")
- The AI middle ground of vague eroticism ("she felt desire building inside her")

Write what actually happens. Name the parts plainly. Let the situation create the charge, not the words.

### AI erotic clichés (never write these)

| ❌ Never | Why it fails |
|---|---|
| "She bit her lip" | Universal AI tic, means nothing |
| "She felt heat building inside her" | Tells instead of shows, vague |
| "She couldn't help herself" | Removes agency in a way that's not interesting |
| "His hands explored her body" | Generic; which hands, which body, what specifically |
| "She moaned softly" | Default; every encounter doesn't sound the same |
| "He looked at her hungrily" | Stock phrase; what does hungry actually look like on this man |
| "She was lost in the moment" | Abstraction where the moment should be |
| Perfect mutual satisfaction as default | Real desire is messier and more specific than this |

### The erotic weight of non-sexual scenes
A solo event doesn't need to be sexual to carry erotic charge. The caught-in-rain scene with the man sharing an umbrella. The street encounter she handled badly and the specific way her body remembers it. The ex's missed call at 11:47pm. The mundane weight of the world making claims on her. This ambient texture — the world being interested in her, the world imposing itself — is part of what makes the explicitly sexual scenes land when they arrive.

Don't oversell non-sexual scenes as erotic. Let the charge be ambient.

---

## Velocity Craft Notes

**Suppressing newlines:** Put `##` at the end of a line to prevent Velocity from inserting a newline after a directive. This is essential when a conditional sits mid-sentence:

```velocity
He glances at you##
#if ($w.hasTrait("SULTRY")) — actually glances back.##
#else and then away.##
#end
```

**Random selection:**
```velocity
$scene.pickFromList(["He doesn't look back.", "He almost trips over his own feet.", "He immediately checks his phone."])
```

**Random boolean for variation:**
```velocity
#if ($scene.randomBoolean())
The second time he walks past, he pretends he didn't.
#end
```

**Indentation:** Use tabs inside text blocks. Tabs are stripped before display; spaces are not and will show as leading whitespace.

**Game effects in text:** Effects can appear in the VM file directly (e.g. `$m.addNpcLikingTiny()`). This is fine for effects that belong next to their prose. But never put effects inside `<sceneDescriptionText>` — that tag is rendered multiple times per session.
