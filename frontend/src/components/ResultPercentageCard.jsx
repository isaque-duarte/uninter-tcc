function levelFor(score) {
  if (score >= 70) return 'high';
  if (score >= 40) return 'medium';
  return 'low';
}

export default function ResultPercentageCard({ score }) {
  const level = levelFor(score);
  return (
    <section className={`result-hero ${level}`}>
      <p>Correlation between Text A and Text B</p>
      <strong>{Number(score).toFixed(1)}%</strong>
      <span>{level} correlation</span>
    </section>
  );
}

