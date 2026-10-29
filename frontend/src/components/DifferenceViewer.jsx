export default function DifferenceViewer({ sections = [] }) {
  const lowerSimilarity = sections.filter((section) => Number(section.similarity) < 85);

  if (!lowerSimilarity.length) {
    return <p className="empty-state">The response did not include low-similarity excerpt pairs.</p>;
  }

  return (
    <div className="difference-grid">
      {lowerSimilarity.map((section, index) => (
        <article className="difference-row" key={`${section.text_a_excerpt}-${index}`}>
          <p>{section.text_a_excerpt}</p>
          <p>{section.text_b_excerpt}</p>
        </article>
      ))}
    </div>
  );
}

