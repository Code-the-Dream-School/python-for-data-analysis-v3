# 2.1 Series and DataFrames

**Objective**: By the end of this module, you will be able to:

* Explain what **Pandas** is and why it is the standard tool for working with tabular data in Python.
* Create a **Series** and describe how its index differs from a plain list's positions.
* Create a **DataFrame** from a dictionary, a list of dictionaries, and a NumPy array.
* Describe the relationship between Pandas and **NumPy** at a high level.

---

## What Is Pandas?

**Pandas** is a powerful, open-source library for data analysis and manipulation in Python. It is the most widely used tool for working with **tabular data** — data arranged in rows and columns, like a spreadsheet or a database table. With Pandas, you can load data, clean it, transform it, and summarize it, all with a small amount of code. You can read more in the [official Pandas documentation](https://pandas.pydata.org/docs/index.html).

### Why Use Pandas?

Pandas gives you two data structures — the **Series** and the **DataFrame** — that make working with data more readable and efficient than plain Python lists and dictionaries. It is well suited for tasks that involve:

* Loading data from different file formats (CSV, JSON, Excel, SQL, and more)
* Cleaning and transforming messy data
* Summarizing data for analysis
* Visualizing data through libraries like Matplotlib and Seaborn

### Getting Started with Pandas

Normally, you would install Pandas with a command like this:

```bash
pip install pandas
```

**For this week, you do not need to install anything.** Week 2 runs in **Kaggle notebooks**, which come with Pandas, NumPy, and most other data libraries already installed — you only need to *import* them.

You also have Pandas available on your own computer: the `python_homework` environment you set up in Week 1 installed it through `requirements.txt`. You will return to that local setup later in the course, when you build and deploy a Streamlit dashboard. For now, everything happens in Kaggle:

```python
import pandas as pd
```

The `as pd` part gives the library a short nickname. Almost every Pandas example you will ever see — in this course, in documentation, and online — uses `pd`, so we will too.

---

## Pandas and NumPy

**NumPy** is a library that provides fast, memory-efficient numerical arrays and operations for Python. It is written in C and runs much faster than equivalent plain-Python code, which makes numerical work in NumPy competitive with compiled languages.

Pandas is **built on top of NumPy**: a Series stores its values in a NumPy array under the hood, and you will often see NumPy numbers (like `int64` and `float64`) when you inspect Pandas data. You do not need to master NumPy to use Pandas, but it helps to know the two are closely related. You can read more in the [NumPy documentation](https://numpy.org/).

---

## The Two Core Structures

Pandas has two main data structures:

1. **Series** — a one-dimensional labeled array, similar to a single column of a spreadsheet. Every value has a label called its **index**.
2. **DataFrame** — a two-dimensional table where each column can hold a different type of data. This is the structure you will use most often; think of it as a collection of Series that share the same index.

### Creating a Series

Run the following code in a Kaggle notebook cell:

```python
import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
print(s)
```

The output is:

```text
0    1
1    3
2    5
3    7
4    9
Name: numbers, dtype: int64
```

A Series is one-dimensional. The column on the **left** is the index (here, the automatic labels `0` through `4`). The column on the **right** is the data. `dtype: int64` tells you the values are 64-bit integers.

### The Index Is Not the Row Number

The most important idea to grasp about a Series is its **index**. Unlike a plain list, a Series lets you give each value a custom label:

```python
import pandas as pd   # you only need to import once per notebook session

data = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(data)
# a    10
# b    20
# c    30
# dtype: int64
```

Index labels do not have to be numbers, they do not have to be in order, and — surprisingly — they do not even have to be unique. Here is a trickier case:

```python
data2 = pd.Series(['Tom', 'Li', 'Antonio', 'Mary'], index=[5, 2, 2, 3])
print(data2)
# 5        Tom
# 2         Li
# 2    Antonio
# 3       Mary
# dtype: object

print(data2[2])
# 2         Li
# 2    Antonio
# dtype: object
```

**Notice what happened:** when you ask for the value at label `2`, and that label is used more than once, Pandas returns *another Series* containing every matching value — not a single item. This is why an index label is **not** the same as a row number.

```python
print(data2[1])
# KeyError! There is no index label 1, even though there is a second row.
```

If you want the plain `0, 1, 2, …` numbering back, you can reset the index:

```python
data3 = data2.reset_index(drop=True)
print(data3)
# 0        Tom
# 1         Li
# 2    Antonio
# 3       Mary
# dtype: object
```

The order of the values never changed — only the labels did. In Pandas, a Series is **value-mutable** (you can change the value stored at a location) but its size and order are fixed, and its index labels are immutable.

### A Series Is Not a List

A list is accessed only by **position**. A Series can be accessed by its **label** or by its position:

```python
# List — access by position only
my_list = [10, 20, 30]
print(my_list[1])          # 20

# Series — access by label...
my_series = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(my_series["b"])      # 20

# ...or by integer position, using .iloc
print(my_series.iloc[2])   # 30
```

A Series also supports operations across the whole structure at once:

```python
my_revised_series = my_series * 2
print(my_revised_series)
# a    20
# b    40
# c    60
# dtype: int64
```

Multiplying an entire list by `2` would *repeat* the list, not double each value. This whole-structure math is one of the main reasons we reach for Pandas.

---

## Creating a DataFrame

A **DataFrame** is a two-dimensional table, like a sheet in a spreadsheet or a table in a database. The most common way to create one is from a dictionary, where each key is a column name and each value is the list of entries in that column:

```python
data = {
    'Name': ['Amara', 'Yulia', 'Carlos'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
```

The output is:

```text
     Name  Age           City
0   Amara   24       New York
1   Yulia   27  San Francisco
2  Carlos   22        Chicago
```

You can also build the same DataFrame from a **list of dictionaries**, where each dictionary is one row:

```python
row_amara = {'Name': 'Amara', 'Age': 24, 'City': 'New York'}
row_yulia = {'Name': 'Yulia', 'Age': 27, 'City': 'San Francisco'}
row_carlos = {'Name': 'Carlos', 'Age': 22, 'City': 'Chicago'}

df = pd.DataFrame([row_amara, row_yulia, row_carlos])
print(df)   # same result as before
```

### Why Not Just Keep a List of Dictionaries?

Plain Python already lets you store rows as a list of dictionaries, so why convert to a DataFrame at all? Because once the data is in a DataFrame, Pandas can operate on an entire **column** at once — fast, vectorized math like `df['Age'] * 2` or `df['Age'].mean()` — instead of you writing a loop over every row. A list of dictionaries stores the column name again in every single row and forces you to iterate by hand for even simple summaries. The DataFrame stores each column once, in an efficient NumPy array, and gives you the whole toolkit of loading, cleaning, filtering, and aggregation that the rest of this course is built on. A list of dictionaries is a fine way to *collect* data (you built one in Week 1), but a DataFrame is how you *work* with it.

### Creating a DataFrame from a NumPy Array

Because Pandas is built on NumPy, you can also create a DataFrame directly from a NumPy array. Here you supply the column names yourself, since an array has no labels of its own:

```python
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
```

### The Index and Column Labels

Like a Series, every DataFrame has an **index** that labels each row. Again, this is **not** the same as the row number — it just happens to default to `0, 1, 2, …` when you don't set it. The index is useful for aligning and combining data, which is why you will sometimes see an `ignore_index=True` option later in the course: it tells Pandas to rebuild a clean index after an operation instead of preserving the old labels.

A DataFrame also has **column labels**, which are usually short descriptive strings. Column labels *can* repeat, but that is almost never helpful, so keep them distinct.

---

### AI Prompt: Retrieval Practice

Now that you have met the two core structures, put the difference into your own words to lock it in.

1. Open your preferred AI chatbot.
2. Explain, in your own words, the difference between a Series and a DataFrame.
3. Use an analogy — for example, a Series is like a single column in a spreadsheet, while a DataFrame is the whole table.
4. Ask the AI to give you feedback on your explanation.

> **Example prompt:** "I am learning Pandas. Here is my understanding of the difference between a Series and a DataFrame: [your explanation]. Does this accurately describe their relationship and their dimensions?"

---

## Videos

Corey Schafer's Pandas series (a favorite from Python Intro) opens with exactly this material:

* [Python Pandas Tutorial (Part 1): Getting Started with Data Analysis](https://www.youtube.com/watch?v=ZyhVh-qRZPA) — what a Series and a DataFrame are, and how they relate.

---

## Check for Understanding

**1. Which Pandas data structure represents a two-dimensional table?**

* A) List
* B) Array
* C) DataFrame
* D) Series

