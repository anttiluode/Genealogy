'use strict';

const PATHS = {
  repos: 'data/repos.json',
  nodes: 'data/nodes.json',
  edges: 'data/edges.json',
  motifs: 'data/motifs.json',
  passIndex: 'data/passes/index.json',
};
const edgeLabels = {
  inherits: 'inherits',
  forks: 'forks',
  rediscovery: 'rediscovery',
  corrects: 'corrects',
  extracts: 'extracts',
  converges: 'converges',
};
let atlas = {repos: [], nodes: [], edges: [], motifs: [], passes: []};
let selectedNode = null;
let currentView = 'genealogy';
let focusSelected = false;

async function loadJson(path) {
  const response = await fetch(path, {cache: 'no-store'});
  if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
  return response.json();
}

async function loadPasses(messages) {
  let index = [];
  try {
    const raw = await loadJson(PATHS.passIndex);
    index = Array.isArray(raw) ? raw : [];
    if (!Array.isArray(raw)) messages.push(`${PATHS.passIndex} is not an array; passes ignored`);
  } catch (error) {
    messages.push(`Could not load ${PATHS.passIndex}: ${error.message}`);
    return {passes: [], nodes: [], edges: [], motifs: []};
  }
  const merged = {passes: [], nodes: [], edges: [], motifs: []};
  for (const entry of index) {
    if (entry.enabled === false) continue;
    const path = `data/passes/${entry.path}`;
    try {
      const payload = await loadJson(path);
      const passId = payload.id || entry.path.replace(/\.json$/i, '');
      merged.passes.push({
        id: passId,
        title: payload.title || passId,
        summary: payload.summary || '',
        order: Number.isFinite(payload.order) ? payload.order : 999,
        reviewed_at: payload.reviewed_at || '',
        path: entry.path,
      });
      for (const node of payload.nodes || []) merged.nodes.push({...node, pass_id: node.pass_id || passId});
      for (const edge of payload.edges || []) merged.edges.push({...edge, pass_id: edge.pass_id || passId});
      for (const motif of payload.motifs || []) merged.motifs.push({...motif, pass_id: motif.pass_id || passId});
    } catch (error) {
      messages.push(`Could not load archaeology pass ${path}: ${error.message}`);
    }
  }
  return merged;
}

async function loadAtlas() {
  const messages = [];
  const base = {};
  for (const key of ['repos', 'nodes', 'edges', 'motifs']) {
    const path = PATHS[key];
    try {
      const value = await loadJson(path);
      base[key] = Array.isArray(value) ? value : [];
      if (!Array.isArray(value)) messages.push(`${path} is not an array; ignored`);
    } catch (error) {
      base[key] = [];
      messages.push(`Could not load ${path}: ${error.message}`);
    }
  }
  base.nodes = base.nodes.map(node => ({
    era: 'Foundation atlas',
    era_order: 0,
    pass_id: 'foundation',
    ...node,
  }));
  base.passes = [{
    id: 'foundation',
    title: 'Foundation atlas',
    summary: 'The first cross-family curated slice.',
    order: 0,
    reviewed_at: '2026-09-15',
  }];
  const passData = await loadPasses(messages);
  const result = {
    repos: base.repos,
    nodes: [...base.nodes, ...passData.nodes],
    edges: [...base.edges, ...passData.edges],
    motifs: [...base.motifs, ...passData.motifs],
    passes: [...base.passes, ...passData.passes].sort((a, b) => a.order - b.order),
  };
  messages.push(...validateClientAtlas(result));
  return {atlas: result, messages};
}

function validateClientAtlas(data) {
  const messages = [];
  const ids = new Set();
  for (const node of data.nodes) {
    if (!node.id) {
      messages.push('Curated node without id');
      continue;
    }
    if (ids.has(node.id)) messages.push(`Duplicate node id: ${node.id}`);
    ids.add(node.id);
  }
  for (const edge of data.edges) {
    if (!ids.has(edge.source) || !ids.has(edge.target)) messages.push(`Dangling edge ignored: ${edge.source} → ${edge.target}`);
  }
  for (const motif of data.motifs) {
    for (const id of motif.nodes || []) if (!ids.has(id)) messages.push(`Motif ${motif.id} references unknown node ${id}`);
  }
  return messages;
}

