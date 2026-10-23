"""
Needle-in-a-haystack retrieval evaluation for a rare class.

Extracted from notebooks/01_dinov2_baseline_bent_tailed.ipynb (Section 5.4),
so the same evaluation protocol can be reused as the pipeline scales to
LoTSS-DR2 / EMU and as new embedding models are compared.

Protocol: for each example of the rare class, treat it as a query (excluding
itself from its own results), search the full index, and measure whether
and how often true rare-class examples appear in the top k. Reported as a
mean + standard deviation over all rare-class queries, plus a hit-rate, and
always alongside a random-retrieval baseline (see `random_baseline`) since a
precision number alone is not interpretable without one.
"""
from __future__ import annotations

import numpy as np


def evaluate_needle_in_haystack(index, embeddings_normed, labels, rare_label, k=20):
    """Leave-one-out retrieval evaluation for a designated rare class.

    Parameters
    ----------
    index : a FAISS index already built over embeddings_normed
    embeddings_normed : (n, d) float32 array, L2-normalised
    labels : (n,) array of class labels, aligned with embeddings_normed
    rare_label : the label value to treat as the rare/target class
    k : number of neighbours to retrieve per query

    Returns
    -------
    dict with n_queries, precision_at_k_mean, precision_at_k_std,
    precision_at_k_values (per-query array), hit_rate_at_k, k.
    """
    rare_indices = np.where(labels == rare_label)[0]
    precisions = []
    hit_at_k = []

    for qi in rare_indices:
        query_vec = embeddings_normed[qi : qi + 1]
        _, indices = index.search(query_vec, k + 1)
        retrieved = indices[0]
        retrieved = retrieved[retrieved != qi][:k]
        retrieved_labels = labels[retrieved]

        precision_at_k = float((retrieved_labels == rare_label).sum()) / k
        precisions.append(precision_at_k)
        hit_at_k.append(bool((retrieved_labels == rare_label).any()))

    precisions = np.array(precisions)
    return {
        "n_queries": len(rare_indices),
        "precision_at_k_mean": float(precisions.mean()),
        "precision_at_k_std": float(precisions.std()),
        "precision_at_k_values": precisions,
        "hit_rate_at_k": float(np.mean(hit_at_k)),
        "k": k,
    }


def random_baseline(labels, rare_label):
    """Expected precision@k under uniformly random retrieval: just the
    rare class's share of the full population."""
    return float((labels == rare_label).sum()) / len(labels)


def random_hit_rate(n_total, n_rare, k=20):
    """Expected hit-rate@k under uniformly random retrieval.

    Hit-rate (at least one rare example in the top k) is only interpretable
    next to this number. When the rare class is common (e.g. ~25% of the
    data) random retrieval already scores ~1.0, so a high hit-rate says
    nothing about the method. The query itself is excluded from the pool.
    """
    from math import comb

    pool = n_total - 1
    positives = n_rare - 1
    negatives = pool - positives
    if negatives < k:
        return 1.0
    return 1.0 - comb(negatives, k) / comb(pool, k)


def normalised_gain(precision, baseline):
    """Prevalence-adjusted score: 0 = no better than random, 1 = perfect.

    Raw lift (precision / baseline) flatters rarer classes, so compare
    datasets with different rare-class shares using this instead.
    """
    return (precision - baseline) / (1.0 - baseline)
