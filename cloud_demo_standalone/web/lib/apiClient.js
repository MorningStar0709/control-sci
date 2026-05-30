const DEFAULT_TIMEOUT_MS = 45000;
const ACCESS_CODE_KEY = 'controlmind_cloud_demo_access_code';

function isFormData(body) {
  return typeof FormData !== 'undefined' && body instanceof FormData;
}

function withRuntime(payload, runtimeConfig) {
  if (!runtimeConfig || isFormData(payload)) return payload;
  return {
    ...(payload || {}),
    runtime_config: runtimeConfig,
  };
}

export function getDemoAccessCode() {
  if (typeof window === 'undefined') return '';
  return window.localStorage.getItem(ACCESS_CODE_KEY) || '';
}

export function setDemoAccessCode(code) {
  if (typeof window === 'undefined') return '';
  const normalized = String(code || '').trim();
  if (normalized) window.localStorage.setItem(ACCESS_CODE_KEY, normalized);
  else window.localStorage.removeItem(ACCESS_CODE_KEY);
  window.dispatchEvent(new CustomEvent('cloud-demo-access-code-change', { detail: { configured: Boolean(normalized) } }));
  return normalized;
}

async function parseResponse(response) {
  const contentType = response.headers.get('content-type') || '';
  const text = await response.text();

  if (contentType.includes('application/json')) {
    try {
      return text ? JSON.parse(text) : {};
    } catch (error) {
      return { raw: text, parse_error: error.message };
    }
  }

  return { raw: text };
}

export async function apiRequest(path, options = {}) {
  const {
    method = 'GET',
    body,
    runtimeConfig,
    timeoutMs = DEFAULT_TIMEOUT_MS,
    headers = {},
  } = options;

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  let requestBody = body;
  const requestHeaders = { ...headers };
  const accessCode = getDemoAccessCode();
  if (accessCode && !requestHeaders['x-demo-code']) {
    requestHeaders['x-demo-code'] = accessCode;
  }

  if (isFormData(body)) {
    if (runtimeConfig) body.append('runtime_config', JSON.stringify(runtimeConfig));
  } else if (body !== undefined) {
    requestBody = JSON.stringify(withRuntime(body, runtimeConfig));
    requestHeaders['Content-Type'] = 'application/json';
  }

  try {
    const response = await fetch(path, {
      method,
      headers: requestHeaders,
      body: requestBody,
      signal: controller.signal,
    });
    const data = await parseResponse(response);

    if (!response.ok) {
      const detail = data?.detail?.error || data?.detail || data?.message || data?.raw;
      return {
        ok: false,
        status: response.status,
        data,
        error: detail || `HTTP ${response.status}`,
      };
    }

    return { ok: true, status: response.status, data, error: null };
  } catch (error) {
    const isTimeout = error.name === 'AbortError';
    return {
      ok: false,
      status: 0,
      data: null,
      error: isTimeout ? `请求超时 (${timeoutMs / 1000}s)` : error.message,
    };
  } finally {
    clearTimeout(timer);
  }
}

export function apiGet(path, options = {}) {
  return apiRequest(path, { ...options, method: 'GET' });
}

export function apiPost(path, body, options = {}) {
  return apiRequest(path, { ...options, method: 'POST', body });
}

export async function startApiTask(path, body, options = {}) {
  const {
    method = 'POST',
    runtimeConfig,
    timeoutMs = DEFAULT_TIMEOUT_MS,
  } = options;
  return apiPost('/api/tasks/start', {
    path,
    method,
    body: withRuntime(body, runtimeConfig),
    timeoutMs,
  }, { timeoutMs: 12000 });
}

export async function startApiSequenceTask(steps, options = {}) {
  const {
    runtimeConfig,
    timeoutMs = DEFAULT_TIMEOUT_MS,
  } = options;
  return apiPost('/api/tasks/start', {
    steps: steps.map(step => ({
      ...step,
      body: step.body === undefined ? undefined : withRuntime(step.body, runtimeConfig),
    })),
    timeoutMs,
  }, { timeoutMs: 12000 });
}

export async function getApiTask(task, options = {}) {
  const taskId = typeof task === 'string' ? task : task?.id;
  const ownerToken = typeof task === 'string' ? options.ownerToken : (task?.owner_token || options.ownerToken);
  const headers = ownerToken
    ? { ...(options.headers || {}), 'x-task-token': ownerToken }
    : options.headers;
  return apiGet(`/api/tasks/status/${encodeURIComponent(taskId)}`, { ...options, headers });
}

export function toFailure(message, data = {}) {
  return {
    status: 'failed',
    message: message || '请求失败',
    ...data,
  };
}

