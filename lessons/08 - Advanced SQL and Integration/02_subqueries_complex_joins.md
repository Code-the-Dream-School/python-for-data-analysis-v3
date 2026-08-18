# 8.2 Subqueries and Complex Joins

**Objective**: By the end of this module, you will be able to:

* Use a subquery in a `WHERE` clause and in a `FROM` clause.
* Explain what a correlated subquery is.
* Join more than two tables, including joining a table to itself.

---

This module continues with the `company.db` database from Module 8.1. It covers two ways to build more capable queries: **subqueries** (a query nested inside another) and **complex joins** (combining three or more tables, or joining a table to itself).

## Subqueries in a WHERE Clause

A **subquery** is a `SELECT` written inside another statement. The inner query runs first, and its result is used by the outer query. A common use is comparing each row against a value computed from the whole table — for example, employees who earn more than the company-wide average:

```sql
SELECT first_name, last_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

The subquery `(SELECT AVG(salary) FROM Employees)` produces a single number, and the outer query keeps every row above it.

## Correlated Subqueries

A **correlated subquery** refers to the outer query, so it is re-evaluated for each outer row. To find the highest-paid employee in *each* department, the subquery must know which department the current row belongs to:

```sql
SELECT department_id, first_name, salary
FROM Employees AS e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department_id = e.department_id
);
```

For each employee `e`, the subquery computes the maximum salary *within that employee's department*, and the row is kept only if the employee earns it. Where two employees tie for the top salary in a department, both appear.

## Subqueries in a FROM Clause

A subquery can also stand in for a table in the `FROM` clause. This is useful when you want to query the *result* of an aggregation. To list only departments whose average salary is above 100,000:

```sql
SELECT department_id, avg_salary
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department_id
)
WHERE avg_salary > 100000;
```

The inner query builds a small table of per-department averages, and the outer query filters it. (You saw one way to filter aggregates with `HAVING` in Module 8.1; a subquery in `FROM` is another.)

---

## Joining More Than Two Tables

A query can join several tables in sequence, each `JOIN` adding another table through a matching key. This is the same chaining you saw with the three-table student-course join in Week 7.

## Self-Joins: the Manager Example

Sometimes you need to join a table *to itself*. In the company database, each department has a `manager_id`, which is the `employee_id` of an employee. To list each employee alongside their department's manager, you use the `Employees` table twice — once for the employees, once for the managers — giving each use a different alias:

```sql
SELECT e.first_name || ' ' || e.last_name AS employee,
       m.first_name || ' ' || m.last_name AS manager
FROM Employees AS e
JOIN Departments AS d ON e.department_id = d.department_id
JOIN Employees AS m ON d.manager_id = m.employee_id;
```

Here `e` is the employee and `m` is the manager, but both are rows from the same `Employees` table. The aliases are what make this work: without them, SQL could not tell which copy of `Employees` you mean. (The `||` operator joins text values, so `first_name || ' ' || last_name` builds a full name.)

A self-join is the tool whenever a table refers to itself — employees and managers, categories and parent categories, pages and the pages that link to them.

---

### AI Prompt: Retrieval Practice

Subqueries let one query depend on the result of another.

1. Open your preferred AI chatbot.
2. Explain, in your own words, what a subquery is and why it is useful for computing an intermediate value before the main query runs.
3. Give an example of when you would use one, such as finding the highest-paid employee within each department.
4. Ask the AI for feedback on your explanation.

> **Example prompt:** "I just learned about SQL subqueries. Here is my understanding of how they work and a use case: [your explanation]. What did I get right, and how could I make the technical explanation clearer?"

---

## Videos

* ["How to do Subqueries in SQL with Examples," Becoming a Data Scientist](https://youtu.be/GpC0XyiJPEo?si=eilh3-5AUHsOFQUg)
* ["How to Join Multiple Tables in SQL," The Knowledge Academy](https://youtu.be/y5EM-oXxDTA?si=v7TZuwwa3nyCBE0d)

---

## Check for Understanding

**1. What is a subquery?**

* A) A query that deletes rows
* B) A `SELECT` statement nested inside another statement, whose result the outer query uses
* C) A faster version of a join
* D) A query that runs on two databases at once

<details>
<summary>Answer</summary>

B) A subquery is a query inside another query; the inner result feeds the outer query.

</details>

**2. What makes a subquery *correlated*?**

* A) It runs faster than a normal subquery
* B) It refers to the outer query, so it is re-evaluated for each outer row
* C) It joins two tables
* D) It can only return one row

<details>
<summary>Answer</summary>

B) A correlated subquery depends on a value from the outer query (like `e.department_id`), so it runs once per outer row.

</details>

**3. To list each employee next to their department's manager (also an employee), what kind of query do you need?**

* A) A subquery in `WHERE`
* B) A self-join — joining the `Employees` table to itself with two aliases
* C) A `GROUP BY`
* D) A `UNION`

<details>
<summary>Answer</summary>

B) Because managers are themselves rows in `Employees`, you join the table to itself, using different aliases (like `e` and `m`) to tell the two uses apart.

</details>

---

## Further Reading

* [SQLBolt: Multi-table queries with JOINs](https://sqlbolt.com/lesson/select_queries_with_joins)
* [SQLite: The SELECT statement](https://www.sqlite.org/lang_select.html) — including subqueries.
