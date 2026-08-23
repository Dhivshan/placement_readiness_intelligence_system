# 📊 placement_readiness_intelligence_system (PRIS)

# Overview
PRIS is a Streamlit-based application designed to evaluate student placement readiness.
It integrates:

Resume parsing (PDF → text → structured features)

Job description analysis

AI feedback generation (Gemini / Groq APIs)

ML readiness scoring (classification + salary estimation)

# ✨ Features
Resume Upload: Extracts text from PDF resumes using PyMuPDF.

Job Description Input: Accepts pasted JD text.

Text Preprocessing: Cleans and normalizes text, removes noise.

AI Analysis:

Gemini / Groq APIs extract structured skills and generate feedback reports.

Normalizes skills using ESCO / skill dictionary.

ML Scoring:

Predicts placement readiness status.

Estimates salary/package.

Provides matched/missing/critical skills breakdown.

Dashboard: Interactive Streamlit UI with readiness results and feedback.

# 📂 Dataset
This project uses synthetic resumes and job descriptions to simulate placement scenarios.

Resumes include academic metrics (Education, skills, projects, Experience).

Job descriptions include required, critical, and optional skills.

Data is synthetic to ensure privacy, reproducibility, and flexibility in experimentation.

Use Cases
Placement status prediction

Salary/package estimation

Student performance analysis

Feature engineering on academic metrics

ML classification testing

Advantages:

Safe for sharing and collaboration.

Flexible — you can design resumes/JDs to test specific ML features.

Balanced dataset size and distribution can be controlled.

# 🔧 Tech Stack
Frontend: Streamlit

Text Extraction: PyMuPDF

ML Models: scikit-learn, joblib

APIs: Google Gemini (google-genai), Groq (requests)

Data Analysis: pandas, numpy, matplotlib, seaborn

# 🚀 Usage
Run the app:
streamlit run app/app.py

Upload a resume (PDF) and paste a job description.
The app will:

Extract and clean text.

Send text to Gemini/Groq for structured parsing.

Normalize skills.

Build features and score readiness.

Display results + AI feedback report.

# 🔧 How to Use Synthetic Data in PRIS
Text Preprocessing

Extract resume text (PDF → text).

Clean JD text.

Normalize formatting.

AI Structuring

Send resume text → Gemini/Groq → structured details.

Send JD text → Gemini/Groq → structured requirements.

Skill Normalization

Map skills to ESCO or a custom dictionary.

Handle synonyms (e.g., “ML” → “Machine Learning”).

Feature Engineering

Matched skills %

Critical skills coverage %

Missing skills count

Critical missing skills count

ML Readiness Scoring

Train/test classifiers on synthetic dataset.

Predict placement readiness and salary estimation.

# 📌 Notes
Gemini/Groq APIs may experience temporary unavailability (503 errors).

The app includes retry logic and fallback between providers.

Dataset is synthetic and intended for experimentation, not production deployment.
