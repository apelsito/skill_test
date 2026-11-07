---
name: byos-lab-node
description: Synthetic Node sandbox acceptance with a pinned registry package and a fixed execution delay.
allowed-tools: list_skill_files read_skill_file read_temp_file list_temp_files run_skill_script save_output_file
run_as_batch: false
---

Run `scripts/proof.js` exactly once with no arguments.
The sandbox installer resolves is-number 7.0.0 from package.json, verifies its
integrity, and disables lifecycle scripts. Do not install packages yourself,
change the declared requirement, or repeat the script.
The script waits exactly 30 seconds before writing `node-lab-proof.bin`.
Wait for the script without supplying arguments.

Save `node-lab-proof.bin` with save_output_file and return its download link.
The script verifies the package and writes exactly `BYOS Node LAB acceptance`
followed by LF. Preserve the original bytes.

The client may request Stop during installation or execution. Stop and confirmed
cleanup are separate results; never repeat a cancelled or uncertain execution.
