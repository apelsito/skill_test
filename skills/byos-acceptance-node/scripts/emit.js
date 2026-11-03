"use strict";

const fs = require("node:fs");
const crypto = require("node:crypto");
const payload = Buffer.from("BYOS Node acceptance\n", "utf8");

async function main() {
  fs.writeFileSync("node-proof.bin", payload);
  console.log(JSON.stringify({ bytes: payload.length, sha256: crypto.createHash("sha256").update(payload).digest("hex") }));
}

main();
