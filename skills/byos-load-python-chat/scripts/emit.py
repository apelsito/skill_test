"""Write the original native-sandbox proof after a fixed load-test interval."""

import argparse
import hashlib
import json
import time
from pathlib import Path

PAYLOAD = b"BYOS Python acceptance\n"
DWELL_SECONDS = 100


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    time.sleep(DWELL_SECONDS)
    args.output.write_bytes(PAYLOAD)
    print(json.dumps({"bytes": len(PAYLOAD), "sha256": hashlib.sha256(PAYLOAD).hexdigest()}))


if __name__ == "__main__":
    main()
