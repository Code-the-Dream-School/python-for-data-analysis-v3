# 2.4 Selecting and Filtering

**Objective**: By the end of this module, you will be able to:

* Select columns, rows, and single cells with `[]`, `.loc`, `.iloc`, `.at`, and `.iat`.
* Explain how `.loc` and `.iloc` slicing differ.
* Filter rows with boolean conditions, combining them safely with `&` and `|`.
* Avoid the common `and`/`&` and `.str` traps that trip up beginners.
* Count missing values with `isna().sum()` as a bridge into data cleaning.

---

Loading a dataset gives you *everything*. Analysis usually needs a *part* of it — one column, the rows that meet a condition, a single cell. This module is about pulling out exactly the piece you want. We'll use this small DataFrame throughout:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 92, 88, 76]
})
```

---

## Selecting Columns

Select a single column with square brackets. The result is a **Series**:

```python
df['Age']
# 0    24
# 1    27
# 2    22
# 3    32
# Name: Age, dtype: int64
```

Select **multiple** columns by passing a *list* of names inside the brackets. The result is a **DataFrame**:

```python
df[['Name', 'Score']]
#       Name  Score
# 0    Alice     85
# 1      Bob     92
# 2  Charlie     88
# 3    David     76
```

Notice the double brackets: the outer `[]` is the selection, and the inner `[...]` is the list of columns.

---

## Selecting Rows and Cells with `.loc` and `.iloc`

Pandas has two main tools for selecting by row:

* **`.loc`** selects by **label** (the index label and column name).
* **`.iloc`** selects by **integer position** (0-based, like a list).

In both, **you give the row first, then the column.**

```python
# By label: row with index 1, column 'Name'
df.loc[1, 'Name']
# 'Bob'

# By position: row 1, column 1
df.iloc[1, 1]
# 27
```

For a **single cell**, `.at` (label) and `.iat` (position) do the same thing and are a little faster — reach for them when you want exactly one value:

```python
df.at[1, 'Name']   # 'Bob'
df.iat[1, 1]       # 27
```

### `.loc` and `.iloc` Slice Differently

This is the single most common source of confusion, so it's worth slowing down. Our DataFrame's index labels happen to be `0, 1, 2, 3`. Watch what slicing does:

```python
df.loc[0:2]    # rows with LABELS 0 through 2 — INCLUDES 2 → 3 rows
df.iloc[0:2]   # rows in POSITIONS 0 up to 2 — EXCLUDES 2 → 2 rows
```

* `.loc` slicing **includes** the end label. `df.loc[0:2]` returns three rows.
* `.iloc` slicing **excludes** the end position, exactly like Python list slicing. `df.iloc[0:2]` returns two rows.

You can also select a specific set of rows by passing a list of labels — something a plain Python list can't do:

```python
df.loc[[0, 2]]   # just the rows labeled 0 and 2
```

In each case, the result is a new DataFrame that is a subset of the original.

---

## Views, Copies, and How to Change a Value

When you select a column with `df['Age']`, you get a **view** into the DataFrame, not a fresh copy. Treat these as read-only. Trying to change a value *through* a view leads to trouble:

```python
df['Age'][1] = 35     # DON'T: "chained assignment"
```

This is called **chained assignment** — you index twice in a row (`['Age']` then `[1]`). Pandas may raise a `SettingWithCopyWarning`, and the change may or may not actually land in `df`. Either way, it's unreliable.

The correct, reliable way to set a value is a single `.loc` (or `.at`) call that names the row and column together:

```python
df.loc[1, 'Age'] = 35     # DO: one clear assignment
```

> **Rule of thumb:** if you're *reading*, `df['col']` is fine. If you're *writing*, use `.loc[row, col]`.

---

## Filtering Rows with Conditions

The most powerful kind of selection is a **boolean filter**: keep only the rows where a condition is true. A comparison on a column produces a Series of `True`/`False` values, and putting that inside `df[...]` keeps the `True` rows:

```python
df[df['Age'] > 24]
#     Name  Age  Score
# 1    Bob   27     92
# 3  David   32     76
```

### Combining Conditions: use `&` and `|`, not `and`/`or`

To combine two conditions, use `&` (and) or `|` (or) — **not** the Python keywords `and`/`or`. You must also wrap each condition in parentheses, because `&` binds more tightly than `>`:

```python
# WRONG — raises an error. 'and' does not work element-by-element on a Series.
df[df['Age'] > 24 and df['Score'] >= 88]

# RIGHT — '&' compares the two boolean Series element by element.
df[(df['Age'] > 24) & (df['Score'] >= 88)]
#   Name  Age  Score
# 1  Bob   27     92
```

Why the difference? Python's `and` expects a single `True`/`False` on each side, but a filter gives it a whole *Series* of them, and Pandas can't reduce that to one value — so it errors. `&` is defined to work position-by-position across the two Series, which is exactly what you want.

### Text Filters: string methods live under `.str`

The `in` keyword doesn't work on a Series either. For text matching, use the `.str` accessor, which exposes string methods that run down the whole column:

```python
# WRONG — the 'in' operator doesn't work on a Series this way.
df["a" in df['Name']]

