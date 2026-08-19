# 1.4 Comprehensions, Lambdas, and Parsing Messy Data

**Objective**: By the end of this module, you will be able to:

* Build a dictionary with a dict comprehension.
* Write a lambda for a small, inline function.
* Use regex to parse semi-structured text into a list of dictionaries.
* Handle malformed rows and produce a clean, table-shaped result.

---

This module brings the week together. You already write **list comprehensions** from the Intro course; here you add **dict comprehensions** and **lambdas**, then put them to work with the regex from Module 1.2 on a real task: turning messy text into structured data. The result — a list of dictionaries — is exactly the shape that Week 2 turns into a Pandas DataFrame.

## Dict Comprehensions

A **dict comprehension** builds a dictionary the same way a list comprehension builds a list, but it produces `key: value` pairs. The syntax adds a colon:

```python
names = ["Alice", "Bob", "Carlos"]
name_lengths = {name: len(name) for name in names}
# {'Alice': 5, 'Bob': 3, 'Carlos': 6}
```

Read it as: *for each `name` in `names`, make an entry whose key is `name` and whose value is `len(name)`.*

## Lambdas

A **lambda** is a small, unnamed function written in one line. `lambda x: x * 2` is a function that takes `x` and returns `x * 2`. Lambdas are useful when a function is needed briefly and giving it a name would be overkill — most often as the `key` that tells a sort *how* to order things:

```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

by_age = sorted(people, key=lambda person: person["age"])
# Bob (25) comes before Alice (30)
```

Here `lambda person: person["age"]` tells `sorted` to order by each person's age. You will use lambdas often in Weeks 3 and 4, where they describe how to transform a column of data.

---

## Parsing Messy Data

Real data often arrives as **semi-structured text**: readable, but not yet in neat rows and columns. Your job is to extract the fields you need and build a clean structure. Regex (Module 1.2) is the tool for pulling the fields out.

Suppose you receive records as lines of text, and some lines are malformed:

```python
raw = """
Alice, 30, New York
Bob, 25, Los Angeles
--- corrupted line ---
Carlos, 41, Chicago
"""
```

You want each valid line as a dictionary with `name`, `age`, and `city`. A regex describes the shape of a valid line, and you build a dictionary from its capture groups. Lines that don't match are skipped rather than allowed to crash the program:

```python
import re

pattern = r"^(\w[\w ]*),\s*(\d+),\s*(.+)$"
records = []

for line in raw.strip().splitlines():
    match = re.match(pattern, line.strip())
    if match:
        records.append({
            "name": match.group(1),
            "age": int(match.group(2)),   # convert the captured text to a number
            "city": match.group(3),
        })
    else:
        print(f"Skipping malformed line: {line!r}")

print(records)
# [{'name': 'Alice', 'age': 30, 'city': 'New York'},
#  {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
#  {'name': 'Carlos', 'age': 41, 'city': 'Chicago'}]
```

Three ideas from the week come together here: the **regex** describes a valid line, the capture groups fill a **dictionary**, and checking `if match` handles the **malformed** rows gracefully.

Now that the records are a list of dictionaries, the comprehension and lambda tools apply directly. Build a lookup with a dict comprehension:

```python
age_by_name = {r["name"]: r["age"] for r in records}
# {'Alice': 30, 'Bob': 25, 'Carlos': 41}
```

Or sort the records with a lambda:

```python
oldest_first = sorted(records, key=lambda r: r["age"], reverse=True)
```

## What You've Built

A list of dictionaries, one per record, each with the same keys, is a **table** in all but name — the keys are the columns and each dictionary is a row. That is precisely what Week 2 loads into a Pandas DataFrame, where the analysis of the rest of the course begins.

---

### AI Prompt: Predict-then-Check

Dict comprehensions read a little differently from list comprehensions. Study this without running it:

```python
words = ["apple", "banana", "cherry"]
result = {word: word[0].upper() for word in words}
```

1. Predict exactly what `result` will be — its keys and its values.
2. Explain to an AI chatbot how a dict comprehension decides the key and the value for each entry.
3. Ask: "Is my understanding of how a dict comprehension builds keys and values correct?"

> **Example prompt:** "Looking at this dict comprehension: [paste code]. I predict `result` will be [your prediction] because [your reasoning]. Am I right about how the key and value are chosen for each entry?"

---

## Videos

* [Python Tutorial: Comprehensions — How they work and why you should be using them](https://www.youtube.com/watch?v=3dt4OGnU5sM) — Corey Schafer on list, dict, and set comprehensions.

---

## Check for Understanding

**1. What does `{n: n * n for n in [1, 2, 3]}` produce?**

* A) `[1, 4, 9]`
* B) `{1: 1, 2: 4, 3: 9}`
* C) `{1, 4, 9}`
* D) An error

<details>
<summary>Answer</summary>

B) A dict comprehension makes `key: value` entries — here each number maps to its square.

</details>

**2. What is a lambda?**

* A) A loop that runs once
* B) A small, unnamed function written in one line
* C) A type of list
* D) A regex pattern

<details>
<summary>Answer</summary>

B) A lambda is an anonymous one-line function, useful where a short function is needed inline (like a sort `key`).

</details>

**3. When parsing lines of text into dictionaries, why check `if match` before building the dictionary?**

* A) To make the code run faster
* B) So that lines that don't fit the pattern are skipped instead of causing an error
* C) Because `re.match` requires it
* D) To sort the results

<details>
<summary>Answer</summary>

B) A malformed line won't match the pattern, so `re.match` returns `None`. Checking `if match` lets you skip those lines gracefully rather than crashing.

</details>

---

## Further Reading

* [Python: List, set, and dict comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Python: Lambda expressions](https://docs.python.org/3/reference/expressions.html#lambda)
