import http from 'http';

export const config = {
  api: {
    bodyParser: false,
  },
};

const BACKEND = process.env.CONTROLMIND_BACKEND_URL || 'http://127.0.0.1:17001';
const HOP_BY_HOP_HEADERS = new Set([
  'connection',
  'content-length',
  'host',
  'keep-alive',
  'proxy-authenticate',
  'proxy-authorization',
  'te',
  'trailer',
  'transfer-encoding',
  'upgrade',
]);
const PROXY_HEADER_ALLOWLIST = new Set(['accept', 'content-type', 'x-request-id', 'x-runtime-profile']);

function proxyHeaders(reqHeaders, targetHost) {
  const headers = {};
  Object.entries(reqHeaders || {}).forEach(([key, value]) => {
    const lower = key.toLowerCase();
    if (!HOP_BY_HOP_HEADERS.has(lower) && PROXY_HEADER_ALLOWLIST.has(lower)) headers[key] = value;
  });
  headers.host = targetHost;
  return headers;
}

function queryString(query) {
  const params = new URLSearchParams();
  Object.entries(query || {}).forEach(([key, value]) => {
    if (key === 'path') return;
    if (Array.isArray(value)) value.forEach(v => params.append(key, v));
    else if (value !== undefined) params.append(key, value);
  });
  const text = params.toString();
  return text ? `?${text}` : '';
}

function offlineResponse(path) {
  return {
    status: 'offline',
    path,
    answer: 'Medical RAG API 未连通。请启动 FastAPI 17001 后再进行本地医学问答。',
    citations: [],
    claims: [],
    evidence_items: [],
    privacy: 'local_only',
  };
}

export default function handler(req, res) {
  return new Promise(resolve => {
    const path = Array.isArray(req.query.path) ? req.query.path.join('/') : String(req.query.path || '');
    const targetUrl = new URL(`${BACKEND}/api/medical-rag/${path}${queryString(req.query)}`);
    const headers = proxyHeaders(req.headers, targetUrl.host);

    const request = http.request({
      hostname: targetUrl.hostname,
      port: targetUrl.port,
      path: `${targetUrl.pathname}${targetUrl.search}`,
      method: req.method,
      headers,
      timeout: 180000,
    }, upstream => {
      res.statusCode = upstream.statusCode || 200;
      Object.entries(upstream.headers).forEach(([key, value]) => {
        if (value !== undefined) res.setHeader(key, value);
      });
      upstream.pipe(res);
      upstream.on('end', resolve);
    });

    request.on('timeout', () => request.destroy(new Error('backend timeout')));
    request.on('error', () => {
      if (!res.headersSent) res.status(200).json(offlineResponse(path));
      resolve();
    });
    req.pipe(request);
  });
}