function escapeHtml(value = '') {
  return String(value).replace(/[&<>'"]/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;',
  }[char]));
}

function renderDiagnostics(messages) {
  const el = document.querySelector('#diagnostics');
  if (!messages.length) {
    el.hidden = true;
    el.textContent = '';
    return;
  }
  el.hidden = false;
  el.textContent = `ATLAS DIAGNOSTICS\n${messages.map(message => `• ${message}`).join('\n')}`;
}

function fillStats() {
  const corrections = atlas.edges.filter(edge => edge.type === 'corrects').length;
  document.querySelector('#stat-repos').textContent = atlas.repos.length || '—';
  document.querySelector('#stat-nodes').textContent = atlas.nodes.length;
  document.querySelector('#stat-edges').textContent = atlas.edges.length;
  document.querySelector('#stat-corrections').textContent = corrections;
  document.querySelector('#stat-motifs').textContent = atlas.motifs.length;
  document.querySelector('#stat-passes').textContent = atlas.passes.length;
  const coverage = atlas.repos.length ? Math.min(100, 100 * atlas.nodes.length / atlas.repos.length) : 0;
  document.querySelector('#coverage-bar').style.width = `${coverage.toFixed(1)}%`;
  document.querySelector('#coverage-text').textContent = atlas.repos.length
    ? `${atlas.nodes.length} / ${atlas.repos.length} repositories interpreted (${coverage.toFixed(1)}%)`
    : `${atlas.nodes.length} reviewed nodes; census unavailable`;
}

function addOptions(select, values) {
  values.filter(Boolean).sort((a, b) => String(a).localeCompare(String(b))).forEach(value => select.add(new Option(value, value)));
}

function setupFilters() {
  addOptions(document.querySelector('#family-filter'), [...new Set(atlas.nodes.map(node => node.family))]);
  addOptions(document.querySelector('#status-filter'), [...new Set(atlas.nodes.map(node => node.status))]);
  for (const pass of atlas.passes) document.querySelector('#pass-filter').add(new Option(pass.title, pass.id));
  for (const type of Object.keys(edgeLabels)) document.querySelector('#edge-filter').add(new Option(edgeLabels[type], type));
  for (const el of [
    document.querySelector('#family-filter'),
    document.querySelector('#status-filter'),
    document.querySelector('#pass-filter'),
    document.querySelector('#edge-filter'),
    document.querySelector('#search'),
  ]) el.addEventListener('input', renderCurrentView);
}

function filters() {
  return {
    q: document.querySelector('#search').value.trim().toLowerCase(),
    family: document.querySelector('#family-filter').value,
    status: document.querySelector('#status-filter').value,
    pass: document.querySelector('#pass-filter').value,
    edge: document.querySelector('#edge-filter').value,
  };
}

function nodeMatches(node, f = filters()) {
  const haystack = [
    node.id, node.family, node.status, node.claim, node.survived, node.killed,
    node.era, node.pass_id, ...(node.tags || []),
  ].join(' ').toLowerCase();
  return (!f.q || haystack.includes(f.q))
    && (!f.family || node.family === f.family)
    && (!f.status || node.status === f.status)
    && (!f.pass || node.pass_id === f.pass);
}

function filteredNodeIds() {
  const f = filters();
  let ids = new Set(atlas.nodes.filter(node => nodeMatches(node, f)).map(node => node.id));
  if (focusSelected && selectedNode) {
    const context = new Set([selectedNode]);
    for (const edge of atlas.edges) {
      if (edge.source === selectedNode) context.add(edge.target);
      if (edge.target === selectedNode) context.add(edge.source);
    }
    ids = new Set([...ids].filter(id => context.has(id)));
  }
  return ids;
}

