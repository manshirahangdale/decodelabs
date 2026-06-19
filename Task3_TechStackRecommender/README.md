# Task 3: AI Tech Stack Recommender 🎯

## Goal
Build a content-based recommendation system that maps a user's skills to the most compatible tech job roles using TF-IDF vectorization and Cosine Similarity.

## Description
This project implements a "Digital Matchmaker" that takes a user's skill set as input, converts both user skills and job role requirements into TF-IDF weighted vectors, and ranks job roles by cosine similarity to recommend the Top 3 most relevant career paths.

## Dataset
`raw_skills.csv` — contains 10 job roles (Data Scientist, DevOps Engineer, Backend Developer, etc.) each mapped to a set of required skills.

## Pipeline (IPO Architecture)
1. **Ingestion** — Captures minimum 3 user skills as input
2. **Vector Mapping** — Converts user skills + job skills into TF-IDF weighted numerical vectors within a shared vocabulary space
3. **Scoring** — Calculates Cosine Similarity between user vector and each job role vector
4. **Sorting** — Ranks job roles in descending order of similarity score
5. **Filtering** — Returns Top 3 highest-scoring career paths

## Key Concepts Used
- **TF-IDF (Term Frequency-Inverse Document Frequency)** — weights specific/rare skills higher than generic/common ones
- **Cosine Similarity** — measures the angle between vectors rather than raw magnitude, making it ideal for comparing skill sets of different lengths
- **Content-Based Filtering** — recommends based on item attributes (skills) rather than user community behavior, avoiding the Cold Start problem

## Key Skills Used
- Logic building & pattern matching
- Feature extraction (TF-IDF)
- Similarity-based recommendation logic
- Data handling (pandas)

## Sample Interaction
