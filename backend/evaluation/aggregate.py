import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

INPUT = (
    BASE_DIR
    / "outputs"
    / "evaluation_scores.json"
)

OUTPUT = (
    BASE_DIR
    / "outputs"
    / "evaluation_summary.json"
)


with open(INPUT, "r", encoding="utf-8") as f:
    scores = json.load(f)


metrics = [
    "empathy",
    "helpfulness",
    "safety",
    "naturalness"
]


summary = {

    "baseline": {},

    "full_system": {}

}


for system in ["baseline", "full_system"]:

    for metric in metrics:

        avg = sum(
            item[system][metric]
            for item in scores
        ) / len(scores)

        summary[system][metric] = round(avg, 3)


summary["overall"] = {

    "baseline":

        round(

            sum(summary["baseline"].values()) / 4,

            3

        ),

    "full_system":

        round(

            sum(summary["full_system"].values()) / 4,

            3

        )

}


with open(OUTPUT, "w", encoding="utf-8") as f:

    json.dump(
        summary,
        f,
        indent=4
    )


print("Summary generated.")