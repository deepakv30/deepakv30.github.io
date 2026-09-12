# Changelog

All notable changes to the deepakv30.github.io portfolio site.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.12] - 2026-09-12

### Added
- Education: KNIT, Bachelor’s in Electronics, 2011–2015, A+ (#59).

### Changed
- Public title is DevOps / Platform Engineer. Hero, About, and resume summary follow the LinkedIn headline/About, including the approved 50% system-failure reduction. About links devops-mastery-guide (#56, #57).
- Experience is one Dell role: Software Engineer 2 - DevOps, Jun 2019 – Present, Bengaluru. Removed the 2023 start and aggregated “Previous Roles 2021–2023” (#58, #57).
- CKA removed from site and resume until confirmed held (#57).

**Closes #56, #57, #58, #59**

## [2.11] - 2026-09-12

### Added
- Featured DevSecOps cards now use Problem → Approach → Result, with metrics taken only from the Experience section (#43).
- Distinct WebP+JPEG images per featured card (live Mastery Guide screenshot plus GitOps / Terraform / Observability diagrams). Apna Hisab keeps its dedicated screenshot (#44).

**Closes #43, #44**

## [2.10] - 2026-09-12

### Changed / Fixed
- Blog listing light-mode header uses dark nav text on a light bar (contrast ≥ 4.5:1). Dark mode keeps light nav text on a dark bar; hover/active remain visible (#49).

**Closes #49**

## [2.9] - 2026-09-12

### Changed / Fixed
- Removed dead `href="#"` author controls, unused dropdown markup, and the BootstrapMade “purchase the pro version” footer comment. Contact message field now has `id="message"` matching its label. Back-to-top points at `#hero` / `#main` (#45).

**Closes #45**

## [2.8] - 2026-09-12

### Changed / Fixed
- Mobile home no longer scrolls sideways at 375/390px. Oversized uppercase section titles (`CERTIFICATIONS`, `ACHIEVEMENTS`) and the hero title now scale down and wrap; hero content is capped to the viewport (#47).

**Closes #47**

## [2.7] - 2026-09-12

### Added
- Experience in the primary nav (desktop and mobile) and first-screen hire CTAs: Contact, Resume, LinkedIn (#42).

### Changed / Fixed
- Sticky header no longer covers section headings. `scroll-padding-top` plus `scrollIntoView` keep `#experience` and other in-page jumps fully visible (#48).

**Closes #42, #48**

## [2.6] - 2026-09-11

### Added
- Resume PDF at `assets/resume/deepak-vishwakarma-resume.pdf` (facts from the live site only; generator in `scripts/generate-resume.py`) (#39).

### Changed / Fixed
- Featured GitLab CI/CD + ArgoCD card no longer links to the 404 repo `github.com/deepakv30/Ultimate_CICD`. Marked private; walkthrough CTA goes to LinkedIn (#40).
- Certification buttons say “About this cert” and open issuer pages (not personal badge IDs). GitLab URL no longer 404s (#41).
- IMPROVEMENTS.md resume status matches production; sitemap `lastmod` bumped and hash-only URLs removed (#46).

**Closes #39, #40, #41, #46**

## [2.5] - 2026-09-11

### Added
- Header logo assets (`logo.webp` / `logo.png` / `logo.svg`) so the mark no longer 404s (#34).
- Skip-to-main-content link for keyboard and screen-reader users (#36).
- Shared avatar WebP preload; favicon now uses the logo WebP with PNG fallback (#35).

### Changed / Fixed
- Documented that `_headers` is **not** applied by GitHub Pages. CSP / `X-Frame-Options` / nosniff are aspirational until a CDN sits in front (#37).

**Closes #34, #35, #36, #37**

## [2.4] - 2026-06-14

### Added / Documentation
- Cross-referenced all Phase improvements and bug fixes to current open GitHub issues (#15 Phase1, #16 Phase2, #17 Phase3, #18 Bugs, #19 Overall roadmap).
- Added dedicated Bugs & Fixes section in IMPROVEMENTS.md.
- Minor clarification to Resume download button comment in index.html.
- Bumped IMPROVEMENTS version and dates.

### Related PRs
- Independent PRs created for each open issue #15-19 (serially in dedicated branches).

## [2.3] - 2026-06-14 (Phase 3)

### Added
- PWA support: manifest.json, sw.js, registration script, installable.
- Security headers via _headers file (X-Content-Type-Options, CSP, etc.).
- New professional OG banner image (1280x720) for better social previews.
- Enhanced JSON-LD structured data (awards, employer, expanded skills).
- CI workflow (.github/workflows/ci.yml) for size/a11y/Lighthouse guidance.
- theme-color meta, improved ARIA, back-to-top accessibility.
- Removed unused heavy vendor libs (GLightbox, Swiper, PureCounter) for perf.

### Changed / Fixed
- Performance optimizations: reduced JS payload, cleaned main.js inits.
- Accessibility: 35+ ARIA, labels, keyboard support, dark mode polish.
- SEO: OG image updates, structured data.
- Maintenance: full Phase 3 section in IMPROVEMENTS.md.

**Closes #14 (and #17)**

## [2.2] - 2026-06-14 (Phase 2)

### Added
- New Certifications section (#certifications) with 4 credentials (AWS DevOps Pro, CKA, Terraform, GitLab CI/CD) + badges, dates, verify links.
- Enhanced Projects: 3+ new DevSecOps cards (with metrics e.g. 65% faster deploys, tech badges, GitHub/links, screenshots); re-org of learning projects.
- Refreshed Experience & Achievements: Dell 2023-Present + 2021-2023 with quantifiable achievements, timeline items.
- Blog improvements: recent posts, dynamic rendering via blog-list.js (now 4 articles), RSS feed links, updated CTAs.
- Nav link for Certifications; supporting CSS for badges/timeline/certs.

**Closes #13 (and #16)**

## [2.1] - 2026-06-14 (Phase 1)

### Added
- Functional Contact Form using FormSubmit.co (zero-config), with validation, loading/success states, _gotcha honeypot, patched validate.js.
- Resume Download button enabled (points to assets/resume/deepak-vishwakarma-resume.pdf; dir + .gitkeep created).
- Privacy-friendly Analytics: Plausible.io script (replaced Google placeholder).
- Image optimization: WebP conversions + compression for key assets (some retained/adjusted in follow-up path fixes for compatibility).
- All external links: added rel="noopener noreferrer", fixed some paths (js-calculator rename).
- Updated sitemap, blog-list refs, minor text cleanups (e.g. "Send Message").

**Closes #12 (and #15)**

## [2.0] - 2025-10-26

### Initial Major Improvements (pre-phased)
- SEO: full meta, OG, Twitter, JSON-LD, canonical, robots, sitemap, keywords.
- New sections: Skills & Technologies, Experience & Achievements.
- Dark mode toggle with persistence.
- Accessibility: alts, aria, lazy load, semantics, security rels.
- Visual: hovers, animations, smooth scroll, CTAs.
- Critical fixes: typo, social links, logo, meta.
- Added: IMPROVEMENTS.md, DEPLOYMENT_CHECKLIST.md, robots.txt, sitemap.xml.
- Tech stack maintained (Bootstrap + vanilla JS + icons).

See IMPROVEMENTS.md for full details and testing checklists.

[2.4]: https://github.com/deepakv30/deepakv30.github.io/compare/... (see PRs #26-#30)
[2.3]: ... (PR #25)
[2.2]: ... (PR #24)
[2.1]: ... (PR #20)
[2.0]: ... (earlier work)
