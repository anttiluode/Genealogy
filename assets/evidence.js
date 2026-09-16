'use strict';

const EVIDENCE_PATH = 'data/evidence.json';
let evidenceRecords = [];
let evidenceLoadState = 'loading';
let evidenceLoadError = '';

function attachEvidenceToAtlas() {
  atlas.evidence = evidenceRecords;
}

function evidenceForNode(nodeId) {
  return evidenceRecords.filter(item => item.node === nodeId);
}

function evidenceResultLabel(result) {
  return ({
    supports: 'supports claim',
    contradicts: 'contradicts claim',
    mixed: 'mixed result',
    inconclusive: 'inconclusive',
  })[result] || result;
}

function formatMetric(metric) {
  if (metric.display) return metric.display;
  if (metric.denominator !== undefined && metric.value !== undefined) {
    return `${metric.value} / ${metric.denominator}`;
  }
  if (metric.treatment !== undefined || metric.control !== undefined) {
    const treatment = metric.treatment !== undefined ? metric.treatment : '—';
    const control = metric.control !== undefined ? metric.control : '—';
    return `${treatment} vs ${control}`;
  }
  if (metric.value !== undefined) return String(metric.value);
  return 'recorded';
}

function evidenceMatches(item, f = filters()) {
  const node = atlas.nodes.find(candidate => candidate.id === item.node);
  if (node) {
    const nodeFilter = {...f, q: '', edge: ''};
    if (!nodeMatches(node, nodeFilter)) return false;
  }
  if (!f.q) return true;
  const haystack = [
    item.id, item.node, item.claim, item.design, item.result, item.replication,
    ...(item.motifs || []), ...(item.controls || []), ...(item.limitations || []),
    ...(item.metrics || []).flatMap(metric => [metric.name, metric.display, metric.comparison]),
  ].join(' ').toLowerCase();
  return haystack.includes(f.q);
}

function buildMotifEvidenceSummary(records = evidenceRecords) {
  const summaries = [];
  for (const motif of atlas.motifs || []) {
    const linked = records.filter(item => (item.motifs || []).includes(motif.id));
    if (!linked.length) continue;
    const representedNodes = [...new Set(linked.map(item => item.node))].sort();
    const supportingNodes = [...new Set(linked.filter(item => item.result === 'supports').map(item => item.node))].sort();
    const challengedNodes = [...new Set(linked.filter(item => item.result !== 'supports').map(item => item.node))].sort();
    summaries.push({
      motif,
      records: linked,
      representedNodes,
      supportingNodes,
      challengedNodes,
      crossRepoSupport: supportingNodes.length >= 2,
    });
  }
  return summaries.sort((a, b) =>
    Number(b.crossRepoSupport) - Number(a.crossRepoSupport)
    || b.supportingNodes.length - a.supportingNodes.length
    || b.representedNodes.length - a.representedNodes.length
    || a.motif.title.localeCompare(b.motif.title));
}

function renderMotifEvidence(records = evidenceRecords) {
  const summaries = buildMotifEvidenceSummary(records);
  if (!summaries.length) return '';
  return `
    <section class="motif-evidence" aria-label="Motif evidence">
      <div class="motif-evidence-head">
        <div><div class="eyebrow">CROSS-REPO TEST HISTORY</div><h3>Motif evidence</h3></div>
        <p>A motif counts support only when an evidence record explicitly names that motif. Two supporting records from one repository do not masquerade as cross-repository replication.</p>
      </div>
      <div class="motif-evidence-grid">
        ${summaries.map(item => `
          <article class="motif-evidence-card ${item.crossRepoSupport ? 'cross-supported' : ''}">
            <div class="motif-evidence-top">
              <span class="motif-evidence-count">${item.records.length}</span>
              <span>${item.crossRepoSupport ? 'support in multiple repos' : 'evidence attached'}</span>
            </div>
            <h4>${escapeHtml(item.motif.title)}</h4>
            <p>${escapeHtml(item.motif.description || '')}</p>
            <div class="motif-evidence-stats">
              <b>${item.representedNodes.length}</b><span>repos tested</span>
              <b>${item.supportingNodes.length}</b><span>repos with supporting records</span>
              <b>${item.challengedNodes.length}</b><span>repos with mixed/null/inconclusive records</span>
            </div>
            <div class="node-links">
              ${item.representedNodes.map(id => `<button data-node="${escapeHtml(id)}">${escapeHtml(id)}</button>`).join('')}
            </div>
          </article>`).join('')}
      </div>
    </section>`;
}

