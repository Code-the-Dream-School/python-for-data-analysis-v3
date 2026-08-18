# 8.1 Aggregation in Depth

**Objective**: By the end of this module, you will be able to:

* Group by more than one column.
* Aggregate across a join and show readable names instead of IDs.
* Filter groups with `HAVING`, and explain how it differs from `WHERE`.

---

Week 7 introduced `GROUP BY` with a single aggregate. This week goes further into the analytical side of SQL, covering skills that let you answer real questions about data. All of this week's examples use one **company database**, which you build once with the setup below.

## Setup: the Company Database

Run this in a cell to create `company.db` in the notebook's working directory. It has a `Departments` table and an `Employees` table, and every department has a manager. The other modules this week reuse this database.

```python
import sqlite3
import os

DB_PATH = "company.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)      # start fresh so results are predictable

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON;")

conn.executescript("""
CREATE TABLE Departments (
  department_id   INTEGER PRIMARY KEY,
  department_name TEXT NOT NULL UNIQUE,
  manager_id      INTEGER
);
CREATE TABLE Employees (
  employee_id   INTEGER PRIMARY KEY,
  first_name    TEXT NOT NULL,
  last_name     TEXT NOT NULL,
  department_id INTEGER NOT NULL,
  title         TEXT NOT NULL,
  salary        INTEGER NOT NULL,
  hire_date     TEXT,
  FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
""")

conn.executemany(
    "INSERT INTO Departments(department_id, department_name) VALUES (?, ?);",
    [(10, "Engineering"), (20, "Sales"), (30, "HR"), (40, "Finance"), (50, "R&D")],
)

employees = [
    (1,  "Alice", "Nguyen",   10, "Software Engineer",        120000, "2019-05-01"),
    (2,  "Bob",   "Smith",    10, "Senior Software Engineer", 135000, "2018-07-15"),
    (3,  "Carol", "Zhang",    10, "Staff Engineer",           135000, "2017-03-20"),
    (4,  "David", "Lee",      10, "QA Engineer",               95000, "2021-11-02"),
    (5,  "Eve",   "Martinez", 20, "Sales Associate",           90000, "2020-01-10"),
    (6,  "Frank", "O'Connor", 20, "Account Executive",        110000, "2016-09-29"),
    (7,  "Grace", "Kim",      20, "Sales Manager",            105000, "2015-04-12"),
    (8,  "Heidi", "Brown",    30, "HR Generalist",             65000, "2022-06-03"),
    (9,  "Ivan",  "Garcia",   30, "HR Manager",                72000, "2019-08-21"),
    (10, "Judy",  "Wilson",   40, "Financial Analyst",        125000, "2017-02-17"),
    (11, "Karl",  "Davis",    40, "Finance Director",         130000, "2014-12-09"),
    (12, "Liam",  "Patel",    50, "Research Scientist",       150000, "2018-10-31"),
    (13, "Mia",   "Chen",     50, "Principal Scientist",      150000, "2013-05-07"),
]
conn.executemany(
    """INSERT INTO Employees
       (employee_id, first_name, last_name, department_id, title, salary, hire_date)
       VALUES (?, ?, ?, ?, ?, ?, ?);""",
    employees,
)

conn.executemany(
    "UPDATE Departments SET manager_id = ? WHERE department_id = ?;",
    [(2, 10), (7, 20), (9, 30), (11, 40), (13, 50)],
)

conn.commit()
conn.close()
print("company.db created.")
```

A small helper for viewing query results as a DataFrame, as in Week 7:

```python
import pandas as pd

def run_query(sql):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(sql, conn)
```

---

## Grouping by Several Columns

`GROUP BY` accepts more than one column, forming one group per *combination*. To see the number of employees and their average salary for each department-and-title pairing:

```sql
SELECT department_id, title, COUNT(*) AS num, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department_id, title;
```

This returns one row for each distinct `(department_id, title)` combination — the same idea as grouping by multiple columns in Pandas (Week 4).

---

## Aggregating Across a Join: Readable Names Instead of IDs

