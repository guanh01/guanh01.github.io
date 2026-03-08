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

## Publication Workflow

Publications are generated from a spreadsheet, not edited as markdown directly:

1. Edit `markdown_generator/publications.xlsx`
2. Run `cd markdown_generator && python pub2md.py` to regenerate all `_publications/*.md` files

The `pub_date` must be `YYYY-MM-DD` format. Output files are named `YYYY-MM-DD-[url_slug].md`.

## Architecture

- **`_config.yml`** — Main site config: author profile, collections, social links, plugin settings
- **`_pages/`** — Top-level pages (about, publications, students, services). `about.md` serves as the homepage via `permalink: /`
- **`teaching.md`** — Teaching page (root-level file rendered at `/teaching/`). Edit this file directly to update courses.
- **`_teaching/`** — Only contains `2020-fall-mlsys.md` (a detail page linked from `teaching.md`)
- **`_publications/`** — Auto-generated publication markdown files (do not hand-edit; regenerate via `pub2md.py`)
- **`_projects/`** — Project pages in HTML format
- **`_layouts/`** — Page templates; `default.html` → `single.html` is the common chain
- **`_includes/`** — Template partials (author profile sidebar, SEO, archive display variants)
- **`_data/navigation.yml`** — Controls the top navigation bar links
- **`_sass/`** — SCSS stylesheets compiled to `assets/css/main.css`
- **`files/`** — PDFs and downloadable files, served at `/files/[filename]`
- **`images/`** — Image assets organized by subdirectory

## Collections

Three Jekyll collections are configured in `_config.yml`: `teaching`, `publications`, `projects` (all with `output: true`).

## Key Conventions

- Publication frontmatter fields: `title`, `collection`, `date`, `venue`, `paperurl`, `authors`
- Pages use YAML frontmatter with `layout`, `title`, `permalink`; most use `layout: archive` or `layout: single`
- Navigation is managed in `_data/navigation.yml`, not in individual page files
- The site uses the `github-pages` gem for dependency management, ensuring GitHub Pages compatibility
