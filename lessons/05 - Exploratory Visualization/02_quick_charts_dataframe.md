# 5.2 Quick Charts from a DataFrame

**Objective**: By the end of this module, you will be able to:

* Make a chart straight from a DataFrame with `df.plot()`.
* Choose the chart with the `kind` parameter: line, bar, hist, scatter, box.
* Plot a `groupby` result directly.
* Know when a quick chart is enough and when to choose the presentation tools in Module 5.3.

---

Now that you can *choose* a chart (Module 5.1), here's the fastest way to *make* one. Pandas has plotting built right into the DataFrame: `df.plot()`. It is built on Matplotlib, but you don't have to touch Matplotlib to get a picture. This is the tool for **exploration** — seeing your data quickly while you work. Polishing a chart for presentation comes in Module 5.3.

> **In Kaggle**, charts render right in the notebook, directly under the cell. You'll usually want Matplotlib imported alongside Pandas, but you don't need `plt.show()` in a notebook — the plot appears on its own.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Month':    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales':    [100, 150, 200, 250, 300, 350],
    'Expenses': [80, 120, 180, 200, 220, 300]
})
```

---

## Picking the Chart with `kind`

`df.plot(kind=...)` makes each of the chart types from Module 5.1. You tell it which columns to use with `x` and `y`. (`df.plot(kind='bar')` and `df.plot.bar()` are two spellings of the same thing.)

**Line — a trend over time:**

```python
df.plot(x='Month', y=['Sales', 'Expenses'], kind='line', title='Sales vs. Expenses')
```

Pass a list to `y` to draw several lines on one chart.

**Bar — comparing categories:**

```python
df.plot(x='Month', y='Sales', kind='bar', title='Monthly Sales')
```

**Histogram — the distribution of one column:**

```python
df['Sales'].plot(kind='hist', bins=5, title='Distribution of Sales')
```

**Scatter — the relationship between two columns:**

```python
df.plot(kind='scatter', x='Sales', y='Expenses', title='Sales vs. Expenses')
```

A scatter plot *requires* both `x` and `y` — it's putting one variable on each axis.

**Box — spread and outliers at a glance:**

```python
df[['Sales', 'Expenses']].plot(kind='box', title='Spread of Sales and Expenses')
```

---

## Plotting a `groupby` Result

Here's where this connects to Week 4. A `groupby` result is itself a Series or DataFrame, so you can call `.plot()` **right on it** — no intermediate step. This is the shortest path from an aggregation to a picture:

```python
sales = pd.DataFrame({
    'Region':  ['East', 'West', 'East', 'West', 'East'],
    'Revenue': [100, 150, 200, 50, 120]
})

sales.groupby('Region')['Revenue'].sum().plot(kind='bar', title='Revenue by Region')
```

The grouped totals (`East`, `West`) become the bars, with the group labels as the x-axis — because `groupby` already put them in the index. Aggregate, then `.plot()`: that's the everyday exploration loop.

---

### AI Prompt: Scaffold Removal

Plots often come out *almost* right — labels overlap, bars are in a strange order, the wrong column is on an axis. When that happens, resist asking the AI to just rewrite it. Ask for direction instead:

> "My `df.plot(kind='bar')` chart has x-axis labels that overlap and are unreadable. Don't give me the full fix — give me 3 keywords or method names I should look into to rotate or space them out."

or

> "I called `df.plot(kind='scatter')` and got an error about a missing argument. Here's my code: [paste code]. Ask me 2 questions that will help me figure out what a scatter plot needs that I didn't provide."

The goal is to learn the tool well enough that the *story* in the chart comes from your own analysis — use AI to unstick yourself, not to think for you.

---

## Check for Understanding

**1. Which call makes a bar chart of `Sales` by `Month` directly from a DataFrame?**

* A) `df.bar('Month', 'Sales')`
* B) `df.plot(x='Month', y='Sales', kind='bar')`
* C) `plt.bar(df)`
* D) `df.chart(kind='bar')`

<details>
<summary>Answer</summary>

B) `df.plot(x=..., y=..., kind='bar')` (or `df.plot.bar(...)`) makes the chart straight from the DataFrame.

</details>

**2. You've computed `df.groupby('Category')['Sales'].sum()`. How do you turn it into a bar chart?**

* A) You can't plot a groupby result directly
* B) Append `.plot(kind='bar')` to the grouped result
* C) Convert it to a list first
* D) Use `plt.groupby()`

<details>
<summary>Answer</summary>

B) The grouped result is a Series, so `.plot(kind='bar')` works right on it — the group labels become the x-axis.

</details>

**3. Why does `df.plot(kind='scatter')` require both `x` and `y`?**

* A) It's an optional style choice
* B) A scatter plot puts one variable on each axis, so it needs to know both
* C) Only `x` is actually required
* D) Scatter plots don't use columns

<details>
<summary>Answer</summary>

B) A scatter plot shows the relationship between two variables — one on each axis — so both `x` and `y` are required.

</details>

---

## Further Reading

* [Chart visualization (pandas)](https://pandas.pydata.org/docs/user_guide/visualization.html) — the official guide to `df.plot()` and every `kind`.
* [`DataFrame.plot` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)
