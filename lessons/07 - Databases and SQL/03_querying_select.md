# 7.3 Querying with SELECT

**Objective**: By the end of this module, you will be able to:

* Retrieve data with `SELECT`, choosing columns and filtering rows with `WHERE`.
* Sort, limit, and de-duplicate results with `ORDER BY`, `LIMIT`, and `DISTINCT`.
* Summarize data with aggregate functions and `GROUP BY`.
* Run queries from Python and view the results as a DataFrame.

---

With tables built and populated (Module 7.2), you can ask questions of the data. The `SELECT` statement retrieves rows, and it is the SQL statement you will use most.

## Running Queries in the Notebook

You can run a query with a cursor and read the results with `fetchall()`, which returns a list of tuples:

```python
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name, age FROM Students")
    rows = cursor.fetchall()

for row in rows:
    print(row)      # each row is a tuple, e.g. ('Jasmine', 20)

conn.close()
```

Tuples are awkward to read. For the rest of this module, use a small helper that runs a query and returns its results as a **DataFrame**, which displays as a clean table in the notebook:

```python
import pandas as pd
import sqlite3

def run_query(sql):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(sql, conn)

run_query("SELECT name, age FROM Students")
```

This helper is the notebook-friendly way to explore a database. It uses `pd.read_sql_query`, which Module 7.5 covers in full. (An interactive command-line version, `sqlcommand.py`, is available as an optional extension for those who want to type SQL at a prompt.)

---

## Selecting Columns and Rows

Choose columns by naming them, or use `*` for all columns. Filter rows with a `WHERE` clause:

```sql
SELECT * FROM Students;                                  -- all columns, all rows
SELECT name, major FROM Students;                        -- two columns
SELECT * FROM Students WHERE major = 'History';          -- only history majors
```

`WHERE` supports the comparison operators `=`, `<`, `>`, `<=`, `>=`, and `<>` (not equal), combined with `AND` and `OR`:

```sql
SELECT * FROM Students WHERE age >= 20 AND major = 'Computer Science';
```

For partial text matches, use `LIKE` with `%` as a wildcard:

```sql
SELECT * FROM Courses WHERE course_name LIKE 'Math%';   -- any course starting with "Math"
```

---

## Sorting, Limiting, and Removing Duplicates

* **`ORDER BY`** sorts the results. Add `DESC` for descending order.
* **`LIMIT`** returns only the first N rows.
* **`DISTINCT`** removes duplicate values.

```sql
SELECT * FROM Students ORDER BY age;             -- youngest first
SELECT * FROM Students ORDER BY age DESC LIMIT 3;  -- the three oldest
SELECT DISTINCT major FROM Students;             -- each major once
```

`SELECT DISTINCT major FROM Students` is the SQL equivalent of the `value_counts()` idea from Week 2 — it answers "what values appear in this column?"

---

## Summarizing with Aggregate Functions

**Aggregate functions** compute a single value from many rows:

* `COUNT(*)` — how many rows
* `SUM(column)` — total
* `AVG(column)` — average
* `MIN(column)` / `MAX(column)` — smallest / largest

```sql
SELECT COUNT(*) FROM Students;        -- number of students
SELECT AVG(age) FROM Students;        -- average age
```

## Grouping with GROUP BY

`GROUP BY` applies an aggregate function *within each group*, the same split-apply-combine idea as Pandas' `groupby` from Week 4. For example, to count how many students are in each major:

```sql
SELECT major, COUNT(*) AS student_count
FROM Students
GROUP BY major;
```

This returns one row per major, with the number of students in each. `AS student_count` names the computed column. Reading it aloud: *group the students by major, then count the rows in each group.*

---

### AI Prompt: Predict-then-Check

`GROUP BY` changes what a query returns. Study this without running it, for a `Students` table where three students major in Biology and one majors in History:

```sql
SELECT major, COUNT(*) AS student_count
FROM Students
GROUP BY major;
```

1. Predict how many rows the result has, and what the `student_count` is for each major.
2. Explain to an AI chatbot how `GROUP BY` decides how many rows to return.
3. Ask: "Is my understanding of how `GROUP BY` and `COUNT(*)` work together correct?"

> **Example prompt:** "Looking at this SQL: [paste query], for a table where three students major in Biology and one in History. I predict the result has [your prediction] rows because [your reasoning]. Am I right about how GROUP BY groups the rows before counting?"

---

## Videos

* [Python SQLite Tutorial: Complete Overview](https://www.youtube.com/watch?v=pd-0G0MigUA) — Corey Schafer's `sqlite3` walkthrough also covers running `SELECT` queries.

> For interactive `SELECT` practice, the [SQLBolt](https://sqlbolt.com/) tutorial (linked in Module 7.1) is strongly recommended.

---

## Check for Understanding

**1. Which query returns only the `name` and `major` columns for students older than 21?**

* A) `SELECT * FROM Students;`
* B) `SELECT name, major FROM Students WHERE age > 21;`
* C) `SELECT age FROM Students WHERE name, major;`
* D) `SELECT name, major FROM Students LIMIT 21;`

<details>
<summary>Answer</summary>

B) Name the columns after `SELECT`, and filter rows with `WHERE age > 21`.

</details>

**2. What does `SELECT DISTINCT major FROM Students` return?**

* A) The number of students
* B) Each distinct major, listed once
* C) All students sorted by major
* D) The most common major

<details>
<summary>Answer</summary>

B) `DISTINCT` removes duplicates, so you get each major that appears, one time each.

</details>

**3. What does `GROUP BY major` do in a query that also uses `COUNT(*)`?**

* A) Sorts the students by major
* B) Groups the rows by major and counts the rows within each group, returning one row per major
* C) Deletes duplicate majors
* D) Selects only the first student in each major

<details>
<summary>Answer</summary>

B) `GROUP BY` forms one group per major, and `COUNT(*)` counts the rows in each — one result row per major.

</details>

---

## Further Reading

* [SQLite: SELECT](https://www.sqlite.org/lang_select.html)
* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/default.asp) — a broad reference for `SELECT`, `WHERE`, `ORDER BY`, and aggregates.
