import json
import random
from pathlib import Path

# ==========================================================
# Configuration
# ==========================================================

TOTAL_SAMPLES = 120

EMOTIONS = [
    "anger",
    "disgust",
    "fear",
    "joy",
    "love",
    "neutral",
    "sadness",
    "surprise"
]

CATEGORIES = [
    "academic",
    "career",
    "family",
    "relationships",
    "health",
    "finance",
    "daily_life",
    "social"
]

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).parent

TEMPLATE_DIR = BASE_DIR / "templates"

OUTPUT_FILE = (
    BASE_DIR
    / "datasets"
    / "stress_scenarios.json"
)

OUTPUT_FILE.parent.mkdir(exist_ok=True)

# ==========================================================
# Load Templates
# ==========================================================

templates = {}

for emotion in EMOTIONS:

    file_path = TEMPLATE_DIR / f"{emotion}.json"

    with open(file_path, "r", encoding="utf-8") as f:

        templates[emotion] = json.load(f)

# ==========================================================
# Determine balanced counts
# ==========================================================

base = TOTAL_SAMPLES // len(EMOTIONS)

remaining = TOTAL_SAMPLES % len(EMOTIONS)

emotion_counts = {}

for i, emotion in enumerate(EMOTIONS):

    emotion_counts[emotion] = base

    if i < remaining:
        emotion_counts[emotion] += 1

print("\nSamples per emotion\n")

for k, v in emotion_counts.items():
    print(f"{k:10s} : {v}")

# ==========================================================
# Generate Dataset
# ==========================================================

dataset = []

for emotion in EMOTIONS:

    messages = templates[emotion]

    required = emotion_counts[emotion]

    generated = []

    while len(generated) < required:

        generated.append(random.choice(messages))

    for msg in generated:

        dataset.append(

            {
                "category": random.choice(CATEGORIES),
                "message": msg,
                "expected_emotion": emotion
            }

        )

# ==========================================================
# Shuffle
# ==========================================================

random.shuffle(dataset)

# ==========================================================
# Assign IDs
# ==========================================================

for idx, item in enumerate(dataset, start=1):

    item["id"] = idx

# ==========================================================
# Save
# ==========================================================

with open(

    OUTPUT_FILE,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        dataset,

        f,

        indent=4,

        ensure_ascii=False

    )

print("\n==========================================")
print("Dataset Generation Completed")
print("==========================================")

print(f"Total Samples : {len(dataset)}")

print(f"Saved To      : {OUTPUT_FILE}")

print("==========================================")