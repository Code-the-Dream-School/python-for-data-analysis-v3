# 8.4 Connecting with SQLAlchemy

**Objective**: By the end of this module, you will be able to:

* Create a database engine with `create_engine` and a database URL.
* Read and write data through an engine with Pandas.
* Use `engine.connect()` for reads and `engine.begin()` for writes.
* Recognize the ORM as a second way to describe a table you already know how to build.

---

So far you have used Python's built-in `sqlite3` module directly. **SQLAlchemy** is a widely used library that connects to databases through an object called an **engine**. This module continues with the `company.db` database from Module 8.1.

## Why SQLAlchemy

It is fair to ask why to change anything, since raw `sqlite3` works. Pandas still fully supports a `sqlite3` connection — there is no deprecation, and `read_sql_query` and `to_sql` work with one exactly as they did in Week 7.

The reason to learn SQLAlchemy is **portability**. Pandas has special built-in support for SQLite specifically, but for any *other* database — PostgreSQL, MySQL, and so on — you connect through SQLAlchemy. SQLAlchemy provides one consistent way to connect that works for every database. And when a project outgrows SQLite and moves to another database, the only thing that changes is the connection string:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///company.db")
# The only thing that changes for a different database is this string:
# create_engine("postgresql://user:pass@host:5432/dbname")
```

A database **URL** names the database system (`sqlite`, `postgresql`, …) and where to find it. For SQLite, `sqlite:///company.db` points at a file in the working directory.

---

## Reading and Writing with an Engine

With an engine, Pandas reads and writes just as before — you pass the engine where you used to pass a `sqlite3` connection:

```python
import pandas as pd

# read the result of a query into a DataFrame
df = pd.read_sql_query("SELECT * FROM Employees", engine)

# write a DataFrame to a table
df.to_sql("employees_copy", engine, if_exists="replace", index=False)
```

This is the same `read_sql_query` and `to_sql` from Week 7.5 — the engine simply takes the place of the raw connection.

---

## Running SQL: `connect()` vs. `begin()`

To run SQL statements directly through SQLAlchemy, you open the engine in a `with` block and wrap the SQL in `text()`. There are two ways to open it, and the difference matters:

* **`engine.connect()`** is for reading. It does not commit changes.
* **`engine.begin()`** is for writing. It commits automatically when the block exits (and rolls back on error).

```python
from sqlalchemy import text

# writing — begin() commits when the block ends
with engine.begin() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS notes (id INTEGER, note TEXT)"))

# reading — connect() does not commit
with engine.connect() as conn:
    rows = conn.execute(text("SELECT * FROM Employees")).fetchall()
```

Use `begin()` whenever the statement changes the database (`INSERT`, `UPDATE`, `DELETE`, `CREATE`); use `connect()` for read-only queries.

---

## The ORM: a Second Way to Describe a Table

Everything above is SQLAlchemy's **Core** interface — you still write SQL. SQLAlchemy also includes an **Object-Relational Mapper (ORM)**, which lets you describe a table as a Python **class**.

> **This section is a demonstration only.** The ORM is shown here so you can see the connection to what you already know. It is **not** used in this week's assignment or in the final project, and you do not need to write classes to complete this course. The point is simply that a class is another way to write a table you already know how to create.

In Week 7 you created tables with `CREATE TABLE`. Here is a small schema written both ways. On the left is the SQL you know; on the right is the ORM class form:

```sql
CREATE TABLE magazines (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

```python
from sqlalchemy import create_engine, Integer, String, ForeignKey, inspect
from sqlalchemy.orm import DeclarativeBase, mapped_column

engine = create_engine("sqlite:///demo.db")

class Base(DeclarativeBase):
    pass

class Magazine(Base):
    __tablename__ = "magazines"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(80), nullable=False)

class Publisher(Base):
    __tablename__ = "publishers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(80), nullable=False)
    magazine_id = mapped_column(ForeignKey("magazines.id"))

Base.metadata.create_all(engine)           # this generates the CREATE TABLE statements
print(inspect(engine).get_table_names())   # ['magazines', 'publishers']
```

`Base.metadata.create_all(engine)` reads the classes and creates the corresponding tables, and `inspect(engine).get_table_names()` confirms they exist. Compare the `Magazine` class to the `CREATE TABLE magazines` statement above: each `mapped_column` matches one column definition. The class is a second notation for the same table — not a new abstraction to learn now.

---

### AI Prompt: Retrieval Practice

The portability argument for SQLAlchemy is worth being able to explain.

1. Open your preferred AI chatbot.
2. Explain why raw `sqlite3` is fine for SQLite, but SQLAlchemy is useful when a project might move to a different database like PostgreSQL.
3. Note what part of the code changes when you switch databases, and what stays the same.
4. Ask the AI for feedback on your explanation.

> **Example prompt:** "I'm learning why data projects use SQLAlchemy. Here is my explanation of why it helps when you might switch databases, and what changes versus stays the same: [your explanation]. Is my reasoning accurate?"

---

## Videos

* ["How to use SQLAlchemy in 2026," Pretty Printed](https://youtu.be/Y-TxICRUy_k?si=QweMFRgAuCdYq3CV)

---

## Check for Understanding

**1. According to this module, why learn SQLAlchemy if raw `sqlite3` still works with Pandas?**

* A) Because Pandas has dropped support for `sqlite3`
* B) For portability — SQLAlchemy connects to every database with one consistent approach, so moving off SQLite only means changing the connection string
* C) Because SQLAlchemy is faster
* D) Because `sqlite3` cannot create tables

<details>
<summary>Answer</summary>

B) Pandas still supports `sqlite3` fully. SQLAlchemy's value is a single connection approach that works for any database; only the connection string changes when you switch databases.

</details>

**2. You need to run an `INSERT` through a SQLAlchemy engine. Which do you use?**

* A) `engine.connect()`, because it is simpler
* B) `engine.begin()`, because it commits the change when the block exits
* C) Either one behaves the same
* D) Neither — engines cannot run `INSERT`

<details>
<summary>Answer</summary>

B) `engine.begin()` commits writes on exit (and rolls back on error). `engine.connect()` is for read-only queries and does not commit.

</details>

**3. What is the relationship between the ORM `Magazine` class and a `CREATE TABLE magazines` statement?**

* A) They are unrelated
* B) The class is a second way to describe the same table; `create_all` generates the equivalent `CREATE TABLE`
* C) The class is required to query the table
* D) The class replaces SQL entirely in this course

<details>
<summary>Answer</summary>

B) The ORM class describes the same table in Python form; `Base.metadata.create_all` produces the matching table. It is shown as a demonstration and is not required in this course.

</details>

---

## Further Reading

* [SQLAlchemy: Establishing connectivity — the Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html)
* [SQLAlchemy: Working with the ORM](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
* [`pandas.read_sql_query` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
