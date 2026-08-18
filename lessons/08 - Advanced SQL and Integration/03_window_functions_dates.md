# 8.3 Window Functions and Dates

**Objective**: By the end of this module, you will be able to:

* Explain how a window function differs from `GROUP BY`.
* Rank rows within groups using `RANK`, `ROW_NUMBER`, and `PARTITION BY`.
* Compute a running total with `SUM() OVER`.
* Work with dates using SQLite's date and time functions.

---

This module covers two features that show SQL can do more analysis than you might expect: **window functions** and **date functions**. Both are useful for the final project, and both continue with the `company.db` database from Module 8.1.

## Window Functions vs. GROUP BY

`GROUP BY` collapses many rows into one row per group — you lose the individual rows. A **window function** computes a value across a related set of rows but *keeps every row*, adding the result as a new column. When you want per-row detail *and* a group-level calculation side by side, a window function is the tool.

A window function uses an `OVER` clause. Inside it, `PARTITION BY` divides the rows into groups (like `GROUP BY`, but without collapsing them), and `ORDER BY` orders the rows within each group.

## Ranking Rows

`RANK()` numbers rows within each partition according to an ordering. To rank employees by salary within their department:

```sql
SELECT first_name, last_name, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM Employees;
```

Every employee row remains, now with a `salary_rank` showing their standing *within their department*. In Engineering, Bob and Carol both earn 135,000, so both receive rank 1, and the next employee receives rank 3 (`RANK` skips after a tie).

Two related functions differ in how they handle ties:

* **`ROW_NUMBER()`** always gives a unique sequential number, even to tied rows (1, 2, 3, 4).
* **`RANK()`** gives tied rows the same rank, then skips (1, 1, 3, 4).
* **`DENSE_RANK()`** gives tied rows the same rank without skipping (1, 1, 2, 3).

## Running Totals

Adding `ORDER BY` inside `OVER` (without `PARTITION BY`) produces a **running total** — a cumulative sum that grows row by row. Ordering employees by hire date shows cumulative salary committed over time:

```sql
SELECT first_name, last_name, hire_date, salary,
       SUM(salary) OVER (ORDER BY hire_date) AS cumulative_salary
FROM Employees;
```

Each row's `cumulative_salary` is the sum of that row's salary and all earlier ones. Add `PARTITION BY department_id` to restart the running total within each department.

---

## Date and Time Functions

Dates in SQLite are stored as text (like `"2019-05-01"`), and SQLite provides functions to work with them.

`date('now')` returns today's date. `JULIANDAY()` converts a date to a number of days, which lets you subtract two dates to get a duration — for example, each employee's tenure:

```sql
SELECT first_name, last_name, hire_date,
       ROUND(JULIANDAY('now') - JULIANDAY(hire_date), 2) AS tenure_in_days
FROM Employees;
```

`strftime()` extracts or formats parts of a date. To get just the hire *year*:

```sql
SELECT first_name, last_name,
       strftime('%Y', hire_date) AS hire_year
FROM Employees;
```

`strftime('%Y', ...)` returns the four-digit year, `'%m'` the month, and `'%d'` the day. These are useful for grouping by year or month — for example, counting how many employees were hired each year:

```sql
SELECT strftime('%Y', hire_date) AS hire_year, COUNT(*) AS hires
FROM Employees
GROUP BY hire_year
ORDER BY hire_year;
```

---

### AI Prompt: Predict-then-Check

Window functions keep rows that `GROUP BY` would collapse. Study this without running it:

```sql
SELECT first_name, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM Employees;
```

1. Predict how many rows this returns compared with `SELECT department_id, MAX(salary) FROM Employees GROUP BY department_id`.
2. Explain to an AI chatbot why the window-function version keeps every employee row while the `GROUP BY` version does not.
3. Ask: "Is my understanding of how a window function differs from `GROUP BY` correct?"

> **Example prompt:** "Looking at this SQL: [paste query]. I predict it returns [your prediction] rows, unlike a `GROUP BY` version, because [your reasoning]. Am I right about how window functions keep individual rows?"

---

## Videos

* ["SQL Window Functions," Maven Analytics](https://youtu.be/rIcB4zMYMas?si=_LPHtrgzFiBZmUkT)
* Date Functions segment of ["Learn 12 Advanced SQL Functions in 20 minutes," Maven Analytics](https://youtu.be/-u-kCJmJHCk?si=13gau3NrnTiwIfZT&t=673) (Start at 11:13)

---

## Check for Understanding

**1. How does a window function differ from `GROUP BY`?**

* A) It is faster
* B) It computes a group-level value but keeps every individual row, rather than collapsing rows into one per group
* C) It only works on numbers
* D) There is no difference

<details>
<summary>Answer</summary>

B) `GROUP BY` returns one row per group; a window function adds a computed column while keeping all the original rows.

</details>

**2. In `RANK() OVER (PARTITION BY department_id ORDER BY salary DESC)`, what does `PARTITION BY` do?**

* A) Sorts the whole table
* B) Divides the rows into groups by department, so the ranking restarts within each department
* C) Deletes duplicate departments
* D) Limits the results to one department

<details>
<summary>Answer</summary>

B) `PARTITION BY` groups the rows for the window calculation — here, the salary ranking is computed separately within each department.

</details>

**3. Which expression gives the number of days between an employee's hire date and today?**

* A) `hire_date - 'now'`
* B) `JULIANDAY('now') - JULIANDAY(hire_date)`
* C) `strftime(hire_date)`
* D) `date(hire_date, 'now')`

<details>
<summary>Answer</summary>

B) `JULIANDAY()` converts each date to a day number, so subtracting them gives the number of days between them.

</details>

---

## Further Reading

* [SQLite: Window functions](https://www.sqlite.org/windowfunctions.html)
* [SQLite: Date and time functions](https://www.sqlite.org/lang_datefunc.html)
