/* A controlled response ambiguity in the real MoonFormer simulator.
 * No training, classifier or generated image. Reads a supplied checkout only.
 * node scripts/audit_moonformer_sign_control.cjs /path/to/MoonFormer [output.json]
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = process.argv[2];
if (!root) throw new Error('Supply a MoonFormer checkout path.');
const expectedHashes = {
  'src/field.js': '8f13f879c6f0a103b0b911491762f74f748b85fe297cfb37fd5be83666471af2',
  'src/probe.js': '7cbae7e0669e051206710bdab4afb26870608cfe41163004e8286161e037edb0',
  'src/moon.js': '9afeebc3670e8ad45e58c9cb5043c5cdc4f3f34971e9d72395480bd9a6486b51',
  'src/write.js': '3267d206072bb2cc2c4a8ed7c152210d2cbcb59fbffcc08748882447b59a439f',
};
const actualHashes = Object.fromEntries(Object.keys(expectedHashes).map(file =>
  [file, crypto.createHash('sha256').update(fs.readFileSync(path.join(root, file))).digest('hex')]));
assert.deepEqual(actualHashes, expectedHashes, 'Use the pinned ef26aef experiment source.');
const { Field, density } = require(path.resolve(root, 'src/field.js'));
const { Probe } = require(path.resolve(root, 'src/probe.js'));
const { teach } = require(path.resolve(root, 'src/write.js'));
const config = { n: 32, lambda: 6, g: 1.2, T: 1.5, epsilon: -.10 };
const material = new Field(config);
teach(material, 'arc', 3001);
const probe = new Probe(32);
const rms = (a, b) => Math.sqrt(a.reduce((s, v, i) => s + (v - b[i]) ** 2, 0) / a.length);
const rows = [];
for (const g of [1.2, 0]) {
  const a = new Field({ ...config, g }), b = new Field({ ...config, g });
  a.values.set(material.values);
  b.values.set(Float64Array.from(material.values, v => -v));
  let last = 0;
  for (const steps of [0, 1, 100, 500]) {
    a.step(steps - last); b.step(steps - last); last = steps;
    const record = {
      g, steps,
      densityDifferenceRms: rms(density(a.values, 32), density(b.values, 32)),
      responseDifferenceRms: rms(probe.fingerprint(a.values), probe.fingerprint(b.values)),
      mirrorFieldResidualRms: Math.sqrt(a.values.reduce((s, v, i) => s + (v + b.values[i]) ** 2, 0) / a.values.length),
    };
    if (steps === 0 || g === 0) {
      assert.equal(record.densityDifferenceRms, 0);
      assert.equal(record.responseDifferenceRms, 0);
      assert.equal(record.mirrorFieldResidualRms, 0);
    } else assert.ok(record.responseDifferenceRms > 1e-5);
    rows.push(record);
  }
}
const receipt = {
  protocol: 'moonformer-sign-pair-v1',
  source_commit: 'ef26aeff37a70ad5142e2b26b0eda333a83708a2',
  source_sha256: actualHashes,
  teaching: { shape: 'arc', seed: 3001, writeSteps: 1500, retainSteps: 6000 },
  field: config,
  readings: rows,
  limitations: [
    'One deliberately engineered sign pair, not two independently learned histories or a general retrieval benchmark.',
    'Identical initial density and wave responses; the signed material display itself need not look identical.',
    'The g=0 control changes the evolution law while starting from the same constructed material.',
    'No classifier, query-selection policy, partial-cue completion or semantic memory is evaluated.',
  ],
};
const serialized = JSON.stringify(receipt, null, 2) + '\n';
if (process.argv[3]) {
  fs.mkdirSync(path.dirname(process.argv[3]), { recursive: true });
  fs.writeFileSync(process.argv[3], serialized);
}
process.stdout.write(serialized);
