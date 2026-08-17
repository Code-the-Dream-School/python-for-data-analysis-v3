# 7.1 Relational Thinking

**Objective**: By the end of this module, you will be able to:

* Explain why a relational database is often better than a folder of CSV files.
* Describe tables, rows, primary keys, and foreign keys.
* Identify one-to-one, one-to-many, and many-to-many associations.
* Explain how constraints and transactions protect data quality.

---

So far your data has lived in files and DataFrames. This week you learn about **relational databases**, the standard way that organizations store structured, interrelated data, and **SQL**, the language used to work with them. This module is about the ideas; the following modules put them into code.

A relational database stores data in **tables**. Each table looks like a spreadsheet: rows are records, and columns have names and data types. Compared with a folder of CSV files, a database offers three things a pile of files cannot:

* **Enforced structure.** The database has a **schema** that defines each table's columns and their types, and it rejects data that does not fit.
* **Defined relationships.** Tables can be linked to one another, so related data stays connected and consistent.
* **Efficient querying.** You can ask precise questions across large, linked tables without loading everything into memory first.

SQLite, the database used in this course, is a single file on disk, and Python's built-in `sqlite3` module works with it directly. SQLite supports a small set of data types — `TEXT`, `NUMERIC`, `INTEGER`, `REAL`, and `BLOB`. The schema can feel rigid at first, but that rigidity is what keeps the data organized and reliable.

---

## Primary Keys and Foreign Keys

Two kinds of key make relationships possible:

* A **primary key** is a column whose value uniquely identifies each row in a table. A `Students` table might use `student_id` as its primary key.
* A **foreign key** is a column that holds the primary key of a row in *another* table, linking the two. An `Enrollments` table might have a `student_id` foreign key that points to a row in `Students`.

Keys are how a database keeps related data connected without repeating it.

---

## Associations

An **association** exists between two tables when one holds a foreign key pointing to the other. There are three kinds.

* **One-to-one.** Each row in table A matches at most one row in table B. For example, a `users` table and a `user_profiles` table, where each profile belongs to exactly one user.
* **One-to-many.** One row in table A matches many rows in table B. A `blogs` table and a `posts` table: one blog has many posts, and each post has a foreign key naming its blog.
* **Many-to-many.** Rows in each table can match many rows in the other. Consider students and courses: a student takes many courses, and a course has many students.

A many-to-many association needs special handling, because a relational row cannot contain a list. You cannot store a list of courses inside a student's row. Instead you add a third table in the middle, called a **join table**. For students and courses, an `Enrollments` join table holds one row per enrollment, each with two foreign keys: one for the student and one for the course. The join table is how the database represents "many students to many courses."

---

## Constraints: the Database Enforces Data Quality

When you define a table, you can attach **constraints** — rules the database enforces on every insert and update. If a change would break a rule, the database rejects it with an error.

* **Data type** — a `TEXT` value cannot go in an `INTEGER` column.
* **`NOT NULL`** — the column must always have a value.
* **`UNIQUE`** — no two rows may share the same value in that column (useful for IDs).
* **`FOREIGN KEY`** — the value must match a real primary key in the referenced table, so you cannot create a record that points to nothing.

This connects directly to Week 3. There, you validated data by hand — checking ranges, removing duplicates, confirming allowed values. Constraints let the *database* enforce those same rules automatically, so invalid data cannot enter in the first place.

---

## Transactions: All or Nothing

A **transaction** is a write operation that either completes fully or not at all. Consider transferring money between two bank accounts:

1. Begin the transaction.
2. Check that account A has enough money.
3. Decrease account A's balance.
4. Increase account B's balance.
5. Commit the transaction.

If the system failed after step 3 but before step 4, money would vanish. A transaction prevents this: either both updates succeed and are committed together, or neither takes effect. This "all or nothing" guarantee is one of the main reasons relational databases are trusted for important data. You will use transactions in code in Module 7.2, and return to them in Week 8.

---

### AI Prompt: Retrieval Practice

Many-to-many associations are the hardest to picture, so practice explaining one.

1. Open your preferred AI chatbot.
2. Explain why a join table (like `Enrollments`) is needed to connect students and courses.
3. Explain why you cannot simply store a list of courses inside a single student's row.
4. Ask the AI: "Did I correctly explain why a relational database needs a join table for a many-to-many association?"

> **Example prompt:** "I'm learning about many-to-many associations in SQL. Here is my explanation of why a join table is necessary and why a row can't hold a list: [your explanation]. Is this accurate?"

---

### AI Prompt: Retrieval Practice

Transactions protect against partial updates. Practice explaining one in your own words.

1. Open your preferred AI chatbot.
2. Explain what a transaction is and why it is described as "all or nothing."
3. Use a scenario other than banking — an online order, or a library checkout — to show why a transaction prevents data errors.
4. Ask the AI for feedback on your explanation and example.

> **Example prompt:** "I'm learning about SQL transactions. Here is my explanation of what they are and a non-banking scenario where one is useful: [your explanation]. Does this accurately show how a transaction keeps data consistent?"

---

## Videos

* ["What is a Relational Database?" IBM Technology](https://youtu.be/OqjJjpjDRLc?si=Cuh0YiONluxRIEk5)

---

## Check for Understanding

**1. What is the difference between a primary key and a foreign key?**

* A) They are the same thing
* B) A primary key uniquely identifies a row in its own table; a foreign key holds another table's primary key to link the two
* C) A foreign key must be text; a primary key must be a number
* D) A primary key links two tables; a foreign key identifies a row

<details>
<summary>Answer</summary>

B) The primary key identifies each row within its table; a foreign key stores the primary key of a row in another table, creating the link between them.

</details>

**2. Why does a many-to-many association require a join table?**

* A) To make queries run faster
* B) Because a relational row cannot hold a list, so the link is stored as one row per pairing in a third table
* C) Because foreign keys are not allowed
* D) It does not — you store a list in one of the tables

<details>
<summary>Answer</summary>

B) A row cannot contain a list of related records, so a join table records each pairing as its own row with two foreign keys.

</details>

**3. How do constraints relate to the manual data validation you did in Week 3?**

* A) They are unrelated
* B) Constraints let the database enforce rules (uniqueness, allowed types, required values) automatically, instead of by hand
* C) Constraints replace the need for any data at all
* D) Constraints only apply to text columns

<details>
<summary>Answer</summary>

B) Constraints move the validation into the database, which rejects invalid data automatically — the same checks you performed manually in Week 3.

</details>

---

## Further Reading

* [The Odin Project: Databases and SQL](https://www.theodinproject.com/lessons/databases-databases-and-sql) — a clear introduction to the core concepts.
* [SQLBolt](https://sqlbolt.com/) — an interactive SQL tutorial, strongly recommended for extra practice this week.
