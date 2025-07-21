from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn
import pdfplumber
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Flask uygulaması başlatma
app = Flask(__name__)
CORS(app)

# CV Scoring Modeli
class CVScoringModel(nn.Module):
    def __init__(self):
        super(CVScoringModel, self).__init__()
        self.fc1 = nn.Linear(5, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Modeli yükle
model = CVScoringModel()
model.load_state_dict(torch.load('models/cv_scoring_model.pth'))
scaler = StandardScaler()

# PDF'den metin çıkarma fonksiyonu
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# CV'deki metni işle
def process_cv_text(text):
    experience = text.lower().count("year")
    education = text.lower().count("bachelor") + text.lower().count("master")
    skills = text.lower().count("python") + text.lower().count("java")
    language = text.lower().count("english")
    communication = text.lower().count("communication")
    return experience, education, skills, language, communication

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['cv']
    file_path = './Oğuzhan Bilgi CV .pdf'
    file.save(file_path)

    text = extract_text_from_pdf(file_path)
    experience, education, skills, language, communication = process_cv_text(text)

    features = [[experience, education, skills, language, communication]]
    features = scaler.fit_transform(features)

    features = torch.tensor(features, dtype=torch.float32)

    with torch.no_grad():
        output = model(features)
        score = output.item()

    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)
