'use strict';

function renderTools() {
  const host = document.querySelector('#tools-content');
  if (!host) return;

  const f = filters();
  const tools = atlas.nodes
    .filter(node => node.usefulness === 'practical' && nodeMatches(node, f))
    .sort((a, b) => {
      const statusRank = {tool: 0, survivor: 1, active: 2, ledger: 3, experiment: 4, negative: 5, 'idea-mine': 6};
      return (statusRank[a.status] ?? 9) - (statusRank[b.status] ?? 9)
        || a.family.localeCompare(b.family)
        || a.id.localeCompare(b.id);
    });

  const families = new Set(tools.map(node => node.family));
  const passes = new Set(tools.map(node => node.pass_id || 'foundation'));

  host.innerHTML = `
    <div class="correction-summary">
      <strong>${tools.length}</strong><span>reviewed practical artifacts</span>
      <strong>${families.size}</strong><span>families represented</span>
      <strong>${passes.size}</strong><span>archaeology passes contributing</span>
    </div>
    <div class="timeline-grid">
      ${tools.map(node => `
        <article class="timeline-card ${escapeHtml(node.status)}">
          <div class="card-top">
            <span>${escapeHtml(node.family)}</span>
            <span>${escapeHtml(node.status)}</span>
          </div>
          <h4><button data-node="${escapeHtml(node.id)}">${escapeHtml(node.id)}</button></h4>
          <p>${escapeHtml(node.claim)}</p>
          <div class="micro survived"><b>why keep it</b>${escapeHtml(node.survived)}</div>
          <div class="micro killed"><b>do not overclaim</b>${escapeHtml(node.killed)}</div>
          <div class="detail-actions">
            <a class="repo-link" href="${escapeHtml(node.url || node.evidence)}">Open artifact ↗</a>
            ${node.evidence && node.evidence !== node.url ? `<a class="repo-link" href="${escapeHtml(node.evidence)}">Evidence ↗</a>` : ''}
          </div>
        </article>`).join('')}
    </div>`;

  if (!tools.length) {
    host.innerHTML = '<div class="empty">No practical artifacts match the current filters.</div>';
    return;
  }

  host.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
    switchView('genealogy');
    selectNode(button.dataset.node);
  }));
}

const renderCurrentViewWithoutTools = renderCurrentView;
renderCurrentView = function renderCurrentViewWithTools() {
  if (currentView === 'tools') renderTools();
  else renderCurrentViewWithoutTools();
};

renderTools();