function familyLayout(nodes) {
  const families = [...new Set(nodes.map(node => node.family))].sort();
  const width = Math.max(1500, 240 * families.length + 180);
  const familyX = new Map(families.map((family, index) => [family, 100 + index * 240]));
  const positions = new Map();
  let maxRows = 1;
  for (const family of families) {
    const group = nodes
      .filter(node => node.family === family)
      .sort((a, b) => (a.era_order || 0) - (b.era_order || 0) || a.id.localeCompare(b.id));
    maxRows = Math.max(maxRows, group.length);
    group.forEach((node, index) => positions.set(node.id, {x: familyX.get(family), y: 84 + index * 122}));
  }
  return {families, familyX, positions, width, height: Math.max(860, maxRows * 122 + 130)};
}

function svgEl(tag, attrs = {}) {
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [key, value] of Object.entries(attrs)) el.setAttribute(key, value);
  return el;
}

function renderGraph() {
  const svg = document.querySelector('#graph');
  svg.replaceChildren();
  const {families, familyX, positions, width, height} = familyLayout(atlas.nodes);
  svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
  const visible = filteredNodeIds();
  const f = filters();

  for (const family of families) {
    const label = svgEl('text', {x: familyX.get(family), y: 34, class: 'family-label'});
    label.textContent = family.toUpperCase();
    svg.append(label);
  }

  const validIds = new Set(atlas.nodes.map(node => node.id));
  for (const edge of atlas.edges) {
    if (!validIds.has(edge.source) || !validIds.has(edge.target)) continue;
    const source = positions.get(edge.source);
    const target = positions.get(edge.target);
    if (!source || !target) continue;
    const sx = source.x + 182, sy = source.y + 33, tx = target.x, ty = target.y + 33;
    const dx = Math.max(60, Math.abs(tx - sx) * 0.45);
    const edgeVisible = visible.has(edge.source) && visible.has(edge.target) && (!f.edge || edge.type === f.edge);
    const path = svgEl('path', {
      d: `M ${sx} ${sy} C ${sx + dx} ${sy}, ${tx - dx} ${ty}, ${tx} ${ty}`,
      class: `edge ${edge.type} ${edge.confidence === 'medium' ? 'medium' : ''} ${edgeVisible ? '' : 'dimmed'}`,
    });
    const title = svgEl('title');
    title.textContent = `${edge.source} → ${edge.target} · ${edge.type} · ${edge.confidence}\n${edge.why || ''}`;
    path.append(title);
    svg.append(path);
  }

  for (const node of atlas.nodes) {
    const p = positions.get(node.id);
    const isVisible = visible.has(node.id);
    const group = svgEl('g', {
      class: `node ${node.status} ${isVisible ? '' : 'dimmed'} ${selectedNode === node.id ? 'selected' : ''}`,
      transform: `translate(${p.x} ${p.y})`, tabindex: '0', role: 'button',
    });
    const rect = svgEl('rect', {width: 182, height: 66, class: 'card'});
    const name = svgEl('text', {x: 11, y: 23, class: 'name'});
    const meta = svgEl('text', {x: 11, y: 43, class: 'meta'});
    const era = svgEl('text', {x: 11, y: 57, class: 'era'});
    const title = svgEl('title');
    name.textContent = node.id.length > 24 ? `${node.id.slice(0, 23)}…` : node.id;
    meta.textContent = `${node.status} · ${node.confidence}`;
    era.textContent = node.era || 'Foundation atlas';
    title.textContent = `${node.id}\n${node.claim}`;
    group.append(rect, name, meta, era, title);
    group.addEventListener('click', () => selectNode(node.id));
    group.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') selectNode(node.id);
    });
    svg.append(group);
  }
}

function edgeButton(edge, direction) {
  const id = direction === 'in' ? edge.source : edge.target;
  return `<button class="lineage-link" data-node="${escapeHtml(id)}"><span>${escapeHtml(edgeLabels[edge.type] || edge.type)}</span>${escapeHtml(id)}</button>`;
}

