# 🔍 Plagiarism Key Detection System

A web-based **Plagiarism Detection System** built using **Python, Flask, and Machine Learning (TF-IDF + Cosine Similarity)**.  
This application allows users to upload multiple documents and detects similarity between them to identify plagiarism.

## 🚀 Live Demo
👉 https://plagiarism-key-detection-7.onrender.com/

## 🛠️ Technologies Used
- Python 3
- Flask (Web Framework)
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- HTML / Jinja Templates

## ✨ Features
- Upload up to **4 documents** at a time
- Text preprocessing and cleaning
- TF-IDF based feature extraction
- Cosine similarity calculation
- Plagiarism classification
- Tabular plagiarism report output
- Simple and user-friendly interface

## 📂 Project Structure
plagiarism_key_detection/
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── detection/
│ ├── init.py
│ └── plagiarism_classifier.py
├── report/
│ ├── init.py
│ └── report_generator.py
├── templates/
│ └── index.html

## ⚙️ How It Works
1. User uploads multiple text documents
2. Text is preprocessed (lowercasing, newline removal)
3. TF-IDF vectors are generated
4. Cosine similarity is calculated between documents
5. Similarity scores are classified
6. A plagiarism report is generated and displayed

# ▶️ How to Run Locally
bash>>
pip install -r requirements.txt
python app.py

Then open:
http://127.0.0.1:10000

📦 Requirements
flask
scikit-learn
pandas
numpy
(All listed in requirements.txt)

👩‍💻 Author
Padmarupa (padmarupa31)
College Mini Project – Plagiarism Detection System
