# Bengali AI Response Evaluation

## Project Overview

This project evaluates AI-generated responses to Bengali questions using a structured scoring system. It focuses on factual accuracy, relevance, grammar, and overall response quality.

The project demonstrates basic skills in AI response evaluation, data annotation, CSV data handling, Python programming, and data validation.

## Project Objectives

- Evaluate the quality of AI-generated Bengali responses.
- Apply consistent scoring criteria.
- Organize evaluation data in CSV format.
- Calculate average evaluation scores using Python.
- Validate data and generate an automated evaluation report.

## Repository Contents

| File | Description |
|---|---|
| `bengali_ai_evaluation.csv` | Sample Bengali questions, AI responses, scores, and comments |
| `evaluation_guidelines.md` | Guidelines for consistent response evaluation |
| `Evaluation Criteria.md` | Additional evaluation criteria |
| `analyze_evaluation.py` | Python script for score analysis and data validation |
| `evaluation_report.txt` | Generated evaluation report, when available |

## Evaluation Criteria

Each response is scored on a scale of 1 to 5 for:

- **Accuracy:** Factual correctness.
- **Relevance:** How directly the response answers the question.
- **Grammar:** Language correctness and readability.
- **Overall Score:** Overall response quality.

## Tools and Technologies

- Python 3
- CSV
- GitHub
- Markdown

## How to Run

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Keep the CSV file in the same folder as the Python script.
4. Run the following command:

```bash
python analyze_evaluation.py
```

The script calculates average scores and checks for common data quality issues. It also generates an evaluation report.

## Sample Results

The initial dataset contains 5 records.

| Metric | Average Score |
|---|---:|
| Accuracy | 4.20/5 |
| Relevance | 4.20/5 |
| Grammar | 4.80/5 |
| Overall Score | 4.20/5 |

These results are based on a small sample and are intended for learning and demonstration, not as a benchmark of AI model performance.

## Limitations and Future Improvements

- Expand the dataset with more diverse Bengali questions.
- Add more examples of partially correct and misleading responses.
- Improve validation and reporting.
- Review scoring consistency with independent evaluators.

## Author

Created as a portfolio project to develop practical skills in Bengali AI response evaluation and data analysis.
