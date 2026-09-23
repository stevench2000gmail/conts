# V02_BESTIARY_001 Planning State — 2026-09-22

## Controlling request
`studio/contentstudio/requests/CONTENT_V02_BESTIARY_001.md` (Phase 1 only: chat pitches, no JSON).
Status: PLANNING — do NOT pitch full monsters until user says: `we conclude the full preview of all monsters planning`.

## Approved ENY_* to carry (10)
- Human: ENY_ROADSIDE_THUG, ENY_HIRED_BLADE
- Humanoid: ENY_FERAL_GOBLIN, ENY_FERAL_ORC, ENY_OGRE
- Beast: ENY_WILD_WOLF, ENY_GIANT_SPIDER, ENY_GRIFFIN
- Fiend: ENY_SHAMBLING_CORPSE, ENY_DEVOURING_BLOOM
- Demon: none yet (5th category canonized 2026-09-22, nature/hierarchy TBD via proposal)

## Global decisions so far
- Lawful soldiery allowed as fightable Human enemies (generic, faction-neutral, no new institutions; paladin holy-magic never final, flagged).
- Flavour variants: 2 male / 2 female WHERE biologically applicable; fallback with reason otherwise (e.g. feral goblins = no females per WORLD_BIBLE; some Beasts/Fiends subtle or nonsensical).
- Canon hard limits kept: existing terrains/cities only for habitat (6 terrains: volcanic_foothills, forested_lake, green_valley, high_plateau, wetland, river_delta; 6 cities; location views graveyard/deep_forest/cave presentation-only). No new named places/factions/institutions/magic rules. Mundane-first. Fiend/Demon origins + magic implications TBD/flagged. All monsters fight (reuse or 1-10 + always_physical/cycle).

## Human — target 60 entries, ~4-5 each across 13 families
1. criminals
2. gangsters
3. thugs (reuse ENY_ROADSIDE_THUG here where fitting)
4. rebels
5. mercenaries
6. hired swords (reuse ENY_HIRED_BLADE here where fitting)
7. assassins (flagged: implies guild, generic only)
8. ninjas (flagged: implies clan/culture, generic only)
9. militia
10. soldiers
11. knights
12. paladins (flagged: holy order + magic, fighters only, no final magic)
13. royal guards (flagged: implies court, generic only)
- Even split approx; no ENY IDs / prose / stats pitched yet.

## Humanoid pool (planning only, no pitches)
Core: gnomes, halflings, dwarves (flagged), goblins, hobgoblins, orcs, ogres, trolls, elves / dark elves / wood elves (flagged), treemen (generic for ents), ratfolk (generic for skaven), snakefolk (generic for naga), fish-maidens female-only, bird-maidens female-only, half-bird-half-fish maidens female-only, oni-horned brutes, kappa river imps, monkey-folk, fox-maidens female-only, rakshasa / yaksha / garuda / naga Indian-aligned set, kobolds (small scavengers, separate from lizardmen), gnolls (hyena-men), goat-horned wildmen, boar-headed brutes, lizard marsh stalkers (separate), faun/satyr raiders, harpy harriers, hag-like outcasts, leshy.
Added this turn: vodyanoy, rusalka female-only, jotnar, duergar as dark-dwarf alias (flagged), fomorian, selkie, sidhe (flagged elf-adjacent), minotaur, centaur, cyclops, lamia female-leaning, div, scorpion-folk, jackal-headed dune stalkers, falcon-headed cliff watchers, croc-folk river brutes, thunderbird cliff folk.
Moved OUT: vampires -> Fiend; gorgon -> Fiend; wendigo -> Fiend; tengu -> Demon candidate; half-breeds dropped.
Open: Humanoid target count — user set 2026-09-22: high-count (4-5 entries each) = 27 families: 1-11, 13, 14, 18-27, 30-32, 43. Low-count (1-2 each) = remaining 24 families. Est ~120-135 high + ~24-48 low = ~145-180 Humanoids. Treemen (12) intentionally low-count.

## Fiend pool — LOCKED 2026-09-23 v2 CLASSIC (planning only, no pitches; 72 families by source)
Model 4/4/4/8/8/4/4/4/4/6/6/4/4/4/4 = 72. Classic iconic TYPE-names. Same-root merged, coincidence parenthesized. Beast #80 fixed: ammit-maws → hippo-pond brutes (mundane delta/wetland). Full list approved in chat 2026-09-23.

