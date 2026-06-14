# Changelog

All notable changes to the deepakv30.github.io portfolio site.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
