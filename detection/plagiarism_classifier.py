def classify_similarity(score):

    if score >= 0.75:
        return "High Plagiarism"

    elif score >= 0.45:
        return "Moderate Plagiarism"

    else:
        return "Low / No Plagiarism"