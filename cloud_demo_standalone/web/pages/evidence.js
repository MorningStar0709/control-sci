import { useEffect, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import { AcceptanceCard, ApiPipeline, EvidenceMatrix, loadCloudState } from '../components/workbench/CloudDemoBlocks';

export default function EvidencePage() {
  const [state, setState] = useState({ health: null, runtime: null, tracks: null });
  useEffect(() => {
    loadCloudState().then(setState);
    const syncHealth = event => setState(prev => ({ ...prev, health: event.detail }));
    window.addEventListener('cloud-demo-health', syncHealth);
    return () => window.removeEventListener('cloud-demo-health', syncHealth);
  }, []);
  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <EvidenceMatrix />
        <ApiPipeline />
        <AcceptanceCard {...state} />
      </div>
    </SectionWrapper>
  );
}
