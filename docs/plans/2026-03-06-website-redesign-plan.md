# Website Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign guanh01.github.io with a clean minimal aesthetic, research-centric homepage, and modern visual styling — all within Jekyll/GitHub Pages.

**Architecture:** Create a new `_layouts/home.html` layout for the homepage (full-width, no sidebar, section-based). Add a new `_sass/_home.scss` for homepage-specific styles. Override color/typography variables in `_sass/_variables.scss`. Restyle existing layouts (single, archive) to match. Keep all existing content and publication pipeline unchanged.

**Tech Stack:** Jekyll, SCSS, Liquid templates, GitHub Pages

---

### Task 1: Update SCSS Variables (Colors & Typography)

**Files:**
- Modify: `_sass/_variables.scss`

**Step 1: Update color and link variables**

In `_sass/_variables.scss`, replace the color and link sections:

```scss
// Replace these existing values:
$text-color                 : $dark-gray;
$primary-color              : #7a8288;
$link-color                 : $info-color;
$link-color-hover           : mix(#000, $link-color, 25%);
$link-color-visited         : mix(#fff, $link-color, 25%);
$masthead-link-color        : $primary-color;
$masthead-link-color-hover  : mix(#000, $primary-color, 25%);

// With:
$text-color                 : #1a1a2e;
$primary-color              : #2563eb;
$link-color                 : #2563eb;
$link-color-hover           : #1d4ed8;
$link-color-visited         : mix(#fff, #2563eb, 15%);
$masthead-link-color        : #1a1a2e;
$masthead-link-color-hover  : #2563eb;
```

**Step 2: Verify build succeeds**

Run: `cd /Users/huiguan/Documents/website/guanh01.github.io && bundle exec jekyll build`
Expected: Build succeeds with no errors.

**Step 3: Commit**

```bash
git add _sass/_variables.scss
git commit -m "update color scheme: blue accents, darker text"
```

---

### Task 2: Create Homepage Layout

**Files:**
- Create: `_layouts/home.html`

**Step 1: Create the home layout**

Create `_layouts/home.html` with this content:

```html
---
layout: default
---

{% include base_path %}

<div id="main" role="main">
  <div class="home-wrapper">

    <!-- Profile Header -->
    <section class="home-profile">
      <div class="home-profile__avatar">
        {% if site.author.avatar contains "://" %}
          <img src="{{ site.author.avatar }}" alt="{{ site.author.name }}">
        {% else %}
          <img src="{{ site.author.avatar | prepend: '/images/' | prepend: base_path }}" alt="{{ site.author.name }}">
        {% endif %}
      </div>
      <div class="home-profile__info">
        <h1 class="home-profile__name">{{ site.author.name }}</h1>
        <p class="home-profile__bio">{{ site.author.bio }}</p>
        <ul class="home-profile__links">
          {% if site.author.email %}<li><a href="mailto:{{ site.author.email }}"><i class="fas fa-fw fa-envelope"></i> Email</a></li>{% endif %}
          {% if site.author.googlescholar %}<li><a href="{{ site.author.googlescholar }}"><i class="fas fa-fw fa-graduation-cap"></i> Scholar</a></li>{% endif %}
          {% if site.author.github %}<li><a href="https://github.com/{{ site.author.github }}"><i class="fab fa-fw fa-github"></i> GitHub</a></li>{% endif %}
          {% if site.author.linkedin %}<li><a href="https://www.linkedin.com/in/{{ site.author.linkedin }}"><i class="fab fa-fw fa-linkedin"></i> LinkedIn</a></li>{% endif %}
          {% if site.author.orcid %}<li><a href="{{ site.author.orcid }}"><i class="ai ai-orcid-square ai-fw"></i> ORCID</a></li>{% endif %}
        </ul>
      </div>
    </section>

    <!-- Main Content (bio, research, news, awards from about.md) -->
    <section class="home-content">
      {{ content }}
    </section>

  </div>
</div>
```

**Step 2: Verify build succeeds**

Run: `bundle exec jekyll build`
Expected: Build succeeds. Homepage not yet using this layout (that comes in Task 4).

**Step 3: Commit**

```bash
git add _layouts/home.html
git commit -m "add home layout with inline profile header"
```

---

### Task 3: Create Homepage SCSS

**Files:**
- Create: `_sass/_home.scss`
- Modify: `assets/css/main.scss`

**Step 1: Create homepage styles**

Create `_sass/_home.scss`:

