# 3.1 Missing Data

**Objective**: By the end of this module, you will be able to:

* Find missing values with `isna()` and `notna()`.
* Remove missing data with `dropna()`.
* Fill missing data with a constant, the mean, or the median using `fillna()`.
* Carry values forward or backward with `ffill()` and `bfill()`.
* Decide when dropping a row is better than filling it, and the reverse.

---

"Garbage in, garbage out" is an old saying in computing. It means that the quality of your analysis can only be as good as the quality of your data. Real-world datasets almost always arrive with gaps — a survey question left blank, a sensor that dropped a reading, a field that was never recorded. **Data cleaning** is the work of preparing messy data so the analysis you build on it is trustworthy, and handling missing values is where it usually starts.

At the end of Week 2 you learned to *find* missing values with `isna().sum()`. This week you decide what to *do* about them.

> **Before you clean, keep a copy.** Cleaning changes your data, and sometimes you'll want to compare against the original or undo a decision. Make an untouched copy first with `raw = df.copy()`, and do your cleaning on `df`. We'll come back to this discipline in Module 3.5.

---

## Finding Missing Values

Pandas represents a missing value as `NaN` (Not a Number). Two methods locate them:

* `isna()` returns `True` wherever a value is missing.
* `notna()` is its opposite — `True` wherever a value *is* present.

```python
import pandas as pd

data = {'Name': ['Amara', 'Yulia', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)

df.isna().sum()
# Name     1
# Age      1
# Score    1
# dtype: int64
```

> `isnull()` and `isna()` are the same method under two names (so are `notnull()` and `notna()`). This course uses `isna()`.

To see the actual *rows* that contain any missing value, combine `isna()` with `any(axis=1)` — `axis=1` means "look across each row":

```python
df[df.isna().any(axis=1)]
#     Name   Age  Score
# 1  Yulia  27.0    NaN
# 2   None  22.0   88.0
# 3  David   NaN   76.0
```

---

## Removing Missing Data with `dropna()`

`dropna()` removes any row that contains at least one missing value:

```python
df.dropna()
#     Name   Age  Score
# 0  Amara  24.0   85.0
```

Notice that this removed entire rows just because each had a single gap. `dropna()` is the right call when only a few rows are affected, or when the missing field is essential and can't be sensibly guessed (a transaction with no amount, say). But when a dataset is wide, a single missing cell per row can wipe out most of your data. Reach for `dropna()` deliberately, not by reflex.

> By default `dropna()` drops *rows*. To drop columns that contain missing values instead, pass `axis=1`.

---

## Filling Missing Data with `fillna()`

Often you'd rather keep the rows and fill the gaps. `fillna()` replaces missing values, and you can fill each column differently by passing a dictionary:

```python
df_filled = df.fillna({
    'Age': df['Age'].mean(),       # fill numeric gaps with the column mean
    'Score': df['Score'].median(), # ...or the median
    'Name': 'Unknown'              # fill text gaps with a placeholder
})
```

The three common strategies:

* **A constant** (`0`, `"Unknown"`) — when a missing value has a clear, meaningful stand-in.
* **The mean** — a reasonable center for roughly symmetric numeric data, but it's pulled by extreme values.
* **The median** — a safer center when the data has outliers, because it isn't dragged around by them.

>> [!Note]
>> **Filling has a cost.** Replacing every missing `Age` with the mean makes the column *look* complete, but it reduces the natural variation in the data and can produce many identical values at one point. Fill a column because it is the right choice for your analysis, not only to remove the `NaN`s.

---

## Forward Fill and Backward Fill

For data with a natural order — a time series, daily readings, anything sequential — the most sensible fill is often the value next to the gap. `ffill()` carries the last valid value *forward*; `bfill()` pulls the next valid value *backward*:

```python
import pandas as pd
import numpy as np

sales = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [100, np.nan, 150, np.nan, 200]
})

sales['Sales'].ffill()   # Tue → 100 (Monday's value carried forward)
sales['Sales'].bfill()   # Tue → 150 (Wednesday's value pulled backward)
```

> **Modern syntax.** Older code writes this as `fillna(method="ffill")`. That form is deprecated and no longer works in current Pandas — use `ffill()` and `bfill()` directly.

---

### AI Prompt: Retrieval Practice

The choice between dropping and filling is a judgment call, and explaining it out loud is a good way to test whether you really understand it.

1. Open your preferred AI chatbot.
2. Explain, in your own words, the difference between `dropna()` and `fillna()`.
3. Describe one scenario where **dropping** a row is the better choice, and one where **filling** with a median or mean is safer.
4. Ask the AI for feedback on your reasoning.

> **Example prompt:** "I'm learning about missing data in Pandas. Here's my explanation of when to use `dropna()` versus `fillna()`: [your explanation]. I think [scenario A] is better for dropping and [scenario B] is better for filling. What did I get right, and what risks am I missing?"

---

## Drop or Fill? Making the Call

There's no universal rule, but these questions guide most decisions:

* **How much is missing?** A handful of rows out of thousands — dropping is fine. Half the column — dropping throws away too much; fill it or reconsider the column.
* **Is the missing field essential?** If a row is meaningless without it (an order with no total), dropping is honest. If the field is secondary, fill it and keep the row.
* **Is there structure to exploit?** Ordered data can be forward/backward filled. Numeric data can take a mean or median. Categorical text usually takes a constant like `"Unknown"`.

The goal isn't to make every `NaN` vanish — it's to make a defensible choice you could explain to someone reviewing your work.

---

## Videos

* [Python Pandas Tutorial (Part 9): Cleaning Data — Casting Datatypes and Handling Missing Values](https://www.youtube.com/watch?v=KdmPHEnPJPs) — Corey Schafer on `dropna`, `fillna`, and handling missing values. (Its datatype-casting half also supports Module 3.2.)

---

## Check for Understanding

**1. Which method removes rows that contain missing values?**

* A) `fillna()`
* B) `dropna()`
* C) `isna()`
* D) `remove_na()`

<details>
<summary>Answer</summary>

B) `dropna()`. (`isna()` only *finds* missing values; `fillna()` replaces them.)

</details>

**2. Your numeric column has a few extreme outliers, and you need to fill its missing values with a center value. Which is the safer choice, and why?**

* A) The mean, because it uses every value
* B) The median, because it isn't pulled by the outliers
* C) Zero, because it's neutral
* D) It makes no difference

<details>
<summary>Answer</summary>

B) The median is resistant to outliers, so it better represents the "typical" value when extremes are present. The mean gets dragged toward the outliers.

</details>

**3. You have daily temperature readings with a few missing days, and want each gap filled with the most recent known reading. Which method fits?**

* A) `bfill()`
* B) `fillna(0)`
* C) `ffill()`
* D) `dropna()`

<details>
<summary>Answer</summary>

C) `ffill()` carries the last valid observation *forward* into the gap — the right choice for "use the most recent known value."

</details>

---

## Further Reading

* [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) — the official guide.
* [`DataFrame.fillna` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
* [`DataFrame.dropna` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
