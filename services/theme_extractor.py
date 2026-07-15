import re

THEME_KEYWORDS = {
    "Artificial Intelligence": [
        "ai", "artificial intelligence", "machine learning",
        "deep learning", "neural network", "llm"
    ],
    "Data Science": [
        "data", "analytics", "statistics", "visualization"
    ],
    "Cybersecurity": [
        "cyber", "security", "hacking", "malware", "encryption"
    ],
    "Cloud Computing": [
        "cloud", "aws", "azure", "gcp", "docker", "kubernetes"
    ],
    "Web Development": [
        "web", "frontend", "backend", "html",
        "css", "javascript", "react", "node"
    ],
    "Software Engineering": [
        "software", "developer", "programming",
        "coding", "java", "python", "c++"
    ],
    "Networking": [
        "network", "communication", "telecom"
    ],
    "IoT": [
        "iot", "internet of things", "sensor", "arduino"
    ],
    "Blockchain": [
        "blockchain", "crypto", "bitcoin", "ethereum"
    ],
    "Sustainability": [
        "green", "climate", "sustainable",
        "environment", "renewable"
    ],
}


def extract_themes(text):

    text = text.lower()

    themes = []

    for theme, keywords in THEME_KEYWORDS.items():

        for keyword in keywords:

            if re.search(r"\b" + re.escape(keyword) + r"\b", text):
                themes.append(theme)
                break

    if not themes:
        themes.append("General Technology")

    return themes
