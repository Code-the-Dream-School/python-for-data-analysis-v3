## Lesson 3 Assignment — Data Cleaning and Validation

### **Objective:**
In this assignment, you will gain hands-on experience cleaning and validating a real-world dataset with Pandas: handling missing values, correcting data types, parsing messy dates, validating ranges, removing duplicates and outliers, standardizing inconsistent text, and using regular expressions. The guided tasks build the individual skills; the closing mini-project asks you to put them together on a single messy dataset and document your decisions.

### **Setup**

Do this assignment in a **Kaggle notebook** (the same environment as Week 2).

1. Create a new Kaggle notebook and name it `CTD_Assignment_3`.
2. **Label each task with a markdown cell.** Before each task's code, add a markdown cell that says which task it is (for example, `Task 1`). This is how you communicate with your reviewer, Jupyter-notebook style. If you choose to use markdown formatting, note that level-two headings (lines starting with `## `) are added automatically to the notebook's table of contents, which makes your work easy to navigate.
3. Put each task's code in its own code cell (or a few cells), and run each cell as you go to make sure it works.
4. After each step, **print the result** so your reviewer can see what happened. A mentor reads your notebook, so keep your output clear and clearly labeled.
5. You only need to import Pandas (and NumPy) once, at the top of the notebook:

   ```python
   import pandas as pd
   import numpy as np
   ```

---

### **Tasks:**

### **Task 1: Handling Missing Data**

1. **Load the provided dataset:**
   - Add the **Code the Dream Assignment 3** dataset with **Add Input**, and read its `employees.csv` file into a DataFrame called `df`. Print it.
   - The DataFrame has columns `Name`, `Age`, `Salary`, `Join Date`, and `City`, with some missing values.

   Here's roughly what the data looks like (for reference — don't paste this in):

   ```python
   data = {
       'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
       'Age': [25, None, 35, 40, 30],
       'Salary': [50000, 60000, None, 80000, 55000],
       'Join Date': ['2020-01-01', None, '2020-03-15', '2020-04-20', None],
       'City': ['New York', 'Los Angeles', 'Chicago', None, 'Miami']
   }
   ```

