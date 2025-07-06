import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
  const [foodName, setFoodName] = useState('');
  const [image, setImage] = useState(null);
  const fileInputRef = useRef(null);
  const navigate = useNavigate();

  const triggerFileInput = () => {
    fileInputRef.current.click();
  };

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const previewUrl = URL.createObjectURL(file);
      setImage(previewUrl);
      localStorage.setItem('imagePreview', previewUrl);   
    }
  };

  // Convert image to base64
  const convertImageToBase64 = (file, callback) => {
    const reader = new FileReader();
    reader.onloadend = () => {
      const base64Image = reader.result.split(',')[1];  // Extract base64 data
      callback(base64Image);  // Pass the base64 data to the callback
    };
    reader.readAsDataURL(file);  // Convert file to base64
  };

  const handleSubmit = async (event) => {
    // Prevent form submission
    event.preventDefault();

    // Check if either food name or image is provided
    if (!foodName.trim() && !image) {
      alert('Please enter a food name or upload an image.');
      return;
    }

    // Save food name or image in localStorage (whichever is provided)
    if (foodName.trim()) {
      localStorage.setItem('foodName', foodName);
    }
    if (image) {
      localStorage.setItem('imagePreview', image);
    }

    let requestBody = {};
    let apiUrl = '';

    if (foodName.trim()) {
      requestBody = { food: foodName };
      apiUrl = 'https://calorie-snap.onrender.com/predict_text';  // Send to food prediction route
      fetchDataToBackend(apiUrl, requestBody);
    } else if (image) {
      // Get the file object from the input
      const file = fileInputRef.current.files[0];
      if (file) {
        // Convert the image file to base64
        convertImageToBase64(file, (base64Image) => {
          requestBody = { image: base64Image };  // Send base64 image data to backend
          apiUrl = 'https://calorie-snap.onrender.com/predict_image';  // Send to image prediction route

          // Send the request to the backend with the base64 image data
          fetchDataToBackend(apiUrl, requestBody);
        });
      }
    }
  };

  // Function to send data to backend
  const fetchDataToBackend = async (apiUrl, requestBody) => {
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestBody),
      });

      const data = await response.json();
      console.log("Backend response:", data);  // Debugging line
      localStorage.setItem('calories', data.calories || 'Unknown');
      localStorage.setItem('info', data.info || 'AI info not available.');
      localStorage.setItem('detectedObjects', JSON.stringify(data.objects || [])); // Save detected objects

      navigate('/results');
    } catch (error) {
      console.error('Error fetching data from backend:', error);
      alert('Something went wrong. Please try again.');
    }
  };

  return (
    <>
      <h2>CalorieSnap</h2>
      <div className="container">
        <div className="card">
          <h3>Enter Food or Add a Picture</h3>

          <input
            type="text"
            placeholder="Food Name"
            value={foodName}
            onChange={(e) => setFoodName(e.target.value)}
          />

          <div className="upload-box" onClick={triggerFileInput}>
            {image ? (
              <img src={image} alt="Preview" className="image-preview" />
            ) : (
              <span>Add a Picture</span>
            )}
            <input
              type="file"
              accept="image/*"
              capture="camera"
              ref={fileInputRef}
              onChange={handleImageUpload}
              hidden
            />
          </div>

          <div className="buttons">
            <button onClick={handleSubmit}>Submit</button>
          </div>
        </div>
      </div>
    </>
  );
}

export default HomePage;
