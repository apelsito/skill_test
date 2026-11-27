---
name: byos-load-python-chat
description: Generate and deliver an original Python proof file from one native BYOS sandbox for a load test.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files run_skill_script save_output_file
run_as_batch: false
---

# Native sandbox load proof

Run the bundled `scripts/emit.py` once with `--output python-proof.bin`.
Use `save_output_file` to deliver the file from that run and return its
download link. Preserve the original bytes.

The program includes a fixed 100-second wait so several native sandboxes can
be observed running at once. Wait for it to finish. It needs no inputs,
network access, additional arguments, or confirmation.

The original file is 23 bytes with SHA-256
`340c29d7751112a3c8d2de760538370b84bc21e0c8355f672a8a68a7687a37f3`.