```scss
/* ==========================================================================
   HOMEPAGE
   ========================================================================== */

.home-wrapper {
  max-width: 800px;
  margin: 0 auto;
  padding: 2em 1em;
}

/* Profile Header */
.home-profile {
  display: flex;
  align-items: flex-start;
  gap: 2em;
  margin-bottom: 2.5em;

  @include breakpoint(max-width $small) {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
}

.home-profile__avatar {
  flex-shrink: 0;

  img {
    width: 160px;
    height: 160px;
    border-radius: 50%;
    object-fit: cover;
  }
}

.home-profile__info {
  flex: 1;
}

.home-profile__name {
  margin: 0 0 0.25em;
  font-size: 1.75em;
  font-weight: 700;
  color: $text-color;
}

.home-profile__bio {
  margin: 0 0 0.75em;
  font-size: 0.95em;
  line-height: 1.5;
  color: mix(#fff, $text-color, 20%);
}

.home-profile__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em 1.25em;

  @include breakpoint(max-width $small) {
    justify-content: center;
  }

  li a {
    color: $link-color;
    text-decoration: none;
    font-size: 0.9em;

    &:hover {
      color: $link-color-hover;
      text-decoration: underline;
    }
  }
}

/* Research Cards */
.research-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25em;
  margin: 1.5em 0 2em;

  @include breakpoint(max-width $small) {
    grid-template-columns: 1fr;
  }
}

.research-card {
  padding: 1.25em;
  border: 1px solid $border-color;
  border-radius: 6px;
  background: #fff;
  transition: box-shadow 0.2s ease;

  &:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  }

  h3 {
    margin: 0 0 0.5em;
    font-size: 1.05em;
    color: $text-color;
  }

  p {
    margin: 0 0 0.5em;
    font-size: 0.85em;
    color: mix(#fff, $text-color, 25%);
    line-height: 1.5;
  }

  .research-card__papers {
    font-size: 0.8em;
    color: $gray;

    a {
      color: $link-color;
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
  }
}

.research-card--emerging {
  border-style: dashed;
  background: $code-background-color;
}

/* Selected Papers */
.selected-papers {
  margin: 2em 0;

  h2 {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }

  .selected-papers__more {
    font-size: 0.65em;
    font-weight: normal;
  }
}

.selected-papers__list {
  list-style: none;
  padding: 0;
  margin: 0;

  li {
    padding: 0.75em 0;
    border-bottom: 1px solid $border-color;
    font-size: 0.9em;

    &:last-child {
      border-bottom: none;
    }
  }

  .venue-tag {
    display: inline-block;
    padding: 0.1em 0.5em;
    font-size: 0.8em;
    font-weight: 600;
    color: $link-color;
    background: mix(#fff, $link-color, 90%);
    border-radius: 3px;
    margin-right: 0.4em;
  }
}

/* Awards */
.home-awards {
  margin: 2em 0;

  ul {
    list-style: none;
    padding: 0;

    li {
      padding: 0.3em 0;
      font-size: 0.9em;

      &:before {
        content: "\2022";
        color: $link-color;
        font-weight: bold;
        margin-right: 0.5em;
      }
    }
  }
}

/* Home content overrides */
.home-content {
  h2 {
    margin-top: 2em;
    padding-bottom: 0.3em;
    border-bottom: 2px solid $border-color;
    font-size: 1.3em;
  }

  a {
    text-decoration: none;

    &:hover {
      text-decoration: underline;
    }
  }
}
```

**Step 2: Import in main.scss**

Add `@import "home";` after the `@import "sidebar";` line in `assets/css/main.scss`.

**Step 3: Verify build succeeds**

Run: `bundle exec jekyll build`
Expected: Build succeeds.

**Step 4: Commit**

```bash
git add _sass/_home.scss assets/css/main.scss
git commit -m "add homepage SCSS: profile header, research cards, selected papers"
```

---

### Task 4: Rewrite Homepage Content

**Files:**
- Modify: `_pages/about.md`

**Step 1: Update frontmatter to use home layout**

Change `about.md` frontmatter from the current layout (implicit single) to:

```yaml
---
layout: home
permalink: /
title: "About me"
excerpt: "About me"
redirect_from:
  - /about/
  - /about.html
---
```

**Step 2: Restructure the page content**

Replace the entire body of `about.md` (everything after frontmatter) with research-centric content. Keep the existing bio paragraphs, but restructure into sections:

1. Short bio (keep existing 2 paragraphs + AWS leave note)
2. Research section with tagline + 2x2 card grid (HTML within markdown)
3. Selected publications (5 recent highlights, HTML)
4. News section (keep existing scrollable div)
5. Awards (keep existing list)

The research cards section should be HTML like:

