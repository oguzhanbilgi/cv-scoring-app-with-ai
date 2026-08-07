# AI-Assisted CV Scoring Prototype

A React-based portfolio prototype for uploading a CV and displaying an ATS-style score returned by a backend service.

> This repository currently contains the **frontend client**. The UI sends the selected CV file to a `/predict` endpoint and displays the returned score. The backend/NLP implementation is not included in this public repository, so this README does not claim functionality that cannot be verified from the code here.

## What it demonstrates

- React state and file-input handling
- Multipart file upload with Axios
- Frontend-to-backend API integration
- Score visualization and conditional UI styling
- GitHub Pages deployment workflow
- AI-assisted development used as part of the learning process

## Tech stack

- React 19
- JavaScript
- Axios
- Create React App
- GitHub Pages

## Current flow

```text
Select CV file
    ↓
React builds FormData
    ↓
POST http://localhost:5000/predict
    ↓
Backend returns { score: ... }
    ↓
UI displays ATS score
```

## Local setup

```bash
git clone https://github.com/oguzhanbilgi/cv-scoring-app-with-ai.git
cd cv-scoring-app-with-ai
npm install
npm start
```

The frontend expects a backend service at:

```text
POST http://localhost:5000/predict
```

with a multipart form field named `cv` and a JSON response containing a `score` value.

## Project status

This is an early portfolio/learning prototype, not a production ATS or hiring decision system. The public repository currently focuses on the frontend experience.

Planned improvements:

- Include or document the backend service
- Replace the hard-coded API URL with environment configuration
- Add upload progress and clearer error states
- Validate file size/type before upload
- Add automated frontend tests
- Add accessible score feedback
- Document the scoring method and limitations if the backend is published

## Responsible use

A CV score should never be treated as a final hiring decision. Any future scoring logic should be transparent, tested for bias and used only as one supporting signal alongside human review.

## Related links

- [Portfolio](https://oguzhanbilgi.github.io/oguzhan-portfolio/)
- [GitHub profile](https://github.com/oguzhanbilgi)
- [LinkedIn](https://www.linkedin.com/in/oguzhanbilgi3/)

## Author

**Oğuzhan Bilgi** — Junior Software Developer / Technical Engineer based in Istanbul, Türkiye.
