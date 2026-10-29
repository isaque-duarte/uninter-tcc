export default function KeywordsList({ keywords = [] }) {
  if (!keywords.length) {
    return <p className="empty-state">No shared keywords were identified.</p>;
  }

  return (
    <ul className="keywords-list">
      {keywords.map((keyword) => (
        <li key={keyword}>{keyword}</li>
      ))}
    </ul>
  );
}

