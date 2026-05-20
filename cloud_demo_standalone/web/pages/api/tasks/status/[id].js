import { taskStore } from '../store';

export default function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
  const id = String(req.query.id || '');
  const task = taskStore().get(id);
  if (!task) {
    res.status(404).json({ status: 'failed', error: 'task not found' });
    return;
  }
  res.status(200).json(task);
}