<details>
<summary>Answer</summary>

C) DataFrame — a DataFrame is two-dimensional (rows and columns). A Series is one-dimensional.

</details>

**2. In a Pandas Series, the index is best described as:**

* A) Always the same as the row's position (0, 1, 2, …)
* B) A label for each value that can be custom, out of order, and even non-unique
* C) A required column of unique integers
* D) The data type of the values

<details>
<summary>Answer</summary>

B) The index is a *label* for each value. It can be custom, out of order, and non-unique, which is exactly why it is not the same as a row number.

</details>

**3. What does `my_series * 2` do, where `my_series = pd.Series([10, 20, 30])`?**

* A) Repeats the values to make a Series of length 6
* B) Raises an error
* C) Doubles each value, giving `20, 40, 60`
* D) Doubles only the first value

<details>
<summary>Answer</summary>

C) Pandas applies the operation to every element, giving `20, 40, 60`. (Multiplying a plain *list* by 2 would repeat it instead.)

</details>

**4. Which of these does **not** create the DataFrame shown below?**

```text
     Name  Age
0   Amara   24
1   Yulia   27
```

* A) `pd.DataFrame({'Name': ['Amara', 'Yulia'], 'Age': [24, 27]})`
* B) `pd.DataFrame([{'Name': 'Amara', 'Age': 24}, {'Name': 'Yulia', 'Age': 27}])`
* C) `pd.DataFrame(['Amara', 'Yulia', 24, 27])`
* D) Both A and B create it

<details>
<summary>Answer</summary>

C) A flat list of values has no column structure, so it cannot produce a two-column table. Both A (a dict of columns) and B (a list of row dicts) produce the DataFrame shown.

</details>

---

## Further Reading

* [Pandas: Intro to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html) — the official guide to Series and DataFrames.
* [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) — a fast tour of the library.
* [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) — helpful background on the array library underneath Pandas.
