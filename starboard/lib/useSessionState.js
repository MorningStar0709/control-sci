import { useEffect, useState } from 'react';

export default function useSessionState(key, initialValue) {
  const [value, setValue] = useState(initialValue);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    try {
      const raw = window.sessionStorage.getItem(key);
      if (raw) setValue(JSON.parse(raw));
    } catch {
      // Ignore malformed session snapshots.
    }
    setHydrated(true);
  }, [key]);

  useEffect(() => {
    if (!hydrated) return;
    window.sessionStorage.setItem(key, JSON.stringify(value));
  }, [hydrated, key, value]);

  return [value, setValue];
}
