---
name: byos-lab-python
description: Synthetic Python sandbox acceptance with a pinned scientific wheel and bounded execution delay.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files run_skill_script save_output_file
run_as_batch: false
---

Run `scripts/proof.py` exactly once with `--output python-lab-proof.bin`.
The sandbox installer resolves requirements.txt before the script. Do not install
packages yourself, change the declared requirement, or repeat the script.
An explicitly requested `--delay` is an integer from 0 through 240 seconds;
wait for the script and preserve those arguments.

Save `python-lab-proof.bin` with save_output_file and return its download link.
The script verifies NumPy 2.2.6 and writes exactly `BYOS Python LAB acceptance`
followed by LF. Preserve the original bytes.

The client may request Stop during installation or execution. Stop and confirmed
cleanup are separate results; never repeat a cancelled or uncertain execution.
