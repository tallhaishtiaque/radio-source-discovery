# radio-source-discovery

Open, benchmarked similarity search and rare-object discovery for radio survey images.

## Goal
Compare general vision foundation models (e.g. DINOv2) against radio-specific
self-supervised models for retrieving rare radio-galaxy morphologies, and package
the best approach as an open similarity-search tool over large radio surveys
(starting with LoTSS-DR2, benchmarked against MiraBest).

## Status
Phase 1 baseline complete: DINOv2 (frozen, vits14) + FAISS similarity
search, evaluated with a leave-one-out needle-in-a-haystack protocol on the
Aniyan & Thorat (2017) FRI/FRII/bent-tailed dataset. Precision@20 = 0.523
(std 0.235) vs a random baseline of 0.248 — a 2.10x lift — with a 0.988
hit-rate@20. See `notebooks/01_dinov2_baseline_bent_tailed.ipynb` for the
full write-up, `docs/plan.md` for the phased plan, and `literature/notes.md`
for paper-by-paper notes.

Note: bent-tailed is ~25% of this small dataset, not survey-scale rare. This
result validates the method on real data; the actual rare-object regime
(<<1% prevalence, millions of sources) is still to be tested (Phase 2-3).

## Structure
- `data/raw/` — untouched downloads (not committed; see data/README.md)
- `data/processed/` — cutouts, resized images, embeddings (not committed)
- `src/data/` — download and preprocessing scripts
- `src/features/` — embedding extraction (DINOv2, baselines)
- `src/index/` — FAISS indexing and nearest-neighbour search
- `src/eval/` — retrieval metrics, blind rediscovery tests
- `notebooks/` — exploratory analysis
- `models/` — trained/fine-tuned model checkpoints (not committed)
- `literature/` — reading notes
- `docs/` — project plan, research outline drafts

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Roadmap
See `docs/plan.md` for the full phased checklist. Short version:
1. ~~Baseline: DINOv2 + FAISS on a first dataset, evaluated properly~~ done
2. Cross-check on MiraBest; scale to a LoTSS-DR2 subset
3. Compare against a radio-specific self-supervised model
4. Cross-survey generalisation + blind rediscovery test on known rare objects (e.g. ORCs)
5. Package as a small tool; write up results