function evidenceCard(item) {
  const sample = item.sample
    ? `${escapeHtml(item.sample.count)} ${escapeHtml(item.sample.unit)}${Number(item.sample.count) === 1 ? '' : 's'}`
    : 'sample not encoded';
  const flags = [
    item.held_out ? 'held-out evaluation' : '',
    item.external_data ? 'external/reference data' : '',
    item.replication || '',
  ].filter(Boolean);
  const metrics = (item.metrics || []).map(metric => `
    <div class="evidence-metric">
      <span>${escapeHtml(metric.name || 'metric')}</span>
      <strong>${escapeHtml(formatMetric(metric))}</strong>
      ${metric.comparison ? `<small>${escapeHtml(metric.comparison)}</small>` : ''}
    </div>`).join('');
  const controls = (item.controls || []).map(control => `<li>${escapeHtml(control)}</li>`).join('');
  const limitations = (item.limitations || []).map(limit => `<li>${escapeHtml(limit)}</li>`).join('');
  const motifTags = (item.motifs || []).map(id => {
    const motif = (atlas.motifs || []).find(candidate => candidate.id === id);
    return `<span>${escapeHtml(motif?.title || id)}</span>`;
  }).join('');

  return `
    <article class="evidence-card ${escapeHtml(item.result)}">
      <div class="evidence-card-top">
        <button class="evidence-node" data-node="${escapeHtml(item.node)}">${escapeHtml(item.node)}</button>
        <span class="evidence-result ${escapeHtml(item.result)}">${escapeHtml(evidenceResultLabel(item.result))}</span>
      </div>
      <div class="eyebrow">${escapeHtml(item.design)} · ${sample}</div>
      <h3>${escapeHtml(item.claim)}</h3>
      ${motifTags ? `<div class="evidence-motifs">${motifTags}</div>` : ''}
      ${metrics ? `<div class="evidence-metrics">${metrics}</div>` : ''}
      ${flags.length ? `<div class="evidence-flags">${flags.map(flag => `<span>${escapeHtml(flag)}</span>`).join('')}</div>` : ''}
      ${controls ? `<details><summary>Controls / nulls</summary><ul>${controls}</ul></details>` : ''}
      ${limitations ? `<details open><summary>Limitations</summary><ul>${limitations}</ul></details>` : ''}
      <a class="repo-link" href="${escapeHtml(item.source)}">source receipt ↗</a>
    </article>`;
}

