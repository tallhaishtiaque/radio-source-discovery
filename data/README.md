# Data

Raw and processed data are not committed to the repo (see .gitignore).

## Dataset used in the current baseline (notebooks/01_dinov2_baseline_bent_tailed.ipynb)

**Aniyan & Thorat (2017) radio galaxy dataset**, Kaggle mirror:
`manangupta15/radio-galaxy-images-frifriibent-tailed` (MIT licensed).
FRI / FRII / bent-tailed cutouts from the VLA FIRST survey.

To run: on Kaggle, "+ Add Input" and search "Radio Galaxy Images -
FRI,FRII,Bent-tailed", enable a GPU accelerator and Internet access (needed
to pull DINOv2 weights via torch.hub).

**Important:** the Kaggle copy ships a `dataset_augmented` folder of rotated
duplicates alongside the originals. Always exclude it — the notebook's
loader does this explicitly (see `src/data/` below) — otherwise retrieval
metrics are inflated by a source matching its own rotated copy.

Actual class counts used in the baseline run (`MAX_PER_CLASS = 300`):
FRI 196, FRII 300, bent-tailed 164 (660 total).

## Planned scale-up datasets
- **MiraBest**: Zenodo 10.5281/zenodo.4288837 — a second, independent
  FRI/FRII benchmark with confidence flags, useful as a cross-dataset check.
- **LoTSS-DR2**: https://lofar-surveys.org/dr2_release.html — the real
  survey-scale target (millions of sources). Start with a small cutout
  sample, not the full catalogue, until the pipeline is validated further.
- **ASKAP EMU pilot** — for the cross-survey generalisation test described
  in the notebook's Section 7.
