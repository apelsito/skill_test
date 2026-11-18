---
name: byos-acceptance-python-chat
description: Verify Python execution and file delivery in a Process Studio Chat.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files run_skill_script save_output_file
run_as_batch: false
---

# Python acceptance for Chat

Use the bundled `scripts/emit.py` and `scripts/manifest.json`.

Run `scripts/emit.py` once with arguments `--output python-proof.bin`. Save the emitted file with `save_output_file` and return the download link. Preserve the emitted bytes.

The output is 23 bytes, with SHA-256 `340c29d7751112a3c8d2de760538370b84bc21e0c8355f672a8a68a7687a37f3`. No input files or dependencies are required.

Use `--delay 30` only when the user explicitly asks to test cancellation.
