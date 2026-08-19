# 1.2 Regular Expressions

**Objective**: By the end of this module, you will be able to:

* Read and write basic regular expressions using character classes, quantifiers, and anchors.
* Extract parts of a match with capture groups.
* Use the `re` module's `search`, `findall`, and `sub` functions.
* Explain the difference between greedy and non-greedy matching.

---

A **regular expression** (regex) is a small language for describing patterns in text. Instead of matching an exact string, you describe its *structure* — "a group of digits," "a word at the start of a line," "anything between two angle brackets" — and let the pattern find every piece of text that fits. Regex is the standard tool for extracting, validating, and cleaning text, and you will use it throughout this course: cleaning messy text in Week 3, and scraping web pages in Week 6.

Python provides regex through the built-in **`re`** module.

> **Test before you code.** Regex is easy to get slightly wrong. Before putting a pattern in your program, try it at [regex101.com](https://regex101.com), which shows exactly what your pattern matches and explains each piece. Getting the pattern right there first will save you time.

---

## Building Blocks of a Pattern

**Literals** match themselves. The pattern `cat` matches the letters `c`, `a`, `t` in order.

**Character classes** match one character out of a set:

* `[aeiou]` — any one vowel.
* `[a-z]` — any one lowercase letter; `[0-9]` — any one digit.
* `[^0-9]` — any character that is *not* a digit (a leading `^` inside the brackets negates the set).

Common classes have shorthands:

| Shorthand | Matches |
|---|---|
| `\d` | a digit (`0-9`) |
| `\w` | a word character (letter, digit, or underscore) |
| `\s` | a whitespace character (space, tab, newline) |
| `\D`, `\W`, `\S` | the opposite of each (a non-digit, non-word, non-space) |

**Quantifiers** say how many times the preceding item may repeat:

| Quantifier | Meaning |
|---|---|
| `*` | zero or more |
| `+` | one or more |
| `?` | zero or one |
| `{3}` | exactly three |
| `{2,4}` | between two and four |

So `\d+` means "one or more digits," and `\d{3}` means "exactly three digits."

**Anchors** match a position rather than a character:

* `^` — the start of the string.
* `$` — the end of the string.
* `\b` — a word boundary (the edge between a word character and a non-word character).

`^Hello` matches only if the string starts with `Hello`; `\bcat\b` matches `cat` as a whole word but not the `cat` inside `category`.

**Capture groups** wrap part of a pattern in parentheses so you can pull it out. `(\d{4})-(\d{2})-(\d{2})` matches a date like `2021-05-01` and captures `2021`, `05`, and `01` as separate groups.

---

## Using the `re` Module

Write patterns as **raw strings** (`r"..."`) so that backslashes are passed through to the regex rather than treated as Python escape characters.

**`re.search`** finds the first match anywhere in the text and returns a match object (or `None` if there is no match):

```python
import re

match = re.search(r"\d+", "Order 12345 shipped")
if match:
    print(match.group())   # '12345'
```

`match.group()` returns the whole match; `match.group(1)` returns the first capture group:

```python
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2021-05-01")
print(m.group(1), m.group(2), m.group(3))   # 2021 05 01
```

**`re.findall`** returns a list of every match:

```python
re.findall(r"\d+", "3 cats, 12 dogs, 100 fish")
# ['3', '12', '100']
```

**`re.sub`** replaces every match with a replacement string. This is a common cleaning tool — here, it removes everything that isn't a digit from a phone number:

```python
re.sub(r"\D", "", "(212) 555-1234")
# '2125551234'
```

---

## Greedy vs. Non-Greedy

By default, quantifiers are **greedy**: they match as much text as possible. Consider extracting an HTML tag from `<b>hi</b>`:

```python
re.findall(r"<.*>", "<b>hi</b>")
# ['<b>hi</b>']   ← matched everything from the first < to the last >
```

`.*` grabbed the whole string because it is greedy. Adding `?` after a quantifier makes it **non-greedy** — it matches as little as possible:

```python
re.findall(r"<.*?>", "<b>hi</b>")
# ['<b>', '</b>']   ← matched each tag separately
```

When a pattern matches more than you intended, an over-greedy quantifier is often the reason. Reach for `*?` or `+?` to match the shortest possible piece.

---

### AI Prompt: Predict-then-Check

Greedy matching is the most common regex surprise. Study this without running it:

```python
import re
text = "Name: Alice, Name: Bob"
result = re.findall(r"Name: (\w+)", text)
```

1. Predict exactly what `result` will be. (Hint: `\w+` is greedy, but `\w` stops at the comma and space. How many matches are there, and what does the capture group return?)
2. Explain to an AI chatbot how `findall` behaves when the pattern has one capture group.
3. Ask: "Is my understanding of what `re.findall` returns when the pattern contains a capture group correct?"

> **Example prompt:** "Looking at this regex: [paste code]. I predict `result` will be [your prediction] because [your reasoning]. Am I right about what `findall` returns when the pattern has a capture group?"

---

## Videos

* [Python Tutorial: re Module — How to Write and Match Regular Expressions](https://www.youtube.com/watch?v=K8L6KVGG-7o) — Corey Schafer on regex and the `re` module.

---

## Check for Understanding

**1. What does the pattern `\d+` match?**

* A) Exactly one digit
* B) One or more digits
* C) Any non-digit character
* D) A literal `d` followed by a `+`

<details>
<summary>Answer</summary>

B) `\d` matches a digit and `+` means "one or more," so `\d+` matches a run of one or more digits.

</details>

**2. Which function replaces every match of a pattern with a replacement string?**

* A) `re.search`
* B) `re.findall`
* C) `re.sub`
* D) `re.match`

<details>
<summary>Answer</summary>

C) `re.sub(pattern, replacement, text)` substitutes every match. `search` finds the first match; `findall` returns all matches.

</details>

**3. `re.findall(r"<.*>", "<a>x</a>")` returns the whole string as one match. How do you make it match each tag separately?**

* A) Use `<.+>`
* B) Use the non-greedy `<.*?>`
* C) Use `re.search` instead
* D) Remove the quantifier

<details>
<summary>Answer</summary>

B) `.*` is greedy and matches as much as possible. The non-greedy `.*?` matches as little as possible, so it captures each tag on its own.

</details>

---

## Further Reading

* [regex101](https://regex101.com) — an interactive regex tester and explainer. Use it while you learn.
* [Python `re` module documentation](https://docs.python.org/3/library/re.html)
* [Python HOWTO: Regular Expressions](https://docs.python.org/3/howto/regex.html)
