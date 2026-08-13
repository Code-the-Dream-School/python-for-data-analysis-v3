# 2.3 Inspecting a Dataset

**Objective**: By the end of this module, you will be able to:

* Preview a DataFrame with `head()` and `tail()`.
* Summarize a dataset's structure with `info()`, `shape`, and `dtypes`.
* Summarize a dataset's *contents* with `describe()` and `value_counts()`.
* Run these methods as a repeatable "first look" routine on any new dataset.

---

When you load a dataset you've never seen, resist the urge to jump straight into analysis. First, get to know it: How big is it? What are the columns and their types? Are values missing? What do the numbers and categories actually look like? Pandas gives you a handful of quick methods for exactly this, and running them in the same order every time turns "poking around" into a dependable routine.

We'll use this small dataset throughout the module:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Amara', 'Yulia', 'Carlos', 'David', 'Eve', 'Frank'],
    'Age': [24, 27, 22, 32, 29, 41],
    'City': ['New York', 'San Francisco', 'Chicago', 'New York', 'Chicago', 'New York'],
    'Department': ['Sales', 'Sales', 'HR', 'Engineering', 'HR', 'Sales']
})
```

> **Kaggle tip:** In a notebook, you don't always need `print()`. If a DataFrame (or `df.head()`) is the **last line** of a cell, Kaggle displays it as a nicely formatted table. Use `print()` when you want to show several things from one cell.

---

## Previewing Rows with `head()` and `tail()`

`head()` and `tail()` show the first or last few rows. By default they show five; pass a number to change that.

```python
# The first 3 rows
df.head(3)
```

```text
     Name  Age           City Department
0   Amara   24       New York      Sales
1   Yulia   27  San Francisco      Sales
2  Carlos   22        Chicago         HR
```

```python
# The last 2 rows
df.tail(2)
```

```text
    Name  Age      City   Department
4    Eve   29   Chicago           HR
5  Frank   41  New York        Sales
```

`head()` is the fastest way to confirm a file loaded correctly. `tail()` is useful for spotting junk that often hides at the *end* of a file, like a totals row or a stray blank line.

---

## Summarizing Structure with `info()`

`info()` gives you a compact summary of the whole DataFrame:

* the number of rows,
* each column's name and data type,
* the number of **non-null** values in each column, and
* the memory the DataFrame uses.

> "Null" means having no value or amounting to nothing. A null value means the data is missing. Note that zero is not a null value - zero is a number, and null would mean no number is present.

```python
df.info()
```

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Name        6 non-null      object
 1   Age         6 non-null      int64
 2   City        6 non-null      object
 3   Department  6 non-null      object
dtypes: int64(1), object(3)
memory usage: 324.0 bytes
```

That **Non-Null Count** column is doing quiet but important work. When a column shows fewer non-null values than there are rows, you've found missing data — which is exactly what Week 3 is about. `object` almost always means text (Python strings).

---

## A Few More One-Line Checks

`info()` is thorough. Sometimes you want just one fact, fast.

**`shape`** gives the dimensions as `(rows, columns)`. Note there are no parentheses — it's an attribute, not a method:

```python
df.shape
# (6, 4)
```

**`dtypes`** lists just the column types:

```python
df.dtypes
# Name          object
# Age            int64
# City          object
# Department    object
# dtype: object
```

## Summarizing the Numbers with `describe()`

`shape`, `dtypes`, and `info()` describe the *structure*. `describe()` describes the *contents* of the numeric columns — count, mean, spread, and the min/quartiles/max:

```python
df.describe()
```

```text
             Age
count   6.000000
mean   29.166667
std     6.794606
min    22.000000
25%    24.750000
50%    28.000000
75%    31.250000
max    41.000000
```

In one line you learn that ages run from 22 to 41 and cluster in the late twenties. This is your first glance at whether the numbers are reasonable — a `max` age of `410` or a `min` of `-3` would jump out here immediately.

> By default `describe()` only reports numeric columns. To summarize text columns instead, pass `df.describe(include='object')` — you'll get counts, number of unique values, and the most frequent value for each.

## Counting Categories with `value_counts()`

For a single categorical column, `value_counts()` tallies how often each value appears, sorted from most to least common:

```python
df['City'].value_counts()
# City
# New York         3
# Chicago          2
# San Francisco    1
# Name: count, dtype: int64
```

This is one of the most useful methods in all of Pandas. It answers "what's in this column, and how is it distributed?" in a single line, and it's how you catch inconsistent categories early — if you saw both `"New York"` and `"new york"` listed separately here, you'd know you have text to clean before Week 3.

## The First-Look Routine

Put together, these methods form a routine you can run on *any* new dataset, in this order:

1. **`df.shape`** — how big is it?
2. **`df.head()`** — what does a row look like?
3. **`df.info()`** — what are the columns, types, and how many values are missing?
4. **`df.describe()`** — are the numbers reasonable?
5. **`df['col'].value_counts()`** — for each important category, what values exist and how often?

Running the same five checks every time means you'll never start analyzing a dataset you don't understand — and you'll spot the problems (missing values, wrong types, messy categories) *before* they corrupt your results.

---

## Summary of Methods

| Method | What it tells you |
|---|---|
| `df.head(n)` / `df.tail(n)` | The first / last `n` rows |
| `df.shape` | Dimensions as `(rows, columns)` |
| `df.info()` | Column names, types, non-null counts, memory use |
| `df.dtypes` | Just the column data types |
| `df.describe()` | Count, mean, spread, and range of numeric columns |
| `df['col'].value_counts()` | How often each value appears in one column |

---

### AI Prompt: Predict-then-Check

Reading a summary is a skill of its own. Study this `info()` output for a dataset with **1,000 rows** — *without* seeing the data itself:

```text
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   user_id  1000 non-null   int64
 1   signup   1000 non-null   object
 2   age      938 non-null    int64
 3   country  1000 non-null   object
```

Before doing anything else:

1. Predict: which column has missing data, and how many values are missing? Which column looks like it might be a date stored as text?
2. Explain your reasoning to an AI chatbot.
3. Ask: "Based only on this `info()` output, which columns would you inspect or clean first, and why?"
4. Compare the AI's answer to yours.

> **Example prompt:** "Here is a Pandas `info()` summary for a 1,000-row dataset: [paste output]. I think [column] has [N] missing values and [column] is a date stored as text. Which columns should I inspect first before analyzing?"

---

## Check for Understanding

**1. Which method gives you column data types, non-null counts, and memory usage all at once?**

* A) `head()`
* B) `tail()`
* C) `describe()`
* D) `info()`

<details>
<summary>Answer</summary>

D) `info()`. (`describe()` summarizes the numeric *values*, not the structure.)

</details>

**2. In `df.info()` output, a column shows `938 non-null` for a DataFrame with 1,000 rows. What does that tell you?**

* A) The column has 938 duplicate values
* B) The column is missing 62 values
* C) The column uses 938 bytes of memory
* D) The column has 938 unique values

<details>
<summary>Answer</summary>

B) Non-null count below the row total means missing data — here, `1000 − 938 = 62` missing values.

</details>

**3. You want to know how many times each category appears in a single column. Which is the right tool?**

* A) `df.describe()`
* B) `df['col'].value_counts()`
* C) `df.shape`
* D) `df.head()`

<details>
<summary>Answer</summary>

B) `value_counts()` tallies each distinct value in a column, sorted from most to least common.

</details>

---

## Further Reading

* [Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html) — the official guide, including `describe` and `dtypes`.
* [`DataFrame.describe` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
* [`Series.value_counts` documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)
