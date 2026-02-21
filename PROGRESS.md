# Newlife Expansion — Project Progress

This file is the persistent memory of this project. It is automatically loaded at every session start. An agent reading this file should be able to pick up and continue without any additional context from the user.

---

## How to Continue

When the user says **"continue"**, **"pick up where we left off"**, or invokes `/continue`:

1. Read this file completely
2. Check `additional_scenes/official_content/` for any new `.yml` files added since last session
3. Move any scenes found there from **Backlog** to **Completed** in this file
4. Start working on the **first item in the Backlog** using the `/new-scene` workflow
5. When a scene is done, update this file: move that item to Completed, update "Last worked on"
6. Continue to the next backlog item until the user says stop

The workflow is: `/scene-concept` to refine if needed → `/new-scene [brief]` → `/scene-review [name]` → fix issues → update this file → next item.

Do not ask the user which scene to work on unless the backlog is empty. The backlog is ordered by priority — work top to bottom.

---

## Project Summary

We are expanding Newlife (a British adult life-sim text game) to make the world feel genuinely alive and unpredictable. The player controls only herself. The world should feel like it has its own life beyond her choices.

**Immediate priority:** Solo events. Only 5 exist in vanilla game. Target: 100+ new scenes. Backlog currently has 50 complete briefs ready to write. The `/continue` skill generates them in parallel batches of 5.

**System we built (Sessions 1-2):**
- `.claude/CLAUDE.md` — project context, auto-loaded by all agents
- `.claude/rules/writing-style.md` — prose standard, anti-patterns, adult content guidance
- `.claude/rules/velocity-syntax.md` — YML + VM technical reference including content gating patterns
- `.claude/rules/scene-design.md` — world-alive design philosophy and content classification
- `.claude/skills/new-scene/SKILL.md` — full scene generation pipeline with content tag field
- `.claude/skills/scene-review/SKILL.md` — QA command
- `.claude/skills/scene-concept/SKILL.md` — concept brainstorm
- `.claude/skills/continue/SKILL.md` — session pickup command
- `.claude/agents/prose-writer/AGENT.md` — VM prose specialist with content gating rules
- `.claude/agents/scene-architect/AGENT.md` — YML structure specialist with content gating rules

**Content filtering system (Session 2):**

The game uses `$w.hasTrait("BLOCK_ROUGH")` and `$w.hasTrait("LIKES_ROUGH")` to control rough/noncon content. All new scenes must tag their content level and gate appropriately:
- VANILLA / SEXUAL — no gating needed
- ROUGH / DUBCON / NONCON — must check `!$w.hasTrait("BLOCK_ROUGH")` at every path that contains that content
- See `.claude/rules/velocity-syntax.md` → "Content Gating" for exact patterns

---

## Completed Scenes

*(None yet — this section fills as scenes are written)*

---

## Backlog (work in this order)

Each item below is a fully specified scene brief. Use it directly as the basis for `/new-scene`. No additional concept work needed unless marked NEEDS REFINEMENT.

---

### 1. `minievent_solo_charitymugger` — READY

**Premise:** She's walking through town and a charity fundraiser with a clipboard steps into her path. He's practised, relentless, and has a story about children or dolphins. The world did not ask her permission before putting him here.

**Choices:**
- Engage warmly (listen to the pitch)
- Brush past with an excuse
- Donate without engaging (just to get away)
- Be openly rude about it (BITCHY gate or high stress)

**Trait branches:**
- `BITCHY` — pre-empts him mid-sentence; he tries anyway; she ends it harder
- `ROMANTIC` — genuinely moved by the cause; donates more than she intended; mild regret
- `CUTE` — can't say no to the sad photos; volunteers her email; immediately regrets the email
- `AMBITIOUS` — calculates the cost-per-interruption in seconds; moves on efficiently

**Consequences:**
- Game flag `CHARITY_MUGGER_DONATED` if she gives money
- Game flag `CHARITY_MUGGER_RUDE` if she was explicitly rude (can be referenced later)
- `$gd.addStat("HEROES_REWARDED")` for donation, `$gd.addStat("ACTS_OF_EVIL")` for rude dismissal
- Second-visit variation: he recognises her (or she recognises him)

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 2. `minievent_solo_overheardfight` — READY

**Premise:** She's in a café or on a bench when a couple nearby has an argument that they're both pretending not to have. Low voices, controlled fury, the specific misery of a relationship visibly breaking down in public. She didn't ask to be here for this.

**Choices:**
- Move to a different seat/spot
- Stay and eavesdrop properly (small arousal penalty, character development)
- Intervene if it escalates
- Text a friend about what she's witnessing (friend flag dependency possible)

**Trait branches:**
- `REFINED` — acutely discomfited by the vulgarity of public suffering; moves
- `ROMANTIC` — reads their whole history into it; can't look away; ends up sad
- `BITCHY` — judges both of them specifically and correctly; inner monologue
- `OVERACTIVE_IMAGINATION` — has written their entire backstory and next five years before her coffee arrives

**Consequences:**
- Game flag `WITNESSED_PUBLIC_FIGHT`
- Small stress effect on PC if she stays too long
- If she intervenes: NPC reveal — the woman thanks her or the man is hostile

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 3. `minievent_solo_traindelay` — READY

**Premise:** Public transport is not running. Delayed, cancelled, or simply packed to the point of absurdity. She is stuck. The platform announcement is apologetic and useless. Other people are reacting in their various ways.

**Choices:**
- Wait it out quietly
- Find an alternative (cab, walk) — costs money
- Get into it with a fellow passenger who's being insufferable
- Talk to someone who seems normal

**Trait branches:**
- `POSH` — the specific indignity of the Northern line; she stands very still
- `AMBITIOUS` — calculates how many minutes this costs her; makes calls
- `DOWN_TO_EARTH` — checks the bus map; this is fine; she's done this before
- `SHY` — the proximity of strangers is the worst part; focuses very hard on her phone

**NPC involvement:** If she talks to someone, a weighted NPC action picks who it is and what they're like. Male NPC with personality-driven interaction.

**Consequences:**
- Game flag `SURVIVED_TRAIN_DELAY`
- If she met someone on the platform: NPC liking bump + knowledge increase
- If she spent money on alternative: small financial effect

**Content tags:** VANILLA — no gating required (any male NPC conversation stays social; no sexual paths in this scene)

**Rarity:** common

---

### 4. `minievent_solo_foundwallet` — READY

**Premise:** On the pavement — a wallet. Fat with cards, some cash visible. No one around who looks like they just dropped it.

**Choices:**
- Hand it in to the nearest shop or police
- Take the cash, leave the rest somewhere findable
- Take the whole thing
- Try to find the owner herself (cards have a name)

**Trait branches:**
- `ROMANTIC` — immediately imagines the owner; their face when they get it back; hands it in
- `BITCHY` — a brief internal debate that isn't very internal; pockets the cash
- `CUTE` — genuinely agonises; takes the high road; tells everyone about it for days
- `DOWN_TO_EARTH` — finders keepers for the cash; cards are useless to her anyway; leaves the rest

**Consequences:**
- `HEROES_REWARDED` stat for handing in, `ACTS_OF_EVIL` for keeping
- Game flag `FOUND_WALLET_HONEST` or `FOUND_WALLET_KEPT` — can be referenced in later scenes or by NPCs
- Random: if she finds the owner herself, a brief encounter with gratitude (and possibly more)

**Content tags:** VANILLA — no gating required (gratitude encounter stays at social level; no sexual content in this scene)

**Rarity:** rare (2 divisors)

---

### 5. `minievent_solo_caughtirain` — READY

**Premise:** She's outside and the sky commits. No warning. Actual British rain — not dramatic storm, just implacable grey soaking. She is not dressed for this.

**Choices:**
- Run for the nearest doorway/shop
- Just walk home in it (requires stoicism or low fitness cost)
- Share an overhang with whoever else is sheltering

**Trait branches:**
- `POSH` — this is personally offensive; the outfit; she flags a cab
- `SULTRY` — wet is wet; she is aware of what she looks like; uses it
- `CUTE` — immediately delighted in a way that surprises her; jumps in a puddle
- `REFINED` — ruins the plan for the day; quietly furious with British weather specifically

**NPC element (weighted):** Another person in the doorway. May offer umbrella. Personality determines how that goes. Can be a route to a conversation or an introduction.

