import { useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import CompareButton from '../components/CompareButton.jsx';
import LoadingIndicator from '../components/LoadingIndicator.jsx';
import PdfUpload from '../components/PdfUpload.jsx';
import { compareTexts } from '../api/comparisonApi.js';

function validPdf(file) {
  return file && file.type === 'application/pdf' && file.name.toLowerCase().endsWith('.pdf');
}

export default function TextComparisonPage() {
  const navigate = useNavigate();
  const [textAFile, setTextAFile] = useState(null);
  const [textBFile, setTextBFile] = useState(null);
  const [errors, setErrors] = useState({ textA: '', textB: '', form: '' });
  const [loading, setLoading] = useState(false);

  const canCompare = useMemo(() => validPdf(textAFile) && validPdf(textBFile), [textAFile, textBFile]);

  function updateFile(slot, file, error) {
    if (slot === 'textA') setTextAFile(error ? null : file);
    if (slot === 'textB') setTextBFile(error ? null : file);
    setErrors((current) => ({ ...current, [slot]: error, form: '' }));
  }

  async function handleCompare() {
    if (!canCompare || loading) return;

    setLoading(true);
    setErrors((current) => ({ ...current, form: '' }));
    try {
      const result = await compareTexts(textAFile, textBFile);
      navigate('/result', { state: { result } });
    } catch (error) {
      setErrors((current) => ({ ...current, form: error.message }));
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="page upload-page">
      <header className="page-header">
        <p>PDF Similarity Analysis</p>
        <h1>Compare two academic texts</h1>
      </header>

      <div className="upload-grid">
        <PdfUpload
          label="Text A PDF"
          file={textAFile}
          onFileChange={(file, error) => updateFile('textA', file, error)}
          validationError={errors.textA}
        />
        <PdfUpload
          label="Text B PDF"
          file={textBFile}
          onFileChange={(file, error) => updateFile('textB', file, error)}
          validationError={errors.textB}
        />
      </div>

      {loading && <LoadingIndicator />}
      {errors.form && <p className="form-error">{errors.form}</p>}

      <div className="action-row">
        <CompareButton disabled={!canCompare} loading={loading} onClick={handleCompare} />
      </div>
    </section>
  );
}

