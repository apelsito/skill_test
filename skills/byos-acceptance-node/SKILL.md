---
name: byos-acceptance-node
description: Produce a fixed Node artifact to verify BYOS execution, delivery and cancellation.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files run_skill_script save_output_file
run_as_batch: false
---

# Node execution acceptance

Use the bundled `scripts/emit.js` and its `scripts/manifest.json` contract.
Run `scripts/emit.js` once without arguments for the normal case.
It writes only the fixed filename `node-proof.bin` in the current workspace.
Save the emitted file with `save_output_file` and return the download link.
Preserve the emitted bytes. Do not recreate the file from this instruction or rewrite it.

The artifact contains exactly the UTF-8 bytes of `BYOS Node acceptance` followed by LF.
21 bytes, SHA-256 `479e9b0f8dd5333ae03ed54464cb379f071a279018f728f94571f403d760f22f`.
The script prints its independently calculated byte count and SHA-256.

For the cancellation case, run `scripts/cancel30.js` without arguments instead.
This entry waits exactly 30 seconds before writing the same fixed artifact, so
cancel the active run while it is waiting. Cancellation and remote cleanup are separate outcomes.

Chat and Bulk Run use the same script and artifact. To select this skill in the
Bulk Run Analysis tab, enable its batch override in My Skills first. No business
input or extra dependency is required. Use an existing authorized Batch Run.
