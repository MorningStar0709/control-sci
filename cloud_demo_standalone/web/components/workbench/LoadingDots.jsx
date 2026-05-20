export default function LoadingDots({
  className = 'w-5',
  dotClassName = 'bg-current',
  sizeClassName = 'h-1.5 w-1.5',
}) {
  return (
    <span className={`inline-flex items-center justify-between ${className}`} aria-hidden="true">
      <span className={`${sizeClassName} animate-bounce rounded-full ${dotClassName} [animation-delay:-0.2s]`} />
      <span className={`${sizeClassName} animate-bounce rounded-full ${dotClassName} [animation-delay:-0.1s]`} />
      <span className={`${sizeClassName} animate-bounce rounded-full ${dotClassName}`} />
    </span>
  );
}
