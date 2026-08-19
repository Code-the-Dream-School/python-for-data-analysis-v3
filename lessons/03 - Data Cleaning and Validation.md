# Lesson 3 — Data Cleaning and Validation

**Lesson Overview**

Real-world data arrives messy: missing values, numbers stored as text, dates in five formats, inconsistent spellings, duplicates, and values that are simply impossible. **Data cleaning** is the disciplined work of turning that mess into something you can trust, and it's where data professionals spend much of their time. You'll handle missing data, fix column types, reshape values, standardize text with the regex you learned in Week 1, and validate what's left against the rules of the real world. The guiding idea is an old one: *garbage in, garbage out*. The quality of your analysis can never exceed the quality of your data.

This week's work happens in **Kaggle notebooks**, and your assignment is submitted as a Kaggle notebook.

**Learning Objectives**

This week, I can...

* Find, remove, and fill missing values, and decide which is appropriate.
* Convert columns to the right types and parse messy dates, recognizing placeholder values that hide missing data.
* Transform columns with operators, `.map()`, and `.apply()`.
* Standardize and extract text using `.str` methods and regular expressions.
* Validate data against ranges and allowed sets, remove duplicates, and judge outliers — while keeping an untouched raw copy.

## Topics

1. **[Missing Data](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/03%20-%20Data%20Cleaning%20and%20Validation/01_missing_data.md)**

   Finding missing values with `isna`, removing them with `dropna`, and filling them with `fillna`, `ffill`, and `bfill` — plus the judgment call of when to drop versus fill.

2. **[Data Types and Dates](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/03%20-%20Data%20Cleaning%20and%20Validation/02_data_types_dates.md)**

   Converting columns with `astype` and `to_numeric`, parsing dates with `to_datetime`, and spotting placeholder values like `"N/A"` that hide missingness behind valid-looking text.

3. **[Transforming Columns](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/03%20-%20Data%20Cleaning%20and%20Validation/03_transforming_columns.md)**

   Adding, replacing, and dropping columns, and reshaping values with operators, NumPy functions, `.map()`, and `.apply()` on a Series.

4. **[Text Standardization and Regex](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/03%20-%20Data%20Cleaning%20and%20Validation/04_text_standardization_regex.md)**

   Normalizing text with `.str` methods, the `map`-versus-`replace` trap, and cleaning and extracting data with regular expressions.

5. **[Validation, Duplicates, and Outliers](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/03%20-%20Data%20Cleaning%20and%20Validation/05_validation_duplicates_outliers.md)**

   Checking values against ranges and allowed sets, removing duplicates, handling outliers with judgment, and keeping a raw copy so every decision is reversible.

## Summary

This week added the tools to fix the data problems you learned to find last week. You can now handle missing values three ways and reason about which fits; convert columns to the types that make analysis possible; recognize the placeholder values that disguise missing data as real text; reshape columns with the `map`/`apply`/lambda toolkit; standardize and extract text with regex; and validate what remains against the rules of the real world — all while protecting the original with a raw copy.

Notice the order these modules follow: fix what's missing, fix the types, reshape the values, standardize the text, then validate the result. This is a repeatable cleaning workflow you can bring to any messy dataset. The `map`/`apply`/lambda tools from Module 3.3 also carry directly into **Week 4**, where you'll stop cleaning single datasets and start combining and reshaping them: grouping, merging, pivoting, and engineering new features.
