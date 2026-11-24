"""Emit a deterministic artifact for execution, cancellation, or live output."""

import argparse
import hashlib
import json
import time
from pathlib import Path

PAYLOAD = b"BYOS Python acceptance\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--delay", type=int, default=0)
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    if not 0 <= args.delay <= 30:
        parser.error("--delay must be between 0 and 30 seconds")
    if args.live and args.delay:
        parser.error("--live uses its own 30-second delay")
    if args.live:
        print("BYOS live output: started", flush=True)
        args.delay = 30
    time.sleep(args.delay)
    args.output.write_bytes(PAYLOAD)
    if args.live:
        print("BYOS live output: finished", flush=True)
    print(json.dumps({"bytes": len(PAYLOAD), "sha256": hashlib.sha256(PAYLOAD).hexdigest()}))


if __name__ == "__main__":
    main()
