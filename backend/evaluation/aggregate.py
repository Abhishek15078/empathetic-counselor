import json
from pathlib import Path


class ResultAggregator:

    def __init__(self):

        self.input_path = (
            Path(__file__).parent
            / "outputs"
            / "evaluation_scores.json"
        )

        self.output_path = (
            Path(__file__).parent
            / "outputs"
            / "evaluation_summary.json"
        )

    # --------------------------------------

    def load_results(self):

        with open(
            self.input_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # --------------------------------------

    def average(self, values):

        if not values:
            return 0

        return round(sum(values) / len(values), 2)

    # --------------------------------------

    def aggregate(self):

        data = self.load_results()

        baseline = {
            "empathy": [],
            "helpfulness": [],
            "safety": [],
            "naturalness": []
        }

        full = {
            "empathy": [],
            "helpfulness": [],
            "safety": [],
            "naturalness": []
        }

        for row in data:

            baseline["empathy"].append(
                row["baseline"]["empathy"]
            )

            baseline["helpfulness"].append(
                row["baseline"]["helpfulness"]
            )

            baseline["safety"].append(
                row["baseline"]["safety"]
            )

            baseline["naturalness"].append(
                row["baseline"]["naturalness"]
            )

            full["empathy"].append(
                row["full_system"]["empathy"]
            )

            full["helpfulness"].append(
                row["full_system"]["helpfulness"]
            )

            full["safety"].append(
                row["full_system"]["safety"]
            )

            full["naturalness"].append(
                row["full_system"]["naturalness"]
            )

        summary = {}

        metrics = [
            "empathy",
            "helpfulness",
            "safety",
            "naturalness"
        ]

        for metric in metrics:

            baseline_avg = self.average(
                baseline[metric]
            )

            full_avg = self.average(
                full[metric]
            )

            summary[metric] = {

                "baseline": baseline_avg,

                "full_system": full_avg,

                "improvement": round(
                    full_avg - baseline_avg,
                    2
                )

            }

        with open(

            self.output_path,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                summary,

                file,

                indent=4

            )

        return summary