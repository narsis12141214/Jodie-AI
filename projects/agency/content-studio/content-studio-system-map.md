# Content Studio — System Map
Reconstructed: 22 August 2026, from the two n8n workflow JSONs Hadi shared (built ~6 May 2026, pre-dating the lost chat windows — which is why no record existed in the repo).
n8n instance: n8n.srv1466538.hstgr.cloud · Workflows tagged `content-studio`

## What the system is

An AI food-photography studio for restaurant tenants. A tenant uploads plain phone photos of their dishes; the system understands the dish, understands the tenant's venue and styling language from reference photos, and generates a set of editorial-grade marketing shots ("the bake-off") — the same dish rendered as magazine-style variants, styled to look like it was shot in THEIR restaurant. Outputs land in Drive + Supabase, batched for client review.

Commercially: this is the engine behind the content-creation service line (Chic £400/mo, LaMure-type deals, Elan roadmap item, any restaurant client).

## Workflow 1 — Reference Ingestion v1 (`3Yta1IOl0gDt8g1J`, active)

Teaches the system what a tenant's restaurant looks like.

1. **Two Drive folder watchers** (poll every minute):
   - Folder `1UI6wG...` → tagged `interior` (photos of the restaurant space)
   - Folder `12OLop...` → tagged `style` (food-styling reference shots)
2. File is made public → `lh3.googleusercontent.com/d/{id}` URL built
3. **GPT-4o Vision analyses the reference** with a category-specific schema:
   - Interior → summary, palette, lighting, materials, mood, composition_cues
   - Style → summary, plating_style, surface, props, garnish, lighting_on_food, mood
4. Metadata merged into Supabase `content_studio_config.config.references.interior[]` / `.style[]` (deduped by URL, newest-first wins at generation time)

**Hardcoded:** tenant = Rendezvous (`tenant_slug: rendezvous`, fixed tenant_id) in both Tag nodes. Any new tenant needs those Set nodes updated or (better) per-tenant folders.

## Workflow 2 — Generation v2 "Bake-off" (`eZE9eMIQ5Sl6ZFMf`, active)

1. **Form trigger** (`/form/b63bdac5-...`): Tenant Email + dish photo upload(s)
2. Tenant looked up by email in Supabase `tenants`; tenant config (with references) loaded
3. Batch row created in `content_batches` (status `processing`, `review_token` generated — implies a client-facing review surface keyed by token)
4. Per source photo: upload to Drive (folder `1ttGQl...`), share public, lh3 URL
5. **Vision Pass** (GPT-4o as "food stylist"): dish_name, components, distinctive_features, plating, vessel → `content_batch_items` row
6. **Fan-out to 8 named variants**, then an **If gate keeps only 4 active**: `hero_moody`, `pullback_table`, `insitu_interior`, `human_element` (the four reference-driven ones). `hero_bright`, `topdown_minimal`, `detail_macro`, `topdown_props` are currently switched off at the gate.
7. **Build Prompt v3.4** — the heart of the system. Per variant, composes a long editorial photography prompt from the dish object + tenant references:
   - Interior-driven overrides (insitu_interior, human_element, pullback_table) inject a REFERENCE SCENE block from the newest interior ref
   - Style-driven overrides (hero_moody, topdown_props) inject a REFERENCE STYLING block from the newest style ref
   - Hard "DISH IDENTITY" language everywhere: references drive scene/style only, never substitute the food
   - **v3.4 patch:** tabletop-material isolation — regex-splits the table surface out of the Vision `materials` array so chair-frame/floor wood stops being rendered as the tabletop
   - Falls back to static v4.1 prompts when no references exist (cold-start safety)
8. **Replicate** `google/nano-banana-pro` — prompt + image_inputs = [source dish, up to 2 relevant refs]. Custom code-node polling, 4-minute ceiling
9. Output downloaded → Drive (folder `1mgjuv...`) → shared → aggregated into `shot_set` jsonb on the item row (status `ready`) → batch flipped to `awaiting_review`

## Dependencies (all must be alive for a test)

- n8n env: `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`, `OPENAI_API_KEY` (raw header in Generation), `REPLICATE_API_TOKEN`
- n8n credentials: Google Drive OAuth (`Google Drive account`) — same credential family that has died twice on the SEO pipeline; check first
- n8n OpenAI credential (`OpenAi account`) — used by Reference Ingestion only (inconsistent with Generation's raw env header; two places to break)
- Supabase tables: `tenants`, `content_studio_config`, `content_batches`, `content_batch_items`

## Known open items (from the code's own comments + read-through)

1. **Parked TODO from v3.4 (6 May, never done):** add a dedicated `tabletop_material` field to the interior Vision schema in Reference Ingestion — the regex patch in Build Prompt treats the symptom
2. **Rendezvous hardcoding x2:** Tag nodes in Reference Ingestion AND the insitu_interior *fallback* prompt text literally names "the actual Rendezvous restaurant interior" — wrong venue name would leak into prompts for any other tenant that has no interior refs
3. 4 of 8 variants gated off — presumably cost control; re-enable at the If node if a client wants the full set
4. Rendezvous is a DEAD client (May 2026, "problem makers") — it survives here as the test tenant only; first real deployment needs a real tenant row + config + folders

## How to run a test

1. Verify env keys + Drive credential in n8n (30 seconds — open either workflow, execute a single Drive node manually)
2. (Optional) Drop 1-2 interior photos and 1-2 styling shots into the respective Drive folders; wait a minute per file; confirm rows merged into `content_studio_config`
3. Open the Generation form URL, enter the tenant's email (must match `tenants.owner_email`), upload 1-2 dish photos, submit
4. Watch the execution: expect per photo ~1 Vision call + 4 Replicate generations (a few minutes each, 4-min polling ceiling)
5. Outputs: Drive output folder + `content_batch_items.shot_set` + batch `awaiting_review`