## Demon pool so far (moved, not pitched)
- Structure requested: 108 unique Demon types: 36 Fallen Host (fallen-angel visual register, origin/theology proposal-only) + 72 Solomonic demons.
- Tengu candidate remains in Demon pool.
- Demon art exception is now present in controlling request: 0 variants, 4 states, 1 full-body, 1 portrait = 6 images each (648 total for 108).
- IMPORTANT RESUME REMINDER: ask OpenCode to resolve the remaining naming conflict in the controlling request. Lines 16 and 76 still require generic reusable names / no proper nouns, but user wants the 72 actual Solomonic demon names. Add a Demon-only naming exception permitting traditional individual names, while explicitly not importing real-world hierarchy, abilities, religious claims, or biographies as canon; all non-Demons retain generic reusable names.

## Beast — agreed 2026-09-22 (lean 1-2 per family, no pitches yet)
Kept: all 6-terrain mundane families + mythical-but-mundane + east/south moon bear, giant cobra, peacock-raptor. Dropped: tiger-man-eater, kappa-turtle beast, temple monkey-troop, all supernatural-flagged.
New-terrain expansion requested (Option B) — pending OpenCode/MECH + art; bestiary pitches stay on existing 6 terrains + 6 cities until approved.

## OpenCode prompt (user-requested, not yet sent)
Please amend canon to allow future standalone non-human factions (e.g. elf, dwarf): Update WORLD_BIBLE.md World Rules + DECISIONS.md: replace `No standalone non-human faction is approved for Version 0.1` with rule permitting future non-human factions only via explicit human-approved proposal, no auto-creation. Keep goblins-no-females, CHR_008 hybrid, feral-vs-Mossgate distinction, CHR_003/CHR_004 culture TBD. Keep bestiary Humanoids as outside-settled-society bands until faction approved; faction societies as canon_change proposals, never final. Validate + tests green.

## Beast — draft 2026-09-23 v3 (planning only, no pitches; user-ordered 15/10/15/20/30 = 90 families)
User model expanded v3: Invertebrates 15 / Reptiles 10 / Birds 15 / Mammals 20 / Mythical 30 (broader mythical-but-mundane, no supernatural abilities). Lean 1-2 each = ~90-180 Beasts. Full draft pitched in chat 2026-09-23 v2, awaiting trim/approval. Carried ENY_WILD_WOLF / GIANT_SPIDER / GRIFFIN placed. Moon bear / giant cobra / peacock-raptor kept. Tiger-man-eater / kappa-turtle / temple monkey-troop stay dropped.
Dedup vs Humanoid (2026-09-23): REMOVED from Beast: nine-tail foxes (keep fox-maidens Humanoid), thunderbird fledglings (keep thunderbird cliff folk Humanoid), garuda-kites (keep garuda Indian set Humanoid, replaced by roc-rulers). KEPT with distinction note (animal vs intelligent band): giant scorpions vs scorpion-folk, marsh crocs/sobek vs croc-folk, tusk-boars/taotie vs boar-headed brutes, rams/stags/horses vs faun/satyr/centaur/goat-horned, cinder foxes vs fox-maidens, jackals/hyenas vs gnolls/jackal-headed,-confirmed animal-only, no society.
Cross-check 2026-09-23 v3 vs all other classes (90 families saved):
- Human (13 fams): no overlap — all Beasts non-human animals.
- Humanoid (~51 fams): 3 removed above. Rest kept as animal-only with no society/culture: snap-turtles explicitly non-kappa (vs kappa river imps); salamanders/skinks/frill-necks vs lizard marsh stalkers/kobolds (animal vs band); cobras/constrictors/pit-vipers/hydra-litters vs snakefolk/naga/lamia (animal vs folk); jackals/laugh-hounds vs gnolls/jackal-headed; all 15 birds vs bird-maidens/harpy/falcon-headed (non-sentient vs folk); mustangs/pegasus-colts/8-legged coursers vs centaur; rams/stags/yale/ceryne vs faun/satyr/goat-horned/minotaur; otters/beavers vs selkie/vodyanoy (animal vs folk); ember-mice vs ratfolk (mouse vs rat); moles/martens/badgers/lynxes vs none; no monkey beasts (vs monkey-folk safe); no spider-folk (spiders safe); no bat-folk (bats safe); no plant beasts (vs treemen/leshy safe); no oni beasts (vs oni-horned safe).
- Fiend (vampires/gorgon/wendigo/corpse/bloom): cave bats vs vampires noted (animal vs unnatural); crest-cocks/carrion-beetles vs corpse (animal vs reanimated); no bloom-plant beasts; gorgon (serpent-hair fiend) vs snake beasts noted (fiend vs animal).
- Demon (108 Fallen+Goetic + tengu candidate): Beast mythicals use generic epithets only, no proper nouns — no collision with 36 Fallen proper names (Lucifer..Bushyasta) or 72 Goetic names (Bael..Andromalius). Sobek-crocs/ammit-maws/sphinx-pards are Egyptian-shape animals only, non-divine, distinct from Ra/Thoth/Set/Sekhmet/Anubis Fallen. Tengu stays Demon-only — no tengu-crow beasts. Oni stays Humanoid-only per cosmology §10 exclusion. Roc/anzu/makara/taotie/kirin etc. have no 36/72 counterpart.
- Internal Beast: delta wyrms (Reptile river) vs lindworm drakes (Mythical highland) split by habitat/scale; river-crabs vs mud-lobsters split (shore vs burrow); web-spiders vs millipedes/centipedes split; canine chain split (wolves highland/forest, fen-hounds wetland, mastiffs cities, foxes volcanic, jackals delta); raptor chain split by terrain.

