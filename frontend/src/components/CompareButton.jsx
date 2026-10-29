import { ArrowRight } from 'lucide-react';

export default function CompareButton({ disabled, loading, onClick }) {
  return (
    <button className="compare-button" type="button" disabled={disabled || loading} onClick={onClick}>
      <span>{loading ? 'Processing' : 'Compare Texts'}</span>
      <ArrowRight size={18} aria-hidden="true" />
    </button>
  );
}

