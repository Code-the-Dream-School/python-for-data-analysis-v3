# Lesson 4 — Data Wrangling and Aggregation

**Lesson Overview**

You've already learned how to load and clean data. This week, you will learn how to reshape and combine it until it can answer the questions you want to ask. This process is called **data wrangling.** You will summarize data by group, combine separate tables into one, reshape long data into readable grids, and engineer new columns that surface patterns the raw data hides.

**Learning Objectives**

This week, I can...

* Summarize data by group with `groupby()` and `agg()`, using a list or a dictionary of functions.
* Combine DataFrames with `merge()`, `join()`, and `concat()`, choosing the right join type.
* Reshape data with `pivot_table()` and navigate results with `set_index`, `reset_index`, `rename`, and `sort_values`.
* Engineer new features with row-wise `apply()`, `pd.cut()` binning, and categorical encoding.

## Topics

1. **[Grouping and Aggregation](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/04%20-%20Data%20Wrangling%20and%20Aggregation/01_grouping_aggregation.md)**

   Summarizing data by group with `groupby()` and aggregate functions, and computing several summaries at once with `agg()` using a list versus a dictionary.

2. **[Combining Datasets](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/04%20-%20Data%20Wrangling%20and%20Aggregation/02_combining_datasets.md)**

   Bringing tables together with `merge()` and `join()` (matching on keys or the index) and `concat()` (stacking rows), plus the four join types and the `_x`/`_y` collision.

3. **[Reshaping with Pivot Tables](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/04%20-%20Data%20Wrangling%20and%20Aggregation/03_pivot_tables.md)**

   Turning long data into wide grids with `pivot_table()`, and navigating the results with `set_index`, `reset_index`, `rename`, and `sort_values`.

4. **[Derived Features](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/04%20-%20Data%20Wrangling%20and%20Aggregation/04_derived_features.md)**

   Creating new columns with row-wise `apply()`, binning numbers into categories with `pd.cut()`, and encoding categories as numbers with `map` and `get_dummies`.

## Summary

This week gave you the tools that turn clean data into insight. You can **aggregate** with `groupby()` to answer "what's the total/average/count per group?"; **combine** separate tables with `merge`, `join`, and `concat`; **reshape** long data into readable pivot grids and move fluidly between shapes with the index tools; and **engineer** new features — row-spanning calculations, bins, and encodings — that make relationships visible.

You've now completed the core data-handling arc: **load (Week 2) → clean (Week 3) → wrangle (Week 4)**. Next week you'll make the results visible by turning these tables and aggregations into charts.
