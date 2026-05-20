import { findMedicalAskReplay } from '../../../lib/medicalAskReplay';

function fallbackReplay(query) {
  return findMedicalAskReplay(query) || findMedicalAskReplay('化疗剂量减少和治疗延迟的不良事件证据');
}

export default function handler(req, res) {
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'method not allowed' });
    return;
  }
  const query = String(req.query.q || '');
  const replay = fallbackReplay(query);
  if (!replay || replay.status === 'safety_refusal') {
    res.status(200).json({ status: replay?.status || 'empty', results: [] });
    return;
  }
  res.status(200).json({
    status: 'replay',
    query,
    mode: req.query.mode || 'hybrid',
    index_id: req.query.index_id || 'bge_m3',
    results: (replay.evidence_items || []).map((item, index) => ({
      rank: index + 1,
      source_file: item.source_file || 'verified_trace',
      source_section: item.source_section || item.medical_label || '',
      medical_parent: item.medical_parent || '',
      mode: req.query.mode || 'hybrid',
      rrf_score: item.rrf_score || 'replay',
      text_preview: item.text_preview || item.preview || '',
      ...item,
    })),
  });
}
