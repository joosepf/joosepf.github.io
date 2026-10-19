# joosepf.github.io

Joosep Fingling's portfolio — a bilingual (Estonian / English) static site, generated
from the project portfolio.

## Structure

```
index.html              Homepage — projects in sections (Formula Student / other / robots),
                        each ordered finished → in-progress → drafts
gallery.html            Image gallery of all project photos (with lightbox)
projects/<slug>.html    One page per project (goal, description, tools, links, images)
assets/portfolio.css    Shared styles (light/dark, responsive), same look as the CV
assets/fonts/           IBM Plex Sans (self-hosted, SIL OFL licence in OFL.txt)
assets/portfolio.js     Language toggle (ET/EN, remembered) + lightbox
images/projects/        Project images
docs/                   CV (cv-et.pdf / cv-en.pdf, linked per language) and other PDFs
build/generate.py       Generator — the single source of truth for the pages
```

## Language

Every page contains both Estonian and English text. The `ET / EN` switch in the top bar
toggles between them and remembers the choice (via `localStorage`). Estonian is the default.

## Editing content

All project text (titles, goals, descriptions, tools, links, images, draft/ongoing flags)
lives in one place — the `P = [...]` list in [build/generate.py](build/generate.py).
A project's `group` (`"fs"`, `"robots"`, or omitted for the general list) picks its homepage
section; the sections themselves are defined in `SECTIONS` in the same file.

Tools (`tools_et` / `tools_en`) are shown as coloured tags. The colour comes from `TAG_KIND`
(keyed by the English name; anything missing is grey). Every tag links to
`index.html?tag=<key>`, which shows only the projects with that tag; the key is made from the
English name, so use exactly the same English spelling for the same tool everywhere.
After editing it, regenerate every page:

```bash
python build/generate.py
```

This rewrites `index.html`, `gallery.html`, and every file in `projects/`.
Because the pages are generated, edit `build/generate.py` rather than the HTML directly
(hand edits to the generated files are overwritten on the next run).

The site is plain static HTML/CSS/JS — no build step is required to *serve* it, only to
regenerate it after a content change.
