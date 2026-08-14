# 3.4 Text Standardization and Regex

**Objective**: By the end of this module, you will be able to:

* Standardize text with `.str` methods like `lower()`, `strip()`, and `upper()`.
* Choose between `map()` and `replace()` and avoid the silent `NaN` trap.
* Clean and extract text with regex using `.str.replace()`, `.str.extract()`, and `.str.contains()`.
* Select columns by name pattern with `df.filter(regex=...)`.

---

Text is the messiest data type. The same city might appear as `"New York"`, `"new york"`, and `" NEW YORK "`; a phone number might be written five different ways. To a computer these are all *different* values, so before you count, group, or match anything, you standardize the text first. This is where Week 1's regex practice applies.

Recall from Module 2.4 that string methods on a Series go through the `.str` accessor.

---

## Basic Normalization

The everyday fixes are lowercasing (or uppercasing) and trimming stray whitespace. `.str` methods chain, so you can do both at once:

```python
import pandas as pd

df = pd.DataFrame({'City': ['New York', ' new york ', 'SAN FRANCISCO', 'San Francisco']})

df['City'] = df['City'].str.lower().str.strip()
df['City'].value_counts()
# City
# new york         2
# san francisco    2
# Name: count, dtype: int64
```

Without that one line, `value_counts()` would report four separate cities instead of two. Inconsistent casing and whitespace split what should be a single group, and every count, `groupby`, and merge that follows inherits the error.

---

## `map()` vs. `replace()`: the Silent `NaN` Trap

Both `map()` and `replace()` can translate values using a dictionary, but they treat values that *aren't in the dictionary* completely differently, and getting this wrong can destroy data without producing an error.

```python
df = pd.DataFrame({'City': ['LA', 'NY', 'Chicago']})

df['City'].map({'LA': 'Los Angeles', 'NY': 'New York'})
# 0    Los Angeles
# 1       New York
# 2            NaN     ← 'Chicago' wasn't in the dictionary, so map() erased it!

df['City'].replace({'LA': 'Los Angeles', 'NY': 'New York'})
# 0    Los Angeles
# 1       New York
# 2        Chicago     ← replace() leaves unmapped values untouched
```

* **`map()`** turns any value *not* in the dictionary into `NaN`. This is useful when you *want* unmapped values flagged as missing, but a problem when you do not expect it.
* **`replace()`** leaves unmapped values unchanged.

The rule of thumb: use **`replace()`** when you're translating *some* values and want to keep the rest. Use **`map()`** with a dictionary only when the dictionary covers every value you intend to keep.

---

### AI Prompt: Predict-then-Check

This trap is worth cementing. Study this code without running it:

```python
import pandas as pd
df = pd.DataFrame({'City': ['LA', 'NY', 'Chicago']})
# Option A
df['City_A'] = df['City'].map({'LA': 'Los Angeles', 'NY': 'New York'})
# Option B
df['City_B'] = df['City'].replace({'LA': 'Los Angeles', 'NY': 'New York'})
```

Before you run it:

1. Predict what happens to `'Chicago'` in `City_A` versus `City_B`.
2. Explain to an AI chatbot why one method produces a `NaN` while the other keeps the original text.
3. Ask: "Is my understanding of the difference between Series `map` and `replace` correct?"
4. Run the code and check.

> **Example prompt:** "Looking at this Pandas code: [paste code]. I predict `City_A` will show [your prediction] and `City_B` will show [your prediction] because [your reasoning]. Am I right about how `map` handles values that aren't in the dictionary?"

---

## Regex with `.str`

For patterns rather than exact values, the `.str` accessor exposes regex-powered methods. Pass `regex=True` where needed and use the pattern skills from Week 1.

**`.str.replace()`** — clean characters by pattern. `\D` matches any non-digit, so this strips everything but the numbers out of messy phone strings:

```python
phones = pd.Series(["(123) 456-7890", "+1-555-123-4567", "555.456.7890"])
phones.str.replace(r"\D", "", regex=True)
# 0    1234567890
# 1    15551234567
# 2    5554567890
# dtype: object
```

