import { findMedicalAskReplay } from '../../../lib/medicalAskReplay';

function fallbackReplay(query) {
  return findMedicalAskReplay(query) || findMedicalAskReplay('化疗剂量减少和治疗延迟的不良事件证据');
}

export default function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'method not allowed' });
    return;
  }
  const query = String(req.body?.query || req.body?.question || '');
  const replay = fallbackReplay(query);
  if (!replay) {
    res.status(200).json({
      status: 'failed',
      message: '未找到可公开回放的医学 RAG trace。',
    });
    return;
  }
  res.status(200).json({
    ...replay,
    status: replay.status || 'replay',
    search_query: replay.search_query || query,
    search_queries: replay.search_queries?.length ? replay.search_queries : [query].filter(Boolean),
    retrieval_mode: req.body?.mode || replay.retrieval_mode || 'hybrid',
    retrieval_index: replay.retrieval_index || { label: 'BGE M3', alias: 'bge_m3' },
  });
}
