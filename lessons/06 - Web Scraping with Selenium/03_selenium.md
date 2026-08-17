# 6.3 Selenium Fundamentals

**Objective**: By the end of this module, you will be able to:

* Set up Selenium and a browser driver with WebDriver Manager.
* Load a page and locate elements with CSS selectors.
* Extract text and attribute values from elements.
* Use XPath when a CSS selector is not enough, and wait for dynamic content to load.

---

You now understand the structure of a page (Module 6.1) and the rules for scraping one (Module 6.2). This module covers the tool: **Selenium**, a library that controls a real web browser from Python.

> **Environment note:** This week's work runs locally in your `python_homework` repository, not in Kaggle, because Selenium needs to launch a real browser on your computer. Install the two libraries in your `python_homework` environment:
>
> ```bash
> pip install selenium
> pip install webdriver-manager
> ```

---

## Why Selenium

You might expect to scrape a page by downloading its HTML directly. For many modern sites that does not work, because the page you see is not fully present in the HTML the server first sends. Instead, the page contains JavaScript that runs *after* loading and fills in the content, sometimes by making further requests for data. To scrape such a page, you need something that loads it, runs its JavaScript, and gives you the finished result. Selenium does this by driving an actual browser.

**WebDriver Manager** handles the browser driver — the component Selenium uses to control the browser — so you do not have to install and update it by hand.

---

## Choosing a Tool: Selenium vs. `requests` and BeautifulSoup

Selenium is not the only way to scrape, and often not the lightest. The other common approach pairs two libraries:

* **`requests`** fetches a page's HTML — the same library you used for APIs in the Intro course.
* **BeautifulSoup** parses that HTML so you can search it for elements and read their text and attributes.

The key difference is JavaScript. `requests` downloads only the HTML the server sends first; it does not run JavaScript. So `requests` + BeautifulSoup works well for **static** pages, where the data is already in that first HTML, and it is faster and simpler than launching a browser. It cannot see content that JavaScript adds after the page loads.

A simple decision rule:

* **Static page** (the data is in the page source) → `requests` + BeautifulSoup.
* **JavaScript-rendered page** (the data is filled in after loading) → Selenium.

This course teaches Selenium because it handles both cases — including the dynamic site in this week's example — and because the harder skill is scraping pages that build themselves with JavaScript. To tell which kind of page you have, view the page source in your browser: if the data you want is missing from the raw source but appears on the rendered page, JavaScript added it, and you need Selenium. The two tools can also be combined: Selenium loads and renders a page, then `driver.page_source` hands the finished HTML to BeautifulSoup to parse.

---

## Setting Up the Driver

This is the standard setup. It launches a Chrome browser that Selenium controls:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
```

By default a browser window opens and you watch the scraping happen, which is useful while developing. To run without a visible window, use **headless** mode:

```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
```

---

## Loading a Page

`driver.get()` loads a URL. It can raise an exception (for example, if the network is down), so wrap it in a `try`/`finally` and always close the browser with `driver.quit()` when you are done:

```python
try:
    driver.get("https://en.wikipedia.org/wiki/Web_scraping")
    # ... extract data ...
except Exception as e:
    print(f"Could not load the page: {type(e).__name__} {e}")
finally:
    driver.quit()
```

---

## Locating Elements with CSS Selectors

To extract data, you first locate the elements that hold it. The most common way is a **CSS selector**, the same syntax used to style pages. `find_element` returns the first match; `find_elements` returns a list of all matches.

Common selector forms:

| Selector | Selects |
|---|---|
| `p` | all `<p>` elements |
| `.book-title` | all elements with `class="book-title"` |
| `[href]` | all elements that have an `href` attribute |
| `div.result` | all `<div>` elements with `class="result"` |

```python
# the first <body> element
body = driver.find_element(By.CSS_SELECTOR, 'body')

# every link inside the body
links = body.find_elements(By.CSS_SELECTOR, 'a')
```

Keep selectors as simple as the page allows. Long, complicated selectors are more likely to break when the site changes — a problem covered in Module 6.4.

---

## Extracting Text and Attributes

Once you have an element, read its text with `.text` and any attribute value with `.get_attribute()`:

```python
first_link = links[0]
print(first_link.text)                 # the visible link text
print(first_link.get_attribute('href'))  # the URL the link points to
```

The page title is available directly as `driver.title`.

---

## Worked Example: Durham County Library

The Durham County Library search results are a realistic target: a list of books, each with a title, one or more authors, and a format and year. This example, and the one in Module 6.4, is the practice you will build on in the assignment.

Start by inspecting the page (Module 6.1). Open the [search results](https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart) in developer tools and find one search result. Each result is an `<li>` element with a class you can read in the Elements tab. Inside it are the title, the author link(s), and a section with the format and year. Note each element's tag and class.

Then extract the results by looping over the `<li>` elements and reading the pieces from each one:

```python
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

results = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')  # class from devtools
books = []

for item in results:
    title = item.find_element(By.CSS_SELECTOR, 'span.title-content').text

    author_links = item.find_elements(By.CSS_SELECTOR, 'a.author-link')
    authors = '; '.join(link.text for link in author_links)   # join multiple authors

    format_year = item.find_element(By.CSS_SELECTOR, 'div.format-info span').text

    books.append({'Title': title, 'Author': authors, 'Format-Year': format_year})

print(books[0])
```

<!-- ===== FLAG (v3): verify Durham selectors ===== -->
> **⚠️ REVIEW** — *The class names above (`cp-search-result-item`, `title-content`, `author-link`, `format-info`) are illustrative. The live Bibliocommons markup must be inspected and the selectors confirmed (and re-confirmed periodically, since the site can change — see Module 6.4). Students find the real classes themselves via developer tools, as in the original Assignment 8. Please verify against the current site before publishing.*

Notice the handling of multiple authors: because a book can have several, `find_elements` returns a list, and the names are joined with `;`.

---

## XPath: When CSS Selectors Are Not Enough

Sometimes the element you want has no useful class or attribute to select. In that case you can find a nearby element that *is* identifiable and move to your target through the page's structure, using **XPath**. XPath can navigate relationships that a CSS selector cannot, such as moving to a parent or a sibling.

The two XPath moves you will need most:

```python
# from a known element, move up to its parent
parent = element.find_element(By.XPATH, '..')

# from a known element, move to the next sibling <div>
sibling = element.find_element(By.XPATH, 'following-sibling::div')
```

For example, if a section is marked only by a heading with a known `id`, you can start at that heading, go up to its parent, then across to the sibling that holds the content. You will use XPath in the assignment to extract a list whose container has no convenient class.

---

## Waiting for Dynamic Content

Because a page's content can be filled in by JavaScript *after* the page loads, an element you want may not exist yet at the moment your code looks for it, which causes an error. Rather than guessing with a fixed `sleep`, tell Selenium to **wait until** the element is present, up to a time limit:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)   # wait up to 10 seconds
results = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'li.cp-search-result-item'))
)
```

`wait.until()` checks repeatedly and continues as soon as the condition is met, or raises a timeout error if the limit passes. This is more reliable than a fixed delay, because it waits exactly as long as needed and no longer.

---

### AI Prompt: Predict-then-Check

CSS selectors target elements based on their type and position. Study this HTML without running any code:

```html
<div class="product-list">
  <p class="description">Item A</p>
  <a href="www.link1.com" class="buy-button">Buy Now</a>
  <p class="description">Item B</p>
  <a href="www.link2.com" class="buy-button">Buy Now</a>
</div>
```

Before writing a script:

1. Predict what `driver.find_elements(By.CSS_SELECTOR, "div.product-list p")` would return.
2. Explain to an AI chatbot why that selector grabs the paragraphs but not the links.
3. Ask: "Is my understanding of how this CSS selector targets nested elements correct?"

> **Example prompt:** "Looking at this HTML: [paste snippet]. I predict the selector `div.product-list p` will select [your prediction] because [your reasoning]. Am I correct? If not, what am I misunderstanding about how CSS selectors target nested elements?"

---

## Check for Understanding

**1. Why do modern web pages often require Selenium rather than downloading the HTML directly?**

* A) HTML files are too large to download
* B) The content is filled in by JavaScript after the page loads, so the initial HTML is incomplete
* C) Selenium is the only way to send a request
* D) Direct downloads are illegal

<details>
<summary>Answer</summary>

B) Selenium runs a real browser that executes the page's JavaScript, so you get the finished content that a direct download would miss.

</details>

**2. You have an element and want the URL it links to. Which do you use?**

* A) `element.text`
* B) `element.get_attribute('href')`
* C) `element.title`
* D) `element.url`

<details>
<summary>Answer</summary>

B) `.get_attribute('href')` reads the attribute value. `.text` would give the visible link text, not the URL.

</details>

**3. An element is added to the page by JavaScript a moment after loading. What is the most reliable way to handle it?**

* A) Use `WebDriverWait` to wait until the element is present
* B) Look for it immediately and let the error happen
* C) Reload the page repeatedly
* D) Use a CSS selector instead of XPath

<details>
<summary>Answer</summary>

A) `WebDriverWait` with an expected condition waits until the element appears (up to a limit), which is more reliable than looking too early or using a fixed delay.

</details>

---

## Further Reading

* [Selenium WebDriver documentation](https://www.selenium.dev/documentation/webdriver/)
* [W3Schools: CSS Selectors](https://www.w3schools.com/css/css_selectors.asp)
* [W3Schools: XPath Introduction](https://www.w3schools.com/xml/xpath_intro.asp)
