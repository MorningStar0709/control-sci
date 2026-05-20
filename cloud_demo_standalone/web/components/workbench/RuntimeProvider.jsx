import { createContext, useContext, useEffect, useMemo, useState } from 'react';
import { apiGet } from '../../lib/apiClient';
import { DEFAULT_RUNTIME_CONFIG, mergeRuntimeDefaults } from '../../lib/runtimeDefaults';

const RuntimeContext = createContext(null);

export function RuntimeProvider({ children }) {
  const [runtimeConfig, setRuntimeConfig] = useState(DEFAULT_RUNTIME_CONFIG);
  const [runtimeOptions, setRuntimeOptions] = useState(null);
  const [health, setHealth] = useState(null);

  async function refreshHealth() {
    const result = await apiGet('/api/demo/health', { timeoutMs: 30000 });
    if (result.ok) {
      setHealth(result.data);
    } else {
      setHealth({ status: 'offline', error: result.error, components: {} });
    }
    return result;
  }

  async function refreshOptions() {
    const result = await apiGet('/api/demo/runtime/options', { timeoutMs: 30000 });
    if (result.ok) {
      setRuntimeOptions(result.data);
      setRuntimeConfig(prev => mergeRuntimeDefaults(result.data, prev));
    }
    return result;
  }

  function updateRuntime(patch) {
    setRuntimeConfig(prev => ({ ...prev, ...(patch || {}) }));
  }

  useEffect(() => {
    refreshOptions();
    refreshHealth();
    const timer = setInterval(refreshHealth, 30000);
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    if (typeof window !== 'undefined' && health) {
      window.dispatchEvent(new CustomEvent('cloud-demo-health', { detail: health }));
    }
  }, [health]);

  const value = useMemo(() => ({
    runtimeConfig,
    runtimeOptions,
    health,
    setRuntimeConfig,
    updateRuntime,
    refreshHealth,
    refreshOptions,
  }), [runtimeConfig, runtimeOptions, health]);

  return <RuntimeContext.Provider value={value}>{children}</RuntimeContext.Provider>;
}

export function useRuntime() {
  const ctx = useContext(RuntimeContext);
  if (!ctx) {
    return {
      runtimeConfig: DEFAULT_RUNTIME_CONFIG,
      runtimeOptions: null,
      health: null,
      setRuntimeConfig: () => {},
      updateRuntime: () => {},
      refreshHealth: async () => ({ ok: false, error: 'RuntimeProvider unavailable' }),
      refreshOptions: async () => ({ ok: false, error: 'RuntimeProvider unavailable' }),
    };
  }
  return ctx;
}
