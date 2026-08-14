# 4.3 Reshaping with Pivot Tables

**Objective**: By the end of this module, you will be able to:

* Reshape data from long to wide with `pivot_table()`.
* Use the `index`, `columns`, `values`, `aggfunc`, and `fill_value` parameters.
* Read a result that has a multi-level index or multi-level columns.
* Navigate and tidy results with `set_index`, `reset_index`, `rename`, and `sort_values`.

---

Module 4.1 summarized data into a single column of results. Sometimes you want a *grid* instead — categories down the side, other categories across the top, a number in each cell. That's a **pivot table**, and it's the same split-apply-combine idea arranged as a two-dimensional layout, like a spreadsheet summary.

Underneath this is the idea of **long vs. wide** data. Our sales data is *long* — one row per observation:

```python
import pandas as pd

sales = pd.DataFrame({
    'Region':  ['East', 'West', 'East', 'West', 'East'],
    'Product': ['Widget', 'Widget', 'Gizmo', 'Gizmo', 'Widget'],
    'Revenue': [100, 150, 200, 50, 120],
    'Units':   [10, 15, 20, 5, 12]
})
```

A pivot table turns it *wide* — products down the side, regions across the top:

```python
pd.pivot_table(sales, index='Product', columns='Region', values='Revenue',
               aggfunc='sum', fill_value=0)
# Region   East  West
# Product
# Gizmo     200    50
# Widget    220   150
```

---

## The Pivot Table Parameters

Each parameter controls one part of the grid:

* **`index`** — what goes down the side (the row labels).
* **`columns`** — what spreads across the top. This is what makes it *wide*.
* **`values`** — which column fills the cells.
* **`aggfunc`** — how to combine when several rows land in one cell (`'sum'`, `'mean'`, `'count'`, …). A pivot table *aggregates*, just like `groupby`.
* **`fill_value`** — what to put in cells that have no matching data (otherwise `NaN`).

Leave out `columns` and you get a summary indexed only by `index` — essentially a `groupby`:

```python
pd.pivot_table(sales, index='Region', values='Revenue', aggfunc='sum')
#         Revenue
# Region
# East        420
# West        200
```

Pass a **list** to `index` (or `columns`) for a multi-level layout — the same multi-level index you saw with grouping in Module 4.1:

```python
pd.pivot_table(sales, index=['Region', 'Product'], values='Revenue', aggfunc='sum')
```

---

## Navigating and Tidying the Result

Grouping and pivoting both put your grouping labels into the **index**, not a normal column — which is why `result['Region']` often raises a `KeyError` after a `groupby`. These four tools move between shapes and clean up the result.

**`reset_index()`** turns the index back into ordinary columns and restores a plain `0, 1, 2` index. It's the fix for "I grouped, and now I can't select my group column":

```python
summary = sales.groupby('Region')['Revenue'].sum().reset_index()
#   Region  Revenue
# 0   East      420
# 1   West      200      ← 'Region' is now a normal column again
```

**`set_index()`** does the reverse — promotes a column to be the index:

```python
sales.set_index('Product')
```

**`rename()`** changes column names:

```python
summary = summary.rename(columns={'Revenue': 'Total Revenue'})
```

**`sort_values()`** orders rows by a column — often the finishing touch that turns a summary into a ranking:

```python
summary = summary.sort_values(by='Total Revenue', ascending=False)
```

> Many of these methods accept `inplace=True` to modify the DataFrame directly, but assigning the result back (`df = df.sort_values(...)`) is the clearer, recommended habit — it's obvious what changed and it chains naturally.

A very common pattern strings several together: group, flatten, rename, sort.

```python
ranking = (sales.groupby('Region')['Revenue'].sum()
                .reset_index()
                .rename(columns={'Revenue': 'Total Revenue'})
                .sort_values(by='Total Revenue', ascending=False))
```

---

### AI Prompt: Predict-then-Check

Whether a variable becomes a row or a column changes the shape of a pivot. Study this without running it:

```python
import pandas as pd
sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'West'],
    'Product': ['Widget', 'Widget', 'Gizmo', 'Gizmo'],
    'Revenue': [100, 150, 200, 50]
})

pivot_a = pd.pivot_table(sales, index='Product', columns='Region', values='Revenue', aggfunc='sum')
pivot_b = pd.pivot_table(sales, index=['Product', 'Region'], values='Revenue', aggfunc='sum')
```

Before you run it:

1. Predict the *shape* of each result — how many columns does `pivot_a` have versus `pivot_b`?
2. Explain to an AI chatbot how moving `Region` from `columns` to part of `index` changes the layout (wide vs. long).
3. Ask: "Is my understanding of how `index` and `columns` reshape a pivot table correct?"
4. Run the code and check.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict `pivot_a` will be shaped [your prediction] and `pivot_b` will be shaped [your prediction] because [your reasoning]. Am I right about how `columns` versus `index` changes the layout?"

---

## Videos

* [Pivot Tables with Pandas | Reuven Lerner](https://youtu.be/ETQXKwM6YMY?si=TigpI9P-bBfKz_OR)
* [Python Pandas Tutorial (Part 7): Sorting Data](https://www.youtube.com/watch?v=T11QYVfZoD0) — Corey Schafer on `sort_values` (the navigation half of this module).

---

## Check for Understanding

**1. In `pivot_table`, which parameter spreads a variable *across the top* to make the data wide?**

* A) `index`
* B) `columns`
* C) `values`
* D) `aggfunc`

<details>
<summary>Answer</summary>

B) `columns` spreads that variable across the top. `index` puts labels down the side, `values` fills the cells, `aggfunc` combines them.

</details>

**2. After `df.groupby('Region')['Revenue'].sum()`, why might `result['Region']` raise a `KeyError`?**

* A) `Region` was deleted
* B) `Region` became the index, not a normal column — use `reset_index()` to bring it back
* C) `groupby` doesn't support selection
* D) The column is misspelled

<details>
<summary>Answer</summary>

B) Grouping moves the group labels into the index. `reset_index()` turns `Region` back into a selectable column.

</details>

**3. Which method turns a normal column into the DataFrame's index?**

* A) `reset_index()`
* B) `set_index()`
* C) `rename()`
* D) `sort_values()`

<details>
<summary>Answer</summary>

B) `set_index()` promotes a column to the index; `reset_index()` does the reverse.

</details>

---

## Further Reading

* [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html) — the official guide.
* [`pandas.pivot_table` documentation](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
* [`DataFrame.sort_values` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
