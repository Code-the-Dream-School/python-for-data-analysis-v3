# 4.2 Combining Datasets

**Objective**: By the end of this module, you will be able to:

* Combine two DataFrames on a shared key with `merge()`.
* Choose the right `how` value: `inner`, `left`, `right`, or `outer`.
* Handle overlapping column names (`_x`/`_y`) and merge on multiple keys.
* Join on the index with `join()`, and stack DataFrames with `concat()`.

---

Real data is rarely in one table. Customer details live in one place, their orders in another; this month's file is separate from last month's. **Combining** brings them together, and there are two distinct moves:

* **Side by side**, matching rows by a shared key — `merge()` and `join()`. (Add *columns.*)
* **Stacked**, one on top of another — `concat()`. (Add *rows.*)

---

## Merging on a Key

`merge()` lines up rows from two DataFrames wherever a shared key matches:

```python
import pandas as pd

people = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
scores = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 92, 88]})

pd.merge(people, scores, on='ID', how='inner')
#    ID   Name  Score
# 0   1  Alice     85
# 1   2    Bob     92
```

The result carries columns from *both* frames. Here the key is `ID`; where an `ID` appears in both, the row gets both `Name` and `Score`.

---

## Choosing `how`: inner, left, right, outer

The `how` value decides which rows survive when the keys don't line up perfectly. With `ID` 3 only in `people` and `ID` 4 only in `scores`:

| `how` | Keeps | Result on our data |
|---|---|---|
| `inner` | only keys in **both** | IDs 1, 2 |
| `left` | all keys from the **left** frame | IDs 1, 2, 3 (Charlie's `Score` is `NaN`) |
| `right` | all keys from the **right** frame | IDs 1, 2, 4 (ID 4's `Name` is `NaN`) |
| `outer` | **all** keys from either | IDs 1, 2, 3, 4 |

```python
pd.merge(people, scores, on='ID', how='left')
#    ID     Name  Score
# 0   1    Alice   85.0
# 1   2      Bob   92.0
# 2   3  Charlie    NaN     ← no matching score, so NaN
```

When a row has no match on the other side, its new columns fill with `NaN`. A **left** merge is the most common choice: it keeps all records from the left frame and attaches matching information where it exists (for example, all customers, plus order totals for those who ordered).

---

## Overlapping Column Names: `_x` and `_y`

If both frames have a non-key column with the *same name*, `merge()` can't keep both under one name, so it appends `_x` (left) and `_y` (right):

```python
left = pd.DataFrame({'ID': [1, 2], 'Age': [30, 25]})
right = pd.DataFrame({'ID': [1, 2], 'Age': [31, 26]})

pd.merge(left, right, on='ID')
#    ID  Age_x  Age_y
# 0   1     30     31
# 1   2     25     26
```

`Age_x` came from `left`, `Age_y` from `right`. Give them meaningful names with `suffixes`:

```python
pd.merge(left, right, on='ID', suffixes=('_2023', '_2024'))
#    ID  Age_2023  Age_2024
```

Seeing an unexpected `_x`/`_y` in your output is a signal you merged two frames that shared a column you forgot about.

---

## Merging on Multiple Keys

When one column isn't enough to identify a match, pass a list. Rows must agree on *every* key:

```python
pd.merge(df1, df2, on=['ID', 'Date'], how='inner')
```

This matches only where both `ID` **and** `Date` are the same — useful for composite keys, like one row per customer *per day*.

---

## Joining on the Index

`join()` is like `merge()` but matches on the **index** rather than a column:

```python
a = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[1, 2, 3])
b = pd.DataFrame({'Score': [85, 92, 88]}, index=[1, 2, 4])

a.join(b, how='outer')
#       Name  Score
# 1    Alice   85.0
# 2      Bob   92.0
# 3  Charlie    NaN
# 4      NaN   88.0
```

Reach for `join()` when the thing you're matching on is already the index; use `merge(..., on=...)` when it's a regular column.

---

## Stacking with `concat()`

`concat()` doesn't match keys — it stacks DataFrames end to end. This is how you combine files with the *same columns*, like twelve monthly exports:

```python
jan = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Sales': [100, 200]})
feb = pd.DataFrame({'Name': ['Charlie', 'Dana'], 'Sales': [150, 175]})

pd.concat([jan, feb], ignore_index=True)
#       Name  Sales
# 0    Alice    100
# 1      Bob    200
# 2  Charlie    150
# 3     Dana    175
```

`ignore_index=True` renumbers the combined rows `0, 1, 2, …` instead of repeating each frame's original index. (This is the one-liner you used to combine the CSV and JSON employees back in the Week 2 assignment.)

---

### AI Prompt: Retrieval Practice

The difference between `inner` and `left` is worth being able to explain out loud.

1. Open your preferred AI chatbot.
2. Explain, in your own words, the difference between an **inner** merge and a **left** merge.
3. Give a real-world scenario where a **left** merge is the right choice (for example, keeping every student on the roster even if they haven't submitted a particular assignment yet).
4. Ask the AI for feedback on your explanation.

> **Example prompt:** "I'm learning about merging DataFrames in Pandas. Here's my explanation of the difference between an inner merge and a left merge: [your explanation]. I think a left merge is useful for [your scenario]. What did I get right, and what should I understand about how `NaN` values appear in the unmatched rows?"

---

## Videos

* [**Pandas Functions: merge vs join vs concat | Misra Turp**](https://youtu.be/788KHREDbX8?si=DTYDl3evsuh_MWJN)

---

## Check for Understanding

**1. You merge two DataFrames and want to keep **every** row from the left one, attaching matches from the right where they exist. Which `how` value?**

* A) `inner`
* B) `left`
* C) `right`
* D) `outer`

<details>
<summary>Answer</summary>

B) `left` keeps all rows from the left frame; unmatched rows get `NaN` in the columns from the right frame.

</details>

**2. After a merge, you see columns named `Price_x` and `Price_y`. What happened?**

* A) The merge failed
* B) Both DataFrames had a `Price` column, so Pandas renamed them to keep both
* C) One price is in dollars and one in cents
* D) `Price_x` is always the correct one

<details>
<summary>Answer</summary>

B) Both frames had a non-key column named `Price`, so it appended `_x` (left) and `_y` (right). Use `suffixes=(...)` to give them clearer names.

</details>

**3. You have twelve monthly CSVs with identical columns and want one combined DataFrame. Which tool fits?**

* A) `merge()` on the index
* B) `join()`
* C) `pd.concat([...], ignore_index=True)`
* D) `groupby()`

<details>
<summary>Answer</summary>

C) `concat()` stacks frames with the same columns end to end; `ignore_index=True` renumbers the combined rows. Merge/join are for matching *columns* across frames, not stacking rows.

</details>

---

## Further Reading

* [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html) — the official guide.
* [`pandas.merge` documentation](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
* [`pandas.concat` documentation](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
