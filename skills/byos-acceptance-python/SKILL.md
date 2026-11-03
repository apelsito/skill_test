---
name: byos-acceptance-python
description: Produce a fixed Python artifact to verify BYOS execution, delivery and cancellation.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files run_skill_script save_output_file
run_as_batch: false
---

# Python execution acceptance

Use the bundled `scripts/emit.py` and its `scripts/manifest.json` contract.
Run the script once with `--output python-proof.bin` and omit `--delay` for the normal case.
Save the emitted file with `save_output_file` and return the download link.
Preserve the emitted bytes. Do not recreate the file from this instruction or rewrite it.

The artifact contains exactly the UTF-8 bytes of `BYOS Python acceptance` followed by LF.
23 bytes, SHA-256 `340c29d7751112a3c8d2de760538370b84bc21e0c8355f672a8a68a7687a37f3`.
The script prints its independently calculated byte count and SHA-256.

For the cancellation case, add `--delay 30`. The script waits before writing, so
cancel the active run while it is waiting. Cancellation and remote cleanup are separate outcomes.

Chat and Bulk Run use the same script and artifact. To select this skill in the
Bulk Run Analysis tab, enable its batch override in My Skills first. No business
input or extra dependency is required. Use an existing authorized Batch Run.
