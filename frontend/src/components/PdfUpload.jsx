import { FileText, Upload } from 'lucide-react';

function isValidPdf(file) {
  return file && file.type === 'application/pdf' && file.name.toLowerCase().endsWith('.pdf');
}

export default function PdfUpload({ label, file, onFileChange, validationError }) {
  function handleChange(event) {
    const selectedFile = event.target.files?.[0] || null;
    onFileChange(selectedFile, selectedFile && !isValidPdf(selectedFile) ? 'Select a valid PDF file.' : '');
  }

  return (
    <label className={`upload-panel ${validationError ? 'has-error' : ''}`}>
      <span className="upload-heading">
        <FileText size={20} aria-hidden="true" />
        {label}
      </span>
      <span className="upload-dropzone">
        <Upload size={22} aria-hidden="true" />
        <span>{file ? file.name : 'Choose one PDF file'}</span>
      </span>
      <input type="file" accept="application/pdf,.pdf" onChange={handleChange} />
      {validationError && <span className="field-error">{validationError}</span>}
    </label>
  );
}

