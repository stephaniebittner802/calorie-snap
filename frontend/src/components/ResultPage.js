import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './ResultPage.css';

function ResultPage() {
  const navigate = useNavigate();
  const [calories, setCalories] = useState(null);
  const [foodName, setFoodName] = useState('');
  const [aiInfo, setAiInfo] = useState('AI info not available.');
  const [detectedObjects, setDetectedObjects] = useState([]);

  useEffect(() => {
    const name = localStorage.getItem('foodName');
    const cals = localStorage.getItem('calories');
    const info = localStorage.getItem('info');
    const objects = JSON.parse(localStorage.getItem('detectedObjects'));

    setFoodName(name);
    setCalories(cals);
    setAiInfo(info || 'AI info not available.');
    setDetectedObjects(objects || []);
  }, []);

  const handleBack = () => {
    navigate('/');
  };

  return (
    <>
      <h2>CalorieSnap</h2>
      <div className="container">
        <div className="result-box">
          <div className="prediction-display">{calories} calories</div>
          <p style={{ marginTop: '20px', fontSize: '1.1rem' }}>{aiInfo}</p>
          <div className="buttons">
            <button onClick={handleBack}>← Back to Home</button>
          </div>
        </div>
      </div>
    </>
  );
}

export default ResultPage;
