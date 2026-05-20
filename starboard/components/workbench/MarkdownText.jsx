import ReactMarkdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import { normalizeDisplayMarkdown } from '../../lib/track1DisplayAdapter';

const markdownComponents = {
  p({ children }) {
    return <p className="my-1.5 leading-relaxed text-gray-800">{children}</p>;
  },
  strong({ children }) {
    return <strong className="font-semibold text-gray-900">{children}</strong>;
  },
  em({ children }) {
    return <em className="text-gray-700">{children}</em>;
  },
  ul({ children }) {
    return <ul className="my-2 list-disc space-y-1 pl-5">{children}</ul>;
  },
  ol({ children }) {
    return <ol className="my-2 list-decimal space-y-1 pl-5">{children}</ol>;
  },
  li({ children }) {
    return <li className="leading-relaxed">{children}</li>;
  },
  code({ children, className }) {
    if (className) {
      return <code className={`${className} font-mono text-[11px] text-gray-800`}>{children}</code>;
    }
    return <code className="rounded bg-gray-100 px-1 py-0.5 font-mono text-[11px] text-gray-700">{children}</code>;
  },
  pre({ children }) {
    return <pre className="my-2 overflow-x-auto rounded border bg-gray-50 p-3 text-xs leading-relaxed text-gray-800">{children}</pre>;
  },
  table({ children }) {
    return <table className="my-2 w-full min-w-full border-collapse text-xs">{children}</table>;
  },
  thead({ children }) {
    return <thead className="bg-gray-50">{children}</thead>;
  },
  th({ children }) {
    return <th className="border bg-gray-50 px-2 py-1 text-left font-semibold text-gray-700">{children}</th>;
  },
  td({ children }) {
    return <td className="border px-2 py-1 align-top text-gray-700">{children}</td>;
  },
  a({ href, children }) {
    return (
      <a className="text-blue-700 underline decoration-blue-200 underline-offset-2" href={href} target="_blank" rel="noreferrer">
        {children}
      </a>
    );
  },
};

export default function MarkdownText({ children, className = '' }) {
  const normalized = normalizeMarkdown(normalizeDisplayMarkdown(children || ''));
  return (
    <div className={`markdown-body text-sm leading-relaxed text-gray-800 ${className}`}>
      <ReactMarkdown
        components={markdownComponents}
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeKatex]}
      >
        {normalized}
      </ReactMarkdown>
    </div>
  );
}

function normalizeMarkdown(value) {
  const normalized = String(value || '')
    .replace(/\r\n/g, '\n')
    .replace(/\\n/g, '\n')
    .replace(/\t/g, '  ')
    .replace(/([^\n])(\n#{1,6}\s)/g, '$1\n$2')
    .replace(/([^\n])(\n[-*+]\s)/g, '$1\n$2')
    .replace(/([^\n])(\n\d+\.\s)/g, '$1\n$2')
    .replace(/\\\\\[/g, '$$')
    .replace(/\\\\\]/g, '$$')
    .replace(/\\\\\(/g, '$')
    .replace(/\\\\\)/g, '$')
    .replace(/\\\[/g, '$$')
    .replace(/\\\]/g, '$$')
    .replace(/\\\(/g, '$')
    .replace(/\\\)/g, '$');

  return wrapBareMathEnvironments(normalized)
    .split('\n')
    .map(wrapBareLatexLine)
    .join('\n')
    .replace(/\$\$\s*\n+/g, '$$\n')
    .replace(/\n+\s*\$\$/g, '\n$$');
}

function wrapBareMathEnvironments(value) {
  const envPattern = /\\begin\{(?:aligned|align|equation|gather|cases|matrix|bmatrix|pmatrix|array)\}[\s\S]*?\\end\{(?:aligned|align|equation|gather|cases|matrix|bmatrix|pmatrix|array)\}/g;
  return value.replace(envPattern, (match, offset, source) => {
    if (isProseContaminatedMathBlock(match)) {
      return match.replace(/\\begin\{(?:aligned|align|equation|gather|cases|matrix|bmatrix|pmatrix|array)\}/g, '').replace(/\\end\{(?:aligned|align|equation|gather|cases|matrix|bmatrix|pmatrix|array)\}/g, '');
    }
    const before = source.slice(0, offset).trimEnd();
    const after = source.slice(offset + match.length).trimStart();
    if (before.endsWith('$$') || before.endsWith('$') || after.startsWith('$$') || after.startsWith('$')) {
      return match;
    }
    return `$$\n${match}\n$$`;
  });
}

function isProseContaminatedMathBlock(block) {
  const chineseChars = (block.match(/[\u4e00-\u9fff]/g) || []).length;
  const mathRows = (block.match(/&=|&\s|\\\\/g) || []).length;
  return chineseChars > 24 || (/教材|试判断|说明理由|其中|即\s|为决策变量|约束矩阵形式/.test(block) && chineseChars > mathRows * 3);
}

function wrapBareLatexLine(line) {
  const trimmed = line.trim();
  if (!trimmed || trimmed.startsWith('$') || trimmed.endsWith('$')) return line;
  if (/^[-*+]\s/.test(trimmed) || /^\d+\.\s/.test(trimmed)) return line;
  if (!looksLikeLatex(trimmed)) return line;
  const prefixMatch = line.match(/^(\s*)/);
  const prefix = prefixMatch?.[1] || '';
  return `${prefix}$$\n${trimmed}\n${prefix}$$`;
}

function looksLikeLatex(text) {
  if (text.length > 260) return false;
  const commandCount = (text.match(/\\(?:frac|dot|ddot|sum|int|lim|begin|end|alpha|beta|gamma|delta|lambda|mu|sigma|theta|omega|Phi|Psi|Omega|left|right|mathbb|mathbf|mathrm|hat|bar|tilde)/g) || []).length;
  if (!commandCount) return false;
  const mathSignals = /[_^=<>]|\\(?:frac|sum|int|begin|dot|ddot|left|right)/.test(text);
  const proseSignals = /[，。；、]/.test(text) || text.length > 140;
  return mathSignals && !proseSignals;
}
