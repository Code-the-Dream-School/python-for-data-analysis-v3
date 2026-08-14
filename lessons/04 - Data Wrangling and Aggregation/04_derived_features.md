# 4.4 Derived Features

**Objective**: By the end of this module, you will be able to:

* Create a column from logic that spans several columns with `apply(axis=1)`.
* Bin a continuous column into categories with `pd.cut()`.
* Encode categories as numbers with label encoding (`map`) and one-hot encoding (`get_dummies`).
* Choose the right encoding for ordered versus unordered categories.

---

**Feature engineering** is creating new columns that make patterns easier to see — and, later, easier for a model to learn from. This module covers three of the most useful moves: computing a value from several columns at once, turning a number into a category, and turning a category into numbers.

---

## Row-Spanning Logic with `apply(axis=1)`

In Module 3.3 you used `.apply()` on a single column — your function saw one value at a time. When a new column depends on **several columns together**, apply the function to the whole DataFrame with `axis=1`. Now your function receives an entire **row**, and can read any column from it.

First, a caution: for simple arithmetic across columns, you don't need `apply` at all — vectorized operations are faster and clearer:

```python
df['Total'] = df['East'] + df['West']   # no apply needed
```

Reach for `apply(axis=1)` when the logic is **conditional and spans columns** — something an operator can't express. A commission calculation is the classic case:

```python
import pandas as pd

sales = pd.DataFrame({
    'Employee': ['Jones', 'Smith', 'Garcia'],
    'Revenue':  [12000, 8000, 15000],
    'Plan':     ['A', 'B', 'A']
})

def commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)

sales['Commission'] = sales.apply(commission, axis=1)
#   Employee  Revenue Plan  Commission
# 0    Jones    12000    A      1100.0
# 1    Smith     8000    B         0.0
# 2   Garcia    15000    A      1250.0
```

`axis=1` is the whole point: it tells Pandas to hand your function one *row* at a time (not one column), so `row['Revenue']` and `row['Plan']` are both available in the same call. That's the step up from Week 3: **one value then, one row now.**
<!-- ===== NEW MATERIAL (v3) — end ===== -->

---

## Binning a Number into Categories with `pd.cut()`

Sometimes a category is more useful than a raw number — "Pass/Fail" instead of an exact score, an age *bracket* instead of an age. `pd.cut()` slices a continuous column into labeled bins.

The most controllable form gives explicit bin edges:

```python
grades = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [78, 40, 95]})

grades['Band'] = pd.cut(grades['Score'], bins=[0, 60, 80, 100],
                        labels=['Fail', 'Pass', 'Distinction'])
#       Name  Score         Band
# 0    Alice     78         Pass
# 1      Bob     40         Fail
# 2  Charlie     95  Distinction
```

The edges `[0, 60, 80, 100]` create three bins: `(0, 60]`, `(60, 80]`, `(80, 100]`. By default each bin includes its **right** edge, so a score of exactly 80 lands in `Pass`.

You can also pass a single number to split the range into that many equal-width bins — `pd.cut(grades['Score'], 3, labels=[...])` — but explicit edges are usually what you want, because *you* decide where the meaningful cutoffs are.

---

## Encoding Categories as Numbers

Many tools — especially machine-learning models — need numbers, not text. There are two standard ways to encode a categorical column, and choosing the wrong one introduces a subtle error.

### Label encoding: `map()` to numbers

Assign each category a number:

```python
sizes = pd.DataFrame({'Size': ['Small', 'Medium', 'Large', 'Medium']})
sizes['Size_Code'] = sizes['Size'].map({'Small': 1, 'Medium': 2, 'Large': 3})
```

This is fine when the categories have a **natural order** (small < medium < large): the numbers preserve that order.

### One-hot encoding: `get_dummies()`

For categories with **no order** — colors, cities, product names — label encoding lies, because it implies `Red(1) < Blue(2) < Green(3)`, an ordering that doesn't exist. **One-hot encoding** avoids this by making a separate yes/no column for each category:

```python
colors = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue']})
pd.get_dummies(colors['Color'], prefix='Color')
#    Color_Blue  Color_Green  Color_Red
# 0       False        False       True
# 1        True        False      False
# 2       False         True      False
# 3        True        False      False
```

Each row has `True` in exactly one column, with no false ordering implied.

> **Note:** current Pandas returns `True`/`False` (boolean) columns from `get_dummies`. If you need `1`/`0` instead, pass `dtype=int`: `pd.get_dummies(colors['Color'], prefix='Color', dtype=int)`.

The rule of thumb: **label encoding for ordered categories, one-hot for unordered ones.**

---

### AI Prompt: Retrieval Practice

Choosing an encoding is a judgment call with a real trap in it.

1. Open your preferred AI chatbot.
2. Explain, in your own words, the difference between label encoding and one-hot encoding.
3. Describe one column where label encoding is appropriate and one where it would introduce a *false ordering* — and say why one-hot fixes it.
4. Ask the AI for feedback on your reasoning.

> **Example prompt:** "I'm learning about encoding categorical data in Pandas. Here's my explanation of label encoding versus one-hot encoding: [your explanation]. I think label encoding suits [your example] but would be wrong for [your example] because [your reasoning]. Did I get the trade-off right?"

---

## Check for Understanding

**1. You need a new column whose value depends on two other columns using `if/else` logic. Which approach fits?**

* A) `df['new'] = df['a'] + df['b']`
* B) `df['new'] = df.apply(my_function, axis=1)`
* C) `df['new'] = df['a'].map(my_function)`
* D) `df['new'] = df.groupby('a')`

<details>
<summary>Answer</summary>

B) `apply(..., axis=1)` passes each whole row to your function, so it can read both columns and branch on them. (A only works for plain arithmetic; C sees just one column.)

</details>

**2. What does `pd.cut(df['Score'], bins=[0, 60, 80, 100], labels=['Fail','Pass','Distinction'])` do?**

* A) Removes scores outside 0–100
* B) Sorts the scores into three labeled ranges
* C) Calculates the average score
* D) Counts how many scores there are

<details>
<summary>Answer</summary>

B) It bins each score into one of the three labeled ranges defined by the edges. A score of 78 falls in `(60, 80]` → `Pass`.

</details>

**3. You're encoding a `City` column (no natural order) for a model. Which encoding avoids implying a false order?**

* A) Label encoding with `map({'NYC': 1, 'LA': 2, ...})`
* B) One-hot encoding with `get_dummies()`
* C) `astype(int)`
* D) `sort_values()`

<details>
<summary>Answer</summary>

B) One-hot encoding gives each city its own yes/no column, with no implied ordering. Label encoding would falsely suggest `NYC(1) < LA(2)`.

</details>

---

## Further Reading

* [`DataFrame.apply` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html) — including the `axis` parameter.
* [`pandas.cut` documentation](https://pandas.pydata.org/docs/reference/api/pandas.cut.html)
* [`pandas.get_dummies` documentation](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
