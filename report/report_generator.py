import pandas as pd

def generate_report(doc_names, similarity_matrix, classifier):

    results = []

    for i in range(len(doc_names)):
        for j in range(i+1, len(doc_names)):

            score = similarity_matrix[i][j]

            results.append({
                "Document 1": doc_names[i],
                "Document 2": doc_names[j],
                "Similarity %": round(score*100,2),
                "Plagiarism Level": classifier(score)
            })

    return pd.DataFrame(results)