export default function LoadingIndicator() {
  return (
    <div className="loading-indicator" role="status" aria-live="polite">
      <span className="spinner" />
      Extracting and comparing the PDFs...
    </div>
  );
}

