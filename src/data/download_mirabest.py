"""
Download and unpack the MiraBest dataset.

Dataset: Porter & Scaife (2023), "MiraBest: a dataset of morphologically
classified radio galaxies for machine learning", Zenodo 10.5281/zenodo.4288837.

Usage:
    python src/data/download_mirabest.py --out data/raw/mirabest
"""
import argparse
import pathlib

ZENODO_RECORD = "https://zenodo.org/records/4288837"  # confirm exact file URLs on the page before running


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("data/raw/mirabest"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    print(f"Visit {ZENODO_RECORD} to confirm current file names, then download into {args.out}.")
    print("This script is a placeholder: fill in the direct file URL(s) once confirmed.")


if __name__ == "__main__":
    main()
