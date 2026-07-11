import json

from pathlib import Path

from evaluation.judge import JudgeLLM


class ScoreRunner:
    """
    Uses the Judge LLM to score
    every baseline and full-system response.
    """

    def __init__(self):

        self.judge = JudgeLLM()

        self.input_path = (
            Path(__file__).parent
            / "outputs"
            / "evaluation_results.json"
        )

        self.output_path = (
            Path(__file__).parent
            / "outputs"
            / "evaluation_scores.json"
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

    def save_scores(

        self,

        scores

    ):

        with open(

            self.output_path,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                scores,

                file,

                indent=4,

                ensure_ascii=False

            )

    # --------------------------------------

    def run(self):

        conversations = self.load_results()

        all_scores = []

        total = len(conversations)

        print()

        print("=" * 60)

        print("Running Judge Evaluation")

        print("=" * 60)

        print()

        for index, item in enumerate(conversations, start=1):

            print(

                f"[{index}/{total}] "

                f"Scenario {item['id']}"

            )

            try:

                baseline_scores = (

                    self.judge.evaluate(

                        item["message"],

                        item["baseline_response"]

                    )

                )

                full_scores = (

                    self.judge.evaluate(

                        item["message"],

                        item["full_response"]

                    )

                )

                all_scores.append(

                    {

                        "id": item["id"],

                        "category": item["category"],

                        "expected_emotion": item["expected_emotion"],

                        "baseline": baseline_scores,

                        "full_system": full_scores

                    }

                )

                print("✓ Finished")

            except Exception as e:

                print("✗ Failed")

                print(e)

                print()

        self.save_scores(all_scores)

        print()

        print("=" * 60)

        print("Scoring Complete")

        print(f"Saved {len(all_scores)} results")

        print(self.output_path)

        print("=" * 60)