from evaluation.aggregate import ResultAggregator

aggregator = ResultAggregator()

summary = aggregator.aggregate()

print()

print("=" * 60)

print("Evaluation Summary")

print("=" * 60)

for metric, values in summary.items():

    print()

    print(metric.upper())

    print(

        f"Baseline : {values['baseline']}"

    )

    print(

        f"Full     : {values['full_system']}"

    )

    print(

        f"Improved : {values['improvement']}"

    )