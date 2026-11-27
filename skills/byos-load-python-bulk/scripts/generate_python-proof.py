"""Generate an original proof from one staged synthetic wiki page."""

import argparse
import hashlib
import json
import time
from pathlib import Path

PAYLOAD = b"BYOS Python acceptance\n"
DWELL_SECONDS = 100


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=Path("python-proof.bin"))
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error("--input must point to the staged wiki page")
    time.sleep(DWELL_SECONDS)
    args.output.write_bytes(PAYLOAD)
    print(json.dumps({"bytes": len(PAYLOAD), "sha256": hashlib.sha256(PAYLOAD).hexdigest()}))


if __name__ == "__main__":
    main()
