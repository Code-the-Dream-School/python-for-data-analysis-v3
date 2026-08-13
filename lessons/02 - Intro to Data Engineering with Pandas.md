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

1. **[Series and DataFrames](<02 - Intro to Data Engineering with Pandas/01_series_data_frames.md>)**

   The two structures Pandas is built on, how a Series index differs from a list's positions, and why a DataFrame beats a list of dictionaries for real work.

2. **[Loading and Saving Data](<02 - Intro to Data Engineering with Pandas/02_loading_saving_data.md>)**

   Reading data from CSV files, JSON files, dictionaries, and web APIs, plus saving your results back out with `to_csv`.

3. **[Inspecting a Dataset](<02 - Intro to Data Engineering with Pandas/03_inspecting_datasets.md>)**

   A dependable "first look" routine — `shape`, `head`, `info`, `describe`, and `value_counts` — for getting to know any new dataset before you analyze it.

4. **[Selecting and Filtering](<02 - Intro to Data Engineering with Pandas/04_selecting_filtering.md>)**

   Pulling out columns, rows, and cells with `.loc` and `.iloc`, filtering with boolean conditions, and counting the missing values that lead into Week 3.

## Summary

This week moved you from *having* data to *working with* it. You now know the two structures every Pandas operation returns — the one-dimensional **Series** and the two-dimensional **DataFrame** — and that their **index** is a label, not a row number. You can pull data in from the four sources you'll actually meet (CSV, JSON, dictionaries, and APIs) and write results back out. You have a repeatable routine for inspecting a dataset so you never analyze something you don't understand. And you can select and filter down to the precise slice a question needs, using `.loc` and `.iloc` correctly and combining conditions with `&` and `|` instead of `and`/`or`.

That last step — running `isna().sum()` and seeing where the gaps are — is the natural handoff into **Week 3: Data Cleaning and Validation**, where you'll decide what to do about the missing and malformed values this week taught you to find.

## Check for Understanding

**1. You've just loaded an unfamiliar CSV into a DataFrame called `df`. Which sequence is the most sensible *first look* before any analysis?**

* A) `df.describe()`, then `df['col'] = df['col'].str.upper()`
* B) `df.shape`, `df.head()`, `df.info()`, `df.describe()`, then `value_counts()` on key categories
* C) `df.to_csv()`, then `df.head()`
* D) `df.loc[0:100]`, then `df.iloc[0:100]`

<details>
<summary>Answer</summary>

B) Size it up, look at a few rows, check types and missing values, sanity-check the numbers, then explore the categories. That's the routine from Module 2.3.

</details>

**2. A colleague reads `data.json` (a list of user objects, each with a nested `address`) with `pd.read_json()` and finds an `address` column full of dictionaries. What's the cleanest fix?**

* A) Delete the `address` column
* B) Load the JSON with `pd.json_normalize()` to flatten the nested fields into columns
* C) Convert the column to a string
* D) Re-save the file as CSV first

<details>
<summary>Answer</summary>

B) `pd.json_normalize()` flattens nested JSON into ordinary columns like `address.city`. (Module 2.2.)

</details>

**3. Given a DataFrame indexed `0, 1, 2, 3`, you want the rows where `Age > 30` **and** `City` is `"Chicago"`. Which expression is correct?**

* A) `df[df['Age'] > 30 and df['City'] == "Chicago"]`
* B) `df[df['Age'] > 30 & df['City'] == "Chicago"]`
* C) `df[(df['Age'] > 30) & (df['City'] == "Chicago")]`
* D) `df.loc[Age > 30 and City == "Chicago"]`

<details>
<summary>Answer</summary>

C) Combine conditions with `&`, and wrap each in parentheses. `and` fails on a Series (A, D), and without parentheses `&` binds too tightly and evaluates in the wrong order (B). (Module 2.4.)

</details>

**4. What does `df.isna().sum()` return, and why is it the last thing you run this week?**

* A) The total number of rows; it confirms the file loaded
* B) A per-column count of missing values; it tells you what Week 3 will need to clean
* C) The sum of every numeric column; it summarizes the data
* D) A list of duplicate rows; it finds repeats

<details>
<summary>Answer</summary>

B) `isna()` marks missing cells as `True`, and summing counts them per column. Those counts are exactly the input to Week 3's cleaning work. (Module 2.4.)

</details>
