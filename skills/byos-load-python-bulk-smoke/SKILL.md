---
name: byos-load-python-bulk-smoke
description: Verify short execution, nonzero exit and cancellation cleanup on synthetic pages.
allowed-tools: run_skill_script
run_as_batch: true
---

# Native sandbox lifecycle smoke checks

Run `scripts/generate_python-smoke.py` on a staged synthetic Markdown page
with one of the fixed `BYOS-SMOKE` markers. The short case writes the original
23-byte proof after two seconds, the failure case exits with code 7 and the
blocked case waits for one short-lived Python child. The fixture uses only the
standard library and has no network or external dependency.
