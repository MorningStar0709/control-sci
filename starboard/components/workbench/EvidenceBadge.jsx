export default function EvidenceBadge({ text = '本地', color = 'green' }) {
  const colors = {
    green: 'bg-green-100 text-green-700',
    blue: 'bg-blue-100 text-blue-700',
    purple: 'bg-purple-100 text-purple-700',
    red: 'bg-red-100 text-red-700',
    yellow: 'bg-yellow-100 text-yellow-700',
    amber: 'bg-amber-100 text-amber-700',
    emerald: 'bg-emerald-100 text-emerald-700',
    gray: 'bg-gray-100 text-gray-600',
  };
  return <span className={`text-[10px] px-1.5 py-0.5 rounded font-mono ${colors[color] || colors.gray}`}>{text}</span>;
}
