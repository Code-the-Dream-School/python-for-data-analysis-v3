# 6.4 Building a Reliable Scraper

**Objective**: By the end of this module, you will be able to:

* Handle errors that scraping raises, and the failures Selenium does *not* raise.
* Add delays and handle multiple pages responsibly.
* Write more robust selectors and understand why scrapers break.
* Save scraped data to CSV, JSON, and a SQLite database.

---

A scraper that works once, on one page, on one day, is a start. A reliable scraper handles the things that go wrong: pages that fail to load, elements that are missing, sites that change their layout, and the need to collect many pages without overloading the server. This module turns the Durham County Library example from Module 6.3 into a scraper you can depend on, and saves its results.

---

## Handling Errors

We'll need to handle two kinds of failure:

**Failures that raise an exception.** `driver.get()` can raise if the network fails or the page times out. Wrap scraping in `try`/`except`/`finally`, and close the browser in `finally` so it always shuts down:

```python
try:
    driver.get(url)
    # ... extract data ...
except Exception as e:
    print(f"An error occurred: {type(e).__name__} {e}")
finally:
    driver.quit()
```

**Failures that do *not* raise.** When a page returns an error code like 404 (not found) or 500 (server error), Selenium does **not** raise an exception — it simply loads an error page. Check that you actually got the page you expected, for example by confirming `driver.title` or the presence of an element you know should be there:

```python
if "Search Results" not in driver.title:
    print("The expected page did not load.")
```

Individual elements can also be missing — a book with no listed author, for instance. Guard those with a `try`/`except` so one missing field does not stop the whole scrape:

```python
from selenium.common.exceptions import NoSuchElementException

try:
    format_year = item.find_element(By.CSS_SELECTOR, 'div.format-info span').text
except NoSuchElementException:
    format_year = None
```

---

## Delays and Multiple Pages

Module 6.2 covered why you scrape at a responsible rate. Here is how: when you request more than one page, pause between requests with `sleep`:

```python
from time import sleep

for page_url in page_urls:
    driver.get(page_url)
    # ... extract data ...
    sleep(2)   # wait two seconds before the next page
```

A search result often spans many pages. To collect all of them, find the "next page" link and follow it in a loop, pausing each time — and stop when there is no next page. Always keep the delay: rapid, back-to-back requests place a heavy load on the server and may get you blocked.

---

## Why Scrapers Break

Scrapers are **frail**. They depend on the structure of a page you do not control, and when the site's owner changes that structure — renames a class, moves a section, redesigns the layout — your selectors no longer match, and the scraper fails or returns nothing. This is normal, and you should expect to maintain a scraper over time.

A few habits make a scraper more robust:

* **Prefer stable anchors.** A meaningful `id` or a piece of known text on the page is less likely to change than a long chain of nested `<div>`s.
* **Keep selectors simple.** The more specific and deep a selector, the more ways it can break.
* **Log failures clearly.** When a selector stops matching, a clear error message tells you what to fix instead of leaving you with silent empty results.

---

## Saving Scraped Data

Once you have your results, usually as a list of dictionaries or a DataFrame, save them. Three formats are common.

**CSV** — from a DataFrame:

```python
import pandas as pd

df = pd.DataFrame(books)
df.to_csv('books.csv', index=False)
```

**JSON** — from the list of dictionaries:

```python
import json

with open('books.json', 'w') as f:
    json.dump(books, f, indent=4)
```

**SQLite** — a database file, useful when you scrape from several sources or want to query the results later:

```python
import sqlite3

conn = sqlite3.connect('books.db')
df.to_sql('books', conn, if_exists='replace', index=False)
conn.close()
```

> Databases are the subject of Weeks 7 and 8. For now, `df.to_sql()` is enough to store a scraped dataset in a SQLite file; you will learn to query it properly later.

Choosing a format depends on the use: CSV for a simple table, JSON to preserve nested structure, and SQLite when the data is large or you plan to query it.

---

### AI Prompt: Scaffold Removal

Scrapers break when sites change, and locating an awkward element is often the hard part. When you are stuck, ask for direction rather than a finished answer:

> "My scraper stopped working after the website updated its layout. Give me 3 high-level hints for making my CSS selectors more robust so they break less easily — don't rewrite my code."

or

> "I need to select an element that has no useful class or id, but it sits next to one that does. Here is the HTML: [paste snippet]. Ask me 3 questions that will help me work out which XPath axis (parent, sibling) to use."

The goal is to get better at navigating a changing page yourself, because sites will keep changing.

---

## Videos

> **🆕 REVIEW (v3)** — *No Corey Schafer video covers scraper reliability or error handling. A short Selenium error-handling or "waits and retries" walkthrough would fit here if the team has one.*

---

## Check for Understanding

**1. A page returns a 404 error. What does Selenium do?**

* A) It raises an exception you can catch
* B) It does not raise — it loads the error page, so you must check the result yourself
* C) It retries automatically
* D) It closes the browser

<details>
<summary>Answer</summary>

B) Selenium does not raise on HTTP error codes. Confirm you got the right page (for example, by checking `driver.title` or an expected element).

</details>

**2. Why should you call `sleep()` between requests when scraping multiple pages?**

* A) It makes the data more accurate
* B) It avoids overloading the server and reduces the chance of being blocked
* C) Selenium requires it
* D) It speeds up the scrape

<details>
<summary>Answer</summary>

B) A delay keeps you from sending rapid, back-to-back requests that burden the server. Fast, unthrottled scraping is inconsiderate and can get you blocked.

</details>

**3. Your working scraper suddenly returns no data. What is the most likely cause?**

* A) Python was updated
* B) The website changed its structure, so your selectors no longer match
* C) The data no longer exists anywhere
* D) Selenium expired

<details>
<summary>Answer</summary>

B) Scrapers are frail: when a site changes its layout or class names, the selectors stop matching. Expect to update a scraper when the target site changes.

</details>

---

## Further Reading

* [Selenium: Waits](https://www.selenium.dev/documentation/webdriver/waits/)
* [Python `csv` module](https://docs.python.org/3/library/csv.html)
* [Python `sqlite3` module](https://docs.python.org/3/library/sqlite3.html)