## Decisions 2026-09-23
- OpenCode Demon fix VERIFIED 2026-09-23: CONTENT_V02_BESTIARY_001.md Line 16 + Line 77 Demon-only exception present, upload item 14 cosmology added, external prompt demon sentence present. WORLD_BIBLE:20 + DECISIONS:212 faction permission confirmed verbatim. `python3 tools/content_staging.py validate` = empty queue green. Commit 4dc83d4.
- Fiend 72-family draft v1 SAVED (4/4/4/8/8/4/4/4/4/6/6/4/4/4/4), awaiting classic-name revision per user 2026-09-23 (user dislikes renamed epithets, wants classic/iconic names).
- Fiend naming DECISION 2026-09-23: use classic iconic TYPE-names (common nouns: Vampire, Gorgon, Wendigo, Jiangshi, Draugr, Vetala, Yurei, Banshee...), no proper individuals (no Dracula/Talos-as-individual/Bael). Complies with generic/reusable rule; Demon-only proper-name exception unchanged. Conflict pinpoint list pitched in chat, fixes pending approval.
- Order confirmed: refine Beast list next, then Fiend, then Demon. Human/Humanoid rough mapping done.
- Humanoid model CONFIRMED: 27 high-count (4-5 each) + 24 low-count (1-2 each), ~145-180 total. Treemen (12) stays low-count.
- Demon cosmology: 108 unique fallen angels, real in-setting. Reference `tmp/the_hundred_and_eight_bestiary_cosmology_v0.1.md` as study material / lost in-game lore only — not canon import. Open questions §16 stay open.
- OpenCode request file created: `/mnt/c/Users/steve/opencode/proj4/tmp/contentStudioRequestMonster.md` (Task 1 Demon naming exception still open; Task 2 faction rule verify-only — WORLD_BIBLE:20 + DECISIONS:212 already permit future factions via proposal).

## Workspace memory (saved 2026-09-23 — persist across chats)
- Controlling request: `/mnt/c/Users/steve/opencode/proj4/studio/contentstudio/requests/CONTENT_V02_BESTIARY_001.md`
  (relative from conts: `../proj4/studio/contentstudio/requests/CONTENT_V02_BESTIARY_001.md`)
- All files it references live under: `/mnt/c/Users/steve/opencode/proj4/` (relative: `../proj4/`)
- On resume: re-read this state file + the controlling request above. Do NOT assume conts/ has canon files.

## How to resume
Say: `resume from where we left off` — I will re-read this file (+ CONTENT_V02_BESTIARY_001.md as controlling) and continue from pending topics.
