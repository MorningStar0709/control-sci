import { useEffect } from 'react';
import { useRouter } from 'next/router';

export default function Index() {
  const router = useRouter();
  useEffect(() => { router.replace('/home'); }, [router]);
  return <div className="p-8 text-gray-500 text-sm">Redirecting to Overview...</div>;
}