```html
## Research

We design algorithms and build systems for efficient and reliable AI.

<div class="research-grid">
  <div class="research-card">
    <h3>Learning</h3>
    <p>Efficient training, federated learning, multi-task learning, GNN training, and compiler-based model optimization.</p>
    <div class="research-card__papers">
      ProTrain (MLSys'26) · Flow (NeurIPS'23) · Flash (ICML'23) · AutoMTL (NeurIPS'22) · SPA (MLSys'25) · Wootz (PLDI'19)
    </div>
  </div>
  <div class="research-card">
    <h3>Serving & Inference</h3>
    <p>Query-aware model scaling, accuracy-throughput tradeoffs, inference pipelines, and model fusion.</p>
    <div class="research-card__papers">
      Proteus (ASPLOS'24) · DiffServe (MLSys'25) · Loki (HPDC'24) · GMorph (EuroSys'24)
    </div>
  </div>
  <div class="research-card">
    <h3>Edge & On-Device ML</h3>
    <p>Adaptive deep learning for resource-constrained IoT and edge environments.</p>
    <div class="research-card__papers">
      CACTUS (MobiSys'24) · WildFiT (SenSys'26) · Atom (MMSys'26)
    </div>
  </div>
  <div class="research-card research-card--emerging">
    <h3>Systems for AI Agents</h3>
    <p>Efficient serving, scheduling, and orchestration for agentic AI workloads.</p>
    <div class="research-card__papers">
      Emerging research direction
    </div>
  </div>
</div>
```

The selected papers section:

```html
## Selected Publications [<span class="selected-papers__more"><a href="/publications/">View all →</a></span>]
{: .selected-papers}

<ul class="selected-papers__list">
  <li><span class="venue-tag">MLSys'26</span> <strong>ProTrain: Efficient LLM Training via Automatic Memory Management.</strong> <a href="https://arxiv.org/pdf/2406.08334">[PDF]</a></li>
  <li><span class="venue-tag">MLSys'25</span> <strong>DiffServe: Efficiently Serving Text-to-Image Diffusion Models with Query-Aware Model Scaling.</strong> <a href="https://arxiv.org/pdf/2411.15381">[PDF]</a></li>
  <li><span class="venue-tag">ASPLOS'24</span> <strong>Proteus: A High-Throughput Inference-Serving System with Accuracy Scaling.</strong> <a href="http://guanh01.github.io/files/2024proteus.pdf">[PDF]</a></li>
  <li><span class="venue-tag">MobiSys'24</span> <strong>CACTUS: Dynamically Switchable Context-aware micro-Classifiers for Efficient IoT Inference.</strong> <a href="http://guanh01.github.io/files/2024mobisys-cactus.pdf">[PDF]</a></li>
  <li><span class="venue-tag">NeurIPS'22</span> <strong>AutoMTL: A Programming Framework for Automating Efficient Multi-Task Learning.</strong> <a href="http://guanh01.github.io/files/2022automtl.pdf">[PDF]</a></li>
</ul>
```

**Step 3: Verify build and check output**

Run: `bundle exec jekyll build`
Expected: Build succeeds. Check `_site/index.html` to verify the homepage renders the new layout with profile header and research cards.

**Step 4: Commit**

```bash
git add _pages/about.md
git commit -m "redesign homepage: research cards, selected papers, inline profile"
```

---

### Task 5: Restyle Navigation (Masthead)

**Files:**
- Modify: `_sass/_masthead.scss`
- Modify: `_sass/_navigation.scss`

**Step 1: Update masthead styling**

In `_sass/_masthead.scss`, update `.masthead` to add sticky positioning and cleaner styling:

```scss
.masthead {
  position: sticky;
  top: 0;
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  z-index: 20;
  animation: intro 0.3s both;
  animation-delay: 0.15s;

  &__inner-wrap {
    max-width: 800px;
    margin: 0 auto;
    padding: 0.75em 1em;
    font-family: $sans-serif-narrow;

    nav {
      z-index: 10;
    }

    a {
      text-decoration: none;
    }
  }
}
```

Remove the `@include container`, `@include clearfix`, and `@include breakpoint($x-large)` from `&__inner-wrap` since we're using max-width centering instead.

**Step 2: Update nav link colors**

In `_sass/_navigation.scss`, the `.greedy-nav a` color already uses `$masthead-link-color` which we updated in Task 1. The hover underline animation (`:before` pseudo-element) should use the new accent color — verify `mix(#fff, $primary-color, 50%)` now produces a blue-tinted underline since `$primary-color` is now `#2563eb`.

**Step 3: Verify build and visual**

Run: `bundle exec jekyll build`
Expected: Build succeeds. Nav bar should be sticky with cleaner spacing.

