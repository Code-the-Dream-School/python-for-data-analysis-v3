# 8.5 Safe and Reliable Queries

**Objective**: By the end of this module, you will be able to:

* Explain SQL injection and prevent it with parameterized queries.
* Recognize that SQLAlchemy is not automatically safe from injection.
* Use transactions and rollbacks to keep the database consistent.
* Add an index and explain when it helps.

---

Writing a query that returns the right answer is not enough. A query also has to be **safe** against malicious input and **reliable** when something goes wrong. This module covers three practices that make the difference: parameterized queries, transactions, and indexing. It continues with the `company.db` database from Module 8.1.

## SQL Injection

**SQL injection** is an attack in which crafted input changes the structure of a query, letting an attacker read, modify, or delete data they should not reach. It happens when untrusted input is placed directly into the SQL text. Consider a query that filters by department, where `department_id` comes from a user:

```python
department_id = "1 OR 1=1"   # malicious input
cursor.execute(f"SELECT * FROM Employees WHERE department_id = {department_id}")
```

The value becomes part of the SQL, so the query reads:

```sql
SELECT * FROM Employees WHERE department_id = 1 OR 1=1;
```

Because `1=1` is always true, this returns *every* employee, ignoring the department filter. A more damaging input could expose or destroy data.

## Parameterized Queries Are the Fix

The fix is to pass input as a **parameter**, never as part of the SQL text. The database then treats the value strictly as data, never as SQL. You have used `?` placeholders since Week 7 — this is why.

With `sqlite3`, use a `?` placeholder and a tuple:

```python
cursor.execute("SELECT * FROM Employees WHERE department_id = ?", (department_id,))
```

Now the malicious input `"1 OR 1=1"` is treated as a single value to match against `department_id`. No department equals that text, so the query safely returns zero rows.

---

## SQLAlchemy Does Not Make You Safe by Default

A common misconception is that using SQLAlchemy protects you from injection automatically. It does not. An f-string built into a `text()` statement is exactly as vulnerable as one built into a `sqlite3` call:

```python
from sqlalchemy import text

# VULNERABLE — returns every row. SQLAlchemy does not save you here.
with engine.connect() as conn:
    conn.execute(text(f"SELECT * FROM Employees WHERE department_id = {department_id}"))
```

Safety comes from **binding the parameter**, not from choosing the library. In SQLAlchemy, use a `:name` placeholder and pass a dictionary:

```python
# SAFE — the bound value is never parsed as SQL, so this returns zero rows.
with engine.connect() as conn:
    conn.execute(
        text("SELECT * FROM Employees WHERE department_id = :dept"),
        {"dept": department_id}
    )
```

The rule, in both `sqlite3` and SQLAlchemy: any part of a query that comes from user input or another untrusted source must be passed as a bound parameter — never inserted into the SQL text with an f-string.

---

## Transactions and Rollbacks

Module 7.1 introduced transactions as an "all or nothing" guarantee. Here is how you use one in code to keep the database consistent when several writes must succeed together. If any statement fails, `rollback()` undoes the whole group:

```python
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Departments (department_id, department_name) VALUES (60, 'Legal')")
        cursor.execute("INSERT INTO Departments (department_id, department_name) VALUES (70, 'Design')")
        conn.commit()          # both succeed → commit together
    except Exception as e:
        conn.rollback()        # any failure → undo both
        print("Error:", e)

conn.close()
```

With SQLAlchemy, `engine.begin()` (from Module 8.4) does this for you: it commits when the block finishes and rolls back if the block raises an error.

---

## Indexing

An **index** speeds up queries that look up rows by a particular column. Without one, the database scans every row to find matches; an index lets it jump to them. Create an index on a column you filter, join, or sort by often:

```sql
CREATE INDEX idx_department ON Employees(department_id);
```

Indexing helps most on **large tables** with columns used frequently in `WHERE`, `JOIN`, or `ORDER BY` clauses. It is not free: an index takes storage and slightly slows inserts and updates, because the index must be maintained too. On a small table the difference is negligible, so add indexes where queries are actually slow, not everywhere by default.

---

### AI Prompt: Retrieval Practice

Being able to explain SQL injection and its fix is an important security skill.

1. Open your preferred AI chatbot.
2. Explain what a parameterized query is and why using placeholders (`?` or `:name`) is safer than building a query with an f-string.
3. Ask the AI: "Can you walk me through a scenario where a query built with an f-string could let malicious input expose or change data it should not?"

> **Example prompt:** "I'm learning to prevent SQL injection in Python. I think parameterized queries work by [your explanation], and this applies in both `sqlite3` and SQLAlchemy. Is that correct? Can you show a concrete example of what could go wrong with an f-string query?"

---

## Videos

* ["Preventing SQL Injections, LinkedIn Learning"](https://youtu.be/S4qtRFsuKVY?si=wlqxbHGVLvRNr91G)

---

## Check for Understanding

**1. Why is `cursor.execute(f"SELECT * FROM Employees WHERE id = {user_input}")` dangerous?**

* A) It runs too slowly
* B) The user input becomes part of the SQL, so crafted input can change what the query does (SQL injection)
* C) f-strings are invalid in SQL
* D) It cannot return any rows

<details>
<summary>Answer</summary>

B) Placing untrusted input directly into the SQL text lets an attacker alter the query. Pass the value as a bound parameter instead.

</details>

**2. Does using SQLAlchemy instead of `sqlite3` prevent SQL injection automatically?**

* A) Yes, SQLAlchemy is always safe
* B) No — an f-string inside `text()` is just as vulnerable; safety comes from binding the parameter
* C) Only if you use the ORM
* D) Only for SQLite

<details>
<summary>Answer</summary>

B) SQLAlchemy is not automatically safe. Whether you use `sqlite3` or SQLAlchemy, you must pass untrusted values as bound parameters.

</details>

**3. When does adding an index help the most?**

* A) On every column of every table
* B) On columns of a large table that are frequently used in `WHERE`, `JOIN`, or `ORDER BY`
* C) Only on primary keys
* D) It never helps

<details>
<summary>Answer</summary>

B) Indexes speed up lookups on frequently queried columns of large tables, at the cost of some storage and slightly slower writes. On small tables the benefit is negligible.

</details>

---

## Further Reading

* [SQLite: CREATE INDEX](https://www.sqlite.org/lang_createindex.html)
* [Python `sqlite3`: how to use placeholders to bind values](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders)
* [SQLAlchemy: Sending parameters](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#sending-parameters)
