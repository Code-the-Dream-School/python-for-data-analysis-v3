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

1. **[Grouping and Aggregation](<04 - Data Wrangling and Aggregation/01_grouping_aggregation.md>)**

   Summarizing data by group with `groupby()` and aggregate functions, and computing several summaries at once with `agg()` using a list versus a dictionary.

2. **[Combining Datasets](<04 - Data Wrangling and Aggregation/02_combining_datasets.md>)**

   Bringing tables together with `merge()` and `join()` (matching on keys or the index) and `concat()` (stacking rows), plus the four join types and the `_x`/`_y` collision.

3. **[Reshaping with Pivot Tables](<04 - Data Wrangling and Aggregation/03_pivot_tables.md>)**

   Turning long data into wide grids with `pivot_table()`, and navigating the results with `set_index`, `reset_index`, `rename`, and `sort_values`.

4. **[Derived Features](<04 - Data Wrangling and Aggregation/04_derived_features.md>)**

   Creating new columns with row-wise `apply()`, binning numbers into categories with `pd.cut()`, and encoding categories as numbers with `map` and `get_dummies`.

## Summary

This week gave you the tools that turn clean data into insight. You can **aggregate** with `groupby()` to answer "what's the total/average/count per group?"; **combine** separate tables with `merge`, `join`, and `concat`; **reshape** long data into readable pivot grids and move fluidly between shapes with the index tools; and **engineer** new features — row-spanning calculations, bins, and encodings — that make relationships visible.

We resolved to threads from earlier weeks:
* The `apply()` you learned on a single Series in Module 3.3 grew into row-wise `apply(axis=1)` in Module 4.4 — one value then, one row now.
* The `concat()` you used almost on faith in the Week 2 assignment got its full explanation in Module 4.2.

You've now completed the core data-handling arc: **load (Week 2) → clean (Week 3) → wrangle (Week 4)**. Next week you'll make the results visible by turning these tables and aggregations into charts.

## Check for Understanding

**1. You want total revenue for each region, with the region as a normal column you can select and sort afterward. Which sequence works?**

* A) `df.groupby('Region')['Revenue'].sum()`
* B) `df.groupby('Region')['Revenue'].sum().reset_index()`
* C) `df.pivot_table(index='Revenue')`
* D) `df.merge('Region')`

<details>
<summary>Answer</summary>

B) Grouping puts `Region` in the index; `reset_index()` turns it back into a selectable, sortable column. (Modules 4.1 and 4.3.)

</details>

**2. You have a customers table and an orders table sharing a `customer_id`, and you want *every* customer in the result even if they've never ordered. Which combine?**

* A) `merge(customers, orders, on='customer_id', how='inner')`
* B) `merge(customers, orders, on='customer_id', how='left')`
* C) `concat([customers, orders])`
* D) `customers.join(orders)`

<details>
<summary>Answer</summary>

B) A **left** merge keeps all customers and attaches order info where it exists; customers with no orders get `NaN`. (Module 4.2.)

</details>

**3. A new column's value depends on an `if/else` across two other columns. Which tool is designed for that?**

* A) A vectorized operator like `df['a'] + df['b']`
* B) `df.apply(func, axis=1)`
* C) `df.groupby('a')`
* D) `pd.cut(df['a'], 3)`

<details>
<summary>Answer</summary>

B) `apply(func, axis=1)` hands each whole row to your function, so it can branch on multiple columns. Vectorized operators handle plain arithmetic but not conditional logic. (Module 4.4.)

</details>

**4. You're encoding an unordered `Category` column (e.g., product type) for analysis. Which method avoids implying a false order between the categories?**

* A) `map()` to integers `1, 2, 3`
* B) `pd.get_dummies()` (one-hot encoding)
* C) `astype('category')`
* D) `sort_values()`

<details>
<summary>Answer</summary>

B) One-hot encoding gives each category its own yes/no column with no implied ranking. Mapping to `1, 2, 3` would falsely suggest an order. (Module 4.4.)

</details>
