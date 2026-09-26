# Literature notes

One row per paper: data used, model, metric, main result, limitations, a gap you could address.

| # | Paper | Data | Model | Metric | Main result | Limitations | Possible gap |
|---|-------|------|-------|--------|--------------|--------------|---------------|
| 0 | **Aniyan & Thorat (2017)** — dataset + CNN classifier we build on directly | VLA FIRST, ~600 imgs (FRI/FRII/bent-tailed) | Supervised CNN | Precision (bent-tailed) | ~95% precision (supervised) | Fixed label set; can't flag unseen classes | Our similarity-search reframing (below) |
| 1 | MiraBest (Porter & Scaife 2023) | NVSS/FIRST, 1,256 imgs | n/a (dataset) | n/a | Standardised FRI/FRII benchmark | Small, only 2 classes + subtypes | Cross-check our result on this second dataset |
| 2 | Self-supervised classification (2025, A&A) | LoTSS-DR2 | Self-supervised + clustering | 12-class map | Continuous morphology map beats hard labels | Needs labelled subset to calibrate | Try on a different survey |
| 3 | Contrastive learning + anomaly search (2024) | ASKAP EMU pilot, MeerKAT GPS | SimCLR | Visual anomaly ranking | Found peculiar objects unsupervised | Manual visual vetting still needed | Automate vetting confidence |
| 4 | ORC discovery via object detection (2025) | ASKAP EMU year 1 | Object detector | Recall on known ORCs | 5 new ORCs found | Object detection is not similarity search | Combine with retrieval approach |
| 5 | Morphology in representation space (2026) | LoTSS-DR3 (13M+) | Same as #2, scaled | New-class discovery | 6 new classes found | Clustering-based, not interactive search | Build an interactive tool instead |
| 6 | COSFIRE anomaly filters (2025) | Small radio benchmark | COSFIRE + LOF | G-Mean | 79% vs 77% (deep baseline) | Small gap over deep learning | Use as a cheap baseline |

## Our own baseline (notebooks/01_dinov2_baseline_bent_tailed.ipynb)

- **Data:** Aniyan & Thorat (2017) via Kaggle mirror, non-augmented copy only. 660 images: FRI 196, FRII 300, bent-tailed 164.
- **Model:** DINOv2 `vits14`, frozen, no fine-tuning. Grayscale replicated to 3 channels.
- **Protocol:** leave-one-out needle-in-a-haystack, precision@20 and hit-rate@20 for retrieving bent-tailed as the "rare" class.
- **Result:** precision@20 = 0.523 (std 0.235) vs random baseline 0.248 -> 2.10x lift. Hit-rate@20 = 0.988.
- **Caveat (self-flagged):** bent-tailed is ~25% of this dataset, not survey-scale rare (<<1%). This validates the method on real data; it does not yet test the actual rare-object regime.
- **Cheapest next step:** re-run with `dinov2_vitb14` (one string change) before investing in a radio-specific model — free ablation, same code.

Fill in rows 1-6 as you read each paper properly. This is a starting skeleton, not a finished review.
