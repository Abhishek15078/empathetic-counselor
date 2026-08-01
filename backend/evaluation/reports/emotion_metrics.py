import json
from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# ==========================================================
# Paths
# ==========================================================

RESULTS_FILE = (
    Path(__file__).resolve().parents[1]
    / "outputs"
    / "evaluation_results.json"
)

OUTPUT_DIR = (
    Path(__file__).resolve().parents[1]
    / "outputs"
)

# ==========================================================
# Load Evaluation Results
# ==========================================================

if not RESULTS_FILE.exists():
    raise FileNotFoundError(
        f"Evaluation results not found:\n{RESULTS_FILE}"
    )

with open(RESULTS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

if not data:
    raise ValueError("evaluation_results.json is empty.")

# ==========================================================
# Extract Labels
# ==========================================================

true_labels = []
predicted_labels = []

for item in data:
    true_labels.append(item["expected_emotion"])
    predicted_labels.append(item["predicted_emotion"])

# Keep label order consistent
labels = sorted(set(true_labels) | set(predicted_labels))

# ==========================================================
# Compute Metrics
# ==========================================================

accuracy = accuracy_score(
    true_labels,
    predicted_labels,
)

precision = precision_score(
    true_labels,
    predicted_labels,
    average="weighted",
    zero_division=0,
)

recall = recall_score(
    true_labels,
    predicted_labels,
    average="weighted",
    zero_division=0,
)

f1 = f1_score(
    true_labels,
    predicted_labels,
    average="weighted",
    zero_division=0,
)

# ==========================================================
# Confusion Matrix
# ==========================================================

cm = confusion_matrix(
    true_labels,
    predicted_labels,
    labels=labels,
)

cm_df = pd.DataFrame(
    cm,
    index=labels,
    columns=labels,
)

cm_df.to_csv(
    OUTPUT_DIR / "confusion_matrix.csv",
    index=True,
)

# ==========================================================
# Classification Report
# ==========================================================

report = classification_report(
    true_labels,
    predicted_labels,
    labels=labels,
    target_names=labels,
    digits=4,
    zero_division=0,
)

with open(
    OUTPUT_DIR / "classification_report.txt",
    "w",
    encoding="utf-8",
) as f:
    f.write(report)

# ==========================================================
# Summary Metrics
# ==========================================================

summary = {
    "Total Samples": len(data),
    "Accuracy": round(float(accuracy), 4),
    "Precision": round(float(precision), 4),
    "Recall": round(float(recall), 4),
    "F1 Score": round(float(f1), 4),
    "Emotion Labels": labels,
}

with open(
    OUTPUT_DIR / "emotion_metrics.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(
        summary,
        f,
        indent=4,
    )

# ==========================================================
# Console Output
# ==========================================================

print("\n" + "=" * 50)
print("Emotion Classification Evaluation")
print("=" * 50)

print(f"Total Samples : {len(data)}")
print(f"Accuracy      : {accuracy:.4f}")
print(f"Precision     : {precision:.4f}")
print(f"Recall        : {recall:.4f}")
print(f"F1 Score      : {f1:.4f}")

print("\nGenerated Files:")
print(f"✓ {OUTPUT_DIR / 'emotion_metrics.json'}")
print(f"✓ {OUTPUT_DIR / 'classification_report.txt'}")
print(f"✓ {OUTPUT_DIR / 'confusion_matrix.csv'}")

print("\nEvaluation completed successfully.")