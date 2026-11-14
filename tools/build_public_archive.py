#!/usr/bin/env python3
"""Build a deterministic, allowlisted public archive without third-party rows."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    names = [x.strip() for x in (ROOT / "archive_allowlist.txt").read_text().splitlines() if x.strip() and not x.startswith("#")]
    if len(set(names)) != len(names):
        raise SystemExit("Duplicate archive path")
    payload = {}
    for name in names:
        q = PurePosixPath(name)
        p = ROOT / name
        if q.is_absolute() or ".." in q.parts or p.is_symlink() or not p.is_file():
            raise SystemExit("Unsafe or missing allowlisted path: " + name)
        if ROOT not in p.resolve().parents:
            raise SystemExit("Path escapes repository: " + name)
        payload[name] = p.read_bytes()
    version = (ROOT / "VERSION").read_text().strip()
    manifest = {"version": version, "scope": "Curated code, synthetic examples and aggregate checks; not a complete source-data archive", "files": {name: {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()} for name, data in sorted(payload.items())}}
    payload["FILE_MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    dest = args.output_dir / ("CCUS_Audit_v" + version + "_PUBLIC.zip")
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(payload.items()):
            entry = zipfile.ZipInfo(name, (2026, 11, 14, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, data)
    with zipfile.ZipFile(dest) as z:
        if z.testzip() is not None:
            raise SystemExit("Archive CRC check failed")
        for name, meta in manifest["files"].items():
            if hashlib.sha256(z.read(name)).hexdigest() != meta["sha256"]:
                raise SystemExit("Archive content hash failed: " + name)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    dest.with_suffix(".sha256").write_text(digest + "  " + dest.name + "\n", encoding="utf-8")
    print(f"PASS: {len(manifest['files'])} allowlisted files plus manifest; {dest.name}; SHA-256 {digest}")


if __name__ == "__main__":
    main()
