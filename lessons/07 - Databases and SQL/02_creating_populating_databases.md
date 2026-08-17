# 7.2 Creating and Populating a Database

**Objective**: By the end of this module, you will be able to:

* Connect to a SQLite database from Python and manage transactions with a `with` block.
* Create tables with `CREATE TABLE`, including data types and constraints.
* Insert data with parameterized statements and `executemany`.
* Insert records that use foreign keys.

---

This module builds the `Students`, `Courses`, and `Enrollments` database from Module 7.1 in code, using Python's built-in `sqlite3` module. This week runs in a **Kaggle notebook**; each step below is a cell. The database is a single file — write it to the notebook's working directory so it is saved with your notebook:

```python
import sqlite3

DB_PATH = "school.db"   # created in the notebook's working directory
```

> **Staying on `sqlite3`.** This week uses the raw `sqlite3` connection directly, so you can see how a database works at the plainest level. Week 8 introduces a higher-level tool (SQLAlchemy). Learn this version first.

---

## Connecting to the Database

`sqlite3.connect()` creates the database file if it does not exist, then connects to it. Using the connection in a `with` block manages the **transaction**: if the block finishes normally, the changes are committed; if it raises an exception, they are rolled back.

```python
with sqlite3.connect(DB_PATH) as conn:
    print("Connected.")

conn.close()   # the with block commits or rolls back, but does not close the connection
```

Note the last line: the `with` block handles the transaction, but you still close the connection yourself with `conn.close()`.

---

## Creating Tables

A `CREATE TABLE` statement defines a table's columns, their types, and their constraints. Use `CREATE TABLE IF NOT EXISTS` so that re-running the cell does not fail because the table already exists. You run SQL through a **cursor**:

```python
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            age INTEGER,
            major TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL UNIQUE,
            instructor_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollments (
            enrollment_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students (student_id),
            FOREIGN KEY (course_id) REFERENCES Courses (course_id)
        )
    """)

conn.close()
```

This applies the constraints from Module 7.1: `PRIMARY KEY` for the unique row identifier, `NOT NULL UNIQUE` so every student and course has a required, non-repeating name, and `FOREIGN KEY` so every enrollment points to a real student and a real course.

---

## Inserting Data with Parameterized Statements

Insert rows with `INSERT INTO`. Always supply the values with `?` placeholders and a tuple, rather than building the SQL string yourself:

```python
with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = 1")   # turn on foreign key enforcement
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Students (name, age, major) VALUES (?, ?, ?)",
        ("Jasmine", 20, "Computer Science")
    )

conn.close()
```

The `?` markers are filled in from the tuple. **Always insert values this way** — never by inserting variables into the SQL text with an f-string. This is called a **parameterized statement**, and it is both safer and more reliable. Week 8 explains exactly why it matters.

Note two details: you do not supply `student_id`, because `INTEGER PRIMARY KEY` fills it in automatically with a unique value; and `PRAGMA foreign_keys = 1` turns on foreign key enforcement, which SQLite leaves off by default.

To insert many rows at once, use `executemany` with a list of tuples:

```python
students = [
    ("Jasmine", 20, "Computer Science"),
    ("Pratik", 22, "History"),
    ("Carlos", 19, "Biology"),
]

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    conn.executemany(
        "INSERT INTO Students (name, age, major) VALUES (?, ?, ?)",
        students
    )
    conn.commit()

conn.close()
```

> **Re-running a cell.** Because `name` is `UNIQUE`, inserting the same students a second time raises `sqlite3.IntegrityError`. When you want a cell to be safe to re-run, either catch that error, or use `INSERT OR IGNORE INTO ...`, which skips rows that would violate a constraint.

---

## Inserting Records with Foreign Keys

An enrollment links a student to a course, so before inserting one you need the `student_id` and `course_id` — which the database assigned automatically. Look them up first, then insert:

```python
def enroll_student(cursor, student_name, course_name):
    cursor.execute("SELECT student_id FROM Students WHERE name = ?", (student_name,))
    student = cursor.fetchone()

    cursor.execute("SELECT course_id FROM Courses WHERE course_name = ?", (course_name,))
    course = cursor.fetchone()

    if student and course:
        cursor.execute(
            "INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)",
            (student[0], course[0])
        )
    else:
        print(f"Could not enroll {student_name} in {course_name}.")

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    enroll_student(cursor, "Jasmine", "Math 101")
    enroll_student(cursor, "Pratik", "Math 101")
    conn.commit()

conn.close()
```

`fetchone()` returns the first matching row as a tuple, so `student[0]` is the `student_id`. Because foreign key enforcement is on, trying to insert an enrollment with a `student_id` that does not exist would raise an error — the database protecting its own integrity.

---

### AI Prompt: Predict-then-Check

Constraints reject data that breaks the rules. Consider this situation without running it:

> You have inserted a student named `"Jasmine"` into the `Students` table, whose `name` column is `TEXT NOT NULL UNIQUE`. Your notebook cell runs the same `INSERT` for `"Jasmine"` a second time.

1. Predict what happens on the second insert.
2. Explain to an AI chatbot which constraint causes it and what error you would expect.
3. Ask: "Is my understanding of how the `UNIQUE` constraint behaves on a duplicate insert correct, and what are two ways to handle it?"

> **Example prompt:** "In SQLite, my `Students.name` column is `TEXT NOT NULL UNIQUE`. I insert 'Jasmine', then run the same insert again. I predict [your prediction] because [your reasoning]. Am I right, and how should I handle it so the cell can be re-run?"

---

## Videos

* [Python SQLite Tutorial: Complete Overview](https://www.youtube.com/watch?v=pd-0G0MigUA) — Corey Schafer on creating a database and tables, inserting data, and running queries with `sqlite3`.

---

## Check for Understanding

**1. In `with sqlite3.connect(DB_PATH) as conn:`, what does the `with` block do at the end?**

* A) It closes the connection automatically
* B) It commits the transaction if the block succeeded, or rolls it back if it raised an exception
* C) It deletes the database
* D) Nothing

<details>
<summary>Answer</summary>

B) The `with` block manages the transaction (commit on success, rollback on error). You still call `conn.close()` yourself to close the connection.

</details>

**2. Why insert values with `?` placeholders and a tuple instead of building the SQL string with an f-string?**

* A) It runs faster
* B) It is the safe, reliable way to pass values into SQL (parameterized statements); Week 8 explains why it matters
* C) f-strings do not work in Python
* D) It is required by Kaggle

<details>
<summary>Answer</summary>

B) Parameterized statements pass values safely and correctly. Building SQL by inserting variables into the text is unsafe — the reason is covered in Week 8.

</details>

**3. You insert an `Enrollments` row whose `student_id` does not exist in `Students`, with foreign keys enforced. What happens?**

* A) It succeeds silently
* B) The database raises an error, because the foreign key constraint requires a matching student
* C) It creates a new student automatically
* D) It deletes the Enrollments table

<details>
<summary>Answer</summary>

B) With `PRAGMA foreign_keys = 1`, the foreign key constraint blocks an enrollment that points to a nonexistent student.

</details>

---

## Further Reading

* [Python `sqlite3` documentation](https://docs.python.org/3/library/sqlite3.html)
* [SQLite: CREATE TABLE](https://www.sqlite.org/lang_createtable.html)
* [SQLite data types](https://www.sqlite.org/datatype3.html)