function selectNode(id) {
  selectedNode = id;
  const node = atlas.nodes.find(item => item.id === id);
  if (!node) return;
  const incoming = atlas.edges.filter(edge => edge.target === id);
  const outgoing = atlas.edges.filter(edge => edge.source === id);
  const detail = document.querySelector('#detail');
  detail.innerHTML = `
    <div class="eyebrow">${escapeHtml(node.family)} · ${escapeHtml(node.era || 'Foundation atlas')}</div>
    <h3>${escapeHtml(node.id)}</h3>
    <div class="badges">
      <span class="badge">${escapeHtml(node.status)}</span>
      <span class="badge">${escapeHtml(node.usefulness)}</span>
      <span class="badge">confidence ${escapeHtml(node.confidence)}</span>
      <span class="badge">${escapeHtml(node.pass_id || 'foundation')}</span>
    </div>
    <div class="detail-block"><small>Claim / question</small><p>${escapeHtml(node.claim)}</p></div>
    <div class="detail-block survived"><small>What survived</small><p>${escapeHtml(node.survived)}</p></div>
    <div class="detail-block killed"><small>What died / narrowed</small><p>${escapeHtml(node.killed)}</p></div>
    <div class="detail-block"><small>Upstream evidence</small><div class="lineage-list">${incoming.map(edge => edgeButton(edge, 'in')).join('') || '<p>None established yet.</p>'}</div></div>
    <div class="detail-block"><small>Downstream evidence</small><div class="lineage-list">${outgoing.map(edge => edgeButton(edge, 'out')).join('') || '<p>None established yet.</p>'}</div></div>
    <div class="detail-block"><small>Tags</small><p>${(node.tags || []).map(escapeHtml).join(' · ')}</p></div>
    <div class="detail-actions">
      <a class="repo-link" href="${escapeHtml(node.url || node.evidence)}">Open repository ↗</a>
      ${node.evidence && node.evidence !== node.url ? `<a class="repo-link" href="${escapeHtml(node.evidence)}">Evidence ↗</a>` : ''}
    </div>`;
  detail.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => selectNode(button.dataset.node)));
  document.querySelector('#focus-selected').disabled = false;
  renderGraph();
}

function renderLegend() {
  document.querySelector('#edge-legend').innerHTML = Object.keys(edgeLabels)
    .map(type => `<span class="${type}"><i></i>${edgeLabels[type]}</span>`).join('');
}

function eraGroups() {
  const groups = new Map();
  for (const node of atlas.nodes) {
    const key = `${String(node.era_order ?? 0).padStart(3, '0')}|${node.era || 'Foundation atlas'}`;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(node);
  }
  return [...groups.entries()].sort(([a], [b]) => a.localeCompare(b)).map(([key, nodes]) => ({
    order: Number(key.split('|')[0]),
    era: key.slice(key.indexOf('|') + 1),
    nodes: nodes.sort((a, b) => a.id.localeCompare(b.id)),
  }));
}

function renderEraStrip() {
  const host = document.querySelector('#era-strip');
  host.innerHTML = eraGroups().map(group => `
    <button class="era-pill" data-era="${escapeHtml(group.era)}">
      <strong>${group.nodes.length}</strong><span>${escapeHtml(group.era)}</span>
    </button>`).join('');
  host.querySelectorAll('[data-era]').forEach(button => button.addEventListener('click', () => {
    switchView('timeline');
    document.querySelector(`[data-era-section="${CSS.escape(button.dataset.era)}"]`)?.scrollIntoView({behavior: 'smooth', block: 'start'});
  }));
}

function renderTimeline() {
  const host = document.querySelector('#timeline-content');
  const f = filters();
  const groups = eraGroups().map(group => ({...group, nodes: group.nodes.filter(node => nodeMatches(node, f))})).filter(group => group.nodes.length);
  host.innerHTML = groups.map(group => `
    <section class="era-section" data-era-section="${escapeHtml(group.era)}">
      <div class="era-heading"><div><div class="eyebrow">ERA ${group.order}</div><h3>${escapeHtml(group.era)}</h3></div><span>${group.nodes.length} reviewed</span></div>
      <div class="timeline-grid">${group.nodes.map(node => `
        <article class="timeline-card ${escapeHtml(node.status)}">
          <div class="card-top"><span>${escapeHtml(node.pass_id || 'foundation')}</span><span>${escapeHtml(node.status)}</span></div>
          <h4><button data-node="${escapeHtml(node.id)}">${escapeHtml(node.id)}</button></h4>
          <p>${escapeHtml(node.claim)}</p>
          <div class="micro survived"><b>survived</b>${escapeHtml(node.survived)}</div>
          <div class="micro killed"><b>killed / narrowed</b>${escapeHtml(node.killed)}</div>
        </article>`).join('')}</div>
    </section>`).join('') || '<div class="empty">No timeline nodes match the current filters.</div>';
  host.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
    switchView('genealogy');
    selectNode(button.dataset.node);
  }));
}