**`.str.extract()`** — pull out part of a string with a capture group. Here, the domain from an email:

```python
emails = pd.Series(["john.doe@example.com", "user@my-domain.org"])
emails.str.extract(r"@(\w[\w.-]+)")
#              0
# 0  example.com
# 1   my-domain.org
```

**`.str.contains()`** — filter rows by pattern. `case=False` makes it case-insensitive:

```python
orders = pd.Series(["Order #10 shipped", "Canceled order", "Shipment #22"])
orders[orders.str.contains(r"ship", case=False, regex=True)]
# 0    Order #10 shipped
# 2         Shipment #22
# dtype: object
```

> **Greedy vs. non-greedy.** A pattern like `.*` grabs as much as it can and can over-match. When removing HTML tags, `<.*>` would eat everything from the first `<` to the last `>` — use the non-greedy `<.*?>` to match one tag at a time. This is the greedy/non-greedy idea from Week 1, now on real columns.

---

## Selecting Columns by Name Pattern

Regex also helps you *select* columns whose names follow a pattern. `df.filter(regex=...)` keeps the columns whose names match — useful when a dataset has many similarly-named fields:

```python
df = pd.DataFrame({'created_at': [1], 'updated_at': [2], 'note': [3]})
df.filter(regex=r"_at$")     # keep columns whose names end in "_at"
#    created_at  updated_at
# 0           1           2
```

---

## Standardize, Then Fix Remaining Inconsistencies

A realistic cleanup combines these tools: normalize first, then replace the specific variants that remain.

```python
df = pd.DataFrame({'City': ['New York', 'new york', 'San Francisco', 'San fran']})

df['City'] = df['City'].str.lower().str.strip()             # normalize casing/spacing
df['City'] = df['City'].replace({'san fran': 'san francisco'})  # fix a known shorthand
```

For near-matches too numerous to list by hand (`"San fran"`, `"S.F."`, `"san francisco "`), the next step up is **fuzzy matching** — measuring how similar two strings are and merging the close ones. It's beyond this course, but worth knowing the term exists for when `replace()` mappings become unmanageable.

---

## Videos

* [Python Tutorial: re Module — How to Write and Match Regular Expressions](https://www.youtube.com/watch?v=K8L6KVGG-7o) — Corey Schafer on regex fundamentals (optional supplement for the regex sections above).

---

## Check for Understanding

**1. You run `df['City'].map({'LA': 'Los Angeles'})` on a column that also contains `'NY'`. What happens to the `'NY'` values?**

* A) They stay as `'NY'`
* B) They become `NaN`
* C) They raise an error
* D) They become `'Los Angeles'`

<details>
<summary>Answer</summary>

B) `map()` turns any value not in the dictionary into `NaN`. To keep `'NY'` unchanged, use `replace()` instead.

</details>

**2. Why standardize casing and whitespace (`.str.lower().str.strip()`) *before* running `value_counts()` or `groupby()`?**

* A) It makes the code run faster
* B) Otherwise `"NY"`, `"ny"`, and `" NY "` are counted as three different groups
* C) `value_counts()` requires lowercase input
* D) It's only a style preference

<details>
<summary>Answer</summary>

B) Inconsistent text splits what should be one category into several, corrupting every count and group.

</details>

**3. Which method extracts a piece of each string using a regex capture group?**

* A) `.str.contains()`
* B) `.str.replace()`
* C) `.str.extract()`
* D) `.str.strip()`

<details>
<summary>Answer</summary>

C) `.str.extract()` pulls out the part of the string matched by the capture group `(...)`. `contains` filters, `replace` substitutes, `strip` trims whitespace.

</details>

---

## Further Reading

* [Working with text data](https://pandas.pydata.org/docs/user_guide/text.html) — the full `.str` toolkit.
* [`Series.str.extract` documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html)
* [`Series.str.contains` documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html)
