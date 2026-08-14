# Lesson 3 — Data Cleaning and Validation

**Lesson Overview**

Week 2 ended with a question: `isna().sum()` showed you *where* the gaps were, but not what to do about them. This week is the answer. Real-world data arrives messy — missing values, numbers stored as text, dates in five formats, inconsistent spellings, duplicates, and values that are simply impossible. **Data cleaning** is the disciplined work of turning that mess into something you can trust, and it's where data professionals spend much of their time. You'll handle missing data, fix column types, reshape values, standardize text with the regex you learned in Week 1, and validate what's left against the rules of the real world. The guiding idea is an old one: *garbage in, garbage out* — the quality of your analysis can never exceed the quality of your data.

This week's work happens in **Kaggle notebooks**, and your assignment is submitted as a Kaggle notebook.

**Learning Objectives**

This week, I can...

* Find, remove, and fill missing values, and decide which is appropriate.
* Convert columns to the right types and parse messy dates, recognizing placeholder values that hide missing data.
* Transform columns with operators, `.map()`, and `.apply()`.
* Standardize and extract text using `.str` methods and regular expressions.
* Validate data against ranges and allowed sets, remove duplicates, and judge outliers — while keeping an untouched raw copy.

## Topics

1. **[Missing Data](<03 - Data Cleaning and Validation/01_missing_data.md>)**

   Finding missing values with `isna`, removing them with `dropna`, and filling them with `fillna`, `ffill`, and `bfill` — plus the judgment call of when to drop versus fill.

2. **[Data Types and Dates](<03 - Data Cleaning and Validation/02_data_types_dates.md>)**

   Converting columns with `astype` and `to_numeric`, parsing dates with `to_datetime`, and spotting placeholder values like `"N/A"` that hide missingness behind valid-looking text.

3. **[Transforming Columns](<03 - Data Cleaning and Validation/03_transforming_columns.md>)**

   Adding, replacing, and dropping columns, and reshaping values with operators, NumPy functions, `.map()`, and `.apply()` on a Series.

4. **[Text Standardization and Regex](<03 - Data Cleaning and Validation/04_text_standardization_regex.md>)**

   Normalizing text with `.str` methods, the `map`-versus-`replace` trap, and cleaning and extracting data with regular expressions.

5. **[Validation, Duplicates, and Outliers](<03 - Data Cleaning and Validation/05_validation_duplicates_outliers.md>)**

   Checking values against ranges and allowed sets, removing duplicates, handling outliers with judgment, and keeping a raw copy so every decision is reversible.

## Summary

This week added the tools to *fix* the data problems you learned to *find* last week. You can now handle missing values three ways and reason about which fits; convert columns to the types that make analysis possible; recognize the placeholder values that disguise missing data as real text; reshape columns with the `map`/`apply`/lambda toolkit; standardize and extract text with regex; and validate what remains against the rules of the real world — all while protecting the original with a raw copy.

Notice the order these modules follow: fix what's *missing*, fix the *types*, reshape the *values*, standardize the *text*, then *validate* the result. That's not arbitrary — it's a repeatable cleaning workflow you can bring to any messy dataset. The `map`/`apply`/lambda tools from Module 3.3 also carry directly into **Week 4**, where you'll stop cleaning single datasets and start combining and reshaping them: grouping, merging, pivoting, and engineering new features.

## Check for Understanding

**1. A numeric column is stored as text and contains a few `"unknown"` entries. Which approach cleans it without crashing?**

* A) `df['col'].astype(float)`
* B) `pd.to_numeric(df['col'], errors='coerce')`, then handle the resulting `NaN`s
* C) `df['col'].dropna()`
* D) `df['col'].str.strip()`

<details>
<summary>Answer</summary>

B) `to_numeric(errors='coerce')` converts valid numbers and turns `"unknown"` into `NaN`, which you then fill or drop. `astype` crashes on the first non-number. (Module 3.2.)

</details>

**2. You standardize a `City` column with `.str.lower().str.strip()`. Why do this *before* a `groupby('City')`?**

* A) `groupby` requires lowercase input
* B) Otherwise `"NY"`, `"ny"`, and `" NY "` are grouped as three separate cities
* C) It makes the code run faster
* D) It's only a matter of style

<details>
<summary>Answer</summary>

B) Inconsistent casing and whitespace split one real category into several, corrupting every group and count downstream. (Module 3.4.)

</details>

**3. You need to keep most values in a column but translate just a couple of codes, leaving the rest untouched. Which is the safe choice?**

* A) `map()` with a dictionary
* B) `replace()` with a dictionary
* C) `dropna()`
* D) `astype(str)`

<details>
<summary>Answer</summary>

B) `replace()` leaves unmapped values unchanged. `map()` would turn every value not in the dictionary into `NaN`. (Module 3.4.)

</details>

**4. Before making any cleaning changes, you run `raw_df = df.copy()`. What does this protect you from?**

* A) Slower performance
* B) Losing your original data — without `.copy()`, `raw_df` and `df` would be the same object, so editing one changes both
* C) Missing values
* D) Duplicate rows

<details>
<summary>Answer</summary>

B) `.copy()` gives you a genuinely independent snapshot, so every cleaning decision stays reversible and auditable. (Module 3.5.)

</details>
