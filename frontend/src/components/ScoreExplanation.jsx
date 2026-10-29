function levelFor(score) {
  if (score >= 70) return 'High';
  if (score >= 40) return 'Medium';
  return 'Low';
}

export default function ScoreExplanation({ explanation, score }) {
  return (
    <section className="analysis-section">
      <h2>Score Explanation</h2>
      <p className="score-level">{levelFor(score)} correlation</p>
      <p>{explanation}</p>
    </section>
  );
}

