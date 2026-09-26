# Issue #73 — Apna Hisab portfolio card → Cloud Run URL + current brand assets

Work in this repo on the CURRENT branch `feat/apna-hisab-cloud-run-card-73` (already checked out from origin/main). Implement the full change yourself. Commit when done. Do NOT push. Do NOT merge. Do NOT touch `main`.

Issue: https://github.com/deepakv30/deepakv30.github.io/issues/73

## Goal

Update the Apna Hisab portfolio card (and resume generator) to the **live Cloud Run** app and current branding.

**Live URL (use exactly):** `https://apna-hisab-xblj7muxgq-el.a.run.app/`  
**Tagline for alt/copy:** Apna Hisab — Split expenses. Know who owes whom.

## Why

Cards still link to `https://apna-hisab.ai.studio/`, which is not the production deploy. Card image is an old AI Studio-era 3D cartoon that no longer matches the product brand.

## Scope (do all of these)

### 1. `index.html` — Apna Hisab featured card (~lines 611–660)
Replace every `https://apna-hisab.ai.studio/` on this card with `https://apna-hisab-xblj7muxgq-el.a.run.app/` for:
- image wrap `<a href=...>`
- title `<a href=...>`
- Live button `<a href=...>`

Update the `<img ... alt="...">` to align with the tagline, e.g.:
`alt="Apna Hisab — Split expenses. Know who owes whom."`
(Keep the picture/webp/jpg structure and classes unchanged.)

Optional (nice-to-have, keep concise): lightly refresh Problem/Approach/Result copy so Result or Problem nods at the tagline, without rewriting the whole case study. Do not invent new tech badges.

### 2. `projects.html` — same Apna Hisab card (~lines 128–176)
Same URL replacements (image wrap, title, Live button) and same alt text update as index.html.
Keep `data-search` sensible (may add `cloud run` / `expenses` if useful; do not bloat).

### 3. `scripts/generate-resume.py`
Change the Apna Hisab resume bullet link from `https://apna-hisab.ai.studio/` to `https://apna-hisab-xblj7muxgq-el.a.run.app/`.
You may lightly align the bullet wording with the tagline (e.g. “split expenses; know who owes whom” / settle via UPI) — keep it one short bullet.

### 4. Replace card images with current brand lockup
Source (real brand asset — do NOT invent a fake logo):
`/workspace/apna-hisab/public/brand/lockup-shared-circle.png` (1400×788, Shared circle lockup)

Overwrite:
- `assets/img/apna-hisab.jpg`
- `assets/img/apna-hisab.webp`

Target roughly **1200×675** (existing card size; other project cards are 1200×675). Scale/crop/letterbox to fit without distorting the lockup. Prefer preserving the lockup content (friends around table + “Apna Hisab” wordmark). Soft paper/sky brand colors from BRAND.md are fine as background if you letterbox.

Tools available on this box:
- `ffmpeg` (has libwebp)
- `cwebp` / `dwebp` (webp package installed)
- `python3` + Pillow if you `pip install --break-system-packages pillow`

Example approach (adapt as needed):
```bash
# scale lockup into 1200x675 canvas (paper #F7F1E5), write jpg + webp
ffmpeg -y -i /workspace/apna-hisab/public/brand/lockup-shared-circle.png \
  -vf "scale=1200:675:force_original_aspect_ratio=decrease,pad=1200:675:(ow-iw)/2:(oh-ih)/2:#F7F1E5" \
  -q:v 3 assets/img/apna-hisab.jpg
ffmpeg -y -i assets/img/apna-hisab.jpg -c:v libwebp -quality 82 assets/img/apna-hisab.webp
```
Or use Pillow/cwebp equivalently. Verify final dimensions ≈1200×675 and files are non-trivial size.

Do **not** use the old AI Studio cartoon. Do **not** invent artwork. Lockup is preferred over a live homepage screenshot for this card.

### 5. Grep cleanup
After edits, ensure **zero** remaining `apna-hisab.ai.studio` references in this repo for this project:
```bash
grep -rn 'apna-hisab.ai.studio' . --include='*.html' --include='*.py' --include='*.md' --include='*.js' --include='*.json' --include='*.css' --include='*.txt' || true
```
Fix any hits in portfolio/resume sources. (Do not chase unrelated history/git objects.)

## Acceptance

- All Apna Hisab Live / title / image links open `https://apna-hisab-xblj7muxgq-el.a.run.app/`
- No remaining `apna-hisab.ai.studio` links in portfolio sources for this project
- `assets/img/apna-hisab.jpg` + `.webp` match current Shared-circle brand lockup
- Alt text / card copy aligned with “Split expenses. Know who owes whom.”

## Do NOT

- Push to remote or open a PR
- Merge to main or commit on main
- Change unrelated project cards
- Invent a fake logo or keep the AI Studio-era asset
- Use HTTP (HTTPS only for URLs)

## Commit

When verified, make one clean commit on this branch, e.g.:
`feat: Apna Hisab card → Cloud Run URL + current brand lockup (#73)`

Include the binary image updates in the commit.
