"use strict";
const fs = require('node:fs');
const crypto = require('node:crypto');
const isNumber = require('is-number');
const version = require('is-number/package.json').version;
if (version !== '7.0.0' || !isNumber(7) || isNumber('LAB')) throw new Error('Package verification failed');
setTimeout(() => {
  const payload = Buffer.from('BYOS Node LAB acceptance\n', 'utf8');
  fs.writeFileSync('node-lab-proof.bin', payload);
  console.log(JSON.stringify({bytes: payload.length, sha256: crypto.createHash('sha256').update(payload).digest('hex'), package_version: version}));
}, 30000);
