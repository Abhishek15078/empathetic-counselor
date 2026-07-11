import json
from pathlib import Path

# ==========================================================
# Categories
# ==========================================================

ACADEMIC = [
    ("I'm terrified I'm going to fail my final exams even though I've been studying every day.", "fear"),
    ("I can't concentrate on my assignments anymore.", "sadness"),
    ("Everyone in my class seems smarter than me.", "sadness"),
    ("I panic every time I think about tomorrow's exam.", "fear"),
    ("My grades keep dropping no matter how hard I study.", "sadness"),
    ("I'm overwhelmed with assignments and deadlines.", "fear"),
    ("I feel like disappointing my parents.", "fear"),
    ("I failed another test today.", "sadness"),
    ("I don't think I'm smart enough for engineering.", "sadness"),
    ("Every exam makes me feel sick with anxiety.", "fear"),
    ("I'm afraid I chose the wrong career path.", "fear"),
    ("I study all day but remember nothing.", "sadness"),
    ("My classmates always outperform me.", "sadness"),
    ("I'm exhausted trying to balance college and life.", "neutral"),
    ("I don't know how I'll finish this semester.", "fear"),
]

WORKPLACE = [
    ("My boss constantly criticizes my work.", "sadness"),
    ("I'm afraid I'll lose my job.", "fear"),
    ("My workload keeps increasing every week.", "anger"),
    ("Nobody appreciates the effort I put in.", "sadness"),
    ("I dread going to work every morning.", "fear"),
    ("I'm struggling with burnout.", "sadness"),
    ("I feel stuck in my current role.", "neutral"),
    ("My coworkers ignore my ideas.", "anger"),
    ("I can't keep up with deadlines anymore.", "fear"),
    ("Work stress is affecting my sleep.", "fear"),
]

SOCIAL = [
    ("I'm scared people are judging me.", "fear"),
    ("I avoid social gatherings because I get anxious.", "fear"),
    ("I never know what to say to people.", "sadness"),
    ("I think everyone secretly dislikes me.", "fear"),
    ("Talking to strangers makes me panic.", "fear"),
    ("I feel lonely even around friends.", "sadness"),
    ("I overthink every conversation.", "fear"),
    ("I hate speaking in public.", "fear"),
    ("I'm afraid of embarrassing myself.", "fear"),
    ("I always compare myself to others.", "sadness"),
]

RELATIONSHIP = [
    ("My partner doesn't seem to understand me anymore.", "sadness"),
    ("We argue almost every day.", "anger"),
    ("I'm scared my relationship is ending.", "fear"),
    ("I feel ignored by someone I love.", "sadness"),
    ("My best friend stopped talking to me.", "sadness"),
    ("I don't know if I should end my relationship.", "neutral"),
    ("I feel guilty after hurting someone close to me.", "sadness"),
    ("I miss someone who left my life.", "sadness"),
]

OVERWHELM = [
    ("Everything feels like too much lately.", "sadness"),
    ("I don't know where to start anymore.", "neutral"),
    ("I'm mentally exhausted.", "sadness"),
    ("Every day feels harder than the last.", "sadness"),
    ("I'm constantly worrying about everything.", "fear"),
    ("I feel trapped by my responsibilities.", "sadness"),
    ("Nothing seems to be going right.", "sadness"),
]

# ==========================================================
# Build Dataset
# ==========================================================

dataset = []

current_id = 1

for category_name, category_data in [
    ("academic", ACADEMIC),
    ("workplace", WORKPLACE),
    ("social", SOCIAL),
    ("relationship", RELATIONSHIP),
    ("overwhelm", OVERWHELM),
]:

    for message, emotion in category_data:

        dataset.append({

            "id": current_id,

            "category": category_name,

            "message": message,

            "expected_emotion": emotion

        })

        current_id += 1

# ==========================================================
# Save JSON
# ==========================================================

output_path = (
    Path(__file__)
    .parent
    / "datasets"
    / "stress_scenarios.json"
)

with open(output_path, "w", encoding="utf-8") as file:

    json.dump(

        dataset,

        file,

        indent=4,

        ensure_ascii=False

    )

print("=" * 50)
print("Dataset Generated Successfully")
print("=" * 50)
print(f"Saved {len(dataset)} scenarios")
print(output_path)