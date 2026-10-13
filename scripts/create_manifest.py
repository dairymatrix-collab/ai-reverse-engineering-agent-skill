#!/usr/bin/env python3
"""Create a deterministic, offline manifest for an authorized analysis target."""
from __future__ import annotations
import argparse, hashlib, json, mimetypes, os
from pathlib import Path

def sha256(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while data := f.read(chunk):
            h.update(data)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=Path("rea-manifest.json"))
    args = ap.parse_args()
    root = args.target.resolve()
    if not root.exists():
        ap.error(f"target does not exist: {root}")
    paths = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
    records = []
    for path in paths:
        stat = path.stat()
        rel = path.name if root.is_file() else str(path.relative_to(root))
        records.append({
            "path": rel,
            "size": stat.st_size,
            "sha256": sha256(path),
            "media_type": mimetypes.guess_type(path.name)[0],
        })
    payload = {"schema": "rea-manifest/v1", "target": str(root), "files": records}
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {len(records)} file record(s) to {args.output.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
