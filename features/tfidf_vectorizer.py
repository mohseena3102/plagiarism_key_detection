from sklearn.feature_extraction.text import TfidfVectorizer

def generate_tfidf(corpus):
    vectorizer = TfidfVectorizer(stop_words="english")
    return vectorizer.fit_transform(corpus)