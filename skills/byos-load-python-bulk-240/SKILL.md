---
name: byos-load-python-bulk-240
description: Generate one original native sandbox load-test proof per synthetic wiki page.
allowed-tools: run_skill_script
run_as_batch: true
---

# Native sandbox load proof for Bulk analysis

For each page, the script-mode executor runs `scripts/generate_python-proof.py`
once with the staged Markdown page as input. The program waits for 240 seconds
and emits the original proof file. It requires no dependencies or network access.

The original file is 23 bytes with SHA-256
`340c29d7751112a3c8d2de760538370b84bc21e0c8355f672a8a68a7687a37f3`.