2. **Explore and fill the missing values:**
   - Create `df1` by calling `dropna()` on `df`. Run `info()` on both `df` and `df1` to compare how many rows have missing values. (Note: `info()` prints on its own — don't wrap it in `print()`, it returns `None`.)
   - Now use `fillna()` on `df` to replace missing values:
     - `Name` → `'Unknown'`
     - `Age` → the **mean** of the `Age` column
     - `Salary` → the **median** of the `Salary` column
     - `Join Date` → `'2020-01-01'`
   - Then use `dropna()` to remove any rows still missing values, and save the result as `df2`. Only `City` should still have missing values at this point. Reset the index.
   - Convert the `Age` column in `df2` to **integer** type with `astype(int)`.
   - Print `df2`.

### **Task 2: Data Types and Dates**

1. **Parse a messy date column:**
   - From the same **Code the Dream Assignment 3** dataset, read the `eclipses.csv` file — a list of eclipses observed in Arkansas — into a DataFrame called `df3`. **Note:** the separator for this file is `|`, so use `sep='|'`.
   - Run `df3.info()` and show the first 5 rows.
   - Try converting the `Date` column with `pd.to_datetime()` — you'll see Pandas raise an error on an invalid date.
   - Add `errors='coerce'` and try again. Print the first 20 rows and look at what's stored for the dates that couldn't be converted (they become `NaT`).

### **Task 3: Validating Data Ranges**

1. **Ensure `Age` values fall within a valid range (18 to 65):**
   - In `df2`, replace ages below 18 or above 65 with `np.nan`. (Use `np.nan` — *not* the string `'NaN'`.)
   - Print the updated DataFrame.
   - Fill the resulting `NaN` values with the **median** of the `Age` column and print again.

### **Task 4: Removing Duplicates & Outliers**

1. **Find and remove duplicate rows (use `df3`):**
   - Run `df3.info()`.
   - Use `duplicated()` to flag duplicate rows, saving the result in `duplicate_series` (it's `True` for each repeated row).
   - Print `df3[duplicate_series == True].head(10)` to see the first 10 duplicates, and `duplicate_series.value_counts()` to count them.
   - Remove duplicates with `drop_duplicates()` and run `info()` again. (By default the first occurrence is kept, which is fine here.)

2. **Handle outliers in `Age` (use `df2`):**
   - Treat values greater than 100 or less than 0 as outliers.
   - Replace them with the **median** of the `Age` column and print the result. (We're using fixed thresholds here rather than a statistical rule.)

### **Task 5: Standardizing Text**

1. **Standardize the `Name` column:**
   - Convert all names to lowercase and trim whitespace with `.str.lower()` and `.str.strip()`. Print the result.

2. **Standardize inconsistent `City` values:**
   - Inspect the variations first:
     ```python
     print(df['City'].value_counts())   # shows all city spellings, so you can spot variations
     ```
   - Replace variations like `'NYC'` → `'New York'` and `'LA'` → `'Los Angeles'`. Print the result.

### **Task 6: Regular Expressions**

Run these examples to see more of what regex can do with `.str` (this reinforces Week 1 and Module 3.4):

1. **Extract log fields:**
   ```python
   log_entries = pd.Series([
       "[2023-10-26 10:00:00] INFO: User logged in",
       "[2023-10-26 10:05:30] WARNING: Invalid input",
       "[2023-10-26 10:10:15] ERROR: Database connection failed"
   ])
   extracted_logs = log_entries.str.extract(r"\[(.*?)\]\s(\w+):\s(.*)")
   ```

2. **Standardize placeholders:**
   ```python
   text_data = pd.Series([
       "Value is {amount}.",
       "The price is [value].",
       "Cost: (number)",
       "Quantity = <qty>"
   ])
   standardized_text = text_data.replace(
       [r"\{.*?\}", r"\[.*?\]", r"\(.*?\)", r"\<.*?\>"],
       "<VALUE>",
       regex=True,
   )
   ```

3. **Select columns ending in `_at`:**
   ```python
   df_times = pd.DataFrame({
       "order_id": [1, 2],
       "created_at": ["2021-01-05", "2021-01-06"],
       "updated_at": ["2021-01-07", "2021-01-08"]
   })
   time_cols = df_times.filter(regex="_at$")
   ```

4. **Find shipped orders:**
   ```python
   orders = pd.Series([
       "Order #123 has been shipped on 2021-01-05",
       "Order #124 has been cancelled",
       "Shipment #125 confirmed on 02/06/2021"
   ])
   shipped_orders = orders[orders.str.contains("ship", case=False)]
   ```

### **Task 7: Mini-Project — Clean a Messy Dataset End-to-End**

The tasks above practiced each technique on its own. Now you'll put them together. Below is a small but genuinely messy customer dataset — every column has at least one problem. Your job is to turn it into an analysis-ready DataFrame **and explain what you did and why**, the way a data professional documents their cleaning.

**Start by building the DataFrame** (this simulates a freshly loaded CSV where everything came in as text):

```python
messy = {
    'customer_id': [101, 102, 103, 103, 104, 105, 106, 107],
    'name':        ['  Alice ', 'BOB', 'charlie', 'charlie', 'Dana', None, 'eve', 'Frank'],
    'age':         ['34', '28', 'unknown', 'unknown', '45', '31', '150', '39'],
    'city':        ['New York', 'new york', 'Chicago', 'Chicago', 'LA', 'Los Angeles', 'chicago ', 'NYC'],
    'signup_date': ['2021-03-15', '03/22/2021', 'March 30, 2021', 'March 30, 2021',
                    'N/A', '2021-04-10', '2021/05/01', 'Feb 30, 2021'],
    'spend':       ['1200.50', '850', '0', '0', '9999999', '430', '620', '-50']
}
customers = pd.DataFrame(messy)
```

**Your steps** (this is less prescriptive than the earlier tasks — you choose the specific methods):

1. **Inspect and diagnose.** Run your first-look routine (`shape`, `head`, `info`, `isna().sum()`). In a **markdown cell**, list every data-quality problem you can spot, column by column.
2. **Keep a raw copy** before you change anything (`raw = customers.copy()`).
3. **Fix types and placeholders.** Convert `age` and `spend` to numeric and `signup_date` to a real datetime, turning placeholders (`'unknown'`, `'N/A'`) and impossible dates (`'Feb 30'`) into proper missing values along the way.
4. **Standardize text.** Clean `name` and `city` so that casing, whitespace, and abbreviations (`'NYC'`, `'LA'`, `'chicago '`) collapse into consistent values. Confirm with `value_counts()`.
5. **Remove duplicates.** The customer with `customer_id` 103 appears twice — decide how to handle it.
6. **Validate and handle outliers.** Ages should be plausible (say, 18–100) and `spend` shouldn't be negative. Decide what to do with the `age` of 150 and the `spend` of 9,999,999 — and say whether you treated each as an error or a real extreme.
7. **Handle remaining missing values**, filling or dropping with a justification for each choice.
8. **Derive a new column.** Add a `spend_band` column (`'Low'` / `'Medium'` / `'High'`) using `.apply()` or `.map()` with a rule of your choosing.
9. **Finish with a short markdown reflection:** what the biggest problems were, which decisions were judgment calls, and how you'd automate this cleaning if the file arrived every week.

Print the cleaned DataFrame and a final `isna().sum()` so your reviewer can see the end state.

> There isn't one "correct" cleaned dataset here — reasonable people would make different calls on the outliers and the missing city. What's being assessed is that your choices are sensible **and clearly explained**.

---

### **Submit Your Assignment**

1. **Save your work.** In the upper right, click **Save Version** and save (a quick save is fine). Make sure the notebook runs top to bottom without errors.
2. **Get a sharing link.** Click **Share**, choose **Public**, make sure **Allow Comments** is on, and copy the public URL.
3. **Submit the link.** Paste the URL into the **assignment submission form**.

---
