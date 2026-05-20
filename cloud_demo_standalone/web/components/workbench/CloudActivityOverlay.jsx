import WorkbenchLoadingCard from './WorkbenchLoadingCard';

export default function CloudActivityOverlay({
  active,
  title = '正在处理云端任务',
  desc = '请求已提交，完成后页面会自动更新。',
  steps = [],
}) {
  if (!active) return null;

  return (
    <div className="pointer-events-none fixed bottom-4 right-4 z-50 w-[min(420px,calc(100vw-2rem))]">
      <WorkbenchLoadingCard
        title={title}
        desc={desc}
        steps={steps}
        className="pointer-events-auto border-gray-300 shadow-xl"
      />
    </div>
  );
}
