# Project plan (summary)

See the full project plan PDF: "Open Similarity Search and Rare-Object
Discovery for Radio Surveys".

## Phase 1 - Baseline
- [x] Get a first dataset running: Aniyan & Thorat (2017) via Kaggle
      (FRI/FRII/bent-tailed, non-augmented copy only)
- [x] Extract DINOv2 (vits14) embeddings — 660 images, 384-dim
- [x] Needle-in-a-haystack evaluation, not just eyeballing neighbours:
      precision@20 = 0.523 (std 0.235) vs random baseline 0.248 (2.10x lift),
      hit-rate@20 = 0.988
- [x] PCA visualisation of embedding space by class
- [x] Explicit limitations write-up (see notebook Section 6)
- [ ] Re-run with `dinov2_vitb14` as a free ablation (one-line change)
- [ ] Write up literature notes for papers 1-4 (see literature/notes.md)

## Phase 2 - Scale up and compare
- [ ] Cross-check the baseline on MiraBest (second, independent dataset)
- [ ] Download a small LoTSS-DR2 cutout sample
- [ ] Swap `IndexFlatIP` for an approximate index (`IndexIVFFlat` /
      `IndexHNSWFlat`) once operating at larger scale
- [ ] Compare DINOv2 vs a radio-specific self-supervised model
- [ ] Get bent-tailed / wide-angle-tail labels at LoTSS scale from Radio
      Galaxy Zoo classifications

## Phase 3 - Evaluate at scale
- [ ] Cross-survey generalisation test: index built on LoTSS-DR2, query
      with ASKAP EMU pilot cutouts, no retraining
- [ ] Blind rediscovery test on known rare objects (e.g. published ORCs)
- [ ] Error analysis: look at the lowest-precision bent-tailed queries from
      the Phase 1 run — are they systematically different?

## Phase 4 - Package and share
- [ ] Simple web interface or CLI tool
- [ ] Model card, tests, Docker
- [ ] Share repo link with UNISA supervisors
