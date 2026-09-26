"""
Extract DINOv2 embeddings for a folder of image cutouts.

Usage:
    python src/features/extract_dinov2.py --images data/processed/mirabest_png --out data/processed/embeddings/mirabest_dinov2.npz

Notes:
- Uses torch.hub to load a pretrained DINOv2 ViT-S/14 model (small, fast to
  start with; swap for ViT-B/14 or ViT-L/14 once the pipeline works).
- Radio images are single-channel; this script repeats the channel to 3
  to match DINOv2's expected input. Revisit this once you compare against
  a radio-specific model, since this is a real domain-gap simplification.
"""
import argparse
import pathlib

import numpy as np
import torch
from PIL import Image
from torchvision import transforms
from tqdm import tqdm

TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def load_model(device: str):
    model = torch.hub.load("facebookresearch/dinov2", "dinov2_vits14")
    model.eval().to(device)
    return model


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images", type=pathlib.Path, required=True)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    model = load_model(args.device)
    paths = sorted(args.images.glob("*.png"))
    if not paths:
        raise SystemExit(f"No .png files found in {args.images}")

    embeddings = []
    names = []
    with torch.no_grad():
        for p in tqdm(paths, desc="Extracting embeddings"):
            img = Image.open(p).convert("L")
            x = TRANSFORM(img).unsqueeze(0).to(args.device)
            feat = model(x).squeeze(0).cpu().numpy()
            embeddings.append(feat)
            names.append(p.stem)

    np.savez(args.out, embeddings=np.stack(embeddings), names=np.array(names))
    print(f"Saved {len(names)} embeddings to {args.out}")


if __name__ == "__main__":
    main()
