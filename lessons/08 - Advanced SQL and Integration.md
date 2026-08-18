# Lesson 8 — Advanced SQL and Integration

**Lesson Overview**

Week 7 covered the fundamentals of databases and SQL. This week goes deeper into the analytical side of SQL and into how databases fit into a data project. You will write more capable queries — multi-column aggregation with `HAVING`, subqueries, self-joins, and window functions — and use SQLite's date functions for time-based analysis. You will then connect databases to Python with **SQLAlchemy**, the standard library for database access, and finish with the practices that make queries safe and reliable: parameterized queries that prevent SQL injection, transactions, and indexing. By the end you can answer detailed analytical questions in SQL and integrate a database into a Pandas workflow.

This week's work happens in **Kaggle notebooks**. You have two submissions this week: the Kaggle assignment and a milestone for your final project. The project milestone instructions are on this week's assignment page.

**Learning Objectives**

This week, I can...

* Aggregate across joins and filter groups with `HAVING`.
* Write subqueries and self-joins, and use window functions and date functions.
* Connect to a database with SQLAlchemy and read and write through an engine.
* Prevent SQL injection with parameterized queries, and use transactions and indexes.

## Topics

1. **[Aggregation in Depth](<08 - Advanced SQL and Integration/01_aggregation_in_depth.md>)**

   Grouping by several columns, aggregating across a join to show readable names, and filtering groups with `HAVING` versus `WHERE`.

2. **[Subqueries and Complex Joins](<08 - Advanced SQL and Integration/02_subqueries_complex_joins.md>)**

   Subqueries in `WHERE` and `FROM`, correlated subqueries, and joining a table to itself with a self-join.

3. **[Window Functions and Dates](<08 - Advanced SQL and Integration/03_window_functions_dates.md>)**

   Ranking and running totals with window functions and `PARTITION BY`, and working with dates using SQLite's date and time functions.

4. **[Connecting with SQLAlchemy](<08 - Advanced SQL and Integration/04_sqlalchemy.md>)**

   Creating an engine with `create_engine`, reading and writing through it with Pandas, the difference between `connect()` and `begin()`, and a look at the ORM.

5. **[Safe and Reliable Queries](<08 - Advanced SQL and Integration/05_safe_queries.md>)**

   Preventing SQL injection with parameterized queries (in both `sqlite3` and SQLAlchemy), using transactions and rollbacks, and adding indexes.

## Summary

This week extended your SQL from basic queries to real analysis. You can aggregate across joins and filter the results with `HAVING`, write subqueries and correlated subqueries, join a table to itself, and use window functions to rank rows and compute running totals without collapsing them. You can work with dates for time-based analysis. You also learned to connect databases through SQLAlchemy, which uses one consistent approach for every database system, and to write queries that are safe against injection and reliable through transactions and indexing.

A few threads came together here. The parameterized `?` placeholders you have used since Week 7 were explained: they prevent SQL injection, and the same care is needed in SQLAlchemy, which is not automatically safe. Transactions, introduced as a concept in Week 7, became practical code. And `read_sql_query` and `to_sql` from Week 7 now work through an engine as well as a raw connection. With two weeks of databases complete, you have the tools to store, query, and analyze data at scale — which is why this week includes a milestone that puts your final-project data into a database and runs analytical queries against it.

## Check for Understanding

**1. You want the departments whose *average* salary exceeds 90,000. Which clause filters on that average?**

* A) `WHERE avg_salary > 90000`
* B) `HAVING AVG(salary) > 90000`
* C) `ORDER BY AVG(salary)`
* D) `PARTITION BY salary`

<details>
<summary>Answer</summary>

B) `HAVING` filters groups after the aggregate is computed; `WHERE` runs before grouping and cannot reference an aggregate. (Module 8.1.)

</details>

**2. You want each employee's salary rank within their department, while keeping every employee row. Which tool fits?**

* A) `GROUP BY department_id`
* B) A window function: `RANK() OVER (PARTITION BY department_id ORDER BY salary DESC)`
* C) A subquery in `WHERE`
* D) `HAVING`

<details>
<summary>Answer</summary>

B) A window function computes the rank within each department but keeps all the rows, unlike `GROUP BY`. (Module 8.3.)

</details>

**3. Does switching from `sqlite3` to SQLAlchemy make your queries safe from SQL injection automatically?**

* A) Yes, SQLAlchemy is always safe
* B) No — an f-string inside `text()` is just as vulnerable; safety comes from passing values as bound parameters
* C) Only when reading data
* D) Only when using the ORM

<details>
<summary>Answer</summary>

B) SQLAlchemy is not automatically safe. In both libraries, untrusted values must be passed as bound parameters, not built into the SQL text. (Modules 8.4 and 8.5.)

</details>

**4. Why learn SQLAlchemy when raw `sqlite3` still works with Pandas?**

* A) Pandas dropped support for `sqlite3`
* B) SQLAlchemy connects to any database with one consistent approach, so only the connection string changes when a project moves off SQLite
* C) SQLAlchemy is required for `GROUP BY`
* D) `sqlite3` cannot run joins

<details>
<summary>Answer</summary>

B) Pandas still fully supports `sqlite3`. SQLAlchemy's benefit is portability across database systems. (Module 8.4.)

</details>
