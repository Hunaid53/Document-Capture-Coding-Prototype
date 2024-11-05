import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Import the CSS file

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/extract', formData);
      setData(response.data);
    } catch (error) {
      console.error("Error extracting data", error);
    }
  };

  return (
    <div className="app-container">
      <h1>Document Capture</h1>
      <form onSubmit={handleSubmit} className="upload-form">
        <input type="file" accept="image/*" onChange={handleFileChange} required />
        <button type="submit" className="submit-button">Extract Data</button>
      </form>
      {data && (
        <div className="extracted-data">
          <h2>Extracted Data</h2>
          <p><strong>Name:</strong> {data.name}</p>
          <p><strong>Document Number:</strong> {data.document_number}</p>
          <p><strong>Expiration Date:</strong> {data.expiration_date}</p>
        </div>
      )}
    </div>
  );
}

export default App;