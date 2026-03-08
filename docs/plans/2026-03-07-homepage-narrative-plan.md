# Homepage Narrative Update — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Update the homepage narrative, research cards, selected publications, and news to reflect broader research vision and recent work.

**Architecture:** All changes are in a single file `_pages/about.md`. We edit in 4 sequential tasks, committing after each, and verify with `bundle exec jekyll serve`.

**Tech Stack:** Jekyll, Markdown, HTML

---

### Task 1: Update Opening Narrative and AWS Note

**Files:**
- Modify: `_pages/about.md:11-15`

**Step 1: Replace lines 11-15 with the following**

Replace the current opening paragraphs and AWS note:

```markdown
My group designs algorithms and builds systems that make machine learning fast, scalable, and reliable. Our work spans the full ML lifecycle — from efficient training and intelligent model serving in the cloud to adaptive inference on resource-constrained edge devices. We also explore problems at the frontier of generative AI, including trustworthy watermarking for AI-generated content and agentic systems for automated software engineering.

_Currently on leave at AWS, working on agentic AI systems for cloud automation and code transformation. Reach me at huiguan@amazon.com if you're interested in this space or research internships._
```

**Step 2: Verify the site builds**

Run: `cd /Users/huiguan/Documents/website/guanh01.github.io && bundle exec jekyll build 2>&1 | tail -5`
Expected: "done" with no errors

**Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "update homepage opening narrative: broader vision, collaborative voice"
```

---

### Task 2: Rename Research Cards and Update Content

**Files:**
- Modify: `_pages/about.md` (the research-grid div, approximately lines 23-52)

**Step 1: Replace the entire research-grid div with the following**

```html
<div class="research-grid" markdown="0">
  <div class="research-card">
    <h3>Learning Algorithms &amp; Systems</h3>
    <p>Efficient training, federated learning, multi-task learning, GNN training, compiler-based optimization, watermarking, and learning on compressed data.</p>
    <div class="research-card__papers">
      ProTrain (MLSys'26) · Flow (NeurIPS'23) · Flash (ICML'23) · AutoMTL (NeurIPS'22) · SPA (MLSys'25) · Wootz (PLDI'19) · Zodiac (NeurIPS'24) · TKDD'25
    </div>
  </div>
  <div class="research-card">
    <h3>Serving &amp; Inference</h3>
    <p>Query-aware model scaling, accuracy-throughput tradeoffs, inference pipelines, and model fusion.</p>
    <div class="research-card__papers">
      Proteus (ASPLOS'24) · DiffServe (MLSys'25) · Loki (HPDC'24) · GMorph (EuroSys'24)
    </div>
  </div>
  <div class="research-card">
    <h3>Edge &amp; On-Device ML</h3>
    <p>Adaptive deep learning for resource-constrained IoT and edge environments.</p>
    <div class="research-card__papers">
      CACTUS (MobiSys'24) · WildFiT (SenSys'26) · Atom (MMSys'26)
    </div>
  </div>
  <div class="research-card">
    <h3>Agentic Systems</h3>
    <p>Multi-agent systems for automated software engineering, cloud infrastructure reconciliation, and agentic AI workloads.</p>
    <div class="research-card__papers">
      IaC Reconciliation (arXiv'25)
    </div>
  </div>
</div>
```

Key changes from current:
- "Learning" → "Learning Algorithms & Systems"; added Zodiac (NeurIPS'24) and TKDD'25 to papers; expanded description
- "Systems for AI Agents" → "Agentic Systems"; removed `research-card--emerging` class; updated description to be concrete; added IaC paper
- Serving & Inference and Edge & On-Device ML unchanged

**Step 2: Verify the site builds**

Run: `cd /Users/huiguan/Documents/website/guanh01.github.io && bundle exec jekyll build 2>&1 | tail -5`
Expected: "done" with no errors

**Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "rename research cards: Learning Algorithms & Systems, Agentic Systems"
```

---

### Task 3: Swap Selected Publication (CACTUS → WildFiT)

**Files:**
- Modify: `_pages/about.md` (the selected-papers list, the line with MobiSys'24 CACTUS)

**Step 1: Replace the CACTUS line with WildFiT**

Find this line:
```html
  <li><span class="venue-tag">MobiSys'24</span> <strong>CACTUS: Dynamically Switchable Context-aware micro-Classifiers for Efficient IoT Inference.</strong> M. Rastikerdar, J. Huang, S. Fang, H. Guan, D. Ganesan. <a href="http://guanh01.github.io/files/2024mobisys-cactus.pdf">[PDF]</a></li>
```

Replace with:
```html
  <li><span class="venue-tag">SenSys'26</span> <strong>WildFiT: Autonomous In-situ Model Adaptation for Resource-Constrained IoT Systems.</strong> M. Rastikerdar, J. Huang, H. Guan, D. Ganesan. <a href="https://arxiv.org/pdf/2409.07796">[PDF]</a></li>
```

Then reorder the list so entries are in reverse chronological order (SenSys'26 should come after MLSys'26 and before MLSys'25). The final selected publications list should be:

```html
<ul class="selected-papers__list" markdown="0">
  <li><span class="venue-tag">MLSys'26</span> <strong>ProTrain: Efficient LLM Training via Automatic Memory Management.</strong> H. Yang, J. Zhou, Y. Fu, X. Wang, R. Roane, H. Guan, T. Liu. <a href="https://arxiv.org/pdf/2406.08334">[PDF]</a></li>
  <li><span class="venue-tag">SenSys'26</span> <strong>WildFiT: Autonomous In-situ Model Adaptation for Resource-Constrained IoT Systems.</strong> M. Rastikerdar, J. Huang, H. Guan, D. Ganesan. <a href="https://arxiv.org/pdf/2409.07796">[PDF]</a></li>
  <li><span class="venue-tag">MLSys'25</span> <strong>DiffServe: Efficiently Serving Text-to-Image Diffusion Models with Query-Aware Model Scaling.</strong> S. Ahmad, Q. Yang, H. Wang, R. Sitaraman, H. Guan. <a href="https://arxiv.org/pdf/2411.15381">[PDF]</a></li>
  <li><span class="venue-tag">ASPLOS'24</span> <strong>Proteus: A High-Throughput Inference-Serving System with Accuracy Scaling.</strong> S. Ahmad, H. Guan, B. Friedman, T. Williams, R. Sitaraman, T. Woo. <a href="http://guanh01.github.io/files/2024proteus.pdf">[PDF]</a></li>
  <li><span class="venue-tag">NeurIPS'22</span> <strong>AutoMTL: A Programming Framework for Automating Efficient Multi-Task Learning.</strong> L. Zhang, X. Liu, H. Guan. <a href="http://guanh01.github.io/files/2022automtl.pdf">[PDF]</a></li>
</ul>
```

**Step 2: Verify the site builds**

Run: `cd /Users/huiguan/Documents/website/guanh01.github.io && bundle exec jekyll build 2>&1 | tail -5`
Expected: "done" with no errors

**Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "swap CACTUS for WildFiT in selected publications"
```

---

### Task 4: Add New News Entries

**Files:**
- Modify: `_pages/about.md` (the news-scroll div, insert new entries at the top before existing entries)

**Step 1: Insert the following news entries at the top of the news list (after the `<div class="news-scroll" markdown="1">` line, before the first existing entry)**

```markdown
- **[Jan. 2026]**: Congratulations to Mohammad and Jin for our work "WildFiT: Autonomous In-situ Model Adaptation for Resource-Constrained IoT Systems" accepted to SenSys'26.

- **[Jan. 2026]**: Congratulations to Hanmei for our work "ProTrain: Efficient LLM Training via Automatic Memory Management" accepted to MLSys'26.

- **[Jan. 2026]**: Congratulations to Kunjal for our work "Atom: Efficient On-Device Video-Language Pipelines Through Modular Reuse" accepted to MMSys'26.

- **[Jan. 2026]**: Congratulations to Kylie Lin for our work "A Four-Stage Framework of Visual Complexity and Trust as Mediated by Effort" accepted to PacificVis'26.

- **[Nov. 2025]**: Thanks for the support from the NSF for the DESC project on [Repurposing Batteryless SmartPhones as Long-lived and Adaptable Sensors for Sustainable and Scalable Environmental Monitoring](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2449995&HistoricalAwards=false).

- **[Nov. 2025]**: Thanks for the support from the NSF for the ACED project on [Revolutionizing Instrumental Analysis Using Foundation Models](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2435822&HistoricalAwards=false).

- **[Oct. 2025]**: Congratulations to Hanmei for our work "An Empirical Study of Microscaling Formats for Low-Precision LLM Training" accepted to ARITH'25.

- **[Oct. 2025]**: Congratulations to Saurabh for our work "Graph Neural Network Training Systems: A Performance Comparison of Full-Graph and Mini-Batch" accepted to VLDB'25.

```

Note: The exact dates (Jan/Nov/Oct) are approximate based on typical acceptance timelines. The user should adjust if needed.

**Step 2: Verify the site builds**

Run: `cd /Users/huiguan/Documents/website/guanh01.github.io && bundle exec jekyll build 2>&1 | tail -5`
Expected: "done" with no errors

**Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "add news entries for 2025-2026 publications and grants"
```

---

### Task 5: Final Verification

**Step 1: Build and serve the site**

Run: `cd /Users/huiguan/Documents/website/guanh01.github.io && bundle exec jekyll serve &`

**Step 2: Visually check localhost:4000**

Verify:
- Opening narrative reads naturally with "my group" / "we" voice
- AWS note mentions both cloud automation and code transformation
- "Learning Algorithms & Systems" card shows Zodiac and TKDD'25
- "Agentic Systems" card shows IaC paper and has concrete description (no "emerging")
- Selected publications show WildFiT (SenSys'26) instead of CACTUS
- News section has new 2025-2026 entries at the top
- No layout or styling regressions