function renderCorrections() {
  const host = document.querySelector('#corrections-content');
  const f = filters();
  const corrections = atlas.edges.filter(edge => edge.type === 'corrects')
    .filter(edge => !f.edge || f.edge === 'corrects')
    .filter(edge => {
      if (!f.q) return true;
      return [edge.source, edge.target, edge.why].join(' ').toLowerCase().includes(f.q);
    });
  const negatives = atlas.nodes.filter(node => ['negative', 'ledger'].includes(node.status) && node.killed && nodeMatches(node, f));
  host.innerHTML = `
    <div class="correction-summary">
      <strong>${corrections.length}</strong><span>explicit correction edges</span>
      <strong>${negatives.length}</strong><span>negative / ledger nodes with narrowed claims</span>
    </div>
    <div class="correction-grid">
      ${corrections.map(edge => `
        <article class="correction-card">
          <div class="eyebrow">${escapeHtml(edge.confidence)} confidence · correction edge</div>
          <h3><button data-node="${escapeHtml(edge.source)}">${escapeHtml(edge.source)}</button><span>→</span><button data-node="${escapeHtml(edge.target)}">${escapeHtml(edge.target)}</button></h3>
          <p>${escapeHtml(edge.why || '')}</p>
          <a href="${escapeHtml(edge.evidence || '#')}">evidence ↗</a>
        </article>`).join('')}
    </div>
    <h3 class="subhead">Claims the corpus itself narrowed</h3>
    <div class="killed-grid">
      ${negatives.map(node => `
        <article class="killed-card">
          <div class="eyebrow">${escapeHtml(node.era || '')}</div>
          <h4><button data-node="${escapeHtml(node.id)}">${escapeHtml(node.id)}</button></h4>
          <p>${escapeHtml(node.killed)}</p>
        </article>`).join('')}
    </div>`;
  host.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
    switchView('genealogy');
    selectNode(button.dataset.node);
  }));
}

function renderCensus() {
  const host = document.querySelector('#census-content');
  if (!atlas.repos.length) {
    host.innerHTML = '<div class="empty"><strong>Census snapshot unavailable.</strong><br>The curated genealogy remains usable.</div>';
    return;
  }
  const q = filters().q;
  const reviewed = new Set(atlas.nodes.map(node => node.id));
  const rows = atlas.repos.filter(repo => !q || [repo.name, repo.description].join(' ').toLowerCase().includes(q)).map(repo => `
    <tr>
      <td><span class="${reviewed.has(repo.name) ? 'reviewed-dot' : 'unread-dot'}"></span><a href="${escapeHtml(repo.url)}">${escapeHtml(repo.name)}</a></td>
      <td>${reviewed.has(repo.name) ? 'reviewed' : escapeHtml(repo.inventory_status || 'unread')}</td>
      <td>${escapeHtml(repo.description || '')}</td>
      <td>${escapeHtml(repo.updated_at || '')}</td>
      <td>${Number(repo.size || 0).toLocaleString()}</td>
    </tr>`).join('');
  host.innerHTML = `<table><thead><tr><th>Repository</th><th>Atlas state</th><th>Description</th><th>Updated</th><th>KB</th></tr></thead><tbody>${rows}</tbody></table>`;
}

function renderMotifs() {
  const host = document.querySelector('#motif-grid');
  const q = filters().q;
  const motifs = atlas.motifs.filter(motif => !q || [motif.id, motif.title, motif.description, ...(motif.nodes || [])].join(' ').toLowerCase().includes(q));
  host.innerHTML = motifs.map(motif => `
    <article class="motif-card">
      <div class="count">${motif.nodes.length}</div>
      <div class="eyebrow">${escapeHtml(motif.pass_id || 'foundation')}</div>
      <h3>${escapeHtml(motif.title)}</h3>
      <p>${escapeHtml(motif.description)}</p>
      <div class="node-links">${motif.nodes.map(id => `<button data-node="${escapeHtml(id)}">${escapeHtml(id)}</button>`).join('')}</div>
    </article>`).join('');
  host.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
    switchView('genealogy');
    selectNode(button.dataset.node);
  }));
}

