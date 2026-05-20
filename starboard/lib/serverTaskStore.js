const STORE_KEY = '__controlmind_task_store__';
const DEFAULT_MAX_RUNTIME_MS = 5 * 60 * 1000;
const MAX_TASK_RUNTIME_MS = 10 * 60 * 1000;
const TASK_SWEEP_MS = 30 * 60 * 1000;
const SECRET_KEYS = /^(authorization|x-demo-code|api[_-]?key|.*token.*|.*secret.*|password)$/i;

function getStore() {
  if (!globalThis[STORE_KEY]) {
    globalThis[STORE_KEY] = new Map();
  }
  return globalThis[STORE_KEY];
}

export function createTask(input) {
  const store = getStore();
  sweepOldTasks(store);
  const id = `task_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 10)}`;
  const task = {
    id,
    status: 'running',
    input: redactSecrets(input),
    data: null,
    error: null,
    max_runtime_ms: getMaxRuntimeMs(input),
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  };
  store.set(id, task);
  return task;
}

function redactSecrets(value) {
  if (Array.isArray(value)) return value.map(item => redactSecrets(item));
  if (!value || typeof value !== 'object') return value;
  const output = {};
  Object.entries(value).forEach(([key, child]) => {
    output[key] = SECRET_KEYS.test(key) ? '***' : redactSecrets(child);
  });
  return output;
}

export function updateTask(id, patch) {
  const store = getStore();
  const current = store.get(id);
  if (!current) return null;
  const next = {
    ...current,
    ...patch,
    updated_at: new Date().toISOString(),
  };
  store.set(id, next);
  return next;
}

export function getTask(id) {
  const store = getStore();
  const task = store.get(id) || null;
  if (!task) return null;
  if (task.status === 'running' && isExpired(task)) {
    return updateTask(id, {
      status: 'failed',
      error: `任务超时 (${Math.round((task.max_runtime_ms || DEFAULT_MAX_RUNTIME_MS) / 1000)}s)`,
    });
  }
  return task;
}

function getMaxRuntimeMs(input) {
  if (Number.isFinite(input?.timeoutMs)) return Math.min(input.timeoutMs + 30000, MAX_TASK_RUNTIME_MS);
  if (Array.isArray(input?.steps) && input.steps.length) {
    const total = input.steps.reduce((sum, step) => sum + (Number.isFinite(step.timeoutMs) ? step.timeoutMs : DEFAULT_MAX_RUNTIME_MS), 0);
    return Math.min(total + 30000, MAX_TASK_RUNTIME_MS);
  }
  return DEFAULT_MAX_RUNTIME_MS;
}

function isExpired(task) {
  const createdAt = Date.parse(task.created_at || '');
  if (!Number.isFinite(createdAt)) return false;
  return Date.now() - createdAt > (task.max_runtime_ms || DEFAULT_MAX_RUNTIME_MS);
}

function sweepOldTasks(store) {
  const now = Date.now();
  for (const [id, task] of store.entries()) {
    const updatedAt = Date.parse(task.updated_at || task.created_at || '');
    if (Number.isFinite(updatedAt) && now - updatedAt > TASK_SWEEP_MS) {
      store.delete(id);
    }
  }
}
