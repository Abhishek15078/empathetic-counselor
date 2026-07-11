import json
from pathlib import Path

from app.database import SessionLocal
from app.repositories.session_repository import SessionRepository
from app.services.orchestrator import AIOrchestrator

from evaluation.baseline import BaselineSystem


class EvaluationRunner:
    """
    Runs both the Full System and the Baseline
    over the evaluation dataset.
    """

    def __init__(self):

        self.baseline = BaselineSystem()

        self.orchestrator = AIOrchestrator()

        self.session_repo = SessionRepository()

        self.dataset_path = (
            Path(__file__).parent
            / "datasets"
            / "stress_scenarios.json"
        )

        self.output_path = (
            Path(__file__).parent
            / "outputs"
            / "evaluation_results.json"
        )

    # -------------------------------------------------
    # Load Dataset
    # -------------------------------------------------

    def load_dataset(self):

        with open(
            self.dataset_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # -------------------------------------------------
    # Save Results
    # -------------------------------------------------

    def save_results(
        self,
        results
    ):

        with open(
            self.output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                results,
                file,
                indent=4,
                ensure_ascii=False
            )

    # -------------------------------------------------
    # Run Evaluation
    # -------------------------------------------------

    def run(self):

        dataset = self.load_dataset()

        results = []

        total = len(dataset)

        print("\nStarting Evaluation...\n")

        for index, scenario in enumerate(dataset, start=1):

            print(
                f"[{index}/{total}] Running Scenario {scenario['id']}..."
            )

            try:

                # ---------------------------------
                # Baseline Response
                # ---------------------------------

                baseline_response = (
                    self.baseline.generate_response(
                        scenario["message"]
                    )
                )

                # ---------------------------------
                # Full System Response
                # ---------------------------------

                db = SessionLocal()

                try:

                    session = self.session_repo.create_session(db)

                    pipeline_result = (
                        self.orchestrator.process_message(
                            session.id,
                            scenario["message"]
                        )
                    )

                    full_response = (
                        pipeline_result.response_text
                    )

                finally:

                    db.close()

                # ---------------------------------
                # Store Result
                # ---------------------------------

                results.append(

                    {
                        "id": scenario["id"],
                        "category": scenario["category"],
                        "message": scenario["message"],
                        "expected_emotion": scenario["expected_emotion"],
                        "baseline_response": baseline_response,
                        "full_response": full_response
                    }

                )

                print("✓ Completed\n")

            except Exception as e:

                print(
                    f"✗ Failed Scenario {scenario['id']}"
                )

                print(e)

                print()

        # ---------------------------------
        # Save Output
        # ---------------------------------

        self.save_results(results)

        print("=" * 60)

        print("Evaluation Finished")

        print(f"Completed: {len(results)} / {total}")

        print(f"Saved to: {self.output_path}")

        print("=" * 60)