# Lesson 7 — Databases and SQL

**Lesson Overview**

You have stored data in CSV files and, briefly, in a SQLite file at the end of Week 6. This week you learn what a database really is and how to work with one. A **relational database** stores structured, interrelated data across linked tables, enforces rules that keep the data consistent, and lets you query it precisely with **SQL**. You will start with the concepts: tables, keys, associations, constraints, and transactions. Then you'll build a database in code, query it, join tables, modify data, and finally connect SQL to Pandas so that the database becomes a source for your analysis. By the end you can create a database, populate it, and pull exactly the data you need into a DataFrame.

This week's work happens in **Kaggle notebooks**, using Python's built-in `sqlite3` module. Your assignment is submitted as a Kaggle notebook.

**Learning Objectives**

This week, I can...

* Explain tables, primary and foreign keys, associations, constraints, and transactions.
* Create and populate a SQLite database with `sqlite3`, using parameterized statements.
* Query data with `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, and joins.
* Modify data with `UPDATE` and `DELETE`, and move data between SQL and Pandas.

## Topics

1. **[Relational Thinking](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/07%20-%20Databases%20and%20SQL/01_relational_thinking.md)**

   Why a relational database beats a folder of CSV files: tables, primary and foreign keys, one-to-many and many-to-many associations, constraints, and transactions.

2. **[Creating and Populating a Database](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/07%20-%20Databases%20and%20SQL/02_creating_populating_databases.md)**

   Connecting with `sqlite3`, defining tables and constraints with `CREATE TABLE`, and inserting data with parameterized statements and foreign keys.

3. **[Querying with SELECT](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/07%20-%20Databases%20and%20SQL/03_querying_select.md)**

   Retrieving and filtering data with `SELECT` and `WHERE`, sorting and limiting results, and summarizing with aggregate functions and `GROUP BY`.

4. **[Joins, Updates, and Deletes](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/07%20-%20Databases%20and%20SQL/04_joins_updates_deletes.md)**

   Combining tables with `INNER JOIN` and `LEFT JOIN`, and changing data with `UPDATE` and `DELETE` — including the danger of a missing `WHERE` clause.

5. **[SQL and Pandas Together](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/07%20-%20Databases%20and%20SQL/05_sql_and_pandas.md)**

   Loading query results into a DataFrame with `pd.read_sql_query`, writing a DataFrame to a table with `df.to_sql`, and deciding what work belongs in SQL versus Pandas.

## Summary

This week added the database to your toolkit. You learned what a relational database is and why its structure — tables, keys, associations, and constraints — keeps data organized and reliable, and how transactions protect it during changes. You built a database with `sqlite3`, defined tables with constraints, and inserted data using parameterized statements. You queried that data with `SELECT`, `WHERE`, `ORDER BY`, and `GROUP BY`, combined tables with joins, and modified data with `UPDATE` and `DELETE`. Finally, you connected SQL to Pandas, using SQL to narrow the data and Pandas to analyze it.

Several ideas from earlier weeks reappeared in SQL form: a `JOIN` is the database version of Week 4's `merge`, `GROUP BY` mirrors Pandas' `groupby`, and constraints enforce automatically the kind of validation you did by hand in Week 3. Next week continues with more advanced SQL — deeper aggregation, subqueries, window functions — and introduces SQLAlchemy, a higher-level way to connect to databases. Week 8 also includes a milestone for your final project.
