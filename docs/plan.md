# Project plan (summary)

See the full project plan PDF: "Open Similarity Search and Rare-Object
Discovery for Radio Surveys".

## Phase 1 - Baseline
- [x] Get a first dataset running: Aniyan & Thorat (2017) via Kaggle
      (FRI/FRII/bent-tailed, non-augmented copy only)
- [x] Extract DINOv2 (vits14) embeddings — 660 images, 384-dim
- [x] Needle-in-a-haystack evaluation, not just eyeballing neighbours:
      precision@20 = 0.523 (std 0.235) vs random baseline 0.248 (2.10x lift).
      (Hit-rate@20 = 0.988 is NOT informative here: random retrieval scores
      0.997 because bent-tailed is ~25% of the data.)
- [x] PCA visualisation of embedding space by class
- [x] Explicit limitations write-up (see notebook Section 6)
- [ ] Re-run with `dinov2_vitb14` as a free ablation (one-line change)
- [ ] Write up literature notes for papers 1-4 (see literature/notes.md)

## Phase 2 - Scale up and compare
- [x] Cross-check the baseline on MiraBest (notebook 02): wide-angle-tail
      (52 of 1,256, 4.1%), precision@20 = 0.074 (95% CI 0.059-0.090) vs random
      0.041, lift 1.8x, normalised gain 0.03 (Phase 1: 0.37). Hit-rate 0.77 vs
      chance 0.57. Beats random, but barely; frozen DINOv2 is weak here.
- [ ] Analyse the MiraBest failure: is the confusion mostly with ordinary
      FRI sources (WAT is an FRI sub-type)? See notebook 02 Fig. 6.
- [ ] Rarity sweep: subsample the rare class to 10%, 1%, 0.1% and re-run
- [ ] Try `dinov2_vitb14` / `vitl14` on both datasets (same code)
- [ ] Add a supervised or fine-tuned baseline to see how much headroom exists
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
