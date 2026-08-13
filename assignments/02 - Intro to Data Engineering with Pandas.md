## Lesson 2 Assignment — Intro to Data Engineering with Pandas

**Objective:**
In this assignment, you will explore the core functionality of the Pandas library: creating, loading, inspecting, selecting, and filtering data using DataFrame methods. The goal is to get comfortable moving data into a DataFrame, getting to know it, and pulling out the pieces you need.

## **Step 1: Set Up Your Notebook**

Do this assignment in a **Kaggle notebook** (the environment you set up in Week 1).

1. Create a new Kaggle notebook and name it `CTD_Assignment_2`.
2. **Label each task with a markdown cell.** Before each task's code, add a markdown cell that says which task it is (for example, `Task 1`). This is how you communicate with your reviewer, Jupyter-notebook style. If you choose to use markdown formatting, note that level-two headings (lines starting with `## `) are added automatically to the notebook's table of contents, which makes your work easy to navigate.
3. Put each task's code in its own code cell (or a few cells), and run each cell as you go to make sure it works.
4. After each step, **print the result and check it against what you expect.** Keep your output clear and clearly labeled.
5. You only need to import Pandas once, at the top of the notebook:

   ```python
   import pandas as pd
   ```

> [!note]
> A few tasks write a file (like `employees.csv`) and then read it back. In Kaggle you can write to the notebook's working directory and read it again in a later cell — using a plain filename like `"employees.csv"` works.

---

## **Tasks:**

## **Task 1: Create and Manipulate a DataFrame**

1. **Create a DataFrame from a dictionary:**
   - Use a dictionary with the following data:
     - `Name`: ['Alice', 'Bob', 'Charlie']
     - `Age`: [25, 30, 35]
     - `City`: ['New York', 'Los Angeles', 'Chicago']
   - Convert the dictionary into a DataFrame.
   - Store it in a variable called `task1_data_frame` and print it to verify.

2. **Add a new column:**
   - Make a copy of the DataFrame named `task1_with_salary` (use the `copy()` method).
   - Add a column called `Salary` with values `[70000, 80000, 90000]`.
   - Print the new DataFrame to check your work.

3. **Modify an existing column:**
   - Make a copy of `task1_with_salary` named `task1_older`.
   - Increment the `Age` column by 1 for each entry.
   - Print the modified DataFrame to verify the change.

4. **Save the DataFrame as a CSV file:**
   - Save the `task1_older` DataFrame to a file named `employees.csv` using `to_csv()`. Do **not** include the index in the file.
   - Print the contents of the CSV file (or open it) to see how it's formatted.

## **Task 2: Loading Data from CSV and JSON**

1. **Read data from a CSV file:**
   - Load `employees.csv` from Task 1 into a new DataFrame stored in `task2_employees`.
   - Print it to verify the contents.

2. **Create and read a JSON file:**

   - Create a file called `additional_employees.json` that adds two employees: **Eve** (age 28, Miami, salary 60000) and **Frank** (age 40, Seattle, salary 95000). You can write the file from a cell:

     ```python
     import json

     new_employees = [
         {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
         {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000},
     ]
     with open("additional_employees.json", "w") as f:
         json.dump(new_employees, f)
     ```

   - Load the JSON file into a new DataFrame stored in `json_employees` and print it to verify.

3. **Combine the two DataFrames:**

   - Stack the two DataFrames into one, stored in `more_employees`. `pd.concat` puts the rows of one DataFrame below another; `ignore_index=True` renumbers the combined rows from 0:

     ```python
     more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
     ```

     *(You'll learn more about combining datasets in Week 4 — for now, this one line is all you need.)*
   - Print `more_employees` to verify all five employees are present.

## **Task 3: Inspecting a Dataset**

1. **Preview with `head()`:**
   - Store the first three rows of `more_employees` in `first_three` and print it.

2. **Preview with `tail()`:**
   - Store the last two rows of `more_employees` in `last_two` and print it.

3. **Get the `shape`:**
   - Store the shape of `more_employees` in `employee_shape` and print it.

4. **Summarize with `info()`:**
   - Print a concise summary of `more_employees` with `info()` to see the data types and non-null counts.

5. **Summarize the numbers with `describe()`:**
   - Store the result of `more_employees.describe()` in `summary_stats` and print it. Look at the `Age` and `Salary` statistics — do the min and max look reasonable?

6. **Count categories with `value_counts()`:**
   - Store the result of `value_counts()` on the `City` column in `city_counts` and print it.

## **Task 4: Selecting and Filtering**

Work from the `more_employees` DataFrame.

1. **Select one column:**
   - Store the `Name` column (a Series) in `names_only` and print it.

2. **Select multiple columns:**
   - Store a DataFrame of just the `Name` and `Salary` columns in `name_and_salary` and print it.

3. **Select by label and position:**
   - Use `.loc` to get the value in the row labeled `0`, column `Name`, and store it in `first_name`.
   - Use `.iloc` to get the value in row position `1`, column position `1`, and store it in `second_age`.
   - Print both.

4. **Filter with a condition:**
   - Store the rows where `Salary` is greater than `75000` in `high_earners` and print it.

5. **Filter with two conditions:**
   - Store the rows where `Age` is greater than `30` **and** `Salary` is greater than `75000` in `senior_high_earners` and print it. (Remember to use `&` and wrap each condition in parentheses.)

6. **Count missing values:**
   - Store the per-column missing-value counts of `more_employees` in `missing_counts` using `isna().sum()`, and print it. (This dataset is clean, so you should see `0` for every column — the same check you'll rely on in Week 3, when the data won't be so tidy.)

## **Task 5 (Optional Stretch): Read Data from an API**

> [!note]
> Turn **Internet** on in the notebook settings panel first.

1. Use `requests` to GET `https://jsonplaceholder.typicode.com/users`, then build a DataFrame from the JSON response and store it in `api_users`.
2. Print the `id`, `name`, and `email` columns for the first five users.
3. Try `pd.json_normalize()` on the response and compare — notice the flattened `address.*` columns.

---

## **Step 2: Submit Your Assignment**

1. **Save your work.** In your Kaggle notebook, click **Save Version** (top right) to run the whole notebook top to bottom and save it. Make sure it runs without errors.
2. **Make the notebook shareable.** In the notebook's **Share** settings, set it to "Public."
3. **Submit the link.** Copy your notebook's URL and paste it into the URL1 of the **assignment submission form**.

---