Grouping by `department_id` gives results labeled `10`, `20`, `30` — not helpful to a reader. Join to `Departments` so the output shows the department *name*:

```sql
SELECT d.department_name AS department,
       MIN(e.salary) AS min_salary,
       MAX(e.salary) AS max_salary,
       COUNT(e.employee_id) AS num_employees
FROM Employees AS e
JOIN Departments AS d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name
ORDER BY d.department_name;
```

Aggregating across a join is a common pattern: the numbers come from one table, and the readable labels come from another.

---

## Filtering Groups with HAVING

`WHERE` filters *rows*, and it runs *before* grouping. `HAVING` filters *groups*, and it runs *after* the aggregate is computed. When your filter is about an aggregate value, you must use `HAVING`.

To list only departments whose average salary is above 70,000:

```sql
SELECT d.department_name,
       AVG(e.salary) AS avg_salary
FROM Departments AS d
JOIN Employees AS e ON d.department_id = e.department_id
GROUP BY d.department_id
HAVING AVG(e.salary) > 70000;
```

In the company data this excludes HR, whose average (68,500) falls below the cutoff; every other department remains. You could not write this with `WHERE AVG(salary) > 70000`, because the average does not exist until the groups are formed. A useful way to remember the order:

* **`WHERE`** filters individual rows *before* they are grouped.
* **`HAVING`** filters groups *after* the aggregate is calculated.

---

### AI Prompt: Predict-then-Check

The difference between `WHERE` and `HAVING` follows from the order SQL runs its steps. Study this without running it:

```sql
SELECT department_id, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department_id
HAVING AVG(salary) > 70000;
```

1. Predict which departments this returns, and how it differs from a query using `WHERE salary > 70000`.
2. Explain to an AI chatbot why `HAVING` is required here rather than `WHERE`.
3. Ask: "Is my understanding of the execution order — that aggregation happens before `HAVING` but after `WHERE` — correct?"

> **Example prompt:** "Looking at this SQL: [paste code]. I predict it returns [your prediction], and it differs from `WHERE salary > 70000` because [your reasoning]. Am I right about why `HAVING` is needed to filter on an aggregate?"

---

## Videos

* ["Basic Aggregate Functions in SQL (COUNT, SUM, AVG, MAX, and MIN)", Becoming a Data Scientist](https://youtu.be/jcoJuc5e3RE?si=trqhNXIGoMZ5hFtL)
* ["Advanced Aggregate Functions in SQL (GROUP BY, HAVING vs. WHERE)", Becoming a Data Scientist](https://youtu.be/nNrgRVIzeHg?si=nwgbsAwhdRHOuZKI)
---

## Check for Understanding

**1. You want only the groups whose average salary exceeds 100,000. Which clause filters on that average?**

* A) `WHERE AVG(salary) > 100000`
* B) `HAVING AVG(salary) > 100000`
* C) `ORDER BY AVG(salary)`
* D) `GROUP BY AVG(salary)`

<details>
<summary>Answer</summary>

B) `HAVING` filters groups after the aggregate is computed. `WHERE` cannot reference an aggregate, because it runs before grouping.

</details>

**2. Why join `Employees` to `Departments` in an aggregation query?**

* A) It is required for `GROUP BY` to work
* B) So the results can show the department name instead of just its numeric ID
* C) To make the query run faster
* D) To remove duplicate departments

<details>
<summary>Answer</summary>

B) The counts and averages come from `Employees`, but the readable department name comes from `Departments` — so you join to label the groups.

</details>

**3. What does `GROUP BY department_id, title` produce?**

* A) One row per department
* B) One row per title
* C) One row per distinct combination of department and title
* D) An error

<details>
<summary>Answer</summary>

C) Grouping by two columns forms one group for each distinct combination of the two values.

</details>

---

## Further Reading

* [SQLBolt: Filtering grouped rows with HAVING](https://sqlbolt.com/lesson/select_queries_with_aggregates_pt_2)
* [SQLite: Aggregate functions](https://www.sqlite.org/lang_aggfunc.html)
