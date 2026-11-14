# Zenodo deposit fields and publication boundary

Prepared archive version: 1.0.0. Record title: **CCUS Schedule-Revision Audit: Code and Aggregate Checks**.

Use a manual Zenodo deposit of the allowlisted ZIP produced by `tools/build_public_archive.py`; do not automatically archive the entire repository for this deposit. First search the account for an existing record for this same research object to avoid duplicate deposits. Reuse an appropriate draft, or create a new version of the matching record when required. Do not replace a different study.

Metadata are provided in `.zenodo.json`, with the same seven creators and order as `CITATION.cff`. Preserve the existing CC BY 4.0 documentation/derived-data scope and the explicit exclusions in the rights notice; do not assign a new blanket software licence. Do not add fabricated ORCIDs, grant numbers, article DOIs or publication/acceptance claims.

After publishing, verify the public landing page, version, creators, licence scope, file name and downloaded file checksum. Record the version-specific DOI and, separately, the concept DOI if supplied. A reserved DOI or an unpublished draft is not evidence that the archive is publicly accessible.

Only after this verification should the README, citation metadata and manuscript data-availability/reference text say that the materials are archived in Zenodo. Until then, the immutable GitHub commit is the verifiable citation target.

Official documentation: https://help.zenodo.org/docs/deposit/create-new-upload/ ; https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/ ; https://help.zenodo.org/docs/deposit/manage-versions/
