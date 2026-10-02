# Save state — `CONTENT_V02_SHEN_CHAIN_001` (Shen rescue chain) — 2026-10-02

## Status: DONE (content promoted, validators green)

Request file: `studio/contentstudio/requests/CONTENT_V02_SHEN_CHAIN_001.md` (proposed).

## What was delivered

1. **Phase 1 pitches** (chat + file): 5 character events (300+ words each), joining prose
   "What Seals Hold" (title confirmed, `scene_text` 2389 chars, in 1900–2500 band),
   Orobas stats confirmed (6/6/6/4, `always_physical`, boss).
   Working copy: `fantagame/tmp/CONTENT_V02_SHEN_CHAIN_001_phase1.md`.
2. **Pre-battle party + ration fix** (user-reported gap: shrine battle opened solo at
   default rations): spec written to `fantagame/tmp/SHEN_CHAIN_PREBATTLE_PARTY_RATION_FIX.md`.
   User confirms the fix is implemented — no longer a concern.
3. **Phase 2 bundle**: `fantagame/content_staging/submissions/V02_shen_chain_001.json`
   (`STG_V02_SHEN_CHAIN_001`: 5 `event` + 1 `combat_enemy` + 1 `character_background`
   joining note `BKG_CHR013_001`). Staging validation passed at delivery.

## Promotion verified (read-only check this session)

- `fantagame/data/events/EVT_SHEN_{MISSING,RUMOR,BODIES,SHRINE,RESCUED}_001.json` live,
  all 5 IDs plus `BKG_CHR013_001` in `data/content_registry.json content_ids`.
- `ENY_OROBAS` ("Orobas of the True Oath", Demon boss) live in `data/enemies.json`
  (no `content_ids` entry — matches the `ENY_*` precedent, no registry entry needed).
- `fantagame/data/characters/CHR_013.json` carries `joining` (method `event`, one-line
  `detail`, `scene_title` "What Seals Hold", full `scene_text`).
- Bundle archived at `fantagame/content_staging/approved/V02_shen_chain_001.json`;
  `submissions/` empty.
- `python tools/runtime_data.py validate` → passed.

## Notes / follow-ups (non-blocking)

- Chain driver stays dormant until Veylorn falls (mechanics-gated, content now resolves).
- Art turn `ART_SHEN_CHAIN_01..05` is separate; events use category-backdrop fallback until then.
- `fantagame/tmp/` working files may be cleaned at will:
  `CONTENT_V02_SHEN_CHAIN_001_phase1.md`, `SHEN_CHAIN_PREBATTLE_PARTY_RATION_FIX.md`.
  Do not touch `fantagame/tmp/upload/` staging.