**Consequences:**
- Game flag if she meets someone in the shelter
- NPC liking if umbrella offered and accepted; first step of a possible recurring NPC

**Content tags:** VANILLA/SEXUAL — the scene itself is VANILLA; if the encounter escalates via followup scene transition, that scene carries its own tags. No BLOCK_ROUGH gating needed here.

**Rarity:** common (this is very British and should fire often)

---

### 6. `minievent_solo_exmissedcall` — READY

**Premise:** She looks at her phone. A missed call from an ex. No voicemail. Just his name and the time: 11:47pm. She didn't hear it.

*Requires: `$exlover` exists. Game checks `$exlover.hasDoneSexualActivity("SEX")` or similar — i.e., someone she has history with.*

**Choices:**
- Call back
- Text (ambiguous, gives her control of what to say)
- Ignore it
- Delete his number

**Trait branches:**
- `ROMANTIC` — she's already thinking about why he called; calls back immediately
- `BITCHY` — deletes it; spends thirty seconds being pleased with herself
- `OVERACTIVE_IMAGINATION` — generates six complete reasons he called before she's decided what to do; paralysis
- `SHY` — texts instead of calling; agonises over every word

**Consequences (vary by choice):**
- Call back: NPC interaction, `$exlover.addNpcLikingSmall()` or relationship flag depending on how it goes
- Ignore: game flag `IGNORED_EX_CALL`, can be referenced if he contacts again with more edge
- Delete: game flag `DELETED_EX_NUMBER`, affects future scenes with that NPC

**Content tags:** SEXUAL — calling back may lead to a charged conversation with erotic undertones; no explicit sex in this scene itself. No BLOCK_ROUGH gating needed (content is consensual/suggestive only).

**Rarity:** uncommon (1 divisor) — requires the precondition, so naturally gated

---

### 7. `minievent_solo_streetperformer` — READY

**Premise:** A busker. Could be genuinely good, could be painful. She passes them every time she comes through here.

**NPC weight dispatch:** Different performer types weighted randomly:
- Violinist (actually good) — common
- Acoustic guitar + singing (competent but generic) — common
- Living statue who moves at her specifically — uncommon
- Something unusual (comedian, acrobat, etc.) — rare

**Choices per type vary**, but always include: stop and watch / walk past / leave money / make a request

**Trait branches:**
- `REFINED` — has opinions about quality; tips generously if good, not at all if not
- `CUTE` — the living statue gets her every time
- `DOWN_TO_EARTH` — it's nice, actually; leaves a quid; walks on
- `POSH` — public performance; divided feelings; leaves money as a kind of apology

**Consequences:**
- Very small (this is a texture event) — stress reduction if she stops, game flag on first encounter
- Game flag `MET_STREET_VIOLINIST` if she stays and talks

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 8. `minievent_solo_neighboursituation` — READY

**Premise:** Something is happening in her building that she cannot ignore. Dispatch layer picks:
- Loud argument through the wall (most common)
- Parcel left with her (someone needs it urgently)
- Neighbour locked out

**Choices and consequences vary by sub-scenario.** The thread connecting them: she did not ask to be involved. The world intruded.

**Trait branches run per sub-scenario** — REFINED/SHY/BITCHY/ROMANTIC all have distinct responses to each.

**Consequences:**
- Neighbour NPC introduced as recurring character (no befriending — just texture)
- Game flag per sub-scenario
- Possible: if she helps the locked-out neighbour, she gets something useful later

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 9. `minievent_solo_daytimeencounter` — READY

**Premise:** On the street during the day — unwanted male attention. Not the dangerous night version. The brazen-in-daylight version: someone who knows he has social cover, a comment called out, slow accompaniment she didn't invite.

**Choices:**
- Ignore entirely (works if she keeps pace)
- Respond sharply
- Engage briefly then extricate
- Walk into the nearest shop to shake him

**Trait branches:**
- `REFINED` — deeply uncomfortable; the specific violation of this; walks into Boots
- `BITCHY` — responds; the exchange is brief and decisive
- `SULTRY` — has a taxonomy of this; handles it with practised efficiency
- `SHY` — freezes up; walks faster; hates that she walked faster

**Consequences:**
- Game flag `HANDLED_STREET_ENCOUNTER_WELL` or `HANDLED_STREET_ENCOUNTER_POORLY` based on choice
- Stress increase if she didn't manage it how she wanted to
- Small: `ACTS_OF_EVIL` if she was particularly cutting back

**Content tags:** VANILLA — unwanted attention, not sexual content. No gating required. (The harassment itself is social discomfort, not explicit content — this is a real-world experience, not a rough content path.)

**Rarity:** uncommon

---

### 10. `minievent_solo_unexpectedbill` — READY

**Premise:** Something costs more than it should. A mistake on a bill, a subscription she forgot, a parking fine, something broke and needs fixing. The mundane hostility of money.

**Choices vary** based on the specific scenario (dispatch layer), but always include:
- Pay it without fighting
- Contest it
- Ignore it and deal with consequences later

**Trait branches:**
- `AMBITIOUS` — immediately on the phone; will not accept this; wins or loses based on a skill check
- `DOWN_TO_EARTH` — absorbs it; this is just what happens
- `BITCHY` — contests it on principle even if she'd rather not deal with it
- `CUTE` — somehow charmed her way to a partial refund by being completely genuine about it

**Consequences:**
- Financial effect (minor)
- Game stat depending on outcome
- Stress effect if she ignores it

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

---

### 11. `minievent_solo_liftencounter` — READY

**Premise:** The lift in her building stops. Not dramatically — it just freezes, door won't open, floor display stays wrong. She is alone, or with a neighbour she barely knows. The repair company says twenty minutes. It's thirty.

**Choices:**
- Wait it out quietly
- Talk to whoever's with her
- Try the emergency button (draws an officious recorded response)
- Get visibly agitated (costs more depending on trait)

**Trait branches:**
- `SHY` — the worst part is the proximity, not the lift; she focuses hard on her phone
- `POSH` — is aware this is undignified; stands very still; will not be the one to speak first
- `OVERACTIVE_IMAGINATION` — has written three disaster scenarios by minute five; is mostly fine
- `FLIRTY` — if someone else is present, the situation has possibilities she's willing to explore

**Consequences:**
- Game flag `SURVIVED_LIFT_BREAKDOWN`
- NPC introduced if someone was present: small liking increase
- Stress +small if SHY and she was with a stranger

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 12. `minievent_solo_friendstandsup` — READY

**Premise:** She's at the arranged spot — café, pub, corner table — and her phone buzzes. "So sorry, can't make it, work thing." Twenty minutes after she was supposed to arrive.

