# Assignment 10 — Final Project I: Pipeline and Analysis

This is Phase 1 of the final project. Make sure you've read the [Final Project Overview](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md) for the two-week arc, the dataset options, and both rubrics. This week is graded against the **Phase 1 rubric**.

## Requirements

Work in a Kaggle notebook, using the dataset from your Week 5 proposal.

### Data Preparation

- Load your dataset with **Add Input** and take a first look (`shape`, `head`, `info`, `describe`, `value_counts`).
- Clean the data using the Week 3 tools: handle missing values, fix data types, standardize text, and remove duplicates as your data requires.
- **Document each cleaning decision in a markdown cell**, explaining what you did and why.
- Save the cleaned data to a file (for example, `cleaned_data.csv`) to commit to your project repository.

### Analysis

- Use at least **two aggregations or derived features** (`groupby`, `agg`, `apply`, `pd.cut`, etc.) that directly serve your question.
- Incorporate the analytical queries from your **Week 8 milestone**.

### Visualization and Insights

- Create at least **three appropriate, fully labeled charts** (title, axis labels, legend where needed), one per finding.
- After each chart, add a markdown cell interpreting what it shows.
- Reach at least **three findings**, each supported by a chart and by text.

### Write-Up

- Write a `summary.md` (about one page) covering the **question**, the **data**, the **findings** (three or more, each pointing to its chart), and the **limitations**.
- Write it in plain language you could read aloud — it becomes your Week 11 presentation script.

## Submission

This week has **two submissions**:

1. **Kaggle notebook.** Save Version, then **Share → Public** with **Allow Comments** on, and copy the public URL.
2. **Pull request.** Commit `summary.md` and your cleaned data file to your project repository, and open a pull request.

Paste both links into the two fields on the **assignment submission form**.

## Rubric

This week is graded against the **Phase 1 rubric** in the [Final Project Overview](../resources/final-project-overview.md#phase-1-rubric--week-10-pipeline-and-analysis). Review it before submitting — it covers Data Preparation, Analysis and Aggregation, Visualization, Insights and Interpretation, and Communication and Reproducibility.
