# 7.4 Joins, Updates, and Deletes

**Objective**: By the end of this module, you will be able to:

* Combine tables with an `INNER JOIN` using an `ON` clause.
* Keep unmatched rows with a `LEFT JOIN`.
* Change rows with `UPDATE` and remove rows with `DELETE`.
* Explain why a missing `WHERE` clause is dangerous.

---

The queries in Module 7.3 read from one table. The real strength of a relational database is combining related tables, which SQL does with a **join**. If you recall `merge` from Week 4, a join is the same idea in SQL: match rows from two tables on a shared key and combine their columns.

## INNER JOIN

A join uses an `ON` clause to say which columns must match. Because the `Students` and `Courses` tables are linked only through the `Enrollments` join table, connecting a student to a course means joining all three:

```sql
SELECT s.name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
```

For each student, the database finds their enrollments, and for each enrollment it finds the matching course, producing one row per student-course pairing. The short names (`s`, `e`, `c`) are **aliases** that save typing; you could write `Students AS s` or just `Students s`.

The `ON` clause pairs a primary key with a foreign key — `Students.student_id` (a primary key) with `Enrollments.student_id` (a foreign key). This is a plain `JOIN`, also called an **INNER JOIN**: it returns only rows that have matches on both sides, the same as a `how='inner'` merge in Pandas.

Run it with the helper from Module 7.3:

```python
run_query("""
    SELECT s.name, c.course_name
    FROM Students s
    JOIN Enrollments e ON s.student_id = e.student_id
    JOIN Courses c ON e.course_id = c.course_id
""")
```

## LEFT JOIN

An `INNER JOIN` drops students who are not enrolled in anything, because they have no matching enrollment. To keep every student, matched or not, use a `LEFT JOIN` — it keeps all rows from the left table and fills the right-side columns with `NULL` where there is no match:

```sql
SELECT s.name, c.course_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c ON e.course_id = c.course_id;
```

A student enrolled in nothing appears once, with `NULL` for `course_name`. This is the SQL version of a `how='left'` merge, and the reasoning is identical: keep every record on the left, attach matches where they exist.

---

## Changing Rows with UPDATE

`UPDATE` changes existing rows. A `WHERE` clause chooses which rows to change:

```sql
UPDATE Students SET major = 'Data Science' WHERE name = 'Carlos';
```

You can compute the new value from the old one:

```sql
UPDATE Products SET price = price * 1.1;   -- raise every price by 10%
```

From Python, an `UPDATE` is a write, so you run it and commit:

```python
with sqlite3.connect(DB_PATH) as conn:
    conn.execute("UPDATE Students SET major = ? WHERE name = ?", ("Data Science", "Carlos"))
    conn.commit()
conn.close()
```

## Removing Rows with DELETE

`DELETE` removes rows, and again `WHERE` chooses which:

```sql
DELETE FROM Enrollments WHERE enrollment_id = 5;
```

---

#### `UPDATE` and `DELETE` apply to **every row that matches the `WHERE` clause**. If there is *no* `WHERE` clause, that means **every row in the table.**

```sql
UPDATE Students SET major = 'Undeclared';   -- changes EVERY student's major
DELETE FROM Students;                        -- deletes EVERY student
```

Both statements run without warning and cannot be undone. Before running an `UPDATE` or `DELETE`, check that it has a `WHERE` clause selecting exactly the rows you intend. A good habit is to first write the same `WHERE` as a `SELECT` and confirm it returns the rows you expect.

---

### AI Prompt: Predict-then-Check

`LEFT JOIN` and `INNER JOIN` treat unmatched rows differently. Study this without running it:

**Tables:**
* `Students`: `(student_id: 1, name: 'Jasmine')`, `(student_id: 2, name: 'Pratik')`
* `Enrollments`: `(enrollment_id: 101, student_id: 1, course_id: 5)`

```sql
SELECT Students.name, Enrollments.course_id
FROM Students
LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id;
```

1. Predict the output for Pratik specifically. Does Pratik have a matching enrollment?
2. Explain to an AI chatbot whether Pratik appears in the results and what his `course_id` will be.
3. Ask: "Is my reasoning about how a LEFT JOIN handles a row with no match correct?"

> **Example prompt:** "Looking at this SQL: [paste query]. I predict the output for Pratik will be [your prediction] because [your reasoning about LEFT JOINs]. Am I correct about how a LEFT JOIN handles a student with no matching enrollment?"

---

## Videos

> * The [SQLBolt](https://sqlbolt.com/) tutorial (Module 7.1) has excellent interactive lessons on joins.

---

## Check for Understanding

**1. In `JOIN Enrollments ON Students.student_id = Enrollments.student_id`, why is `student_id` used rather than `enrollment_id`?**

* A) `enrollment_id` is faster
* B) The `ON` clause matches a primary key to the foreign key that references it; `enrollment_id` has no counterpart in `Students`
* C) Any two columns can be used
* D) `enrollment_id` does not exist

<details>
<summary>Answer</summary>

B) A join matches related keys — here the `Students` primary key and the `Enrollments` foreign key that points to it. `enrollment_id` refers to nothing in `Students`.

</details>

**2. You want every student in the result, including those with no enrollments. Which join?**

* A) `INNER JOIN`
* B) `LEFT JOIN` (with `Students` on the left)
* C) A plain `JOIN`
* D) No join can do this

<details>
<summary>Answer</summary>

B) A `LEFT JOIN` keeps all rows from the left table; unmatched students get `NULL` in the right-side columns. (A plain `JOIN`/`INNER JOIN` drops them.)

</details>

**3. What does `DELETE FROM Students;` (with no `WHERE` clause) do?**

* A) Deletes one student
* B) Deletes every row in the `Students` table
* C) Raises an error
* D) Deletes the most recently added student

<details>
<summary>Answer</summary>

B) With no `WHERE`, `DELETE` removes every row. The same is true of `UPDATE` without `WHERE` — it changes every row. Always confirm your `WHERE` clause first.

</details>

---

## Further Reading

* [SQLBolt: Multi-table queries with JOINs](https://sqlbolt.com/lesson/select_queries_with_joins)
* [SQLite: UPDATE](https://www.sqlite.org/lang_update.html)
* [SQLite: DELETE](https://www.sqlite.org/lang_delete.html)
