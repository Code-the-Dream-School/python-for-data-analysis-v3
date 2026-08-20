## Lesson 1 Assignment — Advanced Python and Regex

This week has **two submissions**:

- **Part A — Kaggle Setup Check:** a Kaggle notebook confirming your notebook environment works.
- **Part B — Python Skills:** regex, file paths, and parsing, submitted as a pull request to your `python_homework` repository.

---

### Part A — Kaggle Setup Check

1. If you haven't already, create a free [Kaggle](https://www.kaggle.com) account and **verify your phone number** (in account settings), which enables attaching datasets and internet access.
2. Create a new notebook named `CTD_Assignment_1`.
3. In a code cell, confirm the environment works:

   ```python
   import pandas as pd
   print("Pandas version:", pd.__version__)

   df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
   df
   ```
4. **Save Version** (which runs the notebook top to bottom), then **Share → Public** with **Allow Comments** on, and copy the public URL.

This confirms your Kaggle environment is ready for Week 2.

---

### Part B — Python Skills

Do Part B in your `python_homework` repository. If you haven't created this already, return to [1.1 - Setting Up for Data Work](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/01%20-%20Advanced%20Python%20and%20Regex/01_setting_up.md).

**Setup:**

1. Create an `assignment1` branch.
2. From inside the repository, create and activate a virtual environment and install the requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux  (.venv\Scripts\activate on Windows)
   pip install -r requirements.txt
   ```
3. Do your work in the `assignment1` folder, marking each task with a comment.

#### Task 1: Regular Expressions

Using the `re` module:

1. From the string `"Order 1234 shipped, invoice 56789, ref 42"`, use `re.findall` to extract **all the numbers** as a list.
2. From the phone string `"(212) 555-1234"`, use `re.sub` to remove every non-digit character, leaving just the digits.
3. From the string `"Date: 2021-05-01"`, use a pattern with **capture groups** and `re.search` to extract the year, month, and day separately, and print all three.

#### Task 2: File Paths

Using `pathlib`:

1. Build a path to `data/sales.csv` with the `/` operator, and print its `.name`, `.stem`, `.suffix`, and `.parent`.
2. Create two small text files in a folder (for example, `data/a.txt` and `data/b.txt`), then use `glob` to list every `.txt` file in that folder and print each file's name.

#### Task 3: Parsing Messy Data

You are given records as lines of text, some of them malformed:

```python
raw = """
Alice, 30, New York
Bob, 25, Los Angeles
--- corrupted line ---
Carlos, 41, Chicago
"""
```

1. Using a regular expression, parse each **valid** line into a dictionary with keys `name`, `age` (as an integer), and `city`, and collect them into a list. Skip malformed lines, printing a message for each one you skip.
2. Build a dict comprehension mapping each person's name to their city.
3. Use `sorted` with a **lambda** to produce the records ordered from oldest to youngest.
4. Print your list of records, the name-to-city dictionary, and the sorted records.

---

### Submit Your Work

You submit **two links** this week:

1. **Part A (Kaggle):** the public URL of your `CTD_Assignment_1` notebook.
2. **Part B (pull request):** commit and push your `assignment1` branch, open a pull request, and copy its URL.

Paste both links into the two fields on the **assignment submission form**. Submit your **Kaggle link** in **URL1** and your **GitHub PR** in **URL2**.
