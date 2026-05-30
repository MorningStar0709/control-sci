import { useEffect, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import {
  AcceptanceCard,
  ApiPipeline,
  DemoRouteMap,
  Notice,
  PageHeader,
  loadCloudState,
} from '../components/workbench/CloudDemoBlocks';

export default function DemoPage() {
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
        <PageHeader title="展示导览" desc="按参观路径组织可操作入口：先确认云端状态，再依次浏览赛道一、赛道二、赛道三，最后回到来源矩阵查看成果与来源。" />
        <DemoRouteMap />
        <ApiPipeline />
        <Notice />
        <AcceptanceCard {...state} />
      </div>
    </SectionWrapper>
  );
}
