# 3.2 Data Types and Dates

**Objective**: By the end of this module, you will be able to:

* Check and convert column types with `dtypes` and `astype()`.
* Convert messy text to numbers with `pd.to_numeric()` and `errors="coerce"`.
* Parse dates with `pd.to_datetime()`, handling invalid dates and mixed formats.
* Recognize placeholder values like `"N/A"` and `"unknown"` that hide missing data behind valid-looking text.

---

A value's **type** determines what you can do with it. You can average a column of numbers but not a column of text; you can sort dates chronologically only if Pandas knows they're dates. When data is loaded from a CSV or an API, columns often arrive as the wrong type — numbers stored as text, dates stored as text — and every calculation downstream depends on fixing that first.

You already met `df.dtypes` in Week 2. `object` almost always means text. When a column you expect to be numeric or a date shows up as `object`, that's your signal to convert it.

---

## Converting Types with `astype()`

When a column is clean and just needs its type changed, `astype()` is the simplest tool:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Amara', 'Yulia', 'Charlie'],
    'Age': ['24', '27', '22'],          # numbers stored as text
})

df['Age'] = df['Age'].astype(int)
df.dtypes
# Name    object
# Age      int64
# dtype: object
```

`astype()` works only when *every* value can be converted. If a single entry is `"unknown"` or blank, `astype(int)` raises an error and nothing converts. Real data is rarely that clean — which is why the next tool exists.

---

## Robust Number Conversion with `to_numeric()`

`pd.to_numeric()` with `errors="coerce"` converts what it can and turns anything it *can't* into `NaN` instead of crashing:

```python
df = pd.DataFrame({
    'Name': ['Amara', 'Yulia', 'Carlos'],
    'Height': ['5.5', 'unknown', '5.9'],   # 'unknown' is not a number
})

df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
df['Height']
# 0    5.5
# 1    NaN     ← 'unknown' could not be parsed, so it became NaN
# 2    5.9
# Name: Height, dtype: float64
```

This is the everyday pattern for numeric columns that arrive as text: coerce first, then handle the resulting `NaN`s with the tools from Module 3.1. `errors="coerce"` is what connects the two modules — it *turns* bad values into the missing values you already know how to fill or drop.

---

<!-- ===== NEW MATERIAL (v3) — begin: placeholder-detection framing ===== -->
> **🆕 NEW in v3** — *Elevated to its own concept, per the porting notes (Week 3.2: "recognizing placeholder values that hide missingness behind a valid string"). v2 replaced `"unknown"` in passing; here it's taught explicitly. Please review.*

## The Hidden Trap: Placeholders That Look Like Data

Not all missing data announces itself as an empty cell. Datasets are full of **placeholder values** — text someone typed in when the real value wasn't available:

* `"N/A"`, `"NA"`, `"n/a"`
* `"unknown"`, `"none"`, `"missing"`
* `"-"`, `"--"`, `"?"`
* `"NaN"` written as literal text

To Pandas, these are ordinary strings. `isna()` won't flag them, `dropna()` won't remove them, and a `value_counts()` will happily list `"unknown"` as if it were a real category. They silently corrupt averages, counts, and groupings.

The fix is to convert them into *real* missing values (`NaN`) so the tools from Module 3.1 can see them. For a **numeric** column, `to_numeric(errors="coerce")` already does this — every non-number becomes `NaN`. For a **text** column, replace them explicitly:

```python
import numpy as np

df['City'] = df['City'].replace(['N/A', 'unknown', '-', '?'], np.nan)
```

A good habit when you first inspect a dataset: run `value_counts()` on suspicious columns and *look* for these placeholders before you trust any summary.
<!-- ===== NEW MATERIAL (v3) — end ===== -->

---

## Parsing Dates with `to_datetime()`

Dates stored as text can't be sorted chronologically, subtracted, or grouped by month. `pd.to_datetime()` converts them into real datetime values, and `errors="coerce"` turns anything unparseable into **`NaT`** (Not a Time — the datetime version of `NaN`):

```python
df = pd.DataFrame({
    'Event': ['Project Start', 'Client Meeting', 'Beta Release', 'Final Launch'],
    'Date': ['2021/01/15', '2021-02-27', '03-15-2021', 'April 31, 2021']  # last one is invalid
})

