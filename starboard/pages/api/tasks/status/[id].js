import { getTask, toPublicTask, verifyTaskOwner } from '../../../../lib/serverTaskStore';

export default function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
  if (req.method !== 'GET') {
    res.status(405).json({ error: 'method not allowed' });
    return;
  }
  const task = getTask(req.query.id);
  if (!task) {
    res.status(404).json({ error: 'task not found' });
    return;
  }
  const token = req.headers['x-task-token'] || req.query.token;
  if (!verifyTaskOwner(task, token)) {
    res.status(403).json({ error: 'task token required' });
    return;
  }
  res.status(200).json(toPublicTask(task));
}
