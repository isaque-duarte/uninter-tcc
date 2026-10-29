import { ArrowLeft } from 'lucide-react';
import { Link, Navigate, useLocation } from 'react-router-dom';
import DifferenceViewer from '../components/DifferenceViewer.jsx';
import KeywordsList from '../components/KeywordsList.jsx';
import ResultPercentageCard from '../components/ResultPercentageCard.jsx';
import ScoreExplanation from '../components/ScoreExplanation.jsx';
import SimilarExcerptsViewer from '../components/SimilarExcerptsViewer.jsx';

export default function ResultPage() {
  const location = useLocation();
  const result = location.state?.result;

  if (!result) {
    return <Navigate to="/" replace />;
  }

  return (
    <section className="page result-page">
      <Link className="back-link" to="/">
        <ArrowLeft size={18} aria-hidden="true" />
        New comparison
      </Link>

      <ResultPercentageCard score={result.final_correlation} />

      <section className="score-grid" aria-label="Similarity scores">
        <div>
          <span>Lexical similarity</span>
          <strong>{Number(result.lexical_similarity).toFixed(1)}%</strong>
        </div>
        <div>
          <span>Semantic similarity</span>
          <strong>{Number(result.semantic_similarity).toFixed(1)}%</strong>
        </div>
      </section>

      <ScoreExplanation explanation={result.score_explanation} score={result.final_correlation} />

      <section className="analysis-section">
        <h2>Similar Excerpts</h2>
        <SimilarExcerptsViewer sections={result.similar_sections} />
      </section>

      <section className="analysis-section">
        <h2>Common Keywords</h2>
        <KeywordsList keywords={result.common_keywords} />
      </section>

      <section className="analysis-section">
        <h2>Duplicated or Paraphrased Content</h2>
        {result.duplicated_or_paraphrased_content.length ? (
          <ul className="content-flags">
            {result.duplicated_or_paraphrased_content.map((item) => (
              <li key={`${item.type}-${item.description}`}>
                <strong>{item.type}</strong>
                <span>{item.description}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="empty-state">No duplicated or paraphrased sections crossed the configured thresholds.</p>
        )}
      </section>

      <section className="analysis-section">
        <h2>Relevant Differences</h2>
        <DifferenceViewer sections={result.similar_sections} />
      </section>
    </section>
  );
}

