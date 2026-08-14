## Lesson 4 Assignment — Data Wrangling and Aggregation with Pandas

### **Objective:**
This assignment deepens your data-wrangling skills: selecting and filtering, aggregating with `groupby`, building pivot tables, applying row-wise logic, merging and joining, engineering new features, and combining messy files. The early tasks are focused drills; the later ones are small integrative projects on real Kaggle datasets.

> [!Note]
> Tasks 3 and 4 are mini-labs on independent Kaggle datasets. Do them together, then resume Task 5. The final tasks (12–14) are integrative mini-projects on real datasets.

### **Setup**

Do this assignment in a **Kaggle notebook** (the same environment as the past two weeks).

1. Create a new Kaggle notebook and name it `CTD_Assignment_4`.
2. **Label each task with a markdown cell.** Before each task's code, add a markdown cell that says which task it is (for example, `Task 1`). This is how you communicate with your reviewer, Jupyter-notebook style. If you use markdown formatting, note that level-two headings (lines starting with `## `) are added automatically to the notebook's table of contents.
3. Put each task's code in its own code cell (or a few cells), and run each cell as you go.
4. **Print your results** so your reviewer can follow along.
5. Import what you need once, at the top:

   ```python
   import pandas as pd
   import numpy as np
   ```

---

### **Tasks:**

### **Task 1: Data Selection**

1. **Create DataFrames `df1`, `df2`, and `df3` from the sample data** (feel free to change the values), and display each:

   ```python
   data1 = {
       'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
       'Age': [25, 30, 35, 40, 30],
       'Salary': [50000, 60000, 70000, 80000, 55000]
   }
   data2 = {
       'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
       'Age': [28, 33, 35, 29, 40],
       'Salary': [52000, 58000, 72000, 61000, 85000]
   }
   data3 = {
       'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
       'Age': [17, 93, 12, 57, 106],
       'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
   }
   ```

2. **Perform these selections on `df1`:**
   - Select the `Name` column and print it.
   - Select both `Name` and `Salary` columns and print the result.
   - Slice the first three rows using `iloc`, and print the result.

### **Task 2: Data Aggregation**

1. **Group `df1` by `Age` and aggregate `Salary`:**
   - Calculate the mean, sum, and count of `Salary` for each age group (use `agg`).
   - Display the aggregated result.

### **Task 3: Practice Pivot Tables**

1. Click **Add Input → Datasets** and search **"Ecommerce Consumer Behavior"** (a dataset from Salahuddin Ahmed). Add it to your notebook.
2. Read the file into a DataFrame called `ecommerce`. Print the first 5 rows to see what the data looks like.
3. The `Purchase_Amount` column is stored as a string (with a dollar sign). Replace it with a numeric version: strip the `$` and convert to `float`.
4. Create a `buying_patterns` pivot table: `index='Purchase_Category'`, `columns=['Gender', 'Income_Level']`, summing `Purchase_Amount`. Print it.
5. Create a `demographics` pivot table: a two-level index on `Income_Level` and `Education_Level`, `columns='Marital_Status'`, counting `Customer_ID`. Print it.

### **Task 4: Practice `apply()`**

1. Add another input by searching **"AI-Powered Job Recommendations"** (a dataset from Samay Ashar).
2. Read the job recommendations file into a DataFrame called `jobs`. Print the first 10 rows so you know the column names.
3. Use `apply()` (with `axis=1`) to add a column `Check These Out` = `"Yes"` if the job is entry level, has a salary ≥ 70000, and requires **both** SQL and Python; `"No"` otherwise.
4. Create `my_jobs` by selecting the rows where `Check These Out` is `"Yes"`. Print the first 10.

### **Task 5: Merging and Joining**

1. **Merge `df1` and `df3` into `df_1_3_merged` on `Name`:**
   - Use an **outer** merge, with `suffixes=['_left', '_right']` to distinguish the overlapping columns.
   - Display the result. (You may see runtime warnings about invalid values — those come from the `NaN`s and are harmless here, so ignore them for now.)
   - The `Salary` column has `NaN` values — replace them with a starting salary of `15000` (`fillna` works on a Series).
   - Replace `NaN` values in `Favorite Color` with `'yellow'`.
   - Build a single `Age` column from `Age_left` and `Age_right`, taking `Age_left` where it isn't `NaN` and `Age_right` otherwise. This is a new technique — here's the tool:
     ```python
     df_1_3_merged['Age'] = np.where(
         df_1_3_merged['Age_left'].notna(),
         df_1_3_merged['Age_left'],
         df_1_3_merged['Age_right']
     )
     # np.where works like a ternary: where the condition is True, take the second value; otherwise the third.
     ```
   - Drop `Age_left` and `Age_right`, and display the result.

2. **Use the `join` method:**
   - Create `df1_b` and `df3_b` from `df1` and `df3`, each with `Name` set as the index.
   - Join them with outer-join logic and display the result. Do **not** use `inplace=True`. Unlike `merge`, `join` doesn't add default suffixes for overlapping columns — check the documentation for how to specify them.

