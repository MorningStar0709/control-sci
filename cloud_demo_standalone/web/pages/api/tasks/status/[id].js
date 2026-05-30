import { taskStore, toPublicTask, verifyTaskOwner } from '../store';

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
  const token = req.headers['x-task-token'] || req.query.token;
  if (!verifyTaskOwner(task, token)) {
    res.status(403).json({ status: 'failed', error: 'task token required' });
    return;
  }
  res.status(200).json(toPublicTask(task));
}
