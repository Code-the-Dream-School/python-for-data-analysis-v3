# 7.5 SQL and Pandas Together

**Objective**: By the end of this module, you will be able to:

* Load the result of a SQL query into a DataFrame with `pd.read_sql_query`.
* Write a DataFrame to a database table with `df.to_sql`.
* Decide what work belongs in SQL and what belongs in Pandas.

---

You now have two tools for working with data: SQL, which stores and queries it in a database, and Pandas, which analyzes it in memory. For a data analyst, the most useful skill of the week is combining them — using SQL to pull exactly the data you need, then Pandas to analyze and visualize it.

## From SQL to a DataFrame

`pd.read_sql_query` runs a `SELECT` and returns the result as a DataFrame. This is the same function behind the `run_query` helper from Module 7.3, and it is the bridge from a database into everything you learned in Weeks 2 through 5:

```python
import pandas as pd
import sqlite3

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query("""
        SELECT s.name, c.course_name
        FROM Students s
        JOIN Enrollments e ON s.student_id = e.student_id
        JOIN Courses c ON e.course_id = c.course_id
    """, conn)

conn.close()
```

Once the result is a DataFrame, every Pandas tool applies: inspection, cleaning, grouping, and plotting. A live database is also more current than a static CSV — the file reflects one moment in the past, while a query reads the data as it is now.

## From a DataFrame to SQL

`df.to_sql` does the reverse: it writes a DataFrame into a database table. You used this in Week 6 to save scraped data to a SQLite file. `if_exists='replace'` overwrites the table if it already exists, and `index=False` avoids writing the DataFrame's index as a column:

```python
with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("student_courses", conn, if_exists="replace", index=False)

conn.close()
```

---

## What Belongs in SQL, and What Belongs in Pandas

Because both tools can filter, join, and aggregate, it helps to know which to use for what.

**Use SQL to reduce the data before it reaches Pandas.** Filtering (`WHERE`), joining (`JOIN`), and aggregating (`GROUP BY`) are best done in the database, especially when the tables are large. The database is built to do this efficiently and close to the stored data, and it returns only the rows you asked for. Pulling an entire large table into Pandas just to filter it wastes memory and time.

**Use Pandas for flexible analysis once the data is in memory.** The exploratory work, custom transformations, statistical summaries, and visualizations from Weeks 3 through 5 are Pandas' strength.

A common and effective workflow follows from this:

1. Write a SQL query that selects, joins, and aggregates down to the data you actually need.
2. Load that result into a DataFrame with `pd.read_sql_query`.
3. Analyze and visualize it in Pandas.

The guiding idea: **let the database narrow the data, then let Pandas analyze it.**

---

### AI Prompt: Retrieval Practice

Deciding where work should happen is a judgment worth practicing.

1. Open your preferred AI chatbot.
2. Explain, in your own words, why it is often better to filter and aggregate a large table in SQL before loading it into Pandas, rather than loading the whole table and doing everything in Pandas.
3. Give an example of a task better suited to Pandas than to SQL.
4. Ask the AI for feedback on your reasoning.

> **Example prompt:** "I'm learning to combine SQL and Pandas. Here is my explanation of why I would filter and aggregate in SQL before loading into Pandas, and an example of something better done in Pandas: [your explanation]. Is my reasoning about the division of labor sound?"

---

## Videos

* [Python Pandas Tutorial (Part 11): Reading/Writing Data to Different Sources — Excel, JSON, SQL, Etc](https://www.youtube.com/watch?v=N6hyN6BW6ao) — Corey Schafer, including reading from and writing to SQL databases with Pandas.

---

## Check for Understanding

**1. Which function loads the result of a SQL query into a DataFrame?**

* A) `df.to_sql()`
* B) `pd.read_sql_query()`
* C) `pd.read_csv()`
* D) `cursor.fetchall()`

<details>
<summary>Answer</summary>

B) `pd.read_sql_query(sql, conn)` runs the query and returns the result as a DataFrame. (`df.to_sql()` does the reverse.)

</details>

**2. You have a database with a very large `orders` table and want to analyze last month's orders in Pandas. What is the better approach?**

* A) Load the entire `orders` table into Pandas, then filter to last month
* B) Use SQL to select only last month's orders, then load that result into Pandas
* C) Export the whole table to CSV first
* D) It makes no difference

<details>
<summary>Answer</summary>

B) Filter in SQL so only the rows you need come into memory. Loading the whole table just to filter it wastes memory and time.

</details>

**3. What does `df.to_sql("results", conn, if_exists="replace", index=False)` do?**

* A) Reads the `results` table into a DataFrame
* B) Writes the DataFrame to a `results` table, replacing it if it exists and omitting the index column
* C) Deletes the `results` table
* D) Renames the DataFrame

<details>
<summary>Answer</summary>

B) `to_sql` writes the DataFrame to the named table; `if_exists='replace'` overwrites an existing table, and `index=False` leaves out the index.

</details>

---

## Further Reading

* [`pandas.read_sql_query` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
* [`DataFrame.to_sql` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
