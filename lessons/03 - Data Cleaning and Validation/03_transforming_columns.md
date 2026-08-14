# 3.3 Transforming Columns

**Objective**: By the end of this module, you will be able to:

* Add, replace, and drop columns in a DataFrame.
* Transform a column with arithmetic operators and NumPy functions.
* Apply a function to every value in a column with `.map()` and `.apply()`.
* Use lambdas and named functions to express the transformation you need.

---

Cleaning isn't only about removing bad values — it's also about *reshaping* good ones: converting units, deriving a category from a number, standardizing a code. This module is about creating new column values from existing ones. It's also the toolkit the next two modules depend on, so it's worth getting comfortable here before moving on.

We'll build up this small DataFrame throughout:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Amara', 'Yulia', 'Carlos'],
    'Salary': [70000, 80000, 90000]
})
```

---

## Adding, Replacing, and Dropping Columns

**Add** a column by assigning to a new name:

```python
df['Department'] = ['Sales', 'HR', 'Engineering']
```

**Replace** a column by assigning back to an existing name. Remember from Module 2.4 that `df['Salary']` is a *view* you don't write into directly — instead you build a new Series from it and assign it back:

```python
df['Salary'] = df['Salary'] * 1.10   # give everyone a 10% raise
```

**Drop** a column with `drop(columns=...)`:

```python
df = df.drop(columns='Department')
```

> `drop(columns='Department')` is the clear, modern way to remove a column. You may also see the older `df.drop('Department', axis=1)` — the `axis=1` says "this is a column, not a row." Both do the same thing.

---

## Transforming a Series

Replacing a column usually means computing its new values from the old ones. There are three common ways to transform a Series:

1. Arithmetic operators (vectorized)
2. NumPy functions
3. `.map()` and `.apply()` within a function.

Let's take a look at each.

### 1. Arithmetic operators (vectorized)

An operator applied to a Series runs on *every* value at once — no loop needed. This is called **vectorization**, and it's both faster and shorter than writing a `for` loop:

```python
df['Salary'] = df['Salary'] + 5000     # add 5000 to every salary
```

The value's type matters: you can square a number column, but you can't raise a text column to a power.

### 2. NumPy functions

NumPy functions operate on a whole Series the same vectorized way:

```python
import numpy as np

prices = pd.Series([4, 9, 16])
np.sqrt(prices)
# 0    2.0
# 1    3.0
# 2    4.0
# dtype: float64
```

> Use NumPy's `np.sqrt()`, not Python's `math.sqrt()`, on a Series — `math.sqrt()` works on a single number and will fail on a whole column.

### 3. `.map()` and `.apply()` with a function

When the transformation is custom logic rather than a single operator, pass a function to `.map()` or `.apply()`. Both call your function once for each value in the Series and collect the results.

You met **lambdas** in Week 1 — a lambda is a small, unnamed function written in one line. It's the usual way to write a quick transform:

```python
df['Salary_Band'] = df['Salary'].apply(lambda x: 'High' if x >= 85000 else 'Standard')
```

`.map()` behaves the same way with a function, and it *also* accepts a dictionary — handy for translating codes to labels:

```python
df['Dept_Code'] = df['Department'].map({'Sales': 'S', 'HR': 'H', 'Engineering': 'E'})
```

(You'll see much more of the dictionary form in Module 3.4, where it's the core of text cleanup — along with an important trap about what happens to values that aren't in the dictionary.)

When the logic is too involved for a one-line lambda, define a named function and pass it in — no parentheses, because you're handing `.apply()` the function itself, not calling it:

```python
def salary_band(value):
    if value >= 85000:
        return 'High'
    elif value >= 75000:
        return 'Mid'
    return 'Standard'

df['Salary_Band'] = df['Salary'].apply(salary_band)
```

---

> **Looking ahead:** Everything above uses `.apply()` on a *single column* — it sees one value at a time. In Week 4 you'll use `.apply()` on a whole DataFrame with `axis=1`, so your function receives an entire *row* and can combine several columns at once (for example, computing a commission from a revenue column and a plan column together). Same method, one step up: one value now, one row later.

---

## Videos

* [Python Pandas Tutorial (Part 5): Updating Rows and Columns — Modifying Data Within DataFrames](https://www.youtube.com/watch?v=DCDe29sIKcE) — Corey Schafer on adding, replacing, and transforming columns, including `map` and `apply`.

---

### AI Prompt: Predict-then-Check

`.map()` with a function transforms each value — but the return value's type matters. Study this without running it:

```python
import pandas as pd
df = pd.DataFrame({'Value': [1, 2, 3, 4]})
df['Label'] = df['Value'].map(lambda x: 'Even' if x % 2 == 0 else 'Odd')
```

Before you run it:

1. Predict the exact contents of the new `Label` column.
2. Explain to an AI chatbot how `.map()` decides what goes in each row, and what the lambda returns for each input value.
3. Ask: "Is my understanding of how a lambda is applied to each value in a Series correct?"
4. Run the code and check.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict the `Label` column will be [your prediction] because [your reasoning]. Am I right about how `.map()` applies the lambda to each value?"

---

## Check for Understanding

**1. What does `df['Price'] = df['Price'] * 1.05` do?**

* A) Multiplies only the first price by 1.05
* B) Raises an error, because you can't multiply a Series
* C) Multiplies every value in the `Price` column by 1.05 at once (vectorized)
* D) Creates a new DataFrame

<details>
<summary>Answer</summary>

C) An operator on a Series is applied to every value at once — this is vectorization. No loop is needed.

</details>

**2. You want to turn a numeric `Score` column into labels (`"Pass"`/`"Fail"`) based on a threshold. Which is a correct approach?**

* A) `df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')`
* B) `df['Result'] = df['Score'] > 60`
* C) `df['Result'] = math.sqrt(df['Score'])`
* D) `df['Result'] = df['Score'].astype(str)`

<details>
<summary>Answer</summary>

A) `.apply()` with a lambda runs your logic on each value and returns the label. (B produces `True`/`False`, not the labels; C and D don't apply a threshold.)

</details>

**3. When you pass a named function to `.apply()`, why do you write `.apply(salary_band)` and not `.apply(salary_band())`?**

* A) Because functions can't take parameters
* B) Because you're giving `.apply()` the function itself to call once per value — the parentheses would call it immediately instead
* C) Because `.apply()` only accepts lambdas
* D) There's no difference

<details>
<summary>Answer</summary>

B) `salary_band` is the function object; `.apply()` calls it for each value. Writing `salary_band()` would call it right now (with no argument) and pass the result instead.

</details>

---

## Further Reading

* [`Series.map` documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)
* [`Series.apply` documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html)
* [`DataFrame.drop` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
