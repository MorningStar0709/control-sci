import { useEffect, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import {
  AchievementOverview,
  CapabilityMatrix,
  LocalCloudMirrorMap,
  MetricGrid,
  OutcomeStrip,
  PageHeader,
  ShowcaseHeader,
  loadCloudState,
} from '../components/workbench/CloudDemoBlocks';

export default function HomePage() {
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
        <ShowcaseHeader health={state.health} />
        <PageHeader title="总览" desc="集中展示三赛道核心成果、公开展示边界、云端服务状态和可核验输出。" />
        <MetricGrid health={state.health} />
        <AchievementOverview />
        <LocalCloudMirrorMap />
        <OutcomeStrip />
        <CapabilityMatrix />
      </div>
    </SectionWrapper>
  );
}
