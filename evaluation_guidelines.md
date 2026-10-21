# Bengali AI Response Evaluation Guidelines

## 1. Purpose

This project evaluates the quality of AI-generated responses to Bengali questions. The goal is to assess factual accuracy, relevance, grammar, and overall response quality using consistent and evidence-based criteria.

## 2. Evaluation Criteria

### 2.1 Accuracy
Evaluate whether the response provides factually correct information.

- **5:** Completely accurate.
- **4:** Mostly accurate, with a minor error.
- **3:** Partially accurate, with some important information missing or incorrect.
- **2:** Mostly inaccurate.
- **1:** Fundamentally incorrect or misleading.

### 2.2 Relevance
Evaluate whether the response directly answers the question.

- **5:** Directly and fully addresses the question.
- **4:** Relevant, with minor unnecessary content.
- **3:** Partially addresses the question.
- **2:** Mostly off-topic or insufficiently responsive.
- **1:** Does not meaningfully address the question.

### 2.3 Grammar
Evaluate the grammatical correctness, spelling, and readability of the Bengali response.

- **5:** Grammatically correct and natural.
- **4:** Minor language errors that do not affect understanding.
- **3:** Noticeable errors, but the meaning remains understandable.
- **2:** Frequent errors that make understanding difficult.
- **1:** Severe language errors that make the response difficult to understand.

## 3. Overall Score

Assign an overall score from 1 to 5 based on the response's combined quality.

- **5 — Excellent:** Accurate, relevant, and grammatically sound.
- **4 — Good:** Strong response with minor weaknesses.
- **3 — Fair:** Partially satisfactory, with noticeable issues.
- **2 — Poor:** Significant factual, relevance, or language problems.
- **1 — Very Poor:** Fundamentally incorrect, misleading, or unhelpful.

The overall score should reflect the severity of errors, not just a simple average. A serious factual error may justify a low overall score even when grammar is good.

## 4. Evaluation Process

1. Read the question carefully.
2. Review the complete AI-generated response.
3. Check factual claims against reliable knowledge or appropriate reference sources.
4. Score Accuracy, Relevance, and Grammar independently.
5. Assign an Overall Score based on the response's combined quality.
6. Write a short comment explaining the main reason for the evaluation.

## 5. Consistency and Objectivity

- Apply the same criteria to all responses.
- Do not reward fluent writing when the information is incorrect.
- Do not penalize a response's grammar merely because its factual content is wrong.
- Use comments to identify significant errors or strengths.
- Avoid personal preferences and unsupported assumptions.
- Record uncertainty when a claim cannot be verified.

## 6. Scope and Limitations

This is a small, manually annotated sample dataset intended for learning and portfolio development. Its scores represent the evaluator's judgments and should not be treated as a validated benchmark of AI performance.

## 7. Dataset Fields

- `ID`: Unique example identifier.
- `Question`: The Bengali question.
- `AI_Response`: The response being evaluated.
- `Accuracy`: Factual correctness score (1–5).
- `Relevance`: Question relevance score (1–5).
- `Grammar`: Language quality score (1–5).
- `Overall_Score`: Overall response quality score (1–5).
- `Comment`: Brief explanation supporting the evaluation.
