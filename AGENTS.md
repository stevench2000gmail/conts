# conts/ Workspace Guide (mandatory for every agent session)

## Rule 1 — 8+ word sentences (MANDATORY)
Every bestiary sketch sentence MUST contain at least 8 words. No fillers. Check every sentence before sending. If the user flags a violation, fix the flagged entries immediately with full rewrites, then continue.

## Rule 2 — Never rely on chat history
Chat transcripts are volatile and machine-local. Anything approved in chat (pitches, IDs, stats, renames, decisions) MUST be written to physical files in this workspace before the turn ends. Approved = saved to file, or it did not happen.

## Rule 3 — Save state means save work, then check in
When the user says “save state”, do ALL of these in order:
1. Update `V02_bestiary_001_planning_state.md` (decisions, locks, renames, progress counters).
2. Write/refresh the work-progress files: `V02_bestiary_001_roster_draft.md` (structure/IDs) + `drafts/` full prose files (family by family, exact approved text).
3. `git add` + `git commit` + `git push` in conts/ so another machine can resume with zero chat context.
4. Report the commit hash + what was saved + what remains.

## Standing conventions (do not violate without explicit user override)
- Phase 1 only: chat pitches, no JSON. No full-monster pitches while Status is PLANNING.
- City-free prose: no specific city proper nouns; generic settlements + generic terrains only (relocatable). Phase 2 habitat IDs terrain-only unless approved otherwise.
- Generic reusable display names, no proper nouns — except Demon-only proper-name exception (36 Fallen + 72 Solomonic, inspiration-only, never canon import).
- Variants: Human/Humanoid/Beast/Fiend = 4 flavour variants (2M/2F where biologically applicable, fallback with stated reason); Demon = 0 variants + “No variants apply” line.
- Every monster fights: reuse ENY_* or 1-10 stats with always_physical/cycle only. Magic stays 1 for Human/Humanoid/Beast unless flagged proposal.
- Canon hard limits: existing terrains/cities only, no new named places/factions/institutions/magic rules. Fiend/Demon origins + magic implications TBD/flagged, never final.
- On resume (`resume from where we left off`): re-read this guide + planning state + controlling request at `../proj4/studio/contentstudio/requests/CONTENT_V02_BESTIARY_001.md` before doing anything.
