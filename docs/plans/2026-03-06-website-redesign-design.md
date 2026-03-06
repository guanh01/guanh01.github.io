# Website Redesign Design Doc

Date: 2026-03-06

## Goal

Comprehensive redesign of guanh01.github.io: visual refresh, new research-centric homepage, clean minimal aesthetic. Stay within Jekyll/GitHub Pages.

## Design Decisions

### Research Framing

Unified tagline: "We design algorithms and build systems for efficient and reliable AI."

Four peer research areas in a 2x2 grid:

1. **Learning** - Efficient training (ProTrain/MLSys'26, COMET/VLDB'22, FLEET/MLSys'20), federated learning (Flow/NeurIPS'23, Flash/ICML'23, Thinking Forward/NeurIPS'24), GNN training systems (SPA/MLSys'25, VLDB'25), multi-task learning (AutoMTL/NeurIPS'22, TreeMTL/AutoML'22, AdapMTL/ACMMM'24), compiler-based pruning/compression (Wootz/PLDI'19, CoCoPIE/CACM'21, NeurIPS'19).
2. **Serving & Inference** - Query-aware model scaling, accuracy-throughput tradeoffs, inference pipelines, model fusion. Key papers: Proteus (ASPLOS'24), DiffServe (MLSys'25), Loki (HPDC'24), GMorph (EuroSys'24).
3. **Edge & On-Device ML** - Adaptive deep learning for resource-constrained environments, context-aware classifiers, in-situ adaptation, on-device pipelines. Key papers: CACTUS (MobiSys'24), WildFiT (SenSys'26), Atom (MMSys'26), MobiCom'23. Funded by NSF CAREER, MemDrive, DESC.
4. **Systems for AI Agents** (emerging area) - Agent serving, scheduling, optimization. No published work yet; future direction.

All four areas are peers. Agent systems is NOT positioned as a convergence point of the other areas.

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
