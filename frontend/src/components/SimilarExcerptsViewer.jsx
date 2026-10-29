export default function SimilarExcerptsViewer({ sections = [] }) {
  if (!sections.length) {
    return <p className="empty-state">No highly similar excerpts were found.</p>;
  }

  return (
    <div className="excerpt-list">
      {sections.map((section, index) => (
        <article className="excerpt-pair" key={`${section.similarity}-${index}`}>
          <div className="excerpt-score">{Number(section.similarity).toFixed(1)}%</div>
          <div>
            <h3>Text A</h3>
            <p>{section.text_a_excerpt}</p>
          </div>
          <div>
            <h3>Text B</h3>
            <p>{section.text_b_excerpt}</p>
          </div>
        </article>
      ))}
    </div>
  );
}