function renderEvidence() {
  const host = document.querySelector('#evidence-content');
  if (!host) return;
  attachEvidenceToAtlas();

  if (evidenceLoadState === 'loading' && !evidenceRecords.length) {
    host.innerHTML = '<div class="empty">Loading empirical evidence ledger…</div>';
    return;
  }
  if (evidenceLoadState === 'error' && !evidenceRecords.length) {
    host.innerHTML = `<div class="empty"><strong>Evidence ledger unavailable.</strong><br>${escapeHtml(evidenceLoadError)}</div>`;
    return;
  }

  const visible = evidenceRecords.filter(item => evidenceMatches(item));
  const represented = new Set(visible.map(item => item.node));
  const supports = visible.filter(item => item.result === 'supports').length;
  const constrained = visible.filter(item => item.result !== 'supports').length;

  host.innerHTML = `
    <div class="evidence-note">
      <strong>Two different questions.</strong>
      <span>Genealogy confidence asks whether an interpretation or ancestry link is documented. This view asks what empirical test was run, what controls existed, and what the result permits us to believe.</span>
    </div>
    <div class="evidence-summary">
      <strong>${visible.length}</strong><span>evidence records</span>
      <strong>${represented.size}</strong><span>repositories represented</span>
      <strong>${supports}</strong><span>supporting results</span>
      <strong>${constrained}</strong><span>mixed, null, contradictory or inconclusive</span>
    </div>
    ${renderMotifEvidence(visible)}
    <div class="evidence-grid">${visible.map(evidenceCard).join('')}</div>`;

  if (!visible.length) {
    host.innerHTML += '<div class="empty">No empirical evidence records match the current filters.</div>';
  }

  host.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
    switchView('genealogy');
    selectNode(button.dataset.node);
  }));
}

function nodeEvidenceMarkup(nodeId) {
  const records = evidenceForNode(nodeId);
  if (!records.length) {
    return `
      <div class="detail-block evidence-detail">
        <small>Empirical evidence</small>
        <p>No structured empirical evidence record has been added yet. This does not mean the repository lacks experiments; it means this archaeology layer has not encoded them yet.</p>
      </div>`;
  }

  return `
    <div class="detail-block evidence-detail">
      <small>Empirical evidence</small>
      <div class="evidence-detail-list">
        ${records.map(item => `
          <div class="evidence-detail-item ${escapeHtml(item.result)}">
            <span class="evidence-result ${escapeHtml(item.result)}">${escapeHtml(evidenceResultLabel(item.result))}</span>
            <p>${escapeHtml(item.claim)}</p>
            <small>${escapeHtml(item.design)}${item.sample ? ` · ${escapeHtml(item.sample.count)} ${escapeHtml(item.sample.unit)}` : ''}</small>
          </div>`).join('')}
      </div>
      <button class="lineage-link evidence-open-view" type="button"><span>evidence</span>open all structured records</button>
    </div>`;
}

const selectNodeWithoutEvidence = selectNode;
selectNode = function selectNodeWithEvidence(id) {
  selectNodeWithoutEvidence(id);
  const detail = document.querySelector('#detail');
  if (!detail) return;
  const actions = detail.querySelector('.detail-actions');
  if (actions) actions.insertAdjacentHTML('beforebegin', nodeEvidenceMarkup(id));
  detail.querySelector('.evidence-open-view')?.addEventListener('click', () => {
    document.querySelector('#search').value = id;
    switchView('evidence');
  });
};

const fillStatsWithoutEvidence = fillStats;
fillStats = function fillStatsWithEvidence() {
  attachEvidenceToAtlas();
  fillStatsWithoutEvidence();
  const el = document.querySelector('#stat-evidence');
  if (el) el.textContent = evidenceRecords.length;
};

const renderCurrentViewWithoutEvidence = renderCurrentView;
renderCurrentView = function renderCurrentViewWithEvidence() {
  if (currentView === 'evidence') renderEvidence();
  else renderCurrentViewWithoutEvidence();
};

async function loadEvidenceLayer() {
  try {
    const value = await loadJson(EVIDENCE_PATH);
    if (!Array.isArray(value)) throw new Error(`${EVIDENCE_PATH} is not an array`);
    evidenceRecords = value;
    evidenceLoadState = 'ready';
    evidenceLoadError = '';
  } catch (error) {
    evidenceRecords = [];
    evidenceLoadState = 'error';
    evidenceLoadError = error.message;
  }
  attachEvidenceToAtlas();
  const stat = document.querySelector('#stat-evidence');
  if (stat) stat.textContent = evidenceRecords.length || '—';
  if (currentView === 'evidence') renderEvidence();
  if (selectedNode) selectNode(selectedNode);
}

loadEvidenceLayer();
