'use strict';

const QUESTIONS_PATH = 'data/questions.json';
let questionRecords = [];
let questionsLoadState = 'loading';
let questionsLoadError = '';

function attachQuestionsToAtlas() {
  atlas.questions = questionRecords;
}

function questionStateLabel(state) {
  return ({
    open: 'open question',
    'partially-resolved': 'partially resolved',
    resolved: 'resolved',
  })[state] || state;
}

function questionEvidence(item) {
  const records = atlas.evidence || evidenceRecords || [];
  const wanted = new Set(item.evidence || []);
  return records.filter(record => wanted.has(record.id));
}

function questionNodes(item) {
  return [...new Set(questionEvidence(item).map(record => record.node))].sort();
}

function questionMatches(item, f = filters()) {
  const linkedNodes = questionNodes(item)
    .map(id => atlas.nodes.find(node => node.id === id))
    .filter(Boolean);
  if (f.family || f.status || f.pass) {
    const nodeFilter = {...f, q: '', edge: ''};
    if (!linkedNodes.some(node => nodeMatches(node, nodeFilter))) return false;
  }
  if (!f.q) return true;
  const experiment = item.candidate_experiment || {};
  const haystack = [
    item.id, item.title, item.state, item.missing_discriminator,
    ...(item.motifs || []), ...(item.evidence || []),
    ...(item.competing_explanations || []), ...(item.known || []), ...(item.notes || []),
    experiment.design, experiment.cost,
    ...(experiment.outcomes || []).flatMap(outcome => [outcome.if, outcome.then]),
    ...linkedNodes.flatMap(node => [node.id, node.family, node.claim]),
  ].join(' ').toLowerCase();
  return haystack.includes(f.q);
}

function motifTitle(id) {
  return (atlas.motifs || []).find(motif => motif.id === id)?.title || id;
}

function evidenceLinkMarkup(record) {
  return `<button class="question-evidence-link" data-evidence="${escapeHtml(record.id)}" title="Open this record in Evidence">${escapeHtml(record.node)} · ${escapeHtml(record.id)}</button>`;
}

function questionCard(item) {
  const evidence = questionEvidence(item);
  const nodes = questionNodes(item);
  const experiment = item.candidate_experiment || {};
  const explanations = (item.competing_explanations || []).map((text, index) => `
    <li><b>${String.fromCharCode(65 + index)}</b><span>${escapeHtml(text)}</span></li>`).join('');
  const known = (item.known || []).map(text => `<li>${escapeHtml(text)}</li>`).join('');
  const outcomes = (experiment.outcomes || []).map(outcome => `
    <div class="question-outcome">
      <span>IF</span><p>${escapeHtml(outcome.if || '')}</p>
      <span>THEN</span><p>${escapeHtml(outcome.then || '')}</p>
    </div>`).join('');
  const notes = (item.notes || []).map(text => `<li>${escapeHtml(text)}</li>`).join('');

  return `
    <article class="question-card ${escapeHtml(item.state)}">
      <div class="question-card-top">
        <span class="question-state ${escapeHtml(item.state)}">${escapeHtml(questionStateLabel(item.state))}</span>
        <span>${evidence.length} evidence record${evidence.length === 1 ? '' : 's'} · ${nodes.length} repo${nodes.length === 1 ? '' : 's'}</span>
      </div>
      <h3>${escapeHtml(item.title)}</h3>
      <div class="question-motifs">${(item.motifs || []).map(id => `<span>${escapeHtml(motifTitle(id))}</span>`).join('')}</div>

      <section class="question-block known">
        <div class="eyebrow">KNOWN SO FAR</div>
        <ul>${known}</ul>
        <div class="question-links">
          ${nodes.map(id => `<button data-node="${escapeHtml(id)}">${escapeHtml(id)}</button>`).join('')}
        </div>
      </section>

      <section class="question-block">
        <div class="eyebrow">COMPETING EXPLANATIONS</div>
        <ol class="question-explanations">${explanations}</ol>
      </section>

      <section class="question-block discriminator">
        <div class="eyebrow">MISSING DISCRIMINATOR</div>
        <p>${escapeHtml(item.missing_discriminator || '')}</p>
      </section>

      <section class="question-experiment">
        <div class="question-experiment-head"><div class="eyebrow">CANDIDATE NEXT EXPERIMENT</div><span>${escapeHtml(experiment.cost || 'cost not encoded')}</span></div>
        <p>${escapeHtml(experiment.design || '')}</p>
        <div class="question-outcomes">${outcomes}</div>
      </section>

      <details>
        <summary>Evidence receipts${notes ? ' & caveats' : ''}</summary>
        <div class="question-evidence-list">${evidence.map(evidenceLinkMarkup).join('') || '<span>No evidence records resolved.</span>'}</div>
        ${notes ? `<ul class="question-notes">${notes}</ul>` : ''}
      </details>
    </article>`;
}

function renderQuestions() {
  const host = document.querySelector('#questions-content');
  if (!host) return;
  attachQuestionsToAtlas();

  if (questionsLoadState === 'loading' && !questionRecords.length) {
    host.innerHTML = '<div class="empty">Loading unresolved question ledger…</div>';
    return;
  }
  if (questionsLoadState === 'error' && !questionRecords.length) {
    host.innerHTML = `<div class="empty"><strong>Questions ledger unavailable.</strong><br>${escapeHtml(questionsLoadError)}</div>`;
    return;
  }

  const visible = questionRecords.filter(item => questionMatches(item));
  const open = visible.filter(item => item.state === 'open').length;
  const partial = visible.filter(item => item.state === 'partially-resolved').length;
  const resolved = visible.filter(item => item.state === 'resolved').length;

  host.innerHTML = `
    <div class="questions-note">
      <strong>Evidence → uncertainty → experiment.</strong>
      <span>This view does not rank ideas or predict winners. It records which explanations remain compatible with the audited evidence and what observation would separate them.</span>
    </div>
    <div class="question-summary">
      <strong>${visible.length}</strong><span>questions shown</span>
      <strong>${open}</strong><span>open</span>
      <strong>${partial}</strong><span>partially resolved</span>
      <strong>${resolved}</strong><span>resolved by encoded evidence</span>
    </div>
    <div class="questions-grid">${visible.map(questionCard).join('')}</div>`;

  if (!visible.length) host.innerHTML += '<div class="empty">No unresolved questions match the current filters.</div>';

  host.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
    switchView('genealogy');
    selectNode(button.dataset.node);
  }));
  host.querySelectorAll('[data-evidence]').forEach(button => button.addEventListener('click', () => {
    document.querySelector('#search').value = button.dataset.evidence;
    switchView('evidence');
  }));
}

const renderCurrentViewWithoutQuestions = renderCurrentView;
renderCurrentView = function renderCurrentViewWithQuestions() {
  if (currentView === 'questions') renderQuestions();
  else renderCurrentViewWithoutQuestions();
};

async function loadQuestionsLayer() {
  try {
    const value = await loadJson(QUESTIONS_PATH);
    if (!Array.isArray(value)) throw new Error(`${QUESTIONS_PATH} is not an array`);
    questionRecords = value;
    questionsLoadState = 'ready';
    questionsLoadError = '';
  } catch (error) {
    questionRecords = [];
    questionsLoadState = 'error';
    questionsLoadError = error.message;
  }
  attachQuestionsToAtlas();
  if (currentView === 'questions') renderQuestions();
}

loadQuestionsLayer();
