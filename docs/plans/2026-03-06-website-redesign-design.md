# Website Redesign Design Doc

Date: 2026-03-06

## Goal

Comprehensive redesign of guanh01.github.io: visual refresh, new research-centric homepage, clean minimal aesthetic. Stay within Jekyll/GitHub Pages.

## Design Decisions

### Research Framing

Unified tagline: "We design algorithms and build systems for efficient and reliable AI."

Four peer research areas in a 2x2 grid:

1. **ML Serving & Inference** - Query-aware model scaling, accuracy-throughput tradeoffs, inference pipelines. Key papers: Proteus (ASPLOS'24), DiffServe (MLSys'25), Loki (HPDC'24).
2. **Edge/IoT Intelligence** - Adaptive deep learning for resource-constrained environments. Key papers: CACTUS (MobiSys'24), WildFiT (SenSys'26), Atom (MMSys'26). Funded by NSF CAREER, MemDrive, DESC.
3. **Efficient Training** - Memory-efficient training, low-precision formats, scaling. Key papers: ProTrain (MLSys'26).
4. **Systems for AI Agents** (new/emerging area) - Agent serving, scheduling, optimization. No published work yet; future direction.

Agent systems is NOT positioned as a convergence point of the other areas -- it's a peer alongside them.

### Homepage Layout

Full-width, section-based (no persistent sidebar):

1. **Profile header** - Photo + name + title + affiliation + social links (Scholar, GitHub, email, LinkedIn, ORCID). Inline horizontal layout.
2. **Research overview** - Tagline + 2x2 card grid of research areas. Each card: area name, 1-line description, 2-3 key papers.
3. **Selected publications** - 3-5 highlighted recent papers with venue tags and PDF links.
4. **News** - Compact scrollable section (keep existing `.news-scroll` approach).
5. **Awards** - Brief inline list.

### Visual Design

- **Typography**: System font stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`)
- **Layout**: Full-width, max content width ~800px centered, generous vertical spacing
- **Colors**:
  - Background: `#ffffff`, alternating sections: `#f8f9fa`
  - Text: `#1a1a2e`
  - Accent/links: `#2563eb`
  - Hover: `#1d4ed8`
  - Borders: `#e5e7eb`
- **Navigation**: Clean horizontal nav bar, minimal styling, sticky on scroll
- **Cards**: Subtle border + light shadow for research area cards

### Other Pages

- **Publications**: Keep collection-based approach. Add year grouping headers. Tag badges for venues. Restyle to match new visual.
- **Teaching, Students, Services**: Keep existing content, restyle to match.
- **No new pages** - Research overview lives on the homepage.

### Technical Approach

- New custom layout: `_layouts/home.html` for homepage (full-width, no sidebar)
- Override SCSS in `_sass/` for typography, colors, spacing, cards
- Keep `_layouts/single.html` and `_layouts/archive.html` for subpages (restyled)
- Keep existing publication pipeline (Excel -> Python -> Markdown) unchanged
- Profile info moves from sidebar to inline header on homepage

### Out of Scope

- Content updates to teaching/projects sections (separate effort)
- Framework migration (staying with Jekyll)
- Dark mode (can be added later)
- Bio/about text rewriting (keeping current text, just reformatting)
