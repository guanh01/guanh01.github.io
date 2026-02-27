# Dead Code Cleanup Design

**Date:** 2026-02-26
**Scope:** Conservative — remove only confirmed-unused includes and one unused plugin

## Context

The codebase has undergone systematic cleanup in recent commits (removing talks infrastructure, comment system, analytics, unused layouts, and template example pages). This pass addresses the remaining dead code: 7 unused includes inherited from the AcademicPages/Minimal Mistakes fork, plus one unused Jekyll plugin.

## Files to Delete

| File | Reason |
|------|--------|
| `_includes/archive-single-cv.html` | No CV collection exists; CV is a standalone page |
| `_includes/archive-single-talk.html` | Talks infrastructure removed in `447702e` |
| `_includes/comment.html` | Comment system removed in `1a079d3` |
| `_includes/paginator.html` | No pagination configured; no posts collection |
| `_includes/feature_row` | AcademicPages template, never used on this site |
| `_includes/gallery` | AcademicPages template, never used on this site |
| `_includes/group-by-array` | Helper template, never referenced |

## Config Change

Remove `jekyll-paginate` from the `plugins` list in `_config.yml`. There is no posts collection and no pagination configuration, so this plugin serves no purpose.

## Verification

Run `bundle exec jekyll build` after all changes to confirm the site builds without errors.

## Out of Scope

- Unused images (`profile-0.jpg`, `reuse-centric.*`)
- Empty config fields (SEO verification, social sharing)
- Pages not in navigation (`cv.md`, `sitemap.md`, `terms.md`)
- JS source files (`_main.js`, `collapse.js`)
- `jekyll-gist` plugin (may be used in future)
