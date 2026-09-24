# V02 Bestiary Roster Draft — Phase 1 backup (2026-09-23)
Purpose: preserve planning/pitching progress for OpenCode Phase 2 JSON later. Full standalone prose and appearance briefs are saved family-by-family in `drafts/`. This file locks structure, IDs, and rules so nothing is lost.
Prose rule: NO city proper nouns (generic settlements + generic terrains only, relocatable). Every sketch sentence 8+ words, no filler.

## HUMAN — LOCKED 65 (13x5, vs 60 target)
1 criminals: ENY_CUTPURSE, ENY_BURGLAR, ENY_SMUGGLER, ENY_COUNTERFEITER, ENY_FENCE
2 gangsters: ENY_GANG_LOOKOUT, ENY_GANG_ENFORCER, ENY_LOAN_SHARK, ENY_PIT_BOSS, ENY_SMUGGLER_BOSS
3 thugs: ENY_ROADSIDE_THUG (reuse), ENY_TOLL_BRUTE, ENY_ALLEY_MUGGER, ENY_CARAVAN_RAIDER, ENY_DOOR_BOUNCER
4 rebels: ENY_BREAD_RIOTER, ENY_DESERTER_CAPTAIN, ENY_HEDGE_PREACHER (magic 2 flagged folk cycle), ENY_TOLL_BREAKER, ENY_STUDENT_AGITATOR
5 mercenaries: ENY_FREE_SPEAR, ENY_COIN_BOW, ENY_CAMPFOLLOWER_BLADE, ENY_SIEGE_HAND, ENY_WAR_DOG_HANDLER
6 hired swords: ENY_HIRED_BLADE (reuse), ENY_DUELING_TUTOR, ENY_BODYGUARD, ENY_ROAD_WARDEN, ENY_RETIREDSERGEANT
7 assassins (generic-only): ENY_KNIFE_ASSASSIN, ENY_GARROTE, ENY_POISONER (cycle), ENY_CROSSBOW_KILLER, ENY_BATHHOUSE_BLADE
8 ninjas (Japanese roles): ENY_SHINOBI (M-only), ENY_KUNOICHI (F-only, cycle), ENY_GENIN (young low), ENY_CHUNIN (older high), ENY_TEPPO_SHINOBI (matchlock, flagged tech)
9 militia: ENY_VILLAGE_MILITIA, ENY_TOWN_WATCHMAN, ENY_HEDGE_WARDEN, ENY_FIRE_BRIGADE, ENY_RIVER_PATROL
10 soldiers: ENY_LINE_INFANTRY, ENY_CROSSBOWMAN, ENY_SCOUT_RIDER, ENY_SAPPER, ENY_STANDARD_BEARER
11 knights: ENY_HEDGE_KNIGHT, ENY_HOUSEHOLD_KNIGHT, ENY_SQUIRE (replaced Lance Leader), ENY_FOOT_KNIGHT, ENY_TOURNEY_CHAMPION
12 paladins (fighters + flagged holy cycle per magic doctrine): ENY_OATHSWORD (3), ENY_CHAPEL_GUARD (3), ENY_MENDICANT_PROTECTOR (2), ENY_RELIC_WARDEN (4), ENY_PENITENT_BLADE (3)
13 royal guards (generic-only): ENY_PALACE_SENTRY, ENY_ESCORT_LANCER, ENY_VAULT_WARDEN, ENY_HONOR_BLADE, ENY_NIGHT_WATCH_CAPTAIN
All Human: magic 1 except Paladin 5 + Hedge Preacher flagged cycle (magic doctrine); Poisoner/Kunoichi cycle mundane tricks magic 1.

## HUMANOID — LOCKED 2026-09-23, 46 families / 170 entries (#1-170, user-approved; Phase 2 JSON pending)
Magic revisit DONE: cast 13 (elves 5/3, sidhe 2/4, div 2/5, hags 2/3, duergar 2/2, cycle flagged) + behavior 27 (sphinxes 5, fox-maidens 5, rusalka 5, treemen/leshy/naga/lamia/sirens/thunderbird 2 each; magic 1 cycle never-cast flagged); other 130 magic 1.
Full prose persistence complete: all former condensed sketches were expanded into standalone eight-sentence descriptions on 2026-09-23. Dark Elf is `ENY_ELF_DARK`; Wood Elf is `ENY_ELF_WOOD`.
High (5 each): gnomes, halflings, dwarves*, goblins*(M-only, reuse FERAL_GOBLIN), hobgoblins, orcs (reuse FERAL_ORC), ogres (reuse OGRE), trolls, elves*, ratfolk, mermaids*(F-only, ex fish-maidens), sphinxes*(F-only, ex bird-maidens), monkey-folk, fox-maidens*(F-only), indian trio (Rakshasa/Yaksha/Garuda), kobolds, gnolls, aegipanes, boar-headed, lizard stalkers, satyrs, harpy harriers (F-led), vodyanoy (M-led), rusalka (F-only), jotnar, jackal-headed.
Low (2 each): treemen (low by design), naga (ex snakefolk), sirens*(F-only, ex half-bird-half-fish), oni, kappa, duergar*, fomorian, selkie, sidhe*, minotaur, centaur, cyclops, lamia (F-leaning), div, scorpion-folk, falcon-headed, croc-folk, thunderbird folk.
* flagged (culture/courts/magic never final; bands only, no settlements/leaders/factions).
Beast folk-vs-animal notes kept: scorpions, crocs, boars, foxes, jackals, spiders, sphinx-pards, ammit (Beast #80 → hippo-pond brutes).

## BEAST — LOCKED 2026-09-23, 90 families / 180 entries (#1-180 Beast, user-approved batch-by-batch; Phase 2 JSON pending)
Inverts 15 / Reptiles 10 / Birds 15 / Mammals 20 / Mythical-but-mundane 30. Carry WOLF/SPIDER/GRIFFIN. Moon bear, cobra, peacock-raptor kept.

## FIEND — 80 families / 160 entries (77 locked 2026-09-23 + F78 Succubi 155-156 + F79-F80 Elementals 159-162 added 2026-09-24; Phase 2 JSON pending)
Frieren/Mimic→JRPG, WHF, LotR + Lake-lurker (Watcher), JRPG (Malboro=BLOOM, Zombie=CORPSE), Chinese, Norse, Greek (Gorgon), J/C (Watcher), Persian (Edimmu replaces Ghul), Indian, Japanese, Celtic, Slavic (Vampire), NativeAm (Wendigo), Egyptian (Ammit). Same-root merged; coincidence parenthesized.

## DEMON — LOCKED 2026-09-23, 108/108 (Fallen 36 per THIRTY_SIX_FALLEN_NINE_ORDERS_V04.md lore + Goetic 72 Bael→Andromalius with #65 Astaroth-Ishtar merged; gender-age presentations; 0 variants; Phase 2 JSON pending)
Fallen 36 per THIRTY_SIX_FALLEN_NINE_ORDERS_V04.md (virtue-unrestrained corruption; counts Norse 6, Chinese 5, J/C 6, Indian 5, Egyptian 3, Celtic 3, Japanese 3, Mesopotamian 2, Iranian 1, Greek 2; validation items 1-6 pending) + 72 Goetic Bael→Andromalius (#37-108) with #65 Astaroth (Ishtar/Inanna/Astarte/Ashtart merged). Tengu placement TBD; Oni stays Humanoid.
