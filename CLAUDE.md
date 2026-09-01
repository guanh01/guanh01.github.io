# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

This is Hui Guan's academic homepage — a Jekyll site based on the AcademicPages fork of Minimal Mistakes, hosted on GitHub Pages at https://guanh01.github.io.

## Build & Serve Commands

```bash
bundle install                    # Install Ruby dependencies (first time or after Gemfile changes)
bundle exec jekyll liveserve      # Build and serve at localhost:4000 with live reload
bundle exec jekyll serve          # Build and serve without live reload
```

Development config override: `_config.dev.yml` sets localhost:4000, expanded SASS, and disables analytics.

## Updating Each Page

Each visible page maps to one source file. Root-level page files (`services.md`, `students.md`, `teaching.md`) are rendered as pages via the `type: pages` defaults in `_config.yml`, so a permalink/layout is applied automatically — editing the file content is enough.

| Page | Edit this | Notes |
|------|-----------|-------|
| Homepage / About | `_pages/about.md` | `layout: home`, `permalink: /`. See breakdown below. |
| Publications | `markdown_generator/publications.xlsx` (+ regenerate) | Do **not** hand-edit `_publications/*.md`. See workflow below. |
| Services | `services.md` | Program/organizing committee lists. Plain markdown. |
| Students | `students.md` | Current students / collaborators / alumni. Plain markdown. |
| Teaching | `teaching.md` | Course list. `_teaching/2020-fall-mlsys.md` is a linked detail page (`/teaching/2020-fall-mlsys`). |

Navigation links (Publications, Teaching, Students, Services) live in `_data/navigation.yml`, not in the page files.

### Homepage / About (`_pages/about.md`)

Four sections, all edited inline in this one file:
- **Intro paragraph(s)** — bio prose at the top.
- **Research** — a `.research-grid` of `.research-card` links. Each card's `href` is `/publications/?area=<slug>`; the `<slug>` must match a research-area slug used on the publications page (see below).
- **News** — a `.news-scroll` list. Add the newest item as the first bullet inside the `<div class="news-scroll" markdown="1">` block.
- **Awards** — a plain bullet list.

### Publications (spreadsheet → generated markdown)

Publications are generated from a spreadsheet, not edited as markdown directly:

1. Edit `markdown_generator/publications.xlsx`
2. Run `cd markdown_generator && python pub2md.py` to regenerate all `_publications/*.md` files

Spreadsheet columns consumed by `pub2md.py`: `pub_date`, `title`, `venue`, `authors`, `tag`, `research_area`, `paper_url`, `code_url`, `extra_links`, `doi`, `url_slug`.
- `pub_date` must be `YYYY-MM-DD`. Output files are named `YYYY-MM-DD-<url_slug>.md`.
- `research_area` is a comma-separated list of area slugs. These drive the filter pills on the publications page. The slug set must stay in sync across three places: the `research_area` column, the `data-area` pills in `_pages/publications.html`, and the research-card `href`s in `_pages/about.md`. Current slugs: `learning-algorithms-and-systems`, `model-serving-and-inference`, `edge-and-on-device-ml`, `agentic-systems`, `ai-for-systems`, `miscellaneous`.
- `extra_links` uses `Label~>URL` entries separated by `|` (e.g. `Slides~>https://...|Video~>https://...`).

The publications page (`_pages/publications.html`) groups entries by year and filters client-side by research area; `?area=<slug>` in the URL pre-selects a filter. The per-entry rendering lives in `_includes/archive-single-publication.html`.

## Architecture

- **`_config.yml`** — Main site config: author profile, collections, defaults, plugin settings
- **`_pages/`** — `about.md` (homepage via `permalink: /`), `publications.html`, `404.md`
- **`services.md`, `students.md`, `teaching.md`** — root-level page files, rendered at `/services/`, `/students/`, `/teaching/`
- **`_teaching/`** — only `2020-fall-mlsys.md`, a detail page linked from `teaching.md`
- **`_publications/`** — auto-generated publication markdown files (do not hand-edit; regenerate via `pub2md.py`)
- **`_layouts/`** — page templates; `compress.html` (output wrapper) → `default.html` → `home.html` / `single.html` / `archive.html`
- **`_includes/`** — template partials (masthead, sidebar, footer, seo, publication entry, etc.)
- **`_data/navigation.yml`** — top navigation bar links
- **`_sass/`** — SCSS stylesheets compiled to `assets/css/main.css` via `assets/css/main.scss`
- **`files/`** — PDFs and downloadable files, served at `/files/[filename]`
- **`images/`** — image assets (e.g. `profile.jpeg`, the author avatar)

## Collections

Two Jekyll collections are configured in `_config.yml`: `teaching` and `publications` (both `output: true`).

## Key Conventions

- Publication frontmatter fields: `title`, `collection`, `date`, `venue`, `authors`, `tag`, `research_areas`, `paperurl`, `codeurl`, `extra_links`, `doi`
- Pages use YAML frontmatter with `layout`, `title`, `permalink`; root page files may omit frontmatter and still render (defaults apply)
- The site uses the `github-pages` gem for dependency management, ensuring GitHub Pages compatibility
