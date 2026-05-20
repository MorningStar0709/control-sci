const $ = (id) => document.getElementById(id);
const SAMPLE_PDF_URL = 'https://cdn-mineru.openxlab.org.cn/demo/example.pdf';

function renderJson(target, data) {
  target.textContent = JSON.stringify(data, null, 2);
}

async function api(path, options = {}) {
  const res = await fetch(path, options);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw data;
  return data;
}

async function loadHealth() {
  const [health, runtime, tracks] = await Promise.all([
    api('/api/health'),
    api('/api/runtime'),
    api('/api/tracks'),
  ]);
  const cards = [
    ['Profile', health.profile],
    ['MinerU', health.components.mineru_official_api.available ? 'configured' : 'missing key'],
    ['DeepSeek', health.components.deepseek_api.available ? 'configured' : 'missing key'],
    ['Quota', `${health.components.quota.remaining}/${health.components.quota.limit}`],
  ];
  $('healthCards').innerHTML = cards.map(([label, value]) => `
    <div class="card">
      <div class="label">${label}</div>
      <div class="value">${value}</div>
    </div>
  `).join('');
  const services = [
    ['MinerU', health.components.mineru_official_api.available],
    ['DeepSeek', health.components.deepseek_api.available],
    ['RAG', true],
    ['验收包', true],
  ];
  $('serviceDots').innerHTML = services.map(([label, ok]) => `
    <span class="service"><span class="dot ${ok ? 'ok' : 'bad'}"></span><span>${label}</span></span>
  `).join('');
  $('readyPill').textContent = `就绪 · 今日实时额度 ${health.components.quota.remaining}/${health.components.quota.limit}`;
  const checks = [
    `运行模式：${runtime.mode}`,
    `离线模型数量：${runtime.local_models.length}`,
    `解析后端：${runtime.parser_backends.map(x => x.id).join(', ')}`,
    `赛道数量：${tracks.tracks.length}`,
    `上传限制：${health.limits.upload_max_mb}MB`,
    `密钥只在服务端环境变量读取`,
  ];
  $('checks').innerHTML = checks.map(item => `<li>${item}</li>`).join('');
}

async function parseUrl() {
  const button = $('parseUrlBtn');
  const url = $('pdfUrl').value.trim();
  if (!url) {
    renderJson($('mineruResult'), {error: '请粘贴公开 PDF URL，或点击“内置样例”。'});
    return;
  }
  button.disabled = true;
  try {
    const data = await api('/api/mineru/url', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({url}),
    });
    renderJson($('mineruResult'), data);
  } catch (error) {
    renderJson($('mineruResult'), error);
  } finally {
    button.disabled = false;
    loadHealth();
  }
}

async function parseSample() {
  const button = $('sampleBtn');
  button.disabled = true;
  try {
    const data = await api('/api/mineru/url', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({url: SAMPLE_PDF_URL}),
    });
    renderJson($('mineruResult'), data);
  } catch (error) {
    renderJson($('mineruResult'), error);
  } finally {
    button.disabled = false;
    loadHealth();
  }
}

async function uploadPdf() {
  const button = $('uploadBtn');
  const file = $('pdfFile').files[0];
  if (!file) {
    renderJson($('mineruResult'), {error: '请选择公开 PDF 文件'});
    return;
  }
  const form = new FormData();
  form.append('file', file);
  button.disabled = true;
  try {
    const data = await api('/api/mineru/upload', {method: 'POST', body: form});
    renderJson($('mineruResult'), data);
  } catch (error) {
    renderJson($('mineruResult'), error);
  } finally {
    button.disabled = false;
    loadHealth();
  }
}

async function ask() {
  const button = $('askBtn');
  button.disabled = true;
  try {
    const data = await api('/api/deepseek/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        question: $('question').value.trim(),
        context: $('context').value.trim(),
      }),
    });
    renderJson($('askResult'), data);
  } catch (error) {
    renderJson($('askResult'), error);
  } finally {
    button.disabled = false;
    loadHealth();
  }
}

$('parseUrlBtn').addEventListener('click', parseUrl);
$('sampleBtn').addEventListener('click', parseSample);
$('uploadBtn').addEventListener('click', uploadPdf);
$('askBtn').addEventListener('click', ask);
loadHealth().catch(err => {
  $('healthCards').innerHTML = `<div class="card"><div class="label">Health</div><div class="value">failed</div></div>`;
  console.error(err);
});