**Step 4: Commit**

```bash
git add _sass/_masthead.scss _sass/_navigation.scss
git commit -m "restyle navigation: sticky, centered, cleaner spacing"
```

---

### Task 6: Restyle Subpages (Single & Archive Layouts)

**Files:**
- Modify: `_sass/_page.scss`
- Modify: `_sass/_archive.scss`
- Modify: `_sass/_sidebar.scss`

**Step 1: Update page content width**

In `_sass/_page.scss`, update `#main` to use centered max-width instead of Susy grid:

```scss
#main {
  max-width: 800px;
  margin: 2em auto 0;
  padding-left: 1em;
  padding-right: 1em;
  animation: intro 0.3s both;
  animation-delay: 0.35s;
}
```

Update `.page` to remove the Susy grid spans:

```scss
.page {
  .page__inner-wrap {
    .page__content,
    .page__meta,
    .page__share {
      width: 100%;
    }
  }
}
```

**Step 2: Update archive layout width**

In `_sass/_archive.scss`, simplify `.archive`:

```scss
.archive {
  margin-bottom: 2em;

  a {
    text-decoration: none;
    color: $link-color;

    &:hover {
      text-decoration: underline;
    }
  }
}
```

Remove the `@include span()` and `@include prefix()` rules.

**Step 3: Hide sidebar on subpages (optional visual cleanup)**

The sidebar is already effectively hidden (right-sidebar-width is 0px in variables). But on the homepage we skip it entirely via the home layout. No changes needed unless sidebar shows on subpages — verify visually.

**Step 4: Restyle publication list**

In `_includes/archive-single-publication.html`, the existing markup is clean. The venue tags are rendered via `post.tag`. Optionally wrap the tag in a `<span class="venue-tag">` for consistent styling:

Replace in `_includes/archive-single-publication.html`:
```
<strong>[{{ tag_display }}] {{ post.title }}.</strong>
```
With:
```
<span class="venue-tag">{{ tag_display }}</span> <strong>{{ post.title }}.</strong>
```

Add venue-tag styling to `_sass/_archive.scss` (reuse the same class from `_home.scss`):

```scss
.venue-tag {
  display: inline-block;
  padding: 0.1em 0.5em;
  font-size: 0.8em;
  font-weight: 600;
  color: $link-color;
  background: mix(#fff, $link-color, 90%);
  border-radius: 3px;
  margin-right: 0.25em;
}
```

**Step 5: Verify build**

Run: `bundle exec jekyll build`
Expected: Build succeeds. Publications page should show styled venue tags.

**Step 6: Commit**

```bash
git add _sass/_page.scss _sass/_archive.scss _sass/_sidebar.scss _includes/archive-single-publication.html
git commit -m "restyle subpages: centered layout, venue tags, cleaner typography"
```

---

### Task 7: Restyle Footer

**Files:**
- Modify: `_sass/_footer.scss`

**Step 1: Clean up footer**

Update `.page__footer` to use centered max-width matching the rest of the site:

```scss
.page__footer {
  // ... keep existing sticky footer fix ...
  footer {
    max-width: 800px;
    margin: 0 auto;
    padding: 2em 1em;
  }
}
```

**Step 2: Verify build**

Run: `bundle exec jekyll build`
Expected: Build succeeds.

**Step 3: Commit**

```bash
git add _sass/_footer.scss
git commit -m "restyle footer: match centered layout"
```

---

### Task 8: Visual QA and Final Adjustments

**Step 1: Run local server**

Run: `bundle exec jekyll serve`
Visit `localhost:4000` and check:
- [ ] Homepage: profile photo + name renders inline
- [ ] Homepage: research cards in 2x2 grid
- [ ] Homepage: selected papers with venue tags
- [ ] Homepage: news section scrollable
- [ ] Homepage: awards section visible
- [ ] Navigation: sticky, centered, clean
- [ ] Publications page: year headers, venue tags
- [ ] Teaching/Students/Services pages: clean, centered
- [ ] Mobile: responsive layout (cards stack to 1-column)
- [ ] Links: blue accent color, hover state works

**Step 2: Fix any visual issues found**

Adjust SCSS as needed for spacing, alignment, font sizes.

**Step 3: Final commit**

```bash
git add -A
git commit -m "final visual adjustments from QA pass"
```

---

### Task 9: Update Design Doc and Clean Up

**Step 1: Mark design doc as implemented**

Add "Status: Implemented" to the top of `docs/plans/2026-03-06-website-redesign-design.md`.

**Step 2: Commit**

```bash
git add docs/plans/
git commit -m "mark website redesign as implemented"
```
