## Lesson 7 Assignment — Databases and SQL

### **Objective**

Design and build a small relational database, populate it, query it, and read a summary of it into Pandas. You will model publishers, magazines, subscribers, and subscriptions — which includes a one-to-many and a many-to-many association.

### **Setup**

Do this assignment in a **Kaggle notebook** named `CTD_Assignment_7`. Label each task with a markdown cell, and put each task's code in one or more code cells.

Start with the imports and a database path in the notebook's working directory. Run your SQL inside `try`/`except` blocks, since any SQL statement can raise an exception:

```python
import sqlite3
import pandas as pd

DB_PATH = "magazines.db"
```

---

### **Task 1: Create the Database**

1. Write code to connect to a new SQLite database at `DB_PATH`, then close the connection.
2. Run the cell and confirm it runs without error. (The database file is created in the working directory.)

### **Task 2: Define the Schema**

Publishers publish magazines, and subscribers subscribe to magazines:

- Each **publisher** has a unique name.
- Each **magazine** has a unique name and belongs to one publisher — a **one-to-many** association (one publisher, many magazines).
- Each **subscriber** has a name and an address.
- A subscriber may subscribe to many magazines, and a magazine may have many subscribers — a **many-to-many** association, handled by a **subscriptions** join table. Each subscription also stores an `expiration_date` (a string).
- All names, the address, and the expiration date must be non-null.

1. **Think first:** In the one-to-many association between publishers and magazines, which table holds the foreign key, and where does it point? What foreign keys does the `subscriptions` table need?
2. Write `CREATE TABLE IF NOT EXISTS` statements for `publishers`, `magazines`, `subscribers`, and `subscriptions`. Include the right data types, `UNIQUE` and `NOT NULL` constraints where needed, and foreign keys where needed. (You may reuse a column name like `name` across tables.)
3. Print a confirmation, or read back the table names, to verify the tables were created.

### **Task 3: Populate the Tables**

1. Enable foreign key enforcement right after connecting:
   ```python
   conn.execute("PRAGMA foreign_keys = 1")
   ```
2. Write a function for each table that inserts an entry using a **parameterized statement**, and handles duplicates. Names of publishers and magazines are unique, so catch the `IntegrityError`. Subscribers are not unique by name alone, so before inserting a subscriber, check that a subscriber with the **same name and address** does not already exist.
3. In your main code, populate each of the four tables with at least **3 entries**. Remember to `commit`.
4. Run the cell more than once and confirm you do not create duplicate data.

### **Task 4: Query the Data**

Write and run these queries, printing the rows returned by each:

1. All information from the `subscribers` table.
2. All magazines, sorted by name.
3. The magazines published by one particular publisher (one you created). This requires a `JOIN` between `magazines` and `publishers`.

You may use the `run_query()` helper from Module 7.3 to display results as a DataFrame, or a cursor with `fetchall()`.

### **Task 5: Summarize with Pandas**

Now read data out of your database and summarize it with Pandas (Module 7.5).

1. Use `pd.read_sql_query` to read a `JOIN` of `subscriptions`, `magazines`, and `subscribers` into a DataFrame, with one row per subscription showing the magazine name and the subscriber name.
2. Print the first 5 rows to confirm it worked.
3. Use `groupby` and `agg` to count the number of subscribers for each magazine.
4. Sort the result by magazine name.
5. Write the summary to a CSV file named `subscribers_by_magazine.csv`.

> As you will see in Week 8, the grouping and counting in this task can also be done directly in SQL, often more efficiently. The concepts of Pandas and SQL overlap closely — this task does the summary in Pandas so you can compare the two approaches next week.

---

### **Submit Your Assignment**

1. **Save your work.** Click **Save Version** and save (a quick save is fine). Make sure the notebook runs top to bottom without errors.
2. **Get a sharing link.** Click **Share**, choose **Public**, make sure **Allow Comments** is on, and copy the public URL.
3. **Submit the link.** Paste the URL into the **assignment submission form**.

---
