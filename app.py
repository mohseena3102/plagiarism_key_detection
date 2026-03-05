from flask import Flask, render_template, request
from detection.plagiarism_classifier import classify_similarity
from report.report_generator import generate_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def preprocess_text(text):
    return text.lower().replace("\n", " ")

def generate_tfidf(docs):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(docs)

def compute_similarity(tfidf_matrix):
    return cosine_similarity(tfidf_matrix)

@app.route("/", methods=["GET", "POST"])
def index():
    report_html = None
    if request.method == "POST":
        documents = {}

        for i in range(1, 5):
            file = request.files.get(f"doc{i}")
            if file and file.filename != "":
                documents[f"Doc{i}"] = file.read().decode("utf-8", errors="ignore")

        if len(documents) >= 2:
            doc_names = list(documents.keys())
            processed_docs = [preprocess_text(t) for t in documents.values()]
            tfidf_matrix = generate_tfidf(processed_docs)
            similarity_matrix = compute_similarity(tfidf_matrix)
            report = generate_report(doc_names, similarity_matrix, classify_similarity)
            report_html = report.to_html(index=False)

    return render_template("index.html", report=report_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)