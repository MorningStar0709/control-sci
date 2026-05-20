export default function ErrorCallout({ title = '请求未完成', message, hint }) {
  if (!message && !hint) return null;
  return (
    <div className="border border-amber-200 bg-amber-50 rounded-lg p-3 text-xs text-amber-800">
      <div className="font-semibold mb-1">{title}</div>
      {message && <div>{message}</div>}
      {hint && <div className="mt-1 text-amber-700">{hint}</div>}
    </div>
  );
}
