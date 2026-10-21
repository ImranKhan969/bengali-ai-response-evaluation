
import csv
from pathlib import Path

FILE_NAME = "bengali_ai_evaluation.csv"
REPORT_NAME = "evaluation_report.txt"

REQUIRED_COLUMNS = [
    "ID",
    "Question",
    "AI_Response",
    "Accuracy",
    "Relevance",
    "Grammar",
    "Overall_Score",
    "Comment",
]

SCORE_COLUMNS = [
    "Accuracy",
    "Relevance",
    "Grammar",
    "Overall_Score",
]


def classify_score(score):
    if score == 5:
        return "Excellent"
    elif score == 4:
        return "Good"
    elif score == 3:
        return "Fair"
    else:
        return "Poor"


def main():
    folder = Path(__file__).parent
    file_path = folder / FILE_NAME
    report_path = folder / REPORT_NAME
    issues = []

    if not file_path.exists():
        print(f"Error: {FILE_NAME} was not found.")
        return

    try:
        with file_path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: CSV file has no header.")
                return

            missing_columns = [
                col for col in REQUIRED_COLUMNS
                if col not in reader.fieldnames
            ]

            if missing_columns:
                print(
                    "Missing columns: "
                    + ", ".join(missing_columns)
                )
                return

            rows = list(reader)

    except (OSError, csv.Error) as error:
        print(f"Error reading CSV: {error}")
        return

    if not rows:
        print("No evaluation records found.")
        return

    seen_ids = set()
    valid_scores = {col: [] for col in SCORE_COLUMNS}
    categories = {
        "Excellent": 0,
        "Good": 0,
        "Fair": 0,
        "Poor": 0,
    }

    for row_number, row in enumerate(rows, start=2):
        record_id = (row.get("ID") or "").strip()

        if not record_id:
            issues.append(f"Row {row_number}: Missing ID.")
        elif record_id in seen_ids:
            issues.append(
                f"Row {row_number}: Duplicate ID {record_id}."
            )
        else:
            seen_ids.add(record_id)

        for col in ["Question", "AI_Response", "Comment"]:
            if not (row.get(col) or "").strip():
                issues.append(
                    f"Row {row_number}: {col} is empty."
                )

        for col in SCORE_COLUMNS:
            value = (row.get(col) or "").strip()

            try:
                score = int(value)

                if not 1 <= score <= 5:
                    raise ValueError

                valid_scores[col].append(score)

                if col == "Overall_Score":
                    category = classify_score(score)
                    categories[category] += 1

            except ValueError:
                issues.append(
                    f"Row {row_number}: Invalid {col} "
                    f"score: {value!r}"
                )

    lines = [
        "BENGALI AI RESPONSE EVALUATION REPORT",
        "=" * 40,
        f"Total records: {len(rows)}",
        "",
        "AVERAGE SCORES",
        "-" * 40,
    ]

    for col, scores in valid_scores.items():
        if scores:
            average = sum(scores) / len(scores)
            lines.append(
                f"{col}: {average:.2f}/5 "
                f"({len(scores)} valid scores)"
            )
        else:
            lines.append(f"{col}: No valid scores")

    lines.extend([
        "",
        "OVERALL SCORE CLASSIFICATION",
        "-" * 40,
    ])

    for category, count in categories.items():
        lines.append(f"{category}: {count}")

    lines.extend([
        "",
        "DATA VALIDATION",
        "-" * 40,
        f"Issues found: {len(issues)}",
    ])

    if issues:
        lines.extend(issues)
    else:
        lines.append("No validation issues found.")

    report = "\n".join(lines) + "\n"

    try:
        report_path.write_text(report, encoding="utf-8")
    except OSError as error:
        print(f"Error saving report: {error}")
        return

    print(report)
    print(f"Report saved to: {REPORT_NAME}")


if __name__ == "__main__":
    main()
