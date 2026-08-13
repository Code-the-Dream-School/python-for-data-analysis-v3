# 2.2 Loading and Saving Data

**Objective**: By the end of this module, you will be able to:

* Load data into a DataFrame from a CSV file, a JSON file, and a Python dictionary.
* Use common `read_csv` parameters, including `sep`, `header`, and `index_col`.
* Save a DataFrame back out to a CSV file with `to_csv`.
* Read data from a web API into a DataFrame.

---

In Module 2.1 you built DataFrames by hand. In real work, the data almost always comes from somewhere else — a file, a database, or the web. This module covers the most common ways to get data *into* a DataFrame and back *out* to a file.

A quick note on where files live in Kaggle: you don't upload files directly into a notebook. Instead you attach a dataset with **Add Input** (covered in Week 1), and its files appear under a path like `/kaggle/input/<dataset-name>/`. In the examples below we use short names like `'data.csv'` to keep them readable, but in your own notebook you will usually pass the full `/kaggle/input/...` path.

---

## Reading a CSV File

A **CSV** (Comma-Separated Values) file is one of the most common formats for tabular data — you worked with CSV files in the Intro course. Pandas reads one into a DataFrame with `pd.read_csv()`:

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

`df.head()` shows the first five rows, which is a quick way to confirm the file loaded the way you expected. `read_csv` also accepts many parameters for files that aren't in the default shape:

```python
df = pd.read_csv('data.csv', sep=';', header=0, index_col='ID')
```

* `sep` — the character that separates columns (the default is a comma). Use this for files that separate columns with something else, like a semicolon or a tab.
* `header` — the row number to use for column names (defaults to the first row, row `0`).
* `index_col` — a column to use as the DataFrame's index instead of the automatic `0, 1, 2, …`.

---

## Reading a JSON File

**JSON** (JavaScript Object Notation) is a popular format for exchanging data on the web — you saw it in the Intro course when working with `requests`. Pandas reads a JSON file with `pd.read_json()`, which mirrors `pd.read_csv()`:

```python
df = pd.read_json('data.json')
print(df.head())
```

The JSON should be in one of two shapes. The first is a **list of objects**, where each object is one row:

```json
[
    {"Name": "Amara", "Age": 24, "City": "New York"},
    {"Name": "Yulia", "Age": 27, "City": "San Francisco"},
    {"Name": "Carlos", "Age": 22, "City": "Chicago"}
]
```

The second is an **object of lists**, where each key is a column. It is a little more compact because the column names appear only once:

```json
{
    "Name": ["Amara", "Yulia", "Carlos"],
    "Age": [24, 27, 22],
    "City": ["New York", "San Francisco", "Chicago"]
}
```

For deeply nested JSON, you may need extra parameters or a preprocessing step before the data fits neatly into a table — you'll see one way to handle that in the API section below.

---

## The `sep` Parameter

Not every "CSV" file uses commas. The `sep` parameter tells Pandas which character separates the columns, and it works for both reading and writing.

**Reading** a file that uses pipes (`|`):

```python
data = pd.read_csv("data.csv", sep="|")
print(data.head())
```

If the file contains:

```text
Name|Age|City
Amara|30|New York
Yulia|25|Los Angeles
```

the output is:

```text
    Name  Age         City
0  Amara   30     New York
1  Yulia   25  Los Angeles
```

**Writing** a file with a tab (`\t`) separator instead of a comma:

```python
df = pd.DataFrame({
    "Name": ["Amara", "Yulia"],
    "Age": [30, 25],
    "City": ["New York", "Los Angeles"]
})

df.to_csv("output.tsv", sep="\t", index=False)
```

`sep` is what lets you work with tab-separated files, pipe-delimited exports, and the region-specific formats that use semicolons.

> **Note:** `delimiter` is an accepted alias for `sep` in `read_csv` — the two do exactly the same thing. You'll see both in code online; this course uses `sep`.

---

## Creating a DataFrame from a Dictionary

You met this in Module 2.1, and we'll restate it here as a "loading" technique: when the data is already in your program as a dictionary of columns, `pd.DataFrame()` turns it straight into a DataFrame, no file needed.

```python
data = {
    'Name': ['Amara', 'Yulia', 'Carlos'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)
```

---

## Saving a DataFrame to a CSV File

Once you've loaded and worked with data, you'll often want to save the result — to share it, hand it to the next stage of a pipeline, or use it later. The `to_csv()` method writes a DataFrame to a CSV file:

```python
DataFrame.to_csv(filepath, sep=',', index=True, header=True, encoding=None)
```

* `filepath` — the name or path of the file to write (e.g. `"output.csv"`).
* `sep` — the delimiter to use (default is a comma).
* `index` — whether to write the DataFrame's index as a column (default `True`).
* `header` — whether to write the column names as the first row (default `True`).

