export default function ControlMindLogo({ size = 'md' }) {
  const box = size === 'sm' ? 'w-8 h-8 rounded-lg' : 'w-10 h-10 rounded-lg';
  const svg = size === 'sm' ? 'w-4 h-4' : 'w-5 h-5';

  return (
    <div className={`${box} bg-white border border-gray-200 shadow-sm flex items-center justify-center flex-shrink-0 text-gray-900`}>
      <svg viewBox="0 0 24 24" className={svg} fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h5" />
        <path d="M14 3v5h5" />
        <path d="M9 12h5M9 16h3" />
        <circle cx="16.5" cy="16.5" r="3.5" />
        <path d="M19.2 19.2 21 21" />
      </svg>
    </div>
  );
}
