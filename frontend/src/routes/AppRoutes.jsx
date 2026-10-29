import { Route, Routes } from 'react-router-dom';
import TextComparisonPage from '../pages/TextComparisonPage.jsx';
import ResultPage from '../pages/ResultPage.jsx';

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<TextComparisonPage />} />
      <Route path="/result" element={<ResultPage />} />
    </Routes>
  );
}

