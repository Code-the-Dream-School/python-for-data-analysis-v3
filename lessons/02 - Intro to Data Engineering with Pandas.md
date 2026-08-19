# Lesson 2 — Intro to Data Engineering with Pandas

**Lesson Overview**

Last week you sharpened your core Python and learned to pull fields out of messy text, ending with data that looked like a table. This week you meet the tool that makes that table a first-class object: **Pandas**, the library at the center of nearly all data work in Python. You'll create its two core structures, load real data from files and the web, size up an unfamiliar dataset with a repeatable routine, and slice out exactly the rows and columns you need. By the end you'll be able to take a raw file and turn it into a clean, well-understood subset ready for analysis — and you'll spot the missing values that Week 3 teaches you to fix.

All of this week's work happens in **Kaggle notebooks**, where Pandas comes pre-installed. Your assignment is submitted as a Kaggle notebook.

**Learning Objectives**

This week, I can...

* Explain what Pandas is, and create Series and DataFrames from Python lists, dictionaries, and NumPy arrays.
* Load data into a DataFrame from CSV files, JSON files, dictionaries, and a web API, and save results back to CSV.
* Inspect an unfamiliar dataset with a repeatable first-look routine (`shape`, `head`, `info`, `describe`, `value_counts`).
* Select and filter the exact rows, columns, and cells I need, and count missing values with `isna().sum()`.

## Topics

1. **[Series and DataFrames](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/02%20-%20Intro%20to%20Data%20Engineering%20with%20Pandas/01_series_data_frames.md)**

   The two structures Pandas is built on, how a Series index differs from a list's positions, and why a DataFrame beats a list of dictionaries for real work.

2. **[Loading and Saving Data](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/02%20-%20Intro%20to%20Data%20Engineering%20with%20Pandas/02_loading_saving_data.md)**

   Reading data from CSV files, JSON files, dictionaries, and web APIs, plus saving your results back out with `to_csv`.

3. **[Inspecting a Dataset](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/02%20-%20Intro%20to%20Data%20Engineering%20with%20Pandas/03_inspecting_datasets.md)**

   A dependable "first look" routine — `shape`, `head`, `info`, `describe`, and `value_counts` — for getting to know any new dataset before you analyze it.

4. **[Selecting and Filtering](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/02%20-%20Intro%20to%20Data%20Engineering%20with%20Pandas/04_selecting_filtering.md)**

   Pulling out columns, rows, and cells with `.loc` and `.iloc`, filtering with boolean conditions, and counting the missing values that lead into Week 3.

## Summary

This week moved you from *having* data to *working with* it. You now know the two structures every Pandas operation returns — the one-dimensional **Series** and the two-dimensional **DataFrame** — and that their **index** is a label, not a row number. You can pull data in from the four sources you'll actually meet (CSV, JSON, dictionaries, and APIs) and write results back out. You have a repeatable routine for inspecting a dataset so you never analyze something you don't understand. And you can select and filter down to the precise slice a question needs, using `.loc` and `.iloc` correctly and combining conditions with `&` and `|` instead of `and`/`or`.

That last step — running `isna().sum()` and seeing where the gaps are — is the natural handoff into **Week 3: Data Cleaning and Validation**, where you'll decide what to do about the missing and malformed values this week taught you to find.
