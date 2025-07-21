import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // CSS dosyasını dahil ediyoruz

function App() {
  const [file, setFile] = useState(null);
  const [score, setScore] = useState(null);
  const [criteria, setCriteria] = useState(null); // Kriter puanları için state

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Lütfen bir CV dosyası seçin.");
      return;
    }

    const formData = new FormData();
    formData.append("cv", file);

    try {
      const response = await axios.post("http://localhost:5000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setScore(response.data.score);
      setCriteria(response.data.criteria); // Kriterleri de alıyoruz
    } catch (error) {
      console.error("Hata oluştu:", error);
    }
  };

  const handleReset = () => {
    setFile(null);
    setScore(null);
    setCriteria(null); // Reset tüm veriler
  };

  return (
    <div className="container">
      <div className="content">
        <h1 className="title">Oğuzhan Bilgi</h1>
        <h2>ATS CV Değerlendirme Aracı</h2>
        <p>CV'nizi yükleyin ve ATS uyumluluğunuzu kontrol edin.</p>
        <div className="upload-area">
          <input
            type="file"
            id="file-upload"
            onChange={handleFileChange}
            accept=".pdf,.doc,.docx"
          />
          <button onClick={handleUpload}>CV Yükle</button>
        </div>
        <div className="reset-button">
          {score && <button onClick={handleReset}>Yeni CV Yükle</button>} {/* Yükleme butonu */}
        </div>

        {score && (
          <div className="score-display">
            <h3>ATS Puanı</h3>
            <div className="score-bar">
              <div
                className="score"
                style={{ width: `${score}%`, backgroundColor: score >= 70 ? "#4caf50" : "#f44336" }}
              >
                {score} / 100
              </div>
            </div>

            {/* Bilgilendirici kriterler */}
            <div className="criteria">
              {criteria && criteria.map((criterion, index) => (
                <div key={index} className="criterion">
                  <h4>{criterion.name}</h4>
                  <div className="criterion-bar">
                    <div
                      className="criterion-progress"
                      style={{ width: `${criterion.score}%`, backgroundColor: "#0072ff" }}
                    >
                      {criterion.score} / 100
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
