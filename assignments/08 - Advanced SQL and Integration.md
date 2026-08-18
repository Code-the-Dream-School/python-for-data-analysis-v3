## Lesson 8 Assignment — Advanced SQL and Integration

This week has **two submissions**:

- **Part A — Advanced SQL Practice:** a Kaggle notebook of advanced queries against the company database.
- **Part B — Final Project Milestone:** a Kaggle notebook that loads your project dataset into SQLite and runs analytical queries against it.

You will submit two Kaggle links.

---

# Part A — Advanced SQL Practice

Create a Kaggle notebook named `CTD_Assignment_8`. In your first cells, **copy the `company.db` setup and the `run_query` helper from Module 8.1** so the database exists in your notebook. Label each task with a markdown cell.

### **Task 1: Aggregation with a Join and HAVING**

Write one query that returns, for each department, the **department name**, the **number of employees**, and the **average salary** — including only departments whose average salary is above 100,000. (Join `Employees` to `Departments` for the name, `GROUP BY` the department, and filter with `HAVING`.) Display the result.

### **Task 2: A Subquery and a Self-Join**

1. Using a **correlated subquery**, list the highest-paid employee (or employees, in case of a tie) in each department: show the department, the employee name, and the salary.
2. Using a **self-join**, list each employee alongside the name of their department's manager.

### **Task 3: Window Functions and Dates**

1. Using a **window function**, write a query that returns each employee's name, department, salary, and their salary **rank within their department**.
2. Using SQLite **date functions**, add a column that gives each employee's tenure (for example, `tenure_in_days` from `hire_date` to today).

### **Task 4: A Transaction and a Parameterized Query**

1. In a **single transaction**, insert a new department named `'Legal'` and two employees in it, using **parameterized statements** (`?` placeholders). Commit on success, and roll back if an error occurs.
2. Write a **parameterized** `SELECT` that returns the employees in a department, where the department id comes from a Python variable and is passed as a bound parameter (not with an f-string).

### **Task 5: Connect with SQLAlchemy**

1. Create a SQLAlchemy **engine** for `company.db` with `create_engine`.
2. Use `pd.read_sql_query` **through the engine** to load your Task 1 department summary into a DataFrame, and print it.
3. Use `df.to_sql` **through the engine** to write that summary DataFrame to a new table called `department_summary`. Confirm the table was created.

---

<!-- ===== NEW MATERIAL (v3) — begin: Part B, Week 8 project milestone ===== -->
> **🆕 NEW in v3** — *Part B is the Week 8 project milestone from the porting notes, replacing v2's web-scraping capstone increment. It puts the student's own project dataset into SQLite and runs analytical queries — results that feed the Week 10 analysis. Please review, and confirm the "CIL" term used for dataset approval, as in Weeks 5–6.*

# Part B — Final Project Milestone: Data in SQLite

This milestone moves your final project forward. Using the dataset from your Week 5 proposal, you will load it into a SQLite database and run analytical queries against it — the same techniques from this week, applied to your own data. The results feed directly into your Week 10 analysis.

In a Kaggle notebook (you may use your project's Phase 1 notebook, or a new one):

1. **Load your dataset** with `Add Input`, and read it into a DataFrame.
2. **Do initial cleaning** using the Week 3 tools — handle missing values, fix types, and remove obvious problems. This does not need to be the final, complete cleaning, but the data should be usable.
3. **Write the cleaned data to a SQLite table** with `df.to_sql`.
4. **Run at least three analytical queries** against the table, and print each result. Include, at minimum:
   - a grouped aggregate that uses `HAVING`, and
   - a query that uses a **window function**.
5. **Add a short markdown note** after each query explaining what it shows about your data.

Keep these queries — they are a first pass at the analysis you will develop in Week 10.

---

## Submit Your Work

You submit **two Kaggle links** this week:

1. **Part A:** Save Version on your `CTD_Assignment_8` notebook, then **Share → Public** with **Allow Comments** on, and copy the URL. Paste the link into **URL1** on your assignment submission form.
2. **Part B:** the URL of your project-milestone notebook, shared the same way. Paste the link into **URL2** on your assignment submission form.

---
