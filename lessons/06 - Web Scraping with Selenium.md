# Lesson 6 — Web Scraping with Selenium

**Lesson Overview**

So far, your data has come from files and APIs. This week you learn to collect data from web pages directly, using **web scraping**. You will start with how a web page is built—HTML and the DOM–then look at the ethical and legal rules that decide whether and how you should scrape a site. With that groundwork, you will use **Selenium** to load pages, locate elements, and extract data, and finally build a scraper that handles errors, scrapes responsibly, and saves its results. The goal is to be able to turn a live web page into a clean, stored dataset.

This week's work runs **locally in your `python_homework` repository**, not in Kaggle, because Selenium launches a real web browser on your computer. Your assignment is a self-contained scraping project, submitted as a pull request.

**Learning Objectives**

This week, I can...

* Describe how HTML and the DOM structure a web page, and inspect a page with developer tools.
* Apply the ethical and legal rules of scraping: `robots.txt`, terms of service, responsible rate, and personal data.
* Use Selenium to load a page and locate elements with CSS selectors and XPath.
* Build a reliable scraper that handles errors, waits for content, and saves results to CSV, JSON, and SQLite.

## Topics

1. **[HTML and the DOM](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/06%20-%20Web%20Scraping%20with%20Selenium/01_html_dom.md)**

   How a web page is built from HTML elements, how the DOM organizes them into a tree, and how to inspect a live page with your browser's developer tools.

2. **[Scraping Ethically and Legally](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/06%20-%20Web%20Scraping%20with%20Selenium/02_scraping_ethics.md)**

   Reading `robots.txt`, checking terms of service, scraping at a responsible rate, handling personal data, and choosing an API when one is available.

3. **[Selenium Fundamentals](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/06%20-%20Web%20Scraping%20with%20Selenium/03_selenium.md)**

   Setting up Selenium, loading pages, locating elements with CSS selectors and XPath, extracting text and attributes, and waiting for dynamic content — with a note on when the lighter `requests` + BeautifulSoup approach fits instead.

4. **[Building a Reliable Scraper](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/lessons/06%20-%20Web%20Scraping%20with%20Selenium/04_reliable_scraper.md)**

   Handling errors, scraping multiple pages responsibly, writing robust selectors, and saving scraped data to CSV, JSON, and SQLite.

## Summary

This week added a new way to obtain data: collecting it from web pages. You learned how a page is structured as HTML and the DOM, and how to inspect one with developer tools to find where your target data lives. You learned the rules that govern scraping — `robots.txt`, terms of service, responsible request rates, personal data, and preferring an API when one exists, and why those decisions come before any code. You then used Selenium to load pages, locate elements with CSS selectors and XPath, and extract their text and attributes, and you built a scraper that handles errors, waits for dynamic content, scrapes politely, and saves its results.

Web scraping is one path to a dataset. The next weeks turn to where data is often stored and queried: Week 7 introduces relational databases and SQL, and Week 8 goes deeper into SQL and connects it back to Pandas. The SQLite files you saved this week are a first look at the databases you will learn to build and query next.
