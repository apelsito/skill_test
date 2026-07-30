const fs = require("node:fs");

function argument(name) {
  const index = process.argv.indexOf(name);
  if (index < 0 || index + 1 >= process.argv.length) {
    throw new Error(`Missing ${name}`);
  }
  return process.argv[index + 1];
}

const inputPath = argument("--input");
const outputPath = argument("--output");
const source = fs.readFileSync(inputPath, "utf8");
fs.writeFileSync(
  outputPath,
  `BYOS OpenShift Node sandbox executed successfully.\n\n${source}`,
  "utf8",
);