**Choices:**
- Stay and make the most of it (solo dinner/drink; reframe as a treat)
- Leave and say she's fine
- Reply honestly that she's annoyed
- Use the time productively (something she'd been putting off)

**Trait branches:**
- `AMBITIOUS` — laptop out before she's finished reading the message; this is productive, actually
- `ROMANTIC` — sits there long enough to feel sorry for herself; orders the wine anyway; the wine helps
- `BITCHY` — sends a reply that is technically polite and is not polite; feels fine about it
- `DOWN_TO_EARTH` — orders what she wanted; reads her phone; it's fine; it really is fine

**Consequences:**
- Game flag `FRIEND_STOOD_ME_UP`
- Friend liking -small if she replied with genuine annoyance
- Stress +small if she handled it badly; -small if she genuinely made something of it

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 13. `minievent_solo_streetphotographer` — READY

**Premise:** A man with a camera — actual camera, not a phone — stops her on the street. Street photographer. He'd like to take her photo. He seems legitimate and apologetic about it.

**Choices:**
- Allow it (he takes one shot, thanks her)
- Decline politely
- Ask to see the others he's taken (conversation opens)
- Ask what he does with the photos (game flag potential)

**Trait branches:**
- `SULTRY` — aware of what she looks like right now; composed; curious about the result
- `SHY` — instinctive no before she's thought about it; might wonder about that later
- `CUTE` — immediately wants to see if it came out well; asks twice; he shows her
- `AMBITIOUS` — asks about the exhibition, the platform; evaluates whether this is useful

**Consequences:**
- Game flag `PHOTOGRAPHED_BY_STRANGER`
- If she stayed and talked: NPC introduced with possible recurring potential
- Arousal tiny if SULTRY and she saw herself reflected in his attention

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 14. `minievent_solo_weddingnotification` — READY

**Premise:** Social media delivers news. Someone she knows — an ex, or a friend of an ex — has announced an engagement. The photos are inescapable. They look happy.

*Requires: at least one NPC with sex history (`$m.hasDoneSexualActivity("SEX")`)*

**Choices:**
- Like the post (costs something she can't name)
- Ignore it (closes the app immediately)
- Look through their profile
- Text someone about it

**Trait branches:**
- `ROMANTIC` — feels something complicated and specific; stares longer than intended; the venue is wrong for him
- `AMBITIOUS` — notes the venue, the cost, what this says about his situation now; decides she's fine
- `BITCHY` — fully formed opinion in under four seconds; keeps most of it to herself; shares the best part with one person
- `OVERACTIVE_IMAGINATION` — by the time she closes the app she has lived the alternate life and buried it

**Consequences:**
- Game flag `SAW_EX_ENGAGEMENT`
- Stress +small
- If she looked through the profile: flag `STALKED_EX_PROFILE`

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon (1 divisor) — requires precondition

---

### 15. `minievent_solo_selfcheckout` — READY

**Premise:** The self-checkout machine has decided today is not the day. Unexpected item in the bagging area. Please wait for assistance. She has been waiting for assistance for four minutes. The queue behind her is aware.

**Choices:**
- Wait patiently (eventually resolved)
- Abandon everything and leave
- Get sharp with the assistant when they finally arrive
- Find this darkly funny and post about it

**Trait branches:**
- `BITCHY` — specific complaint about the machine, the design, the concept; is completely right; the assistant has heard this before
- `DOWN_TO_EARTH` — this is just Wednesday; waits; the assistant has been doing this all shift and it shows
- `POSH` — the specific humiliation of being held up by a machine; uses the manned checkout from now on
- `CUTE` — somehow makes the assistant laugh in the process; the whole thing resolves with unusual warmth

**Consequences:**
- Game flag `DEFEATED_BY_SELF_CHECKOUT`
- Stress +small if she waited; `ACTS_OF_EVIL` small if she was rude to staff

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 16. `minievent_solo_phonedead` — READY

**Premise:** It dies. Not a low battery warning — just gone. She is not at home. She does not know where she is going from memory alone.

**Choices:**
- Find a café with wifi and sort it from there
- Ask someone for directions (costs something)
- Navigate by memory and landmarks
- Find somewhere to charge it (costs time, possibly money)

**Trait branches:**
- `SHY` — asking someone is genuinely hard; she walks an extra fifteen minutes to avoid it; it's fine
- `AMBITIOUS` — problem to solve; dispatches efficiently; slight irritation
- `DOWN_TO_EARTH` — she can read a city; finds the right road in five minutes; this is not a crisis
- `POSH` — Costa, wifi, orders something she didn't want just to use the table; resolves it correctly

**Consequences:**
- Game flag `SURVIVED_DEAD_PHONE`
- If she asked someone: small chance of NPC interaction (brief exchange)
- Stress +small if she handled it poorly

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 17. `minievent_solo_dogapproach` — READY

**Premise:** A dog with no social sense has decided she's the most interesting person here. It is attached to a lead. The lead is attached to its owner. The owner is male, mildly apologetic, and letting the dog continue.

**Choices:**
- Engage the dog fully (conversation with owner follows)
- Politely decline the dog's advances (brief awkward exchange)
- Use the dog deliberately as an icebreaker
- Ignore the dog, which is harder than it sounds

**Trait branches:**
- `CUTE` — completely undone by the dog; the owner becomes secondary; she asks his name (the dog's)
- `SULTRY` — is aware the dog is a social device; handles the owner accordingly
- `SHY` — the dog is fine; the owner is the problem; she pats it and moves on before he can speak
- `DOWN_TO_EARTH` — pats the dog; brief word; moves on; this is just how dogs are

**Consequences:**
- NPC introduced: owner with weighted personality
- Game flag `MET_DOG_OWNER`
- If she engaged fully: NPC liking bump + recurring potential

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 18. `minievent_solo_overheardflattery` — READY

**Premise:** She hears it. Not to her face — to each other. Male voices, low, with the specific public carelessness of men who assume women aren't listening. One of them has an opinion about her. It is not entirely unpleasant.

**Choices:**
- Act like she didn't hear (keeps walking)
- Pause long enough to let them know she heard
- Turn and look (outcome varies by personality)
- Comment as she passes (BITCHY or SULTRY gate)

**Trait branches:**
- `SULTRY` — she knew; slows down anyway; doesn't turn; knows what she's doing; it costs her nothing
- `BITCHY` — turns and stares at the one who said it, exactly long enough; he looks away first; she walks on
- `SHY` — heard it; found it complicated; kept walking; thinks about it at intervals for the rest of the afternoon
- `REFINED` — distasteful and also slightly gratifying; she doesn't know what to do with that

**Consequences:**
- Arousal tiny if she found it flattering
- Game flag `OVERHEARD_STREET_RATING`
- Stress +small if she found it uncomfortable

**Content tags:** VANILLA, TRANSFORMATION (she knows exactly what's behind the assessment — she used to make that calculation; being on this side of it has a specific charge at low femininity)

**Rarity:** common

---

### 19. `minievent_solo_gymdistraction` — READY

**Premise:** At the gym. A distraction she didn't ask for. Dispatch picks which kind: machine she wants is occupied by someone using it wrong; someone offers unrequested advice; eye contact she doesn't know what to do with.

**Choices:**
- Work around it efficiently
- Engage (conversation follows)
- Make her feelings known (BITCHY gate)
- Use the situation to her advantage (SULTRY/FLIRTY gate)

**Trait branches:**
- `AMBITIOUS` — optimises around the obstacle; the distraction is irrelevant; she came here to work
- `SULTRY` — is aware of the eye contact and what it means; makes a decision; acts on it or doesn't
- `SHY` — the whole space is high-cost; focuses hard on her music; considers leaving early
- `FLIRTY` — her interest and his are approximately matched; something gets said eventually

**Consequences:**
- Game flag `GYM_REGULAR_MET` if she spoke to him
- NPC introduced with random personality
- Arousal small if SULTRY/FLIRTY and the eye contact resolved into something

**Content tags:** SEXUAL (suggestive; arousal tracking; no explicit content) — no BLOCK_ROUGH gating needed

**Rarity:** common

---

### 20. `minievent_solo_dreamwake` — READY

**Premise:** She wakes from a dream that wasn't entirely innocent. The dream is already fading. The feeling isn't. It's 6:47am and she doesn't need to be anywhere until nine.

**Choices:**
- Go back to sleep (dream continues, or it doesn't)
- Get up immediately (efficient; cold shower)
- Stay in bed with it deliberately (arousal path)
- Check her phone to ground herself (what she finds varies by active flags)

**Trait branches:**
- `ROMANTIC` — tries to hold on to it; can't; lies there a little longer than she should; the feeling recedes anyway
- `AMBITIOUS` — up immediately; not a productive state of mind before nine; shower; gone
- `SHY` — slightly embarrassed in front of herself; gets up; doesn't think about who was in it
- `OVERACTIVE_IMAGINATION` — has the whole second and third act of the dream constructed before she's fully awake

**Consequences:**
- Arousal small regardless (the situation earned it)
- Stress -small (rest)
- If she checked her phone and an ex flag is active: additional weight

**Content tags:** SEXUAL, TRANSFORMATION (at low femininity: waking into desire she's still not entirely used to having for anyone from this angle; the AMBITIOUS branch earns a specific beat about efficiency vs. what just happened)

**Rarity:** common

---

### 21. `minievent_solo_oldmessages` — READY

**Premise:** Scrolling back. She doesn't mean to — looking for something else — and then there they are. Messages from someone she was with. The timestamps. The tone. The way he used to text.

*Requires: NPC with sex history*

**Choices:**
- Keep scrolling (goes further back; gets more complicated)
- Close the app
- Re-read a specific thread
- Text him right now (risky)

**Trait branches:**
- `ROMANTIC` — feels the texture of who she was then; stays too long; doesn't regret it exactly
- `BITCHY` — remembers exactly why it ended; closes the app; correct decision; moves on
- `SHY` — notes how often she initiated, how much she tried, what she said; closes the app
- `OVERACTIVE_IMAGINATION` — has reconstructed an entire relationship arc from six texts; this is a known problem

**Consequences:**
- Arousal small if the memories were good
- Game flag `READ_OLD_MESSAGES`
- If she texted: NPC liking +small, flag `INITIATED_LATE_NIGHT_TEXT`

**Content tags:** SEXUAL — evocative but not explicit; arousal may track. No BLOCK_ROUGH gating.

**Rarity:** uncommon (1 divisor) — requires sex history with NPC

---

### 22. `minievent_solo_overheardneighbours` — READY

**Premise:** It's past eleven. She's in her flat. The wall between her and the next unit is doing nothing. She can hear them. She cannot not hear them.

**Choices:**
- Headphones immediately (resolves it)
- Wait it out (involuntary listening)
- Knock on the wall
- Find herself listening more deliberately than she meant to

**Trait branches:**
- `REFINED` — mortified; headphones immediately; thinks about the wall's structural inadequacy
- `ROMANTIC` — something complicated; not jealousy exactly; just awareness of it happening somewhere near her
- `FLIRTY` — makes a note; thinks about whether she knows them; she might
- `OVERACTIVE_IMAGINATION` — has supplied the full scene in her head before she finds the headphones; this is not helpful

**Consequences:**
- Arousal small if she stayed/listened deliberately
- Game flag `HEARD_NEIGHBOURS` (first occurrence)
- Stress -small if she found it humanising rather than irritating

**Content tags:** SEXUAL — arousal tracking; prose implies, doesn't describe. No BLOCK_ROUGH gating.

**Rarity:** uncommon

---

### 23. `minievent_solo_nightfollowed` — READY

**Premise:** Walking home at night. She's been aware of footsteps behind her for two streets now. They've matched her pace. Slowed when she slowed. This is the specific vigilance that lives in the back of every woman's mind at this hour.

**Choices:**
- Cross the street (the footsteps do, or don't, follow)
- Speed up
- Stop and turn
- Walk into a lit shop or doorway

**Trait branches:**
- `SHY` — quickens pace; hates herself for it; the relief when she reaches her door costs something
- `BITCHY` — stops and turns; the look is specific; the footsteps stop and then don't continue
- `AMBITIOUS` — threat assessment; three exits already mapped; manages it efficiently; mild irritation
- `SULTRY` — has run this before; knows the protocol; doesn't break stride; it resolves

**Consequences:**
- Game flag `FOLLOWED_WALKING_HOME`
- Stress +small or +medium depending on how it resolved
- If she confronted: outcome varies (backs down, escalates, fizzles)

**Content tags:** VANILLA, TRANSFORMATION (at low femininity: she knows what the male threat logic is from the other side — which makes being the one monitored more specific, not less frightening)

**Rarity:** uncommon

---

### 24. `minievent_solo_aggressiveapproach` — READY

**Premise:** A man approaches. She declines. He doesn't leave. Not violently — with the specific persistence of someone who has decided that no is a negotiating position. She is in public. Others are present but not intervening.

**Choices:**
- Firm repeat refusal (he escalates or gives up)
- Fabricate she's meeting someone (escape route)
- Walk away mid-sentence
- Ask a nearby person for help

**Trait branches:**
- `BITCHY` — makes the cost of continuing very clear, very fast; he decides it isn't worth it
- `SHY` — the fabricated excuse comes out badly; she escapes; the whole exchange costs more than it should
- `SULTRY` — has this conversation with practised economy; ends it; he was predictable anyway
- `CUTE` — good-faith attempts at polite refusal are misread as encouragement; gets blunter; it works

**Consequences:**
- Game flag `HANDLED_AGGRESSIVE_APPROACH_WELL` or `_POORLY` based on outcome
- Stress +small (mandatory; this is uncomfortable regardless of trait and outcome)

**Content tags:** VANILLA (social confrontation, not sexual content) — no BLOCK_ROUGH gating needed. Escalation to physical would be a separate NONCON scene.

**Rarity:** uncommon (1 divisor)

---

### 25. `minievent_solo_witnessedaccident` — READY

**Premise:** A minor collision on the street — bike, or car, or someone simply not looking. Not serious, but not nothing. She is the nearest person who has actually stopped.

**Choices:**
- Stay and help
- Call 999 and step back
- Check if others are handling it and continue on
- Get the driver's details for the cyclist

**Trait branches:**
- `CUTE` — kneels down immediately; asks the right questions; the parent finds them both crouched in the road
- `AMBITIOUS` — efficient; calls it in; delegates; continues; five minutes lost, two useful
- `SHY` — wants to help but orbits the outer edge of the event; ends up leaving without having been useful; bothers her
- `BITCHY` — if the driver was clearly at fault, she will make that known before she leaves

**Consequences:**
- Game flag `WITNESSED_STREET_ACCIDENT`
- `HEROES_REWARDED` if she stayed and actively helped
- Stress -small if she helped well (agency feels good)

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 26. `minievent_solo_beggar` — READY

**Premise:** Outside a Pret or Boots. He's been there a while. He asks specifically for change for food. The concrete ask is harder to say no to than a general plea.

**Choices:**
- Give him money
- Say no and keep walking
- Buy him something from the shop
- Stop and talk briefly

**Trait branches:**
- `CUTE` — feels it immediately; gives more than she meant to; feels better about this than she probably should
- `POSH` — it's complicated; gives something; feels briefly virtuous; immediately suspicious of the feeling
- `DOWN_TO_EARTH` — makes a quick read of the situation; acts on her read; moves on; no drama
- `BITCHY` — has a read on this particular situation; acts accordingly; it is not always the unkind call

**Consequences:**
- `HEROES_REWARDED` for giving; game flag `GAVE_MONEY_TO_BEGGAR`
- Nothing negative for not giving — it's not a moral failing, it's a choice

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 27. `minievent_solo_gossipopportunity` — READY

**Premise:** She knows something. About someone in her social circle — a colleague, a friend-of-friend. Something she wasn't supposed to find out. She has the opportunity to mention it, now, to someone who would definitely want to know.

**Choices:**
- Say nothing
- Share it (social capital; moral cost)
- Share a softened version (hedged; still carries weight)
- Use the knowledge to help the person it's about, quietly

**Trait branches:**
- `BITCHY` — brief internal debate; says it; it's probably deserved anyway; feels fine
- `ROMANTIC` — overthinks the consequences for everyone involved; says nothing; probably the right call
- `AMBITIOUS` — evaluates the usefulness of the information against the cost of sharing it; decides
- `DOWN_TO_EARTH` — not her business; moves the conversation on

**Consequences:**
- `ACTS_OF_EVIL` stat if she shared it
- `HEROES_REWARDED` if she used it to protect someone
- Game flag `SHARED_GOSSIP` — can surface later as "did you tell her?" moment

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 28. `minievent_work_kitchen` — READY

**Premise:** The office kitchen. She's making tea. A colleague she's barely spoken to is already there. They're both waiting for things. The silence has a specific length.

**NPC dispatch:** AVERAGE most common; CARING or CHARMING possible.

**Choices:**
- Make small talk (goes somewhere based on his personality)
- Maintain the comfortable silence
- Start a conversation about something she actually cares about
- Ask about the work thing she's been wondering about

**Trait branches:**
- `SHY` — the silence is fine; she focuses on the kettle; he is respecting this; she leaves marginally warmer toward him
- `FLIRTY` — the proximity of an office kitchen is not a neutral context; she notices things
- `AMBITIOUS` — finds out something useful about the project; the relationship was incidental but functional
- `DOWN_TO_EARTH` — just a good conversation about the bad coffee; finds out he's alright

**Consequences:**
- NPC introduced with personality
- Game flag `MET_KITCHEN_COLLEAGUE`
- If it went well: NPC liking +small, knowledge +small

**Content tags:** VANILLA — no gating required here

**Rarity:** common

---

### 29. `minievent_work_laterunning` — READY

**Premise:** She's stayed late. The office has mostly emptied. Someone she doesn't expect is still there when she comes back from the kitchen. He looks up.

**NPC:** weighted towards boss or colleague with established flag.

**Choices:**
- Brief exchange and leave
- Stay and talk (she had a reason to stay anyway)
- Find out what he's working on
- Accept his offer of a drink when they're both done

**Trait branches:**
- `AMBITIOUS` — she's here for the same reason; mutual professional recognition; something shifts in her understanding of him
- `SHY` — the empty office is socially different from daytime; harder to read; she leaves sooner than she needed to
- `SULTRY` — is aware of the specific quality of a late office; proceeds with purpose or doesn't; it's her call
- `ROMANTIC` — gives this more weight than it probably deserves; knows she's doing this; stays anyway

**Consequences:**
- NPC liking +small if the conversation was good
- Game flag `STAYED_LATE_WITH_NPC`
- Arousal small if SULTRY/ROMANTIC and something charged happened

**Content tags:** SEXUAL (charged atmosphere; erotic undertone if pursued) — no BLOCK_ROUGH gating needed

**Rarity:** uncommon (1 divisor)

---

### 30. `minievent_work_officerumour` — READY

**Premise:** She overhears — or is directly told — that something about her has been circulating. Could be flattering, damaging, or both. The ambiguity is its own problem.

**Dispatch:**
- "She's apparently quite close with [manager/client]" — ambiguous
- Something true she'd rather weren't common knowledge
- Something fabricated entirely

**Choices:**
- Ignore it
- Find out exactly what's being said and by whom
- Address it directly with the most likely source
- Escalate (HR or her manager)

**Trait branches:**
- `AMBITIOUS` — information management; this affects her position; acts quickly and specifically
- `BITCHY` — has already narrowed the source to two people; proceeds accordingly
- `POSH` — deeply undignified; decides to be above it; is not entirely above it
- `SHY` — the knowledge that people are talking about her is its own kind of damage regardless of content

**Consequences:**
- Game flag `OFFICE_RUMOUR_CIRCULATING`
- Stress +small
- If she addressed it: NPC liking change based on approach

**Content tags:** VANILLA/SEXUAL depending on dispatch — the scene framework is VANILLA

**Rarity:** uncommon

---

### 31. `minievent_friend_adviceseeking` — READY

**Premise:** Her friend has something to tell her and is doing it badly. The thing is personal — a relationship, a body, a decision she's ashamed of. She needs it to land somewhere safe.

**Choices:**
- Listen fully without comment
- Ask the question that gets to the real thing faster
- Offer the opinion she was asked for (risks the friendship if it's wrong)
- Redirect gently toward something actionable

**Trait branches:**
- `ROMANTIC` — leans in; feels the weight of being trusted with this; says the right thing slowly
- `BITCHY` — has the right answer; delivers it; the friend may not love it but it's correct
- `CUTE` — instinctive warmth; exactly the right register for this kind of confidence
- `AMBITIOUS` — has a solution in forty seconds; restrains herself from leading with it; marginally succeeds

**Consequences:**
- Friend liking +small (good response) or -small (tone-deaf)
- Game flag `RECEIVED_FRIEND_CONFIDENCE`
- If opinion was offered and was wrong: flag `FRIEND_CONFLICT_ADVICE`

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 32. `minievent_friend_jealousy` — READY

**Premise:** Something she has is bothering her friend. The friend hasn't said it. They don't need to — there's a quality to how they're talking about it. The PC may or may not notice.

**Choices:**
- Doesn't notice (scene plays around her)
- Notices and says nothing
- Notices and says something carefully
- Notices and says something directly

**Trait branches:**
- `BITCHY` — noticed in the first two minutes; has clocked the exact target; makes a decision about whether it's her problem
- `CUTE` — genuinely doesn't notice; the scene plays out around her unawareness in a way that's almost charming
- `ROMANTIC` — notices; overthinks what it means for the friendship; says something gentle that might have been better left unsaid
- `AMBITIOUS` — if it's career-related jealousy: recognises it as information and adjusts accordingly

**Consequences:**
- Friend liking: flat if unaddressed; +small if handled with care; -small if handled badly
- Game flag `FRIEND_WAS_JEALOUS`
- If she called it out directly: flag `CALLED_OUT_FRIEND_JEALOUSY`

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 33. `minievent_solo_changingroom` — READY

**Premise:** Trying on clothes. The cubicle next to her is occupied. Through the thin partition: a conversation, an opinion, something she wasn't supposed to hear. The changing rooms are doing something to her afternoon.

**Dispatch:**
- Two women talking; the conversation is illuminating or embarrassing
- Someone asks her opinion through the partition
- She's alone longer than expected; the attendant forgot about her

**Trait branches:**
- `REFINED` — specific feelings about the partition's inadequacy; focused on her own reflection
- `OVERACTIVE_IMAGINATION` — the overheard conversation becomes a complete narrative; she has the full backstory before she's done the zip
- `CUTE` — helps the other person enthusiastically; overstays her usefulness; they exchange numbers
- `SULTRY` — the mirror; the specific context; uses the extra time deliberately; minor arousal

**Consequences:**
- Game flag `CHANGING_ROOM_ENCOUNTER`
- Arousal small if SULTRY and she used the time
- NPC possible if conversation led somewhere

**Content tags:** SEXUAL — arousal tracking possible. No BLOCK_ROUGH gating.

**Rarity:** uncommon

---

### 34. `minievent_solo_tubeeye` — READY

**Premise:** On the tube or the bus. Brief, vivid eye contact with a stranger. Not the usual accidental-and-look-away variety. This was deliberate and held.

**Choices:**
- Look away first
- Hold it until one of them looks away
- Smile (small bravery)
- Move toward them when a seat opens

**Trait branches:**
- `SULTRY` — held it; made the decision; knows what follows if she wants it to
- `SHY` — looked away; spent the next four stops thinking about it; will never know
- `FLIRTY` — the smile; immediate; it works or it doesn't; she's fine either way
- `ROMANTIC` — a stranger on the tube and she is giving it the weight of a novel; she knows she's doing this

**Consequences:**
- If she moved toward them: NPC introduced; brief conversation; possible liking and flag
- Arousal small if something happened
- Game flag `TUBE_STRANGER_ENCOUNTER` if any contact made

**Content tags:** SEXUAL, TRANSFORMATION (at low femininity: the specific experience of being looked at — being the one looked at — by a man on a tube is still interesting in a way she can't entirely account for; she knows what he'd be thinking)

**Rarity:** uncommon

---

### 35. `minievent_solo_windowsight` — READY

**Premise:** Walking past a ground-floor flat at night, lit up. She wasn't looking. Then she was. The couple inside aren't being careful. They either don't know or don't care.

**Choices:**
- Look away immediately and walk faster
- Pause involuntarily
- Stop and watch deliberately (arousal path)
- Catch herself and feel things about it

**Trait branches:**
- `ROMANTIC` — it's specifically the tenderness she notices; the way he's looking at her; she keeps walking
- `OVERACTIVE_IMAGINATION` — has the arc of their evening before she's looked away; may be wrong
- `REFINED` — the intrusion of it; the specific way they've made their private business public; moves on
- `SULTRY` — aware of what she's looking at; takes a moment; moves on deliberately

**Consequences:**
- Arousal small/medium if she stopped and watched deliberately
- Game flag `ACCIDENTAL_VOYEUR`
- Stress small if she found it uncomfortable

**Content tags:** SEXUAL — arousal tracking; prose implies, doesn't describe. No BLOCK_ROUGH gating.

**Rarity:** uncommon (1 divisor)

---

### 36. `minievent_solo_bouncer` — READY

**Premise:** At the door of a club or bar, the man with the clipboard looks her over. He says she's good to go, but the way he says it carries something he's added himself. She's going to have to walk past him.

**Choices:**
- Walk past without responding
- Smile back (he remembers her on the way out)
- Say something that costs him the satisfaction
- Wait for her friend still in the queue

**Trait branches:**
- `SULTRY` — has filed his face; has decided how to play the way out; this is filed under later
- `BITCHY` — says the specific thing that lands; he laughs because he can't not; she walks in
- `SHY` — the words don't come until she's already inside; too late; bothers her a little
- `REFINED` — the transaction of it; the small power of the door; says nothing; walks through

**Consequences:**
- Game flag `BOUNCER_INTERACTION`
- Arousal tiny if SULTRY and she made a decision
- Stress small if SHY and she didn't handle it how she wanted

**Content tags:** VANILLA (power dynamic, social friction) — no gating required

**Rarity:** uncommon

---

### 37. `minievent_solo_foundnote` — READY

**Premise:** In a charity shop book, or tucked under her wiper, or slipped under her door. A handwritten note. Not for her — it was for someone else — but she's the one who has it.

**Dispatch:**
- A love note, old, someone's history in someone else's handwriting
- A phone number with nothing else — no name, no context
- Someone's list, mundane and specific, with one item on it that isn't mundane

**Choices vary by dispatch** — but always: keep it, discard it, or act on it.

**Trait branches:**
- `ROMANTIC` — reads the love note twice; feels the weight of other people's histories; keeps it
- `OVERACTIVE_IMAGINATION` — the phone number; the list; she has the complete person constructed before she's decided
- `BITCHY` — discard; move on; this is not her situation
- `CUTE` — can't throw away the love note; keeps it in the book it came from; tells someone about it

**Consequences:**
- Game flag `FOUND_HANDWRITTEN_NOTE`
- If she called the number: brief NPC phone exchange (random outcome)
- Arousal tiny if ROMANTIC and the love note was specific

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 38. `minievent_solo_shoptheft` — READY

**Premise:** She sees someone pocket something small from a shop. They see her see. The decision window is two seconds before they're at the door.

**Choices:**
- Say nothing (they walk out; she knows)
- Alert staff
- Say something directly to the person
- Pretend she didn't see

**Trait branches:**
- `BITCHY` — a very specific look; the shoplifter reads it perfectly and walks faster; she says nothing; it was enough
- `ROMANTIC` — reads the desperation in the action; says nothing; feels okay about this; also, the thing was small
- `AMBITIOUS` — calculates: not her problem; no upside to intervention; continues
- `POSH` — the certainty about what she saw; the internal debate about whether to act; decides against; it costs something small

**Consequences:**
- `ACTS_OF_EVIL` small if she said nothing (complicity)
- `HEROES_REWARDED` if she alerted staff and it led somewhere
- Game flag `WITNESSED_SHOPLIFTING`

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 39. `minievent_solo_unexpectedgoodtalk` — READY

**Premise:** In a queue, or a waiting room, or on a train platform. Someone starts a conversation that goes somewhere she didn't expect. Not flirtation — an actual conversation about something that matters.

**NPC:** weighted toward INTERESTING trait; any personality.

**Choices:**
- Engage fully
- Give polite short answers
- Take it somewhere she's interested in
- Ask something personal that changes the register

**Trait branches:**
- `AMBITIOUS` — finds the conversation useful in a way she didn't expect; exchanges details; might actually follow up
- `ROMANTIC` — the specific rarity of an honest conversation with a stranger; she's still thinking about it later
- `SHY` — the short answers; then something she actually wanted to say; she's surprised she said it; so is he
- `DOWN_TO_EARTH` — a good talk; fine; moves on with slightly more warmth toward people than she had before

**Consequences:**
- NPC introduced with INTERESTING trait
- Game flag `UNEXPECTED_GOOD_CONVERSATION`
- Stress -small (good conversations restore something)
- NPC liking +small if she engaged

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 40. `minievent_solo_spokenabout` — READY

**Premise:** She walks in on a conversation about herself. Not cruel — but not private either. Two people she knows, talking about her, in the register of people who don't know she's here.

*Requires: at least two NPCs with established liking*

**Choices:**
- Back out before they see her
- Stay quiet long enough to hear more
- Make her presence known immediately
- Walk in normally and let them see her when they see her

**Trait branches:**
- `BITCHY` — knows immediately; chooses; the choice is decisive and she lives with it
- `ROMANTIC` — depends entirely on the tone of what she caught; if it was fond, this lands very differently
- `POSH` — the social wrongness of all the options; picks the least bad; manages it correctly
- `OVERACTIVE_IMAGINATION` — has completed the conversation from the fragment she caught; may be significantly wrong

**Consequences:**
- Game flag `OVERHEARD_CONVERSATION_ABOUT_SELF`
- NPC liking change (up or down depending on tone and her choice)
- Stress small either direction

**Content tags:** VANILLA — no gating required

**Rarity:** rare (2 divisors) — requires multiple established NPCs

---

### 41. `minievent_partner_unexpectedgift` — READY

**Premise:** He's brought something. Not a birthday, not a holiday. Just because. It's either exactly right or exactly wrong — both carry weight.

*Requires: PC has a boyfriend/partner*

**Dispatch:**
- Exactly right: something small and specific that shows he's been paying attention
- Almost right: he tried; the effort is visible in the wrongness
- Clearly wrong: he did not try, or he tried and this is his understanding of her

**Trait branches:**
- `ROMANTIC` — the exactly-right version lands hard; she was not prepared for this; it costs her something good
- `POSH` — evaluates the taste of it; the almost-right version produces a complicated internal moment
- `BITCHY` — the clearly-wrong version; she manages to thank him; tells one person later with extreme specificity
- `CUTE` — delighted by any version of this; even the wrong gift is the thought; she means this

**Consequences:**
- NPC liking +small (received well) or flat (didn't)
- Game flag `PARTNER_BROUGHT_GIFT`
- Relationship quality flag based on dispatch

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 42. `minievent_partner_hisex` — READY

**Premise:** They're out together. His ex. Here. The two of them have a moment he needs to navigate, and the PC watches from approximately one metre away.

*Requires: PC has a boyfriend*

**Choices (PC's internal/external response):**
- Be completely fine (varies by how convincingly she performs this)
- Make an excuse to step away
- Stay close (protective instinct, or something else)
- Ask him about it afterwards

**Trait branches:**
- `ROMANTIC` — watches the exchange for information about what she is to him; reads everything; some of it may be wrong
- `SULTRY` — is aware of what she looks like standing here; stands the way she stands; fine
- `AMBITIOUS` — immediate comparison; herself versus the ex; files the results; is fine
- `SHY` — the physicality of the implied comparison; focuses on something that isn't them

**Consequences:**
- NPC knowledge +small (learns something about his history)
- Arousal tiny if SULTRY and she made something of it
- Game flag `MET_HIS_EX`
- Relationship flag based on how she handled it

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon (1 divisor) — requires partner

---

### 43. `minievent_solo_lostchild` — READY

**Premise:** In a large shop — John Lewis, a supermarket, somewhere with enough floor space for this to happen. A child, about four, standing still in the way children only stand when they've realised they've made a mistake.

**Choices:**
- Take the child to customer service
- Stay with the child and look for the parent
- Alert staff from where she is
- Crouch down and ask who they were with

**Trait branches:**
- `CUTE` — in front of the child immediately; exactly the right register; the parent finds them both crouched in an aisle
- `AMBITIOUS` — customer service; announcement; resolved in four minutes; she continues her shopping
- `SHY` — the specific anxiety of being a stranger with a child; does the right thing anyway; it costs more than it should
- `ROMANTIC` — feels the specific weight of this small person trusting her; is the right person for this moment

**Consequences:**
- `HEROES_REWARDED` stat
- Game flag `HELPED_LOST_CHILD`
- Stress -small (it resolved; she was useful)

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon (1 divisor)

---

### 44. `minievent_solo_exinperson` — READY

**Premise:** In person. Not a call, not a text — him, here, in front of her. At a shop, a pub, a corner she turns. No warning.

*Requires: ex-lover NPC exists with sex history*

**Choices:**
- Brief exchange and move on
- Stop and actually talk
- Pretend she didn't see him (requires not having made eye contact first)
- Invite him for a coffee

**Trait branches:**
- `ROMANTIC` — the shock of the actual face versus the mental version; has to recalibrate; takes a breath
- `BITCHY` — brief, controlled; exits cleanly; feels fine; it is fine
- `SHY` — the unexpected physicality of him; forgets what to do with her hands; manages it eventually
- `AMBITIOUS` — evaluates how she wants this to go; executes accordingly; no lingering

**Consequences:**
- NPC liking change based on interaction
- Game flag `UNEXPECTED_EX_ENCOUNTER`
- Arousal small if ROMANTIC and it went well
- Stress small regardless

**Content tags:** SEXUAL, TRANSFORMATION (the ex knew her before and after — or only after; if before, that changes everything about what this encounter means at low femininity)

**Rarity:** uncommon (1 divisor) — requires ex-lover NPC

---

### 45. `minievent_solo_latebarencounter` — READY

**Premise:** She stayed too late at the pub. Not drunk — just later than she intended. The bar has thinned to the kind of people who are still here at this hour. The light is doing something.

**NPC dispatch:** AVERAGE most likely; JERK or CHARMING possible.

**Choices:**
- Have one more and talk to him
- Get her coat and go
- Move to a different spot (closer or further)
- Order from the bar and let whatever happens, happen

**Trait branches:**
- `DOWN_TO_EARTH` — just someone at a bar; easy conversation; she goes home at a reasonable time
- `SULTRY` — late bar, low lights; is aware of what this situation is; decides what she wants from it
- `ROMANTIC` — gives it more weight than it deserves; knows she's doing this; has a drink anyway
- `AMBITIOUS` — has already decided she's leaving in twenty minutes; adjusts this if the conversation is worth it

**Consequences:**
- NPC introduced with personality
- Game flag `LATE_NIGHT_BAR_MEETING`
- Arousal small if SULTRY and she stayed
- NPC liking +small if conversation went somewhere

**Content tags:** SEXUAL — charged context; no explicit content in this scene. No BLOCK_ROUGH gating.

**Rarity:** uncommon

---

### 46. `minievent_solo_boredatevent` — READY

**Premise:** She agreed to something she no longer wants to be at. A party, a work event, a friend-of-a-friend situation. She knows no one. The event is continuing without her consent.

**Choices:**
- Commit to it (finds someone worth talking to)
- Find the food or bar and park there
- Text someone to invent an excuse
- Leave without explanation

**Trait branches:**
- `CUTE` — gives it a real chance; ends up in a conversation she didn't expect; leaves glad she stayed
- `POSH` — manages the room with practised efficiency; knows exactly how to be present without being consumed
- `SHY` — the buffet table is a good place to stand; she's there for twelve minutes
- `FLIRTY` — finds the most interesting person and goes to them; this is not a social difficulty for her

**Consequences:**
- Game flag `WENT_TO_SOLO_SOCIAL_EVENT`
- NPC introduced if she found someone
- Stress -small if she left early and was right to; -small also if she stayed and it worked

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 47. `minievent_work_performancereview` — READY

**Premise:** Her manager wants to discuss her progress. Official, scheduled, inevitable. What he says and how he says it are two different documents.

**Choices:**
- Accept the feedback and move on
- Push back on a specific point
- Ask directly about the pay or promotion she's been expecting
- Let him talk; say very little; file everything

**Trait branches:**
- `AMBITIOUS` — goes in with prepared points; comes out having moved something; the meeting was a tool
- `POSH` — the specific register of being assessed by someone; manages it correctly; feels nothing about it until later
- `SHY` — the one-to-one is its own difficulty; the feedback hits differently in this context; may not push back even when she's right
- `BITCHY` — if the feedback is wrong, she knows it; decides in the room whether to say so; decides yes

**Consequences:**
- Game flag `HAD_PERFORMANCE_REVIEW`
- Career stat change based on approach
- Flag `CHALLENGED_MANAGER_REVIEW` if she pushed back and was right

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon (work event)

---

### 48. `minievent_solo_photographedwithout` — READY

**Premise:** She notices someone has taken a photo of her. Without asking. They're already looking at the screen. She didn't consent to this and they didn't try to hide it.

**Choices:**
- Ask them to delete it (confrontation; various outcomes)
- Ignore it (knows she saw)
- Take out her own phone and photograph them back (BITCHY gate)
- Leave the situation

**Trait branches:**
- `BITCHY` — asks; the ask is very specific; they delete it; she checks
- `SULTRY` — if the photo was clearly meant to be flattering: decides how to receive this; handles it with control
- `SHY` — wants to say something; the moment passes; she's still annoyed about it twenty minutes later
- `POSH` — the gall of it; asks politely; it's not a polite ask

**Consequences:**
- Game flag `PHOTOGRAPHED_WITHOUT_CONSENT`
- Stress +small regardless (this is always uncomfortable)
- `ACTS_OF_EVIL` tiny if she ignored it (small moral cost to not acting)

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon

---

### 49. `minievent_solo_flatmatesituation` — READY

**Premise:** Something in her building that involves her flatmate or immediate neighbour, but not in the loud-argument way. More specific: they need something, they've done something, or something of hers was involved without her knowledge.

**Dispatch:**
- Flatmate ate her food (small, annoying, requires a response)
- A package came for her while she was out; neighbour has it; she has to knock for it
- Her flatmate has a friend staying she wasn't told about

**Choices vary by sub-scenario** — but always: address it, ignore it, escalate.

**Trait branches:**
- `BITCHY` — addresses it; every version; the address is precise and not disproportionate
- `DOWN_TO_EARTH` — the food thing is annoying but she deals with it; the package: she just knocks
- `SHY` — the knock on the neighbour's door is somehow the hardest part; the brief exchange costs something
- `POSH` — the flatmate's friend situation: deeply, specifically, a problem

**Consequences:**
- NPC introduced (neighbour or flatmate) with random personality
- Game flag per sub-scenario
- Relationship texture established — not friendship, just co-existence

**Content tags:** VANILLA — no gating required

**Rarity:** common

---

### 50. `minievent_chain_charityreturn` — READY

**Premise:** He's at the same spot. The clipboard man. He doesn't recognise her immediately. Then he does.

*Requires: `$gd.hasGameFlag("CHARITY_MUGGER_DONATED")` OR `$gd.hasGameFlag("CHARITY_MUGGER_RUDE")`*

**Dispatch based on flag:**
- If she donated: warm; grateful; pushes for a direct debit upgrade
- If she was rude: he's noticed; brief beat; both make a decision

**Choices (donated):**
- Chat briefly and leave
- Upgrade the donation (he wins)
- Politely decline the upgrade

**Choices (rude):**
- Acknowledge wordlessly and pass
- Acknowledge verbally (apologise or double down)
- Ignore it entirely — he does too

**Trait branches:**
- `ROMANTIC` — finds the reunion oddly specific; the specific-ness of the city
- `BITCHY` — remembers exactly what she said; decides what to do with that; it's consistent
- `AMBITIOUS` — his relentlessness is briefly admirable; she leaves efficiently

**Consequences:**
- Flag `CHARITY_MUGGER_SECOND_ENCOUNTER`
- `ACTS_OF_EVIL` if she doubled down

**Content tags:** VANILLA — no gating required

**Rarity:** uncommon (1 divisor) — requires flag precondition

---

---

### 51. `minievent_solo_mirrormoment` — READY

**Premise:** She catches herself in a mirror — a shop window, a bathroom mirror, a full-length one in a changing room. Nothing prompted it. She just happened to look.

**Choices:**
- Look properly (a moment with her reflection)
- Glance and keep moving
- Adjust something (hair, posture) and see what happens to the image

**Trait branches:**
- `SULTRY` — looks the way she looks at things; finds her own reflection interesting; notes what men see
- `POSH` — assesses; presentable; fine; moves on with the information
- `SHY` — the mirror catches her before she can avoid it; doesn't linger
- `ROMANTIC` — holds the look; feels something specific she couldn't put into words

**Transformation branches (FEMININITY < 50, male-start):**
There are still moments where the reflection takes her slightly by surprise. Not the face — she's used to the face. Something subtler. The way she's standing. The way the light catches her. She looks like someone. She looks like a woman.

**Transformation branches (FEMININITY ≥ 75, male-start):**
She's had this reflection for long enough that it has stopped being notable. She adjusts her hair. Moves on.

**Consequences:**
- Arousal tiny if SULTRY
- Game flag `LOOKED_IN_MIRROR` (first time triggers longer text on repeat)

**Content tags:** VANILLA, TRANSFORMATION

**Rarity:** common

---

### 52. `minievent_solo_catcall_received` — READY

**Premise:** Two men, or one, from the other side of the street or a passing van or a doorway. Words directed at her that she didn't ask for. It's not dangerous. It is impossible to pretend it's neutral.

**Choices:**
- Keep walking (the default; the thing most women do)
- Look over briefly (acknowledgement without engagement)
- Say something back (varies heavily by trait)
- Let the anger arrive and decide what to do with it

**Trait branches:**
- `SULTRY` — files it; this is one register of the same attention she finds useful elsewhere; walks on
- `BITCHY` — says something; brief; he wasn't expecting that; he should have been
- `SHY` — keeps walking; the second-hand embarrassment is its own weight; thinks about it later
- `REFINED` — the specific vulgarity of it; the way it lands in a public space; she is still angry two streets later

**Transformation branches (FEMININITY < 50, male-start):**
The thing is: she knows exactly what they're doing. She used to be the kind of man who would never have done that, but she was at parties with men who did. She knows what's behind it. And knowing what's behind it doesn't make it feel any smaller. If anything it's worse.

**Transformation branches (FEMININITY ≥ 75, male-start):**
She's been here before. Many times. The specific tiredness of it is something she knows now in the way she knows other things about being a woman.

**Consequences:**
- Game flag `RECEIVED_CATCALL`
- Stress +small
- `ACTS_OF_EVIL` tiny if she said nothing (the moral weight of witnesses who kept walking)

**Content tags:** VANILLA, TRANSFORMATION

**Rarity:** common

---

### 53. `minievent_solo_firstattraction` — READY

**Premise:** She notices a man — specifically, in a way that lands in her body before she's thought about it. Not aesthetically. Actually. This is either entirely familiar by now or it still costs her something to admit.

*Most powerful at low FEMININITY — the specific surprise of desire from this side. At high FEMININITY, this is simply desire. Both are valid.*

**NPC dispatch:** Man at a café, on the street, in a queue. Weighted average — he's not remarkable, which makes the response more honest.

**Choices:**
- Keep moving; ignore what she noticed
- Let herself look (deliberate)
- Do something about it (talk to him — brave at any femininity)
- Try to analyse why (OVERACTIVE_IMAGINATION or low-femininity branching)

**Trait branches:**
- `FLIRTY` — the noticing is just the beginning of a decision she's already made
- `ROMANTIC` — gives the noticing more meaning than it probably has; knows she's doing this
- `AMBITIOUS` — irrelevant; she has somewhere to be; files him and continues
- `SHY` — noticed, said nothing, the noticing follows her

**Transformation branches (FEMININITY < 30, male-start):**
This still feels new in a way she doesn't fully know what to do with. Not wrong — she stopped thinking of it as wrong a while ago — but new. Men looked at women that way. She used to look at women that way. And now someone is going to look at her that way if she gives him the chance.

**Transformation branches (FEMININITY 30–74, male-start):**
She's past the part where noticing a man surprises her. She's not past the part where it's interesting.

**Consequences:**
- Arousal small if she let herself look
- NPC introduced with personality if she spoke to him
- Game flag `NOTICED_MAN_ATTRACTED` (first occurrence)

**Content tags:** SEXUAL, TRANSFORMATION

**Rarity:** common

---

### 54. `minievent_solo_malesolidarity_excluded` — READY

**Premise:** A conversation she's not part of. Men talking with each other — colleagues, strangers at a bar, someone on the street — in the specific register of men talking to men. She used to be in those conversations. She isn't now.

**Dispatch:**
- Work context: colleagues dismiss her contribution, continue the discussion between themselves
- Social: a man turns to another man to validate a point she'd already made
- Street: two men with that specific ease of public male space; she has to navigate around them

**Choices:**
- Let it go
- Insert herself (AMBITIOUS or BITCHY gate)
- Note it and file it
- Feel the specific thing she feels and decide what to do with that

**Trait branches:**
- `AMBITIOUS` — inserts herself; makes the point she was making; they hear it differently from her than they would have from a man; she notices this too
- `BITCHY` — sharp; specific; he remembers it
- `REFINED` — the social wrongness of the moment; the specific invisibility; manages it with composure; is furious later
- `DOWN_TO_EARTH` — this is just how it is sometimes; picks her battles; this isn't one

**Transformation branches (FEMININITY < 50, male-start):**
She used to be in those conversations. She was probably exactly like that — not cruelly, just not noticing. The specific thing about being on this side of it is that she knows it isn't malice. It's just a room she used to be in.

**Transformation branches (FEMININITY ≥ 75, male-start):**
She's been invisible in rooms like this before. She's learned which rooms are worth the effort and which aren't.

**Consequences:**
- Game flag `EXCLUDED_FROM_MALE_SPACE`
- Stress +small
- If she inserted herself: NPC liking change; career flag if work context

**Content tags:** VANILLA, TRANSFORMATION

**Rarity:** uncommon

---

### 55. `minievent_solo_femalesolidarity` — READY

**Premise:** A moment of female solidarity she's included in. Something small and specific: a look shared with a stranger when a man does something predictable. A woman she doesn't know who helps with something she didn't ask for. Being included in a "we" that she wasn't always part of.

**Dispatch:**
- Shared look with stranger about male behaviour (no words; just acknowledgement)
- Woman warns her about something ahead (wet floor, wrong platform, something more)
- Being asked "are you alright?" by a female stranger who noticed something

**Choices:**
- Accept the solidarity fully
- Reciprocate briefly
- Feel uncertain what to do with it

**Trait branches:**
- `ROMANTIC` — feels the weight of being included; specifically the shared-look version; it means something to her
- `POSH` — the unsolicited intimacy of a stranger's solidarity; manages it correctly; grateful in a contained way
- `SHY` — the woman meant to be helpful; it lands; she doesn't know how to say that
- `CUTE` — the best person to receive this kind of small kindness; she says thank you in a way that means it

**Transformation branches (FEMININITY < 50, male-start):**
She wasn't in this before. Not this specific thing — the woman-to-woman check that happens without negotiation. She used to be on the outside of it and not know it.

**Transformation branches (FEMININITY ≥ 75, male-start):**
She's used to this. It's one of the things she didn't expect to be real and turned out to be.

**Consequences:**
- Stress -small (this restores something)
- Game flag `MOMENT_FEMALE_SOLIDARITY`

**Content tags:** VANILLA, TRANSFORMATION

**Rarity:** uncommon

---

### 56. `minievent_solo_bodyawareness` — READY

**Premise:** A moment of unexpected physical awareness. Not arousal — more specific than that. The specific weight of her body doing something she didn't grow up doing.

**Dispatch:**
- Running to catch a bus (the specific experience of running in this body)
- Lifting something heavy (differently limited than she used to be)
- The cold (her body registers it differently than she was used to)
- A sudden noise that makes her flinch (a physical startle response that surprises her)

**Trait branches:**
- `DOWN_TO_EARTH` — notices; adjusts; continues; bodies are just bodies
- `AMBITIOUS` — files it as data; notes the limitation or difference; problem-solves around it
- `REFINED` — the specific physical experience as information about who she is now
- `OVERACTIVE_IMAGINATION` — takes the body moment and extrapolates it further than she needs to

**Transformation branches (FEMININITY < 50, male-start):**
She's mostly used to the body now. Mostly. There are still moments where it surprises her with something — not the obvious things any more, but the small ones. The way cold feels. The way she braces.

**Transformation branches (FEMININITY ≥ 75, male-start):**
The body is just the body. She stopped treating it as foreign a long time ago. The bus catches her slightly off guard but that's about fitness, not anything else.

**Consequences:**
- Game flag `BODY_AWARENESS_MOMENT`
- No lasting consequence — this is a texture scene

**Content tags:** VANILLA, TRANSFORMATION

**Rarity:** uncommon

---

## Style Notes for This Session's Writing

- **Adult content:** This is an adult game. Sexual content should be genuinely erotic, not mechanically explicit. Desire should be complicated by who the PC is. See `.claude/rules/writing-style.md` — adult content section.
- **Hot means specific:** The most arousing content in this game is not the most explicit — it's the most specific. What she wants in what way, complicated by who she is and who he is.
- **The world being alive IS the kink:** Unpredictability, loss of control, things happening to her rather than because of her — this is the game's core erotic logic. Lean into it.

---

## Last Worked On
Session 2 (setup complete) — no scenes written yet. System fully built.
- Agent Teams enabled (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json)
- `scene-generator` agent created — handles one scene end-to-end autonomously
- `/continue` skill redesigned for parallel batch execution (5 scenes at a time)
- 50 complete scene briefs in backlog (items 1-50)
- Content filtering system documented across all workflow files
- Transformation fantasy fully integrated: API in velocity-syntax.md, writing guide in writing-style.md, design guidance in scene-design.md, prose-writer agent updated, 6 transformation-specific scenes added (51–56), 8 existing briefs tagged TRANSFORMATION

Next: Run `/continue` — it will take the first 5 READY scenes, spawn parallel agents, generate them simultaneously, update this file, and continue batching until the backlog is empty.