df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df['Date']
# 0   2021-01-15
# 1   2021-02-27
# 2   2021-03-15
# 3          NaT     ← April 31 doesn't exist, so it became NaT
# Name: Date, dtype: datetime64[ns]
```

Two things to note:

* **`format='mixed'`** lets Pandas handle a column where the dates aren't all written the same way (`2021/01/15` vs. `03-15-2021`). Without it, mixed formats can raise an error or parse inconsistently.
* **Count what failed.** After coercing, check how many values didn't parse — a high count means the format is off or the column isn't really dates:

  ```python
  df['Date'].isna().sum()   # counts the NaT values → here, 1
  ```

There's the `isna().sum()` habit again: after every type conversion, it tells you how much didn't survive.

---

### AI Prompt: Predict-then-Check

The difference between `astype()` and `to_numeric()` on messy data is a common stumbling point. Study this code without running it:

```python
import pandas as pd
df = pd.DataFrame({'Score': ['90', '85', 'unknown', '77']})

# Option A
result_a = df['Score'].astype(int)
# Option B
result_b = pd.to_numeric(df['Score'], errors='coerce')
```

Before you run it:

1. Predict what happens with **Option A** and what happens with **Option B**.
2. Explain to an AI chatbot why one crashes while the other succeeds, and what the `'unknown'` value becomes in the version that works.
3. Ask: "Is my understanding of how `errors='coerce'` handles values that can't be converted correct?"
4. Run the code and check.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict Option A will [your prediction] and Option B will [your prediction] because [your reasoning]. Am I right about what `errors='coerce'` does with the `'unknown'` value?"

---

## Videos

Two videos from Corey Schafer's Pandas series cover the two halves of this module:

* [Python Pandas Tutorial (Part 9): Cleaning Data — Casting Datatypes and Handling Missing Values](https://www.youtube.com/watch?v=KdmPHEnPJPs) — `astype`, converting types, and the missing values that result.
* [Python Pandas Tutorial (Part 10): Working with Dates and Time Series Data](https://www.youtube.com/watch?v=UFuo7EHI8zc) — parsing and working with datetimes.

---

## Check for Understanding

**1. A column of numbers is stored as text, but a few entries say `"unknown"`. Which conversion succeeds without crashing?**

* A) `df['col'].astype(int)`
* B) `df['col'].astype(float)`
* C) `pd.to_numeric(df['col'], errors='coerce')`
* D) None of these will work

<details>
<summary>Answer</summary>

C) `to_numeric(errors='coerce')` converts the valid numbers and turns `"unknown"` into `NaN`. `astype` crashes on the first value it can't convert.

</details>

**2. After `pd.to_datetime(df['Date'], errors='coerce')`, what does a `NaT` value mean?**

* A) The date was a weekend
* B) The original value could not be parsed as a valid date
* C) The date is in the future
* D) The column is not really a date column

<details>
<summary>Answer</summary>

B) `NaT` ("Not a Time") is the datetime equivalent of `NaN` — it marks a value that couldn't be parsed, like `"April 31"`.

</details>

**3. A column contains the values `"N/A"` and `"unknown"`. Why won't `df.dropna()` remove those rows?**

* A) `dropna()` only works on numeric columns
* B) Those are ordinary text strings, not real missing values — Pandas doesn't see them as `NaN`
* C) You must call `dropna(text=True)`
* D) It will remove them

<details>
<summary>Answer</summary>

B) They're valid strings as far as Pandas is concerned. You have to convert them to real `NaN` first (with `replace(...)` or `to_numeric(errors='coerce')`) before `dropna`/`fillna` can act on them.

</details>

---

## Further Reading

* [`pandas.to_numeric` documentation](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)
* [`pandas.to_datetime` documentation](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
* [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) — how `NaN` and `NaT` behave.
