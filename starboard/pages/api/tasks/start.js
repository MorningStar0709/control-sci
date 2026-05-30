import { createTask, toPublicTask, updateTask } from '../../../lib/serverTaskStore';

const ALLOWED_PREFIXES = ['/api/demo/', '/api/evidence/', '/api/medical-rag/'];
const BACKEND = process.env.CONTROLMIND_BACKEND_URL || 'http://127.0.0.1:17001';
const MAX_STEP_TIMEOUT_MS = 5 * 60 * 1000;
const FORWARD_HEADER_ALLOWLIST = new Set(['accept', 'content-type', 'x-request-id', 'x-runtime-profile']);

function allowedPath(path) {
  return typeof path === 'string' && ALLOWED_PREFIXES.some(prefix => path.startsWith(prefix));
}

async function runTask(task, origin, payload) {
  if (Array.isArray(payload.steps) && payload.steps.length) {
    await runSequenceTask(task, origin, payload);
    return;
  }
  const { path, method = 'POST', body, headers = {}, timeoutMs = 180000 } = payload;
  const effectiveTimeoutMs = Math.min(timeoutMs, MAX_STEP_TIMEOUT_MS);
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), effectiveTimeoutMs);

  try {
    const requestHeaders = sanitizeForwardHeaders(headers);
    const options = {
      method,
      headers: requestHeaders,
      signal: controller.signal,
    };
    if (body !== undefined && method !== 'GET') {
      options.body = JSON.stringify(body);
      requestHeaders['Content-Type'] = 'application/json';
    }
    const response = await fetch(resolveTaskUrl(origin, path), options);
    const text = await response.text();
    let data = null;
    try {
      data = text ? JSON.parse(text) : {};
    } catch {
      data = { raw: text };
    }
    if (!response.ok) {
      updateTask(task.id, {
        status: 'failed',
        data,
        error: data?.detail?.error || data?.detail || data?.message || data?.raw || `HTTP ${response.status}`,
      });
      return;
    }
    updateTask(task.id, { status: 'done', data, error: null });
  } catch (error) {
    updateTask(task.id, {
      status: 'failed',
      data: null,
      error: error.name === 'AbortError' ? `任务超时 (${effectiveTimeoutMs / 1000}s)` : error.message,
    });
  } finally {
    clearTimeout(timer);
  }
}

async function fetchStep(origin, step) {
  const { path, method = 'POST', body, headers = {}, timeoutMs = 180000 } = step;
  if (!allowedPath(path)) throw new Error(`unsupported task path: ${path}`);
  const effectiveTimeoutMs = Math.min(timeoutMs, MAX_STEP_TIMEOUT_MS);
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), effectiveTimeoutMs);
  try {
    const requestHeaders = sanitizeForwardHeaders(headers);
    const options = { method, headers: requestHeaders, signal: controller.signal };
    if (body !== undefined && method !== 'GET') {
      options.body = JSON.stringify(body);
      requestHeaders['Content-Type'] = 'application/json';
    }
    const response = await fetch(resolveTaskUrl(origin, path), options);
    const text = await response.text();
    let data = null;
    try {
      data = text ? JSON.parse(text) : {};
    } catch {
      data = { raw: text };
    }
    if (!response.ok) {
      throw new Error(data?.detail?.error || data?.detail || data?.message || data?.raw || `HTTP ${response.status}`);
    }
    return data;
  } finally {
    clearTimeout(timer);
  }
}

function sanitizeForwardHeaders(headers = {}) {
  const output = {};
  Object.entries(headers || {}).forEach(([key, value]) => {
    const lower = key.toLowerCase();
    if (FORWARD_HEADER_ALLOWLIST.has(lower)) output[key] = value;
  });
  return output;
}

function resolveTaskUrl(origin, path) {
  if (path.startsWith('/api/demo/') || path.startsWith('/api/evidence/') || path.startsWith('/api/medical-rag/')) {
    return `${BACKEND}${path}`;
  }
  return `${origin}${path}`;
}

async function runSequenceTask(task, origin, payload) {
  const results = {};
  try {
    for (const step of payload.steps) {
      updateTask(task.id, { status: 'running', current_step: step.key || step.path, data: { ...results } });
      results[step.key || step.path] = await fetchStep(origin, step);
    }
    updateTask(task.id, { status: 'done', data: results, error: null, current_step: null });
  } catch (error) {
    updateTask(task.id, { status: 'failed', data: results, error: error.message });
  }
}

export default function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'method not allowed' });
    return;
  }

  const { path, steps } = req.body || {};
  if (!allowedPath(path) && !(Array.isArray(steps) && steps.every(step => allowedPath(step.path)))) {
    res.status(400).json({ error: 'unsupported task path' });
    return;
  }

  const proto = req.headers['x-forwarded-proto'] || 'http';
  const host = req.headers.host;
  const origin = `${proto}://${host}`;
  const task = createTask(req.body);
  runTask(task, origin, req.body);
  res.status(202).json(toPublicTask(task));
}