### **Task 6: Filtering Rows**

1. Filter `df1` for rows where `Age` is greater than 30, and display them.

### **Task 7: Sorting Data**

1. Sort `df1` by `Salary` in descending order and display the result.

### **Task 8: Renaming Columns**

1. Rename `df1`'s `Age` to `Employee Age` and `Salary` to `Employee Salary`. Do **not** use `inplace=True` (you'll want the original for the next task). Display the result.

### **Task 9: Transforming a Column**

1. Increase every salary in `df1` by 10% and display the updated DataFrame.

### **Task 10: Concatenating DataFrames**

1. Concatenate `df1` and `df2` to stack `df2`'s rows below `df1`'s. Use `ignore_index=True` to renumber the rows, and display the result.

### **Task 11: Encoding Categorical Variables**

1. Create a small DataFrame with a `Color` column = `['Red', 'Blue', 'Green', 'Blue', 'Red']`.
2. Apply both encodings:
   ```python
   df["Color_Label"] = df["Color"].map({"Red": 1, "Blue": 2, "Green": 3})   # label encoding
   df_encoded = pd.get_dummies(df["Color"], prefix="Color")                 # one-hot encoding
   ```
3. Display both results. (Note: `get_dummies` returns `True`/`False` columns in current Pandas — add `dtype=int` if you'd rather see `1`/`0`.)
4. In a markdown cell, note which of these two encodings would be appropriate for an **unordered** category like color, and why.

### **Task 12: Data Wrangling a Kaggle Dataset (Football)**

For this task, you'll find the international teams that are weakest on defense.

1. Click **Add Input → Datasets** and search **"international football results"** (a dataset from Mart Jürisoo). Add it.
2. Find the CSV path by running the notebook's first cell (the `os.walk('/kaggle/input')` loop it starts with). You want `.../results.csv`. Read it into `football_results` and print the first 5 rows.
3. Every row has a home team and an away team, but we want results *per team* regardless of side. Build that:
   - `results_1`: select `home_team`, `away_team`, `home_score`, `away_score`, `date` from `football_results`. Print the first 5 rows.
   - `results_2` (home perspective): rename `home_team`→`team`, `away_team`→`opponent`, `home_score`→`points_for`, `away_score`→`points_against`. Don't use `inplace=True`.
   - `results_3` (away perspective): rename `away_team`→`team`, `home_team`→`opponent`, `away_score`→`points_for`, `home_score`→`points_against`.
   - Concatenate `results_2` and `results_3` (resetting the index) back into `football_results`. Print the first 5 rows.
4. `groupby('team')` and take the `mean()` of `points_against`. Store the resulting Series in `points_against`.
5. Sort `points_against` in descending order and print the first 10 — the teams that concede the most on average.

### **Task 13: More Football Wrangling**

Starting from the `football_results` DataFrame you built in Task 12, print the most recent 10 games for **Tunisia**. You'll figure out the steps — remember to sort so you get the right games, and prefer creating a new DataFrame over `inplace=True`.

### **Task 14: Consolidating Messy Files (Mini-Project)**

Real data often arrives split across several messy files with duplicate and inconsistent records. Here you'll consolidate four files into one clean table.

1. Add the input dataset **"Code The Dream Assignment 6"** → four CSV files (~400 rows each).
2. Load all four into DataFrames and `concat` them into `df_all` (~1600 rows).
3. Install and import `thefuzz` for approximate string matching:
   ```python
   try:
       from thefuzz import process
   except ImportError:
       !pip install thefuzz
       from thefuzz import process
   ```
4. Fix spelling errors in `Name` (then repeat for `Address`): keep names that appear often, and snap rare misspellings to the closest common name:
   ```python
   df_names = df_all.value_counts("Name")
   good_names = list(df_names[df_names > 2].index)
   df_all["Name"] = df_all["Name"].map(
       lambda x: x if x in good_names else process.extractOne(x, good_names)[0]
   )
   ```
5. Fix `Zip` and `Phone` by taking the most common value per person:
   ```python
   def fix_anomaly(group):
       group_na = group.dropna()
       if group_na.empty:
           return group
       mode = group_na.mode()
       if mode.empty:
           return group
       return mode.iloc[0]

   df_all["Zip"] = df_all.groupby(["Name", "Address"])["Zip"].transform(fix_anomaly)
   df_all["Phone"] = df_all.groupby(["Name", "Address"])["Phone"].transform(fix_anomaly)
   ```
6. Drop duplicates → you should end up with roughly 400 unique records.
7. Run `info()` and note how many nulls remain.

---

### **Submit Your Assignment**

1. **Save your work.** In the upper right, click **Save Version**. Make sure the notebook runs top to bottom without errors.
2. **Get a sharing link.** Click **Share**, choose **Public**, make sure **Allow Comments** is on, and copy the public URL.
3. **Submit the link.** Paste the URL into the **assignment submission form**.

---
