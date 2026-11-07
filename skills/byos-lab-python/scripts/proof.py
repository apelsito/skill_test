"""Write a known original after scientific-package verification and a bounded wait."""
import argparse
import hashlib
import json
from pathlib import Path
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--delay', type=int, default=0)
    args = parser.parse_args()
    if not 0 <= args.delay <= 240:
        parser.error('--delay must be between 0 and 240 seconds')
    if args.output != Path(args.output).name or args.output in ('', '.', '..'):
        parser.error('--output must name a file in the working directory')
    import numpy
    assert numpy.__version__ == '2.2.6' and int(numpy.array([1, 2, 3]).sum()) == 6
    time.sleep(args.delay)
    payload = b'BYOS Python LAB acceptance\n'
    Path(args.output).write_bytes(payload)
    print(json.dumps({'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest(), 'numpy_version': numpy.__version__}))


if __name__ == '__main__':
    main()
