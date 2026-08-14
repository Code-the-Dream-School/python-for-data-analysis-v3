# 4.1 Grouping and Aggregation

**Objective**: By the end of this module, you will be able to:

* Summarize data by group with `groupby()` and aggregate functions.
* Group by one column or several at once.
* Apply multiple aggregations with `agg()` using a list and a dictionary.
* Explain why a list of functions and a dictionary produce differently-shaped results.

---

Week 3 left you with clean data; this week, you'll start asking questions of it. The most interesting questions are about *groups*, not individual rows: total revenue **by region**, average score **by class**, order count **by customer**. **Aggregation** answers these by summarizing many rows into one number per group.

The mental model is **split–apply–combine**: 

* Pandas *splits* the data into groups,
* *applies* a summary function to each group,
* and *combines* the results into a new table.

`groupby()` is how you express this model.

We'll use this small sales dataset throughout:

```python
import pandas as pd

sales = pd.DataFrame({
    'Region':  ['East', 'West', 'East', 'West', 'East'],
    'Product': ['Widget', 'Widget', 'Gizmo', 'Gizmo', 'Widget'],
    'Revenue': [100, 150, 200, 50, 120],
    'Units':   [10, 15, 20, 5, 12]
})
```

---

## Grouping by One Column

Group by a column, pick the column you want to summarize, and apply an aggregate function:

```python
sales.groupby('Region')['Revenue'].sum()
# Region
# East    420
# West    200
# Name: Revenue, dtype: int64
```

Read it as: *split the rows by `Region`, then sum `Revenue` within each group.* The group labels (`East`, `West`) become the index of the result.

Common aggregate functions include `sum()`, `mean()`, `count()`, `min()`, `max()`, `median()`, and `std()`:

```python
sales.groupby('Region')['Revenue'].mean()
# Region
# East    140.0
# West    100.0
# Name: Revenue, dtype: float64
```

---

## Grouping by Several Columns

Pass a list of columns to group by more than one. The result has a row for each *combination* that appears in the data:

```python
sales.groupby(['Region', 'Product'])['Revenue'].sum()
# Region  Product
# East    Gizmo      200
#         Widget     220
# West    Gizmo       50
#         Widget     150
# Name: Revenue, dtype: int64
```

This produces a **multi-level index** (`Region` and `Product` together identify each row) — a structure you'll see again with pivot tables in Module 4.3.

---

## Multiple Aggregations with `agg()`

`sum()` gives one number per group. `agg()` lets you compute several summaries at once, and *how you call it* changes the shape of what you get back.

**A dictionary** applies a chosen function to each named column — useful when different columns need different summaries:

```python
sales.groupby('Region').agg({'Revenue': 'sum', 'Units': 'mean'})
#         Revenue  Units
# Region
# East        420   14.0
# West        200   10.0
```

**A list of functions** on a column computes all of them — and because each column now holds several results, the column header becomes **two levels** (`Revenue → sum`, `Revenue → mean`, …):

```python
sales.groupby('Region').agg({'Revenue': ['sum', 'mean', 'count']})
#         Revenue
#             sum   mean  count
# Region
# East        420  140.0      3
# West        200  100.0      2
```

That two-level header is the key difference: a **single function** per column gives you flat columns, while a **list of functions** nests them under the original column name. Knowing which shape you'll get saves confusion when you go to use the result — a column you access as `result['Revenue']` in the first case becomes `result[('Revenue', 'sum')]` in the second.

---

### AI Prompt: Predict-then-Check

The shape of an `agg()` result is a common source of confusion. Study this without running it:

```python
import pandas as pd
df = pd.DataFrame({'Team': ['A', 'B', 'A', 'B'], 'Points': [10, 20, 30, 40]})

result_1 = df.groupby('Team').agg({'Points': 'sum'})
result_2 = df.groupby('Team').agg({'Points': ['sum', 'mean']})
```

Before you run it:

1. Predict the columns of `result_1` versus `result_2`. Which one has a two-level column header?
2. Explain to an AI chatbot *why* asking for a list of functions changes the shape of the result.
3. Ask: "Is my understanding of how `agg()` with a single function differs from `agg()` with a list correct?"
4. Run the code and check.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict `result_1` will have columns [your prediction] and `result_2` will have [your prediction] because [your reasoning]. Am I right about why the list of functions changes the shape?"

---

## Videos

* [Python Pandas Tutorial (Part 8): Grouping and Aggregating — Analyzing and Exploring Your Data](https://www.youtube.com/watch?v=txMdrV1Ut64) — Corey Schafer on `groupby` and aggregation.

---

## Check for Understanding

**1. What does `sales.groupby('Region')['Revenue'].sum()` return?**

* A) The total revenue across all regions, as one number
* B) The sum of `Revenue` for each `Region`, indexed by region
* C) The number of rows in each region
* D) An error

<details>
<summary>Answer</summary>

B) It splits rows by `Region` and sums `Revenue` within each group, giving one total per region with the region as the index.

</details>

**2. You want the `sum` of `Revenue` and the `mean` of `Units` for each region. Which call is correct?**

* A) `df.groupby('Region').agg(['sum', 'mean'])`
* B) `df.groupby('Region').agg({'Revenue': 'sum', 'Units': 'mean'})`
* C) `df.groupby('Region').sum().mean()`
* D) `df.agg('Region')`

<details>
<summary>Answer</summary>

B) A dictionary maps each column to the function you want for it. (A applies both functions to every column; C and D don't do what's asked.)

</details>

**3. Why does `agg({'Revenue': ['sum', 'mean']})` produce a two-level column header?**

* A) It's a bug
* B) Because each column now holds several results, so they're nested under the original column name
* C) Because the data has two regions
* D) Because you grouped by two columns

<details>
<summary>Answer</summary>

B) Asking for a list of functions gives multiple result columns per input column, so Pandas nests them (`('Revenue', 'sum')`, `('Revenue', 'mean')`). A single function keeps the columns flat.

</details>

---

## Further Reading

* [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html) — the official guide.
* [`DataFrameGroupBy.agg` documentation](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html)