# RIGHT — keep rows whose Name contains a lowercase 'a'.
df[df['Name'].str.contains("a")]
#       Name  Age  Score
# 2  Charlie   22     88
# 3    David   32     76
```

Note that `str.contains("a")` is **case-sensitive**: `"Alice"` has an uppercase `A` but no lowercase `a`, so it doesn't match. (Week 1's regex and Week 3's text cleaning both build on `.str`.)

The same `.str` rule applies when you *transform* text. Calling a plain string method on a Series fails; going through `.str` works:

```python
df['Name'] = df['Name'].upper()        # WRONG — a Series has no .upper()
df['Name'] = df['Name'].str.upper()    # RIGHT — .str.upper() runs it on every value
```

---

## One Last Check: Where Is Data Missing?

Filtering leads naturally to a question you'll ask about every real dataset: *which values are missing?* A **missing value** is an empty cell — Pandas shows it as `NaN` (Not a Number) — and it's exactly what the "non-null count" in `df.info()` was hinting at.

`df.isna()` returns a DataFrame of `True`/`False`, with `True` wherever a value is missing. Summing that gives a per-column count of missing values, because `True` counts as `1`:

```python
df.isna().sum()
# Name     0
# Age      0
# Score    0
# dtype: int64
```

Our tidy example has no gaps, so every count is `0`. On real data, this one line is usually the first thing you run after loading — and whatever it turns up is where **Week 3: Data Cleaning and Validation** picks up.

---

## Summary of Methods

| Goal | Tool | Example |
|---|---|---|
| One column (→ Series) | `df['col']` | `df['Age']` |
| Several columns (→ DataFrame) | `df[['a', 'b']]` | `df[['Name', 'Score']]` |
| Row/cell by label | `.loc` / `.at` | `df.loc[1, 'Name']` |
| Row/cell by position | `.iloc` / `.iat` | `df.iloc[1, 1]` |
| Filter rows | `df[condition]` | `df[df['Age'] > 24]` |
| Combine conditions | `&`, `|` (with `()`) | `df[(a) & (b)]` |
| Count missing values | `df.isna().sum()` | `df.isna().sum()` |

---

### AI Prompt: Predict-then-Check

`.loc` and `.iloc` look similar but slice differently. Study this code without running it:

```python
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [23, 27, 32, 44]}
df = pd.DataFrame(data)

subset_loc = df.loc[0:2, ['Name']]
subset_iloc = df.iloc[0:2]
```

Before you run it:

1. Predict how many rows are in `subset_loc` versus `subset_iloc`.
2. Explain to an AI chatbot why the results differ, even though both use the numbers 0 and 2.
3. Ask: "Is my reasoning about label-based slicing versus position-based slicing correct?"
4. Run the code and check.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict `subset_loc` has [number] rows and `subset_iloc` has [number] rows because [your reasoning]. Am I right that `.loc` includes the end label while `.iloc` does not?"

---

## Check for Understanding

**1. What does `df[['Name', 'Age']]` return?**

* A) A Series
* B) A DataFrame with two columns
* C) An error
* D) A single cell

<details>
<summary>Answer</summary>

B) Passing a *list* of column names returns a DataFrame. (A single name like `df['Name']` returns a Series.)

</details>

**2. `df.loc[0:2]` and `df.iloc[0:2]` are run on a DataFrame indexed `0, 1, 2, 3`. How many rows does each return?**

* A) Both return 2
* B) Both return 3
* C) `.loc` returns 3, `.iloc` returns 2
* D) `.loc` returns 2, `.iloc` returns 3

<details>
<summary>Answer</summary>

C) `.loc` **includes** the end label (rows 0, 1, 2 → 3 rows); `.iloc` **excludes** the end position (rows 0, 1 → 2 rows).

</details>

**3. Which expression correctly keeps rows where `Age > 24` AND `Score >= 88`?**

* A) `df[df['Age'] > 24 and df['Score'] >= 88]`
* B) `df[(df['Age'] > 24) & (df['Score'] >= 88)]`
* C) `df[df['Age'] > 24 & df['Score'] >= 88]`
* D) `df.loc[Age > 24, Score >= 88]`

<details>
<summary>Answer</summary>

B) Use `&` (not `and`) and wrap each condition in parentheses. Option C fails because `&` binds more tightly than `>`, so it evaluates in the wrong order without the parentheses.

</details>

**4. You need to change the value in row `1`, column `Age`. Which is the reliable way?**

* A) `df['Age'][1] = 30`
* B) `df.loc[1, 'Age'] = 30`
* C) `df[1]['Age'] = 30`
* D) `df.Age(1) = 30`

<details>
<summary>Answer</summary>

B) A single `.loc[row, col]` assignment is the reliable way. Option A is chained assignment, which can raise `SettingWithCopyWarning` and may not update `df`.

</details>

---

## Further Reading

* [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html) — the official guide to `.loc`, `.iloc`, and boolean selection.
* [Boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing) — combining conditions.
* [Working with text data](https://pandas.pydata.org/docs/user_guide/text.html) — the full `.str` toolkit.
