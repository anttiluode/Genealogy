'use strict';

const GRAPH_ZOOM_MIN = 0.5;
const GRAPH_ZOOM_MAX = 6;
const GRAPH_ZOOM_STEP = 1.25;

let graphBounds = null;
let graphViewport = null;
let graphZoom = 1;
let graphPanState = null;
let lastAppliedViewBox = '';

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function parseViewBox(value) {
  const parts = String(value || '').trim().split(/[\s,]+/).map(Number);
  if (parts.length !== 4 || parts.some(part => !Number.isFinite(part))) return null;
  const [x, y, width, height] = parts;
  if (width <= 0 || height <= 0) return null;
  return {x, y, width, height};
}

function serializeViewBox(box) {
  return `${box.x.toFixed(3)} ${box.y.toFixed(3)} ${box.width.toFixed(3)} ${box.height.toFixed(3)}`;
}

function sameExtent(a, b) {
  if (!a || !b) return false;
  return Math.abs(a.width - b.width) < 0.01 && Math.abs(a.height - b.height) < 0.01;
}

function sameBox(a, b) {
  if (!a || !b) return false;
  return Math.abs(a.x - b.x) < 0.01
    && Math.abs(a.y - b.y) < 0.01
    && sameExtent(a, b);
}

function constrainGraphViewport(box) {
  if (!graphBounds) return box;
  const next = {...box};

  if (next.width >= graphBounds.width) {
    next.x = graphBounds.x + (graphBounds.width - next.width) / 2;
  } else {
    next.x = clamp(next.x, graphBounds.x, graphBounds.x + graphBounds.width - next.width);
  }

  if (next.height >= graphBounds.height) {
    next.y = graphBounds.y + (graphBounds.height - next.height) / 2;
  } else {
    next.y = clamp(next.y, graphBounds.y, graphBounds.y + graphBounds.height - next.height);
  }

  return next;
}

function updateZoomLevel() {
  const label = document.querySelector('#zoom-level');
  if (label) label.textContent = `${Math.round(graphZoom * 100)}%`;
}

function applyGraphViewport() {
  const svg = document.querySelector('#graph');
  if (!svg || !graphViewport) return;
  lastAppliedViewBox = serializeViewBox(graphViewport);
  if (svg.getAttribute('viewBox') !== lastAppliedViewBox) svg.setAttribute('viewBox', lastAppliedViewBox);
  updateZoomLevel();
}

function resetGraphViewport() {
  if (!graphBounds) return;
  graphViewport = {...graphBounds};
  graphZoom = 1;
  applyGraphViewport();
}

function zoomGraph(factor, clientX = null, clientY = null) {
  const svg = document.querySelector('#graph');
  if (!svg || !graphBounds || !graphViewport || !Number.isFinite(factor) || factor <= 0) return;

  const nextZoom = clamp(graphZoom * factor, GRAPH_ZOOM_MIN, GRAPH_ZOOM_MAX);
  if (Math.abs(nextZoom - graphZoom) < 1e-9) return;

  let u = 0.5;
  let v = 0.5;
  if (Number.isFinite(clientX) && Number.isFinite(clientY)) {
    const rect = svg.getBoundingClientRect();
    if (rect.width > 0 && rect.height > 0) {
      u = clamp((clientX - rect.left) / rect.width, 0, 1);
      v = clamp((clientY - rect.top) / rect.height, 0, 1);
    }
  }

  const anchorX = graphViewport.x + graphViewport.width * u;
  const anchorY = graphViewport.y + graphViewport.height * v;
  const ratio = graphZoom / nextZoom;
  const width = graphViewport.width * ratio;
  const height = graphViewport.height * ratio;

  graphViewport = constrainGraphViewport({
    x: anchorX - width * u,
    y: anchorY - height * v,
    width,
    height,
  });
  graphZoom = nextZoom;
  applyGraphViewport();
}

function panGraph(deltaX, deltaY) {
  if (!graphViewport || !Number.isFinite(deltaX) || !Number.isFinite(deltaY)) return;
  graphViewport = constrainGraphViewport({
    ...graphViewport,
    x: graphViewport.x + deltaX,
    y: graphViewport.y + deltaY,
  });
  applyGraphViewport();
}

function syncGraphBoundsFromSvg() {
  const svg = document.querySelector('#graph');
  if (!svg) return;
  const raw = svg.getAttribute('viewBox') || '';
  if (raw === lastAppliedViewBox) return;
  const incoming = parseViewBox(raw);
  if (!incoming) return;

  if (!graphBounds || !sameExtent(incoming, graphBounds)) {
    graphBounds = incoming;
    graphViewport = {...incoming};
    graphZoom = 1;
    applyGraphViewport();
    return;
  }

  if (graphViewport && !sameBox(incoming, graphViewport)) applyGraphViewport();
}

function setupGraphViewport() {
  const svg = document.querySelector('#graph');
  if (!svg) return;

  syncGraphBoundsFromSvg();

  const observer = new MutationObserver(records => {
    if (records.some(record => record.type === 'attributes' && record.attributeName === 'viewBox')) {
      syncGraphBoundsFromSvg();
    }
  });
  observer.observe(svg, {attributes: true, attributeFilter: ['viewBox']});

  document.querySelector('#zoom-in')?.addEventListener('click', () => zoomGraph(GRAPH_ZOOM_STEP));
  document.querySelector('#zoom-out')?.addEventListener('click', () => zoomGraph(1 / GRAPH_ZOOM_STEP));
  document.querySelector('#zoom-reset')?.addEventListener('click', resetGraphViewport);

  svg.addEventListener('wheel', event => {
    event.preventDefault();
    const factor = clamp(Math.exp(-event.deltaY * 0.0015), 0.72, 1.38);
    zoomGraph(factor, event.clientX, event.clientY);
  }, {passive: false});

  svg.addEventListener('pointerdown', event => {
    if (event.button !== 0) return;
    if (event.target.closest?.('.node')) return;
    graphPanState = {pointerId: event.pointerId, x: event.clientX, y: event.clientY};
    svg.setPointerCapture?.(event.pointerId);
    svg.classList.add('panning');
  });

  svg.addEventListener('pointermove', event => {
    if (!graphPanState || graphPanState.pointerId !== event.pointerId || !graphViewport) return;
    const rect = svg.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return;
    const dx = (event.clientX - graphPanState.x) * graphViewport.width / rect.width;
    const dy = (event.clientY - graphPanState.y) * graphViewport.height / rect.height;
    graphPanState.x = event.clientX;
    graphPanState.y = event.clientY;
    panGraph(-dx, -dy);
  });

  const stopPan = event => {
    if (!graphPanState || graphPanState.pointerId !== event.pointerId) return;
    graphPanState = null;
    svg.classList.remove('panning');
  };
  svg.addEventListener('pointerup', stopPan);
  svg.addEventListener('pointercancel', stopPan);
  svg.addEventListener('lostpointercapture', () => {
    graphPanState = null;
    svg.classList.remove('panning');
  });
}

setupGraphViewport();
