export function taskStore() {
  if (!globalThis.__controlmindCloudTasks) {
    globalThis.__controlmindCloudTasks = new Map();
  }
  return globalThis.__controlmindCloudTasks;
}

function createOwnerToken() {
  return `tok-${Date.now()}-${Math.random().toString(16).slice(2, 14)}`;
}

export function createTask(data) {
  const id = `cloud-${Date.now()}-${Math.random().toString(16).slice(2)}`;
  const task = {
    id,
    owner_token: createOwnerToken(),
    status: 'done',
    data,
    created_at: new Date().toISOString(),
  };
  taskStore().set(id, task);
  return task;
}

export function verifyTaskOwner(task, token) {
  return Boolean(task?.owner_token && token && task.owner_token === token);
}

export function toPublicTask(task) {
  if (!task) return null;
  const { owner_token, ...publicTask } = task;
  return publicTask;
}
