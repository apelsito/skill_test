import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

source = Path(args.input).read_text(encoding="utf-8")
Path(args.output).write_text(
    "BYOS OpenShift Python sandbox executed successfully.\n\n" + source,
    encoding="utf-8",
)
