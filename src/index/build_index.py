"""
Build a FAISS index from saved embeddings and run a nearest-neighbour query.

Usage:
    python src/index/build_index.py --embeddings data/processed/embeddings/mirabest_dinov2.npz --query-name <image_stem> --k 10
"""
import argparse

import faiss
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--embeddings", required=True)
    parser.add_argument("--query-name", required=True, help="Name (stem) of the query image")
    parser.add_argument("--k", type=int, default=10)
    args = parser.parse_args()

    data = np.load(args.embeddings, allow_pickle=True)
    embeddings = data["embeddings"].astype("float32")
    names = data["names"]

    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    try:
        qi = list(names).index(args.query_name)
    except ValueError:
        raise SystemExit(f"Query name {args.query_name!r} not found among {len(names)} embeddings")

    scores, idx = index.search(embeddings[qi : qi + 1], args.k + 1)
    print(f"Nearest neighbours for {args.query_name}:")
    for score, i in zip(scores[0], idx[0]):
        if names[i] == args.query_name:
            continue
        print(f"  {names[i]:30s}  similarity={score:.3f}")


if __name__ == "__main__":
    main()
