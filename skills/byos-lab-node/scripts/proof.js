"use strict";
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

async function main() {
  const args = process.argv.slice(2);
  const options = {delay: 0};
  for (let i = 0; i < args.length; i += 2) {
    if (!['--output', '--delay'].includes(args[i]) || args[i + 1] === undefined || options[args[i]] !== undefined) throw new Error('Invalid arguments');
    options[args[i]] = args[i + 1];
  }
  const output = options['--output'];
  const delay = options['--delay'] === undefined ? 0 : Number(options['--delay']);
  if (!output || path.basename(output) !== output || ['.', '..'].includes(output)) throw new Error('Output must name a file in the working directory');
  if (!Number.isInteger(delay) || delay < 0 || delay > 240 || (options['--delay'] !== undefined && !/^\d+$/.test(options['--delay']))) throw new Error('Delay must be an integer from 0 through 240');
  const isNumber = require('is-number');
  const version = require('is-number/package.json').version;
  if (version !== '7.0.0' || !isNumber(7) || isNumber('LAB')) throw new Error('Package verification failed');
  await new Promise(resolve => setTimeout(resolve, delay * 1000));
  const payload = Buffer.from('BYOS Node LAB acceptance\n', 'utf8');
  fs.writeFileSync(output, payload);
  console.log(JSON.stringify({bytes: payload.length, sha256: crypto.createHash('sha256').update(payload).digest('hex'), package_version: version}));
}
main().catch(error => {console.error(error.message); process.exitCode = 1;});