A full example:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Amara', 'Yulia', 'Carlos'],
    'Age': [26, 31, 36],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000]
})

df.to_csv("employees.csv", index=False)
print("DataFrame saved to employees.csv")
```

The resulting `employees.csv` looks like this:

```text
Name,Age,City,Salary
Amara,26,New York,70000
Yulia,31,Los Angeles,80000
Carlos,36,Chicago,90000
```

> **Watch the `index` parameter.** We passed `index=False` on purpose. If you leave it at the default `True`, Pandas writes the index as an unnamed first column, and the *next* time you read the file you'll get a stray `Unnamed: 0` column. Unless the index carries real meaning you want to keep, `index=False` is the safer choice when saving.

---

## Reading Data from a Web API

A lot of data doesn't live in a file at all — it's served by a **web API** that returns JSON when you ask for it. You used the `requests` library for exactly this in the Intro course. The pattern is: fetch the JSON with `requests`, then hand it to Pandas.

> **Kaggle setup:** network access is turned off by default in a new notebook. To call an API, open the notebook settings panel on the right and switch **Internet** on. (This uses the account verification you completed in Week 1.)

```python
import requests
import pandas as pd

# A free, no-key test API that returns a JSON list of users
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()      # parse the JSON body into Python objects

df = pd.DataFrame(data)     # a list of dicts becomes a DataFrame
print(df[["id", "name", "email"]].head())
```

Because the response is a list of dictionaries (the same shape you saw in the JSON section above), `pd.DataFrame()` turns it directly into a table.

Real APIs often nest data (here, each user has an `address` that is itself an object). When a column comes back holding whole dictionaries, `pd.json_normalize()` flattens the nesting into ordinary columns:

```python
df = pd.json_normalize(data)
print(df.columns.tolist())
# includes flattened columns like 'address.city' and 'address.zipcode'
```

> **A good habit:** always check that the request succeeded before trusting the data. `response.raise_for_status()` will raise a clear error if the API returned a failure code, instead of letting a broken response flow silently into your DataFrame.

---

## Summary of Methods

| Source | Method | Example |
|---|---|---|
| CSV file | `pd.read_csv()` | `df = pd.read_csv('data.csv')` |
| JSON file | `pd.read_json()` | `df = pd.read_json('data.json')` |
| Dictionary | `pd.DataFrame()` | `df = pd.DataFrame(data)` |
| Web API (JSON) | `requests` + `pd.DataFrame()` | `pd.DataFrame(requests.get(url).json())` |
| Save to CSV | `df.to_csv()` | `df.to_csv('out.csv', index=False)` |

---

### AI Prompt: Predict-then-Check

Loading data is full of small "gotchas," and the `sep` parameter is a classic one. Study this code without running it:

```python
import pandas as pd
from io import StringIO

raw = "Name;Age;City\nAmara;30;New York\nYulia;25;Los Angeles"
df = pd.read_csv(StringIO(raw))
print(df.shape)
print(df.columns.tolist())
```

Before you run it:

1. Predict the shape of `df` and what its column names will be. (Hint: the data uses semicolons, but we never set `sep`.)
2. Explain to an AI chatbot why the columns come out the way they do.
3. Ask: "Is my reasoning about how `read_csv` splits columns when the separator doesn't match correct?"
4. Run the code and see if you were right.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict `df.shape` will be [your prediction] and the columns will be [your prediction] because [your reasoning]. Am I right about what happens when the file's real separator isn't the one `read_csv` expects?"

---

## Check for Understanding

**1. Which function loads data from a JSON file into a DataFrame?**

* A) `pd.read_csv()`
* B) `pd.read_json()`
* C) `pd.DataFrame()`
* D) `pd.read_dict()`

<details>
<summary>Answer</summary>

B) `pd.read_json()`.

</details>

**2. Your CSV file separates columns with semicolons (`;`). Which parameter tells `pd.read_csv()` about that?**

* A) `separator`
* B) `delimiter`
* C) `sep`
* D) Both B and C

<details>
<summary>Answer</summary>

D) Both `sep` and `delimiter` work — they are aliases for the same option.

</details>

**3. You save a DataFrame with `df.to_csv("out.csv")` and later read it back with `pd.read_csv("out.csv")`. You notice an extra `Unnamed: 0` column. What most likely caused it?**

* A) The file was corrupted
* B) `to_csv` wrote the index as a column because `index=False` was not set
* C) `read_csv` always adds an extra column
* D) The DataFrame had a hidden column

<details>
<summary>Answer</summary>

B) With the default `index=True`, `to_csv` writes the index as an unnamed column, which reappears as `Unnamed: 0` on read. Saving with `index=False` avoids it.

</details>

---

## Further Reading

* [`pandas.read_csv` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) — the full list of parameters.
* [`pandas.read_json` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html)
* [`pandas.json_normalize` documentation](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) — flattening nested JSON from APIs.
