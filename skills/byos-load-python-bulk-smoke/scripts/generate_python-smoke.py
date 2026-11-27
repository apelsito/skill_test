"""Verify documentation fixture cases in the native sandbox."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


PROOF = b"BYOS Python acceptance\n"
MODES = {"BYOS-SMOKE short", "BYOS-SMOKE failure", "BYOS-SMOKE blocked"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    with args.input.open("rb") as source:
        lines = source.read(65536).decode("utf-8").splitlines()
    selected = [line for line in lines if line in MODES]
    if len(selected) != 1:
        parser.error("require exactly one fixed BYOS-SMOKE marker")
    if selected[0] == "BYOS-SMOKE short":
        time.sleep(2)
        args.output.write_bytes(PROOF)
        return 0
    if selected[0] == "BYOS-SMOKE failure":
        return 7
    child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    print(json.dumps({"event": "smoke_child_started", "child_pid": child.pid}), flush=True)
    return child.wait() or 8


if __name__ == "__main__":
    raise SystemExit(main())