function queueScore(repo, reviewed) {
  if (reviewed.has(repo.name)) return {score: -999, reasons: []};
  const name = repo.name.toLowerCase();
  let score = 0;
  const reasons = [];
  for (const word of ['geometric', 'clockfield', 'splat', 'neuron', 'eeg', 'pkas', 'deerskin', 'phase', 'world', 'brain', 'operator', 'moire']) {
    if (name.includes(word)) {
      score += 3;
      reasons.push(`family hint: ${word}`);
    }
  }
  if ((repo.size || 0) > 500) { score += 2; reasons.push('nontrivial repository'); }
  if ((repo.size || 0) > 5000) { score += 2; reasons.push('large archive'); }
  if (/v\d|bet\d|[0-9]$/.test(name)) { score += 1; reasons.push('version-ladder candidate'); }
  return {score, reasons};
}

function renderQueue() {
  const host = document.querySelector('#queue-content');
  const reviewed = new Set(atlas.nodes.map(node => node.id));
  if (!atlas.repos.length) {
    host.innerHTML = '<article class="queue-card"><div class="eyebrow">MANUAL PRIORITY</div><h3>Version ladders first</h3><p>Current priority: Splat/Slapstack, Clockfield, PKAS/Deerskin, EEG tools and GAx/ThirdWay/TransformerStudy.</p></article>';
    return;
  }
  const ranked = atlas.repos.map(repo => ({repo, ...queueScore(repo, reviewed)}))
    .filter(item => item.score >= 0)
    .sort((a, b) => b.score - a.score || a.repo.name.localeCompare(b.repo.name))
    .slice(0, 30);
  host.innerHTML = ranked.map(item => `
    <article class="queue-card">
      <div class="eyebrow">priority ${item.score}</div>
      <h3><a href="${escapeHtml(item.repo.url)}">${escapeHtml(item.repo.name)}</a></h3>
      <p>${escapeHtml(item.repo.description || 'No repository description.')}</p>
      <div class="why">${item.reasons.join(' · ') || 'unreviewed'}</div>
    </article>`).join('');
}

function switchView(view) {
  currentView = view;
  document.querySelectorAll('.tab').forEach(button => button.classList.toggle('active', button.dataset.view === view));
  document.querySelectorAll('.view').forEach(section => section.classList.toggle('active', section.dataset.view === view));
  renderCurrentView();
}

function renderCurrentView() {
  if (currentView === 'genealogy') renderGraph();
  else if (currentView === 'timeline') renderTimeline();
  else if (currentView === 'corrections') renderCorrections();
  else if (currentView === 'census') renderCensus();
  else if (currentView === 'survivors') renderMotifs();
  else renderQueue();
}

async function init() {
  const loaded = await loadAtlas();
  atlas = loaded.atlas;
  renderDiagnostics(loaded.messages);
  fillStats();
  setupFilters();
  renderLegend();
  renderEraStrip();
  renderGraph();
  renderTimeline();
  renderCorrections();
  renderMotifs();
  renderCensus();
  renderQueue();

  document.querySelectorAll('.tab').forEach(button => button.addEventListener('click', () => switchView(button.dataset.view)));
  document.querySelector('#reset-detail').addEventListener('click', () => {
    selectedNode = null;
    focusSelected = false;
    document.querySelector('#focus-selected').disabled = true;
    document.querySelector('#focus-selected').classList.remove('active');
    document.querySelector('#detail').innerHTML = '<div class="detail-placeholder"><span class="crosshair">＋</span><h3>Select a repository</h3><p>Inspect what survived, what died, and the evidence traffic around it.</p></div>';
    renderGraph();
  });
  document.querySelector('#focus-selected').addEventListener('click', event => {
    if (!selectedNode) return;
    focusSelected = !focusSelected;
    event.currentTarget.classList.toggle('active', focusSelected);
    renderGraph();
  });
}

init();
