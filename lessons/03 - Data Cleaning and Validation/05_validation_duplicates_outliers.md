# 3.5 Validation, Duplicates, and Outliers

**Objective**: By the end of this module, you will be able to:

* Keep an untouched raw copy of your data before cleaning.
* Validate values against allowed ranges and allowed sets.
* Find and remove duplicate rows with `duplicated()` and `drop_duplicates()`.
* Spot outliers with simple rules and decide whether they're errors or real.

---

The earlier modules fixed *format* — missing values, wrong types, messy text. Validation asks a different question: **are these values plausible at all?** An age of 150, a department that doesn't exist, a salary a thousand times larger than the rest — these can be correctly typed and perfectly formatted while still being wrong. This module is the final gate before analysis: catch impossible values, remove accidental duplicates, and make a considered call on outliers.

---

## First, Keep a Raw Copy

We mentioned this in Module 3.1; here it becomes its own step. Before you change anything, save an untouched copy of the original data:

```python
raw_df = df.copy()   # never modified — your reference point
# ...do all cleaning on df...
```

Cleaning is a series of judgment calls, and you will sometimes want to undo one, compare "before and after," or prove to a reviewer what you changed. A raw copy makes every cleaning decision reversible and auditable. Note that it must be `.copy()` — a plain `raw_df = df` would be two names for the *same* DataFrame, so edits to `df` would change `raw_df` too.

---

## Validating Ranges

A **range check** confirms numeric values fall within sensible limits. Values outside the range are usually errors, so a common approach is to replace them with `NaN` and then handle them with the missing-data tools from Module 3.1:

```python
import numpy as np

# Ages must be between 18 and 65; anything else becomes NaN
df['Age'] = df['Age'].apply(lambda x: x if 18 <= x <= 65 else np.nan)

# Then fill the flagged values with the median
df['Age'] = df['Age'].fillna(df['Age'].median())
```

The lambda passed to `.apply()` (from Module 3.3) keeps a value when it's in range and returns `NaN` otherwise.

> A vectorized alternative does the same thing without `apply`, using a boolean mask and `.loc`:
> ```python
> df.loc[(df['Age'] < 18) | (df['Age'] > 65), 'Age'] = np.nan
> ```
> Both are correct — the mask version is faster on large data, the `apply` version reads a little more like a sentence. Use whichever is clearer to you.

---

## Validating Allowed Values

For categorical columns, the check is membership in an **allowed set** rather than a numeric range. `.isin()` tests each value against the set, and `~` (not) flips it to find the *invalid* rows:

```python
valid_departments = {'Sales', 'HR', 'Engineering'}

# Rows whose Department is NOT one of the allowed values
df[~df['Department'].isin(valid_departments)]
```

Surfacing the invalid rows lets you decide what to do — correct a typo (`"Salez"` → `"Sales"`), set it to `NaN`, or drop the row. The point of validation is to *find* the problems deliberately, not to let them slip through into your analysis.

---

## Removing Duplicates

Duplicate rows inflate counts and skew averages. `duplicated()` flags them and `drop_duplicates()` removes them:

```python
df.duplicated()          # True for each row that repeats an earlier one
df = df.drop_duplicates()  # keep the first occurrence, drop the rest
```

Sometimes a row is a duplicate only in the columns that matter — the same customer entered twice with different timestamps, say. Use `subset=` to define "duplicate" by specific columns:

```python
df = df.drop_duplicates(subset='Name')   # one row per Name
```

> By default the *first* occurrence is kept. Pass `keep='last'` to keep the last instead, or `keep=False` to drop every row that has a duplicate.

---

## Handling Outliers

An **outlier** is a value far from the rest of the data. Unlike a range violation, an outlier is not automatically wrong, which is the key point of this section. A straightforward rule can flag them:

```python
# Replace clearly impossible ages with the median
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)
```

But before you "fix" an outlier, ask whether it's an **error or a real extreme**:

* A recorded age of `150` is an error — no one is 150. Replace or remove it.
* A customer who spent 100× the average might be a real high-value customer. Deleting them would erase your most important data point.

Use outlier rules to *flag* extreme values, then apply domain judgment before changing anything. Deleting outliers without checking is a common way to produce a clean-looking but misleading analysis, which is one reason to keep the raw copy.

---

### AI Prompt: Retrieval Practice

Whether an outlier is an error or a genuine extreme is a judgment call worth practicing out loud.

1. Open your preferred AI chatbot.
2. Describe two outliers in your own words: one that is almost certainly a data-entry **error**, and one that is likely a **real** extreme value worth keeping.
3. Explain how you'd decide between replacing an outlier and keeping it.
4. Ask the AI whether your reasoning is sound and what questions it would ask about the data before deciding.

> **Example prompt:** "I'm learning to handle outliers in a dataset. I think [example A] is probably a data-entry error I should replace, and [example B] is a real extreme value I should keep, because [your reasoning]. What would you check about the data before deciding whether to remove an outlier?"

---

## Check for Understanding

**1. Why should you make `raw_df = df.copy()` before cleaning, rather than `raw_df = df`?**

* A) `.copy()` is faster
* B) `raw_df = df` makes two names for the same DataFrame, so cleaning `df` would also change `raw_df`
* C) There's no difference
* D) `.copy()` automatically cleans the data

<details>
<summary>Answer</summary>

B) Without `.copy()`, both names point at the same object and you'd lose your untouched reference the moment you edit `df`.

</details>

**2. Which method removes duplicate rows, keeping the first occurrence by default?**

* A) `duplicated()`
* B) `drop_duplicates()`
* C) `unique()`
* D) `remove_duplicates()`

<details>
<summary>Answer</summary>

B) `drop_duplicates()` removes repeats. `duplicated()` only *flags* which rows are duplicates.

</details>

**3. You find a customer whose spending is 100× everyone else's. What's the best first step?**

* A) Delete the row immediately — it's an outlier
* B) Investigate whether it's a data-entry error or a real high-value customer before changing anything
* C) Replace it with the median automatically
* D) Ignore all outliers

<details>
<summary>Answer</summary>

B) Outliers aren't automatically errors. Flag it, then use domain judgment — deleting a real extreme value can badly distort your conclusions.

</details>

---

## Further Reading

* [`DataFrame.drop_duplicates` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)
* [`Series.isin` documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html)
* [`DataFrame.copy` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html)
