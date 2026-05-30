import { createTask } from './store';

const BASE = (process.env.NEXT_PUBLIC_BASE_URL || 'http://127.0.0.1:18081').replace(/\/$/, '');
const ALLOWED_PATHS = new Set([
  '/api/mineru/url',
  '/api/mineru/upload',
  '/api/quiz/generate',
  '/api/quiz/grade',
  '/api/agent/plan',
  '/api/medical-rag/ask',
  '/api/deepseek/ask',
]);

async function callStep(step, accessCode = '') {
  if (!ALLOWED_PATHS.has(step.path)) {
    throw new Error(`unsupported task path: ${step.path}`);
  }
  const target = `${BASE}${step.path}`;
  const response = await fetch(target, {
    method: step.method || 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(accessCode ? { 'x-demo-code': accessCode } : {}),
    },
    body: step.body === undefined ? undefined : JSON.stringify(step.body),
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data?.detail?.error || data?.error || `HTTP ${response.status}`);
  return data;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'method not allowed' });
    return;
  }
  try {
    const payload = req.body || {};
    const accessCode = String(req.headers['x-demo-code'] || '').trim();
    let data;
    if (Array.isArray(payload.steps)) {
      const result = {};
      for (const step of payload.steps) {
        result[step.key] = await callStep(step, accessCode);
      }
      data = result;
    } else {
      data = await callStep(payload, accessCode);
    }
    const task = createTask(data);
    res.status(200).json({ id: task.id, owner_token: task.owner_token, status: task.status });
  } catch (error) {
    const task = createTask({ status: 'failed', message: error.message });
    res.status(200).json({ id: task.id, owner_token: task.owner_token, status: task.status });
  }
}
