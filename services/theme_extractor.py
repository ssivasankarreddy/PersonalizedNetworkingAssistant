from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CANDIDATE_LABELS = [
    "Artificial Intelligence",
    "Machine Learning",
    "Climate Change",
    "Smart Cities",
    "Blockchain",
    "Cybersecurity",
    "Cloud Computing",
    "Healthcare",
    "Finance",
    "Education",
    "Data Science",
    "Urban Planning",
    "Sustainability"
]


def extract_themes(text):
    result = classifier(
        text,
        candidate_labels=CANDIDATE_LABELS,
        multi_label=True
    )

    themes = []

    for label, score in zip(result["labels"], result["scores"]):
        if score > 0.40:
            themes.append(label)

    return themes