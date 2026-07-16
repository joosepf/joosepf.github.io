# joosepf.github.io

Joosep Fingling's portfolio — a bilingual (Estonian / English) static site, generated
from the project portfolio.

## Structure

```
index.html              Homepage — list of all projects (finished → in-progress → drafts)
gallery.html            Image gallery of all project photos (with lightbox)
projects/<slug>.html    One page per project (goal, description, tools, links, images)
assets/portfolio.css    Shared styles (light/dark, responsive)
assets/portfolio.js     Language toggle (ET/EN, remembered) + lightbox
images/projects/        Project images
docs/                   CV and other PDFs
build/generate.py       Generator — the single source of truth for the pages
```

## Language

Every page contains both Estonian and English text. The `ET / EN` switch in the top bar
toggles between them and remembers the choice (via `localStorage`). Estonian is the default.

## Editing content

All project text (titles, goals, descriptions, tools, links, images, draft/ongoing flags)
lives in one place — the `P = [...]` list in [build/generate.py](build/generate.py).
After editing it, regenerate every page:

```bash
python build/generate.py
```

This rewrites `index.html`, `gallery.html`, and every file in `projects/`.
Because the pages are generated, edit `build/generate.py` rather than the HTML directly
(hand edits to the generated files are overwritten on the next run).

The site is plain static HTML/CSS/JS — no build step is required to *serve* it, only to
regenerate it after a content change.
