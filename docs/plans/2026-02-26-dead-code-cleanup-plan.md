# Dead Code Cleanup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove 7 unused includes and 1 unused plugin from the Jekyll site.

**Architecture:** Delete files that are confirmed unreferenced, remove `jekyll-paginate` from config, verify the site still builds.

**Tech Stack:** Jekyll, GitHub Pages

---

### Task 1: Delete unused includes

**Files:**
- Delete: `_includes/archive-single-cv.html`
- Delete: `_includes/archive-single-talk.html`
- Delete: `_includes/comment.html`
- Delete: `_includes/paginator.html`
- Delete: `_includes/feature_row`
- Delete: `_includes/gallery`
- Delete: `_includes/group-by-array`

**Step 1: Delete all 7 files**

```bash
rm _includes/archive-single-cv.html _includes/archive-single-talk.html _includes/comment.html _includes/paginator.html _includes/feature_row _includes/gallery _includes/group-by-array
```

**Step 2: Verify they're gone**

```bash
ls _includes/archive-single-cv.html _includes/archive-single-talk.html _includes/comment.html _includes/paginator.html _includes/feature_row _includes/gallery _includes/group-by-array 2>&1
```

Expected: All 7 "No such file or directory" errors.

**Step 3: Commit**

```bash
git add -u _includes/
git commit -m "remove 7 unused includes (cv, talk, comment, paginator, feature_row, gallery, group-by-array)"
```

---

### Task 2: Remove jekyll-paginate from config

**Files:**
- Modify: `_config.yml:182` (remove from `plugins` list)
- Modify: `_config.yml:189` (remove from `whitelist` list)

**Step 1: Edit `_config.yml`**

Remove line 182 (`  - jekyll-paginate`) from the `plugins` block:

```yaml
# Before
plugins:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jekyll-redirect-from

# After
plugins:
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jekyll-redirect-from
```

Remove line 189 (`  - jekyll-paginate`) from the `whitelist` block:

```yaml
# Before
whitelist:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jemoji

# After
whitelist:
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jemoji
```

**Step 2: Commit**

```bash
git add _config.yml
git commit -m "remove unused jekyll-paginate plugin from config"
```

---

### Task 3: Verify site builds

**Step 1: Run Jekyll build**

```bash
bundle exec jekyll build
```

Expected: Build completes with no errors. Warnings about GitHub Metadata are OK.

**Step 2: Verify no references to deleted files remain**

```bash
grep -r "archive-single-cv\|archive-single-talk\|comment.html\|paginator\|feature_row\|gallery\|group-by-array" _includes/ _layouts/ _pages/ _config.yml 2>/dev/null
```

Expected: No output (no remaining references).
