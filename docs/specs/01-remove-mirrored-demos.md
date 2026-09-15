## Outcome
Portfolio no longer hosts mirrored copies of JS Calculator and Todo Application; Demo CTAs open each project's own GitHub Pages site.

## Context
Issue #68. Standalone Pages: https://deepakv30.github.io/JS-Calculator/ and https://deepakv30.github.io/Todo-Application/.

## Scope
**In:** delete `js-calculator/` and `Todo-Application/`; retarget `index.html` + `sitemap.xml`; CHANGELOG note.
**Out:** deleting `assets/img/Todo-Application.*` screenshots; redesigning project cards.

## Constraints
- Feature branch + PR; merge only when CI green.
- Do not invent career facts or new project metrics.

## Invariants
- **I1** Folders `js-calculator/` and `Todo-Application/` absent after merge. Check: `test ! -d js-calculator && test ! -d Todo-Application`
- **I2** Demo hrefs are absolute Pages URLs. Check: `grep -F deepakv30.github.io/JS-Calculator index.html`
- **I3** Screenshot assets remain. Check: `test -f assets/img/Todo-Application.webp`

## Prior decisions
- Apps own their GitHub Pages; portfolio is the index, not a second host.

## Task breakdown
1. Delete mirrored folders
2. Update links + sitemap + changelog
3. Open PR Closes #68

## Acceptance criteria
- Given the portfolio home page, when Demo is clicked for JS Calculator, then https://deepakv30.github.io/JS-Calculator/ opens.
- Given the portfolio home page, when Demo is clicked for Todo, then https://deepakv30.github.io/Todo-Application/ opens.
- Given a fresh clone after merge, when listing the repo root, then neither mirrored folder exists.

## Implementation notes
Keep `rel="noopener noreferrer"` on external demo links.
