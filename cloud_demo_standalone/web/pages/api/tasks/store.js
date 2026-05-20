export function taskStore() {
  if (!globalThis.__controlmindCloudTasks) {
    globalThis.__controlmindCloudTasks = new Map();
  }
  return globalThis.__controlmindCloudTasks;
}

export function createTask(data) {
  const id = `cloud-${Date.now()}-${Math.random().toString(16).slice(2)}`;
  taskStore().set(id, {
    id,
    status: 'done',
    data,
    created_at: new Date().toISOString(),
  });
  return id;
}
