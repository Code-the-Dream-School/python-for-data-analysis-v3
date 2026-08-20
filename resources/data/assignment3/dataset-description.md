# Code the Dream Assignment 3

Teaching dataset for the Week 3 (Data Cleaning and Validation) assignment of Code the Dream's **Python for Data Analysis** course. The data is intentionally messy — it exists so students can practice cleaning it. Upload both files as a single CTD-owned Kaggle dataset titled **"Code the Dream Assignment 3"**.

## Files

### `employees.csv`
A small employee table with missing values in every column.

| Column | Type | Notes |
|---|---|---|
| `Name` | text | some values missing |
| `Age` | integer | some values missing |
| `Salary` | integer | some values missing |
| `Join Date` | text (date) | some values missing |
| `City` | text | some values missing (these rows are dropped in the assignment) |

Used in **Task 1 (Handling Missing Data)**. The missing values are arranged so that after filling `Name`, `Age`, `Salary`, and `Join Date`, only `City` is still missing.

### `eclipses.csv`
A pipe-delimited (`|`) list of eclipses observed in Arkansas.

| Column | Type | Notes |
|---|---|---|
| `Date` | text (date) | mostly valid; a few values are deliberately invalid (e.g., `2024-02-30`, `not recorded`, `2023-13-05`) |
| `Type` | text | Partial / Annular / Total |
| `Location` | text | an Arkansas city |
| `Coverage` | integer | percent of the sun covered |

Used in **Task 2 (Data Types and Dates)** — the invalid dates become `NaT` under `pd.to_datetime(..., errors="coerce")` — and **Task 4 (Duplicates)**, since the file contains a few exact duplicate rows.

> **Separator:** `eclipses.csv` uses `|`, not a comma. Read it with `pd.read_csv(path, sep="|")`.

## Regenerating

Both files are produced by `generate_assignment3.py` in this folder:

```bash
python generate_assignment3.py
```

Edit that script to change the data; it is the source of truth for these fixtures.
