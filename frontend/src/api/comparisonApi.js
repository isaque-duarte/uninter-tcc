const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export async function compareTexts(textAFile, textBFile) {
  const formData = new FormData();
  formData.append('text_a_pdf', textAFile);
  formData.append('text_b_pdf', textBFile);

  const response = await fetch(`${API_BASE_URL}/compare`, {
    method: 'POST',
    body: formData,
  });

  let payload = null;
  try {
    payload = await response.json();
  } catch {
    payload = null;
  }

  if (!response.ok) {
    throw new Error(payload?.detail || 'The comparison could not be completed.');
  }

  return payload;
}

