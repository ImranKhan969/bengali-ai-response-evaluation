
import csv
from pathlib import Path

FILE_NAME = "bengali_ai_evaluation.csv"
SCORE_COLUMNS = [
    "Accuracy",
    "Relevance",
    "Grammar",
    "Overall_Score",
]


def main():
    file_path = Path(__file__).parent / FILE_NAME

    if not file_path.exists():
        print(f"Error: {FILE_NAME} was not found.")
        return

    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No evaluation records found.")
        return

    print("BENGALI AI RESPONSE EVALUATION")
    print("-" * 35)
    print(f"Total records: {len(rows)}")

    for column in SCORE_COLUMNS:
        scores = []

        for row in rows:
            try:
                score = int(row[column])
                if 1 <= score <= 5:
                    scores.append(score)
                else:
                    print(f"Warning: Invalid score in {column}: {score}")
            except (ValueError, KeyError, TypeError):
                print(f"Warning: Missing or invalid value in {column}")

        if scores:
            average = sum(scores) / len(scores)
            print(f"Average {column}: {average:.2f}/5")

    print("-" * 35)
    print("Analysis completed.")


if __name__ == "__main__":
    main()
