## Lesson 6 Assignment — Web Scraping Mini-Project

### **Objective**

Build a complete, small web-scraping project from start to finish: choose a site, confirm it is acceptable to scrape, extract a dataset with Selenium, clean it with Pandas, save it to CSV and a SQLite database, and document the whole thing in a README. This brings together everything from this week and applies the cleaning skills from Week 3.

### **Setup**

This assignment runs locally in your `python_homework` repository (not Kaggle), because Selenium launches a real browser.

1. Create an `assignment6` git branch, and an `assignment6` folder inside `python_homework`.
2. Make sure the scraping libraries are installed in your environment:
   ```bash
   pip install selenium
   pip install webdriver-manager
   ```
3. Put your code in the `assignment6` folder. Mark each part of your program with a comment describing what it does.

---

### **Step 1: Choose and Check Your Site**

You will scrape a small dataset from this practice site:

- **[books.toscrape.com](http://books.toscrape.com/)** — a sandbox built specifically for scraping practice. It lists 1,000 books across many pages, each with a title, price, star rating, and availability. Because it exists for practice, there are no ethical concerns, and its layout is stable.

Apply Module 6.2 before writing code:

1. Read the site's `robots.txt` and confirm the pages you want are allowed.
2. Check the site's terms of service.
3. Confirm the data is not personal data.

Write down what you found — you will include it in your README.

### **Step 2: Inspect the Page**

Using your browser's developer tools (Module 6.1), find the elements that hold the data you want. For each field you plan to collect, note the tag and the class or attribute that identifies it. A good target is each book's **title**, **price**, **rating**, and **availability**.

### **Step 3: Scrape the Data**

Write a Selenium program (for example, `scrape.py`) that:

1. Sets up the driver and loads your starting page (Module 6.3).
2. Locates the repeated elements that hold each record (for the book site, each book is an element in a list).
3. Extracts your chosen fields from each record into a dictionary, and appends each dictionary to a `results` list.
4. Handles missing fields gracefully with `try`/`except`, so one incomplete record does not stop the program (Module 6.4).
5. Collects at least **50 records**. For the book site, this means following the "next" page link across several pages — **pause with `sleep()` between pages** so you scrape responsibly.

Print your `results` as you build the program so you can confirm each step works before moving on.

### **Step 4: Clean the Data**

Load your `results` into a Pandas DataFrame and apply the cleaning skills from Week 3. At a minimum:

1. Convert any numeric field stored as text to a number (for the book site, `price` comes in as text like `"£51.77"` — strip the symbol and convert to a float).
2. Check for and handle missing values and duplicates.
3. Standardize at least one text field (for example, trim whitespace or normalize casing).

Show the data before and after cleaning (for example, with `head()` and `isna().sum()`), so your reviewer can see what you changed.

### **Step 5: Save the Data**

Save your cleaned DataFrame two ways (Module 6.4):

1. To a CSV file (for example, `books.csv`).
2. To a SQLite database file (for example, `books.db`), using `df.to_sql()`.

### **Step 6: Write a README**

Create a `README.md` in your `assignment6` folder that documents the project:

- The site you scraped and a one-line statement that `robots.txt` and the terms of service permit it.
- The fields you collected.
- How to run your program.
- The cleaning steps you applied.
- A short note on anything that was difficult and how you handled it.

### **Optional Stretch**

- Scrape **all** available pages rather than a fixed number, stopping automatically when there is no next page (keep the delay between pages).
- Try a JavaScript-rendered page, such as [quotes.toscrape.com/js](http://quotes.toscrape.com/js/), and use `WebDriverWait` to wait for the content to load before scraping (Module 6.3).

---

### **What Your Submission Should Include**

- A Selenium program that scrapes at least 50 records, handles missing fields, and pauses between pages.
- Cleaning code that converts types and handles missing values and duplicates.
- A `books.csv` (or equivalent) and a SQLite database file.
- A `README.md` documenting the project and confirming the site is acceptable to scrape.

---

### **Submit Your Assignment**

1. **Commit and push.** Within `python_homework`, `git add` and `git commit` your `assignment6` files to the `assignment6` branch, then push the branch to GitHub.
2. **Open a pull request** for the `assignment6` branch against your main branch.
3. **Submit the link.** Copy the pull request URL and paste it into the **assignment submission form**.

---
