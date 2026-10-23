# Literature notes

One row per paper: data used, model, metric, main result, limitations, a gap you could address.

| # | Paper | Data | Model | Metric | Main result | Limitations | Possible gap |
|---|-------|------|-------|--------|--------------|--------------|---------------|
| 0 | **Aniyan & Thorat (2017)** — dataset + CNN classifier we build on directly | VLA FIRST, ~600 imgs (FRI/FRII/bent-tailed) | Supervised CNN | Precision (bent-tailed) | (reported accuracy not yet verified against the paper) | Fixed label set; can't flag unseen classes | Our similarity-search reframing (below) |
| 1 | MiraBest (Porter & Scaife 2023) | NVSS/FIRST, 1,256 imgs | n/a (dataset) | n/a | Standardised FRI/FRII benchmark with 10 reduced labels incl. wide-angle-tail (52) | Small; Zenodo record 5588282 (not 4288837) carries the sub-types | Used in notebook 02 as our second dataset |
| 2 | Self-supervised classification (2025, A&A) | LoTSS-DR2 | Self-supervised + clustering | 12-class map | Continuous morphology map beats hard labels | Needs labelled subset to calibrate | Try on a different survey |
| 3 | Contrastive learning + anomaly search (2024) | ASKAP EMU pilot, MeerKAT GPS | SimCLR | Visual anomaly ranking | Found peculiar objects unsupervised | Manual visual vetting still needed | Automate vetting confidence |
| 4 | ORC discovery via object detection (2025) | ASKAP EMU year 1 | Object detector | Recall on known ORCs | 5 new ORCs found | Object detection is not similarity search | Combine with retrieval approach |
| 5 | Morphology in representation space (2026) | LoTSS-DR3 (13M+) | Same as #2, scaled | New-class discovery | 6 new classes found | Clustering-based, not interactive search | Build an interactive tool instead |
| 6 | COSFIRE anomaly filters (2025) | Small radio benchmark | COSFIRE + LOF | G-Mean | 79% vs 77% (deep baseline) | Small gap over deep learning | Use as a cheap baseline |

## Our own baselines

### Notebook 01: Aniyan & Thorat (2017), bent-tailed
- **Data:** Kaggle mirror, non-augmented copy only. 660 images: FRI 196, FRII 300, bent-tailed 164 (24.8%).
- **Model:** DINOv2 `vits14`, frozen. Grayscale replicated to 3 channels.
- **Protocol:** leave-one-out needle-in-a-haystack, precision@20.
- **Result:** precision@20 = 0.523 (std 0.235) vs random 0.248, lift 2.1x, normalised gain 0.37.
- **Correction:** the logged hit-rate@20 = 0.988 is not informative. Random retrieval gives 0.997 on this dataset.

### Notebook 02: MiraBest (Porter & Scaife 2023), wide-angle-tail
- **Data:** Zenodo record 5588282 via the dataset's own loader (`MiraBest_F`). 1,256 images; all ten reduced-label counts verified against the published Table 2. Rare class = labels 1 and 4 (wide-angle-tail, 49 confident + 3 uncertain) = 52 images (4.1%).
- **Result:** precision@20 = 0.074 (bootstrap 95% CI 0.059-0.090) vs random 0.041, lift 1.8x, normalised gain 0.03 (CI 0.02-0.05). Hit-rate@20 = 0.769 vs chance 0.567.
- **Reading:** statistically better than chance, practically weak. Normalised gain fell from 0.37 to 0.03 on the rarer, harder task.
- **Caveats:** different catalogues and pixel scales across datasets; WAT is an FRI sub-type so the "other" class contains many look-alikes; Phase 1 per-query data was not attached in this run, so the datasets were not compared statistically.

### Next
Rarity sweep, larger DINOv2 backbones, a radio-specific embedding, and a supervised baseline to measure headroom.

Fill in rows 2-6 as you read each paper properly. This is a starting skeleton, not a finished review.
