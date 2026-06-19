import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# STEP 1: INGESTION (Dataset)
# ---------------------------
# raw_skills.csv - job roles mapped to required skills
data = {
    "Job Role": [
        "Data Scientist", "DevOps Engineer", "Backend Developer",
        "Frontend Developer", "Cloud Architect", "ML Engineer",
        "System Admin", "Full Stack Developer", "Data Analyst",
        "Security Engineer"
    ],
    "Skills": [
        "Python SQL Machine Learning Data Analysis Statistics",
        "AWS Docker Kubernetes CI/CD Automation Linux",
        "Java Python SQL APIs Databases Backend",
        "JavaScript HTML CSS React Frontend UI",
        "AWS Cloud Computing Azure Kubernetes Networking",
        "Python Machine Learning TensorFlow Data Structures Algorithms",
        "Linux Networking Automation Cloud Security",
        "JavaScript Python SQL React APIs Backend Frontend",
        "SQL Excel Python Data Analysis Statistics Visualization",
        "Networking Security Cloud Linux Automation Encryption"
    ]
}

df = pd.DataFrame(data)
print("=== Job Role Dataset ===")
print(df)
print()

# Save as CSV (so you have an actual raw_skills.csv file)
df.to_csv('raw_skills.csv', index=False)


# ---------------------------
# STEP 2: USER INPUT
# ---------------------------
def get_user_skills():
    print("=== Tech Stack Recommender ===")
    print("Enter at least 3 skills (comma-separated)")
    print("Example: Python, Cloud, Automation\n")
    
    user_input = input("Your skills: ")
    user_skills = [skill.strip() for skill in user_input.split(",")]
    
    if len(user_skills) < 3:
        print("Please enter at least 3 skills!")
        return get_user_skills()
    
    return " ".join(user_skills)  # join into one string for vectorizing


# ---------------------------
# STEP 3: PROCESS (TF-IDF + Vector Mapping)
# ---------------------------
def build_tfidf_matrix(df, user_skills_text):
    # Combine job skills + user input into one corpus
    # so they share the SAME vocabulary space
    corpus = df["Skills"].tolist() + [user_skills_text]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    return tfidf_matrix, vectorizer


# ---------------------------
# STEP 4: SCORING (Cosine Similarity)
# ---------------------------
def calculate_similarity(tfidf_matrix):
    # Last row = user vector, all rows before = job role vectors
    user_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]
    
    similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()
    return similarity_scores


# ---------------------------
# STEP 5: SORTING & FILTERING (Top-N Output)
# ---------------------------
def recommend_top_n(df, similarity_scores, n=3):
    df = df.copy()
    df["Similarity Score"] = similarity_scores
    
    # Sort descending by score
    ranked = df.sort_values(by="Similarity Score", ascending=False)
    
    # Filter top N
    top_n = ranked.head(n)
    return top_n


# ---------------------------
# MAIN PIPELINE
# ---------------------------
def main():
    user_skills_text = get_user_skills()
    
    tfidf_matrix, vectorizer = build_tfidf_matrix(df, user_skills_text)
    similarity_scores = calculate_similarity(tfidf_matrix)
    top_matches = recommend_top_n(df, similarity_scores, n=3)
    
    print("\n=== Top 3 Recommended Career Paths ===\n")
    for rank, (_, row) in enumerate(top_matches.iterrows(), start=1):
        match_percent = round(row["Similarity Score"] * 100, 2)
        print(f"Rank {rank}: {row['Job Role']}")
        print(f"  Required Skills: {row['Skills']}")
        print(f"  Match Score: {match_percent}%\n")


if __name__ == "__main__":
    main()
