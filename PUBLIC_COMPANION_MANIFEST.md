# Public companion and archive manifest

The curated deposit is the exact file list in `archive_allowlist.txt`. Build it with `python tools/build_public_archive.py --output-dir ../public-release`.

The ZIP contains a SHA-256 `FILE_MANIFEST.json` for every included payload file. The outer archive hash is written alongside the ZIP. This archive is narrower than the full repository: legacy data/ contents, journal PDFs, reviewer replies, author records, raw source workbooks and private project-level model inputs are not included.

Retain the exact source commit and cite the version-specific Zenodo DOI only after successful publication. The initial snapshot does not claim an assigned DOI.
