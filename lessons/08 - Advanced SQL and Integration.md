# Lesson 8 — Advanced SQL and Integration

**Lesson Overview**

Week 7 covered the fundamentals of databases and SQL. This week goes deeper into the analytical side of SQL and into how databases fit into a data project. You will write more capable queries and use SQLite's date functions for time-based analysis. You will then connect databases to Python with **SQLAlchemy**, the standard library for database access, and finish with the practices that make queries safe and reliable: parameterized queries that prevent SQL injection, transactions, and indexing. By the end you can answer detailed analytical questions in SQL and integrate a database into a Pandas workflow.

This week's work happens in **Kaggle notebooks**. You have two submissions this week: the Kaggle assignment and a milestone for your final project. The project milestone instructions are on this week's assignment page.

**Learning Objectives**

This week, I can...

* Aggregate across joins and filter groups with `HAVING`.
* Write subqueries and self-joins, and use window functions and date functions.
* Connect to a database with SQLAlchemy and read and write through an engine.
* Prevent SQL injection with parameterized queries, and use transactions and indexes.

## Topics

1. **[Aggregation in Depth](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/08%20-%20Advanced%20SQL%20and%20Integration/01_aggregation_in_depth.md)**

   Grouping by several columns, aggregating across a join to show readable names, and filtering groups with `HAVING` versus `WHERE`.

2. **[Subqueries and Complex Joins](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/08%20-%20Advanced%20SQL%20and%20Integration/02_subqueries_complex_joins.md)**

   Subqueries in `WHERE` and `FROM`, correlated subqueries, and joining a table to itself with a self-join.

3. **[Window Functions and Dates](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/08%20-%20Advanced%20SQL%20and%20Integration/03_window_functions_dates.md)**

   Ranking and running totals with window functions and `PARTITION BY`, and working with dates using SQLite's date and time functions.

4. **[Connecting with SQLAlchemy](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/08%20-%20Advanced%20SQL%20and%20Integration/04_sqlalchemy.md)**

   Creating an engine with `create_engine`, reading and writing through it with Pandas, the difference between `connect()` and `begin()`, and a look at the ORM.

5. **[Safe and Reliable Queries](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/08%20-%20Advanced%20SQL%20and%20Integration/05_safe_queries.md)**

   Preventing SQL injection with parameterized queries (in both `sqlite3` and SQLAlchemy), using transactions and rollbacks, and adding indexes.

## Summary

This week extended your SQL from basic queries to real analysis. You can aggregate across joins and filter the results with `HAVING`, write subqueries and correlated subqueries, join a table to itself, and use window functions to rank rows and compute running totals without collapsing them. You can work with dates for time-based analysis. You also learned to connect databases through SQLAlchemy, which uses one consistent approach for every database system, and to write queries that are safe against injection and reliable through transactions and indexing.

A few threads came together here. The parameterized `?` placeholders you have used since Week 7 were explained: they prevent SQL injection, and the same care is needed in SQLAlchemy, which is not automatically safe. Transactions, introduced as a concept in Week 7, became practical code. And `read_sql_query` and `to_sql` from Week 7 now work through an engine as well as a raw connection. With two weeks of databases complete, you have the tools to store, query, and analyze data at scale — which is why this week includes a milestone that puts your final-project data into a database and runs analytical queries against it.
