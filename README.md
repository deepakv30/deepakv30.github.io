# deepakv30.github.io

Personal portfolio website for Deepak Vishwakarma (DevSecOps Engineer).

**Live Site**: https://deepakv30.github.io/

## Quick Links
- [IMPROVEMENTS.md](IMPROVEMENTS.md) — Full phased improvement history, metrics, testing checklist (references GitHub issues)
- [CHANGELOG.md](CHANGELOG.md) — Release notes (v2.0+)
- [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- [sitemap.xml](sitemap.xml) | [robots.txt](robots.txt)

## Project Tracking (GitHub)
See the [issues page](https://github.com/deepakv30/deepakv30.github.io/issues) for the current roadmap. Phases 1–3 (#15–#19) shipped; later a11y/perf/security follow-ups are filed separately (#34–#37).

## Local Development
```bash
# Simple static serve
python -m http.server 8000
# or npx serve .
```
Open http://localhost:8000

## Contributing / Roadmap
See IMPROVEMENTS.md "Testing Checklist", "Next Steps", and GitHub milestones (when configured) + issues labeled `enhancement`, `roadmap`, `bug`.

PRs welcome for new projects, blog posts, or perf/a11y tweaks.

## Tech
Static HTML/CSS/JS (Bootstrap 5, vanilla, icons). Hosted on GitHub Pages.

## Security headers

The repo includes a Netlify-style [`_headers`](_headers) file (CSP, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`). **GitHub Pages does not apply `_headers`.** Live responses on https://deepakv30.github.io/ only include GitHub's HSTS.

Treat `_headers` as the policy we would enforce behind Cloudflare/Netlify, not as live protection. To actually ship those headers, put a CDN in front of Pages and map the same policies. Do not cite `_headers` in audits as evidence of CSP or clickjacking defenses on GitHub Pages.

## Contact
- Email: deepakv.knit@gmail.com
- LinkedIn: https://www.linkedin.com/in/deepakv30/
- GitHub: https://github.com/deepakv30
- Medium: https://medium.com/@deepakv30
