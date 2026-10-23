# radio-source-discovery

Open, benchmarked similarity search and rare-object discovery for radio survey images.

## Goal
Compare general vision foundation models (e.g. DINOv2) against radio-specific
self-supervised models for retrieving rare radio-galaxy morphologies, and package
the best approach as an open similarity-search tool over large radio surveys
(starting with LoTSS-DR2, benchmarked against MiraBest).

## Status
Two baseline experiments done with the same frozen DINOv2 (vits14) + FAISS
pipeline and the same leave-one-out needle-in-a-haystack protocol
(`src/eval/needle_in_haystack.py`):

| Dataset | Rare class | Rare share | Precision@20 | Random | Lift | Normalised gain |
|---|---|---|---|---|---|---|
| Aniyan & Thorat (2017) | bent-tailed (164 of 660) | 24.8% | 0.523 | 0.248 | 2.1x | 0.37 |
| MiraBest (Porter & Scaife 2023) | wide-angle-tail (52 of 1,256) | 4.1% | 0.074 (95% CI 0.059-0.090) | 0.041 | 1.8x | 0.03 |

**Honest reading:** frozen general-purpose DINOv2 embeddings beat random
guessing on both datasets, but the margin is modest on the first and very
small on the harder, rarer MiraBest task (about 1.5 correct results in each
top 20). The method does not yet look strong enough for rare-object
discovery as-is. Wide-angle-tails are a sub-type of FRI, so confusion with
ordinary FRI sources is expected and worth analysing (notebook 02, Fig. 6).

**Hit-rate caveat:** hit-rate@20 is only meaningful next to its chance level.
For Aniyan & Thorat, random retrieval already gives a hit-rate of 0.997, so
the reported 0.988 is not evidence of anything. For MiraBest it is 0.77
against a chance level of 0.57.

Notebooks: `notebooks/01_dinov2_baseline_bent_tailed.ipynb`,
`notebooks/02_mirabest_crosscheck.ipynb`. Plan: `docs/plan.md`. Paper
notes: `literature/notes.md`.

Still untested: the real rare-object regime (<<1% prevalence, millions of
sources), radio-specific embeddings, and larger DINOv2 backbones.

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
2. ~~Cross-check on MiraBest~~ done (weak result, see Status); next: scale to a LoTSS-DR2 subset
3. Compare against a radio-specific self-supervised model
4. Cross-survey generalisation + blind rediscovery test on known rare objects (e.g. ORCs)
5. Package as a small tool; write up results
