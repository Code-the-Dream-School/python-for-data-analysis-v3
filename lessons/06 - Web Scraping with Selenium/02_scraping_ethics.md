# 6.2 Scraping Ethically and Legally

**Objective**: By the end of this module, you will be able to:

* Read a site's `robots.txt` file and respect its rules.
* Check a site's terms of service before scraping.
* Scrape at a responsible rate and identify your scraper.
* Recognize when data is personal and when an official API is the better choice.

---

Web scraping is powerful, and that makes it easy to misuse. A scraper can send thousands of requests in a minute, collect data a site never intended to publish in bulk, or violate rules the site owner has clearly stated. This module comes *before* the tools on purpose: you should decide whether and how to scrape a site before you write any code.

---

## `robots.txt`

Most websites publish a file called `robots.txt` at the root of the domain — for example, `https://en.wikipedia.org/robots.txt`. It states which parts of the site automated programs are allowed to access. You can read it by opening the URL in your browser; no code is required.

A `robots.txt` file looks like this:

```text
User-agent: *
Disallow: /search
Disallow: /admin
```

* `User-agent` names which automated programs the rule applies to. `*` means all of them.
* `Disallow` lists paths that should not be accessed by those programs.

Before scraping any site, read its `robots.txt` and stay within what it allows.

**Activity:** Open [Wikipedia's robots.txt](https://en.wikipedia.org/robots.txt). Identify which sections are restricted, and notice that some rules apply to specific user agents. Consider why a site might restrict those particular sections.

---

## Terms of Service

`robots.txt` is a useful starting point, but it isn't the highest-level guideline. Many sites have **terms of service** (ToS) — a legal agreement that may prohibit automated collection of their data regardless of what `robots.txt` says. A site can allow a path in `robots.txt` and still forbid scraping in its ToS. Check the site's terms before collecting data, especially if you plan to publish or share it. When the terms forbid scraping, do not scrape the site.

## Scrape at a Responsible Rate

A browser makes one request when a person opens a page. A scraper can make hundreds per minute, which places real load on the server and can disrupt the site for its actual users. Scrape considerately:

* **Add a delay between requests** so you are not sending them as fast as the computer allows. A short pause (for example, one to two seconds) between pages is a reasonable default.
* **Request only what you need**, and avoid fetching the same page repeatedly.
* **Prefer off-peak times** for large jobs when possible.

Sending many rapid requests is both inconsiderate and a good way to get your access blocked.

## Identify Your Scraper

Every request includes a **User-Agent** string that identifies the program making it. Some sites ask automated tools to identify themselves honestly rather than pretending to be an ordinary browser. Being identifiable is part of scraping in good faith, and some sites use it to offer a documented, permitted path for automated access.

## Personal Data

Just because data is visible on a page does not mean you may collect and store it. **Personal data** — names, contact details, and other information about identifiable people — is subject to privacy laws (such as the GDPR in Europe) and to ordinary ethical limits. Avoid collecting personal data unless you have a clear, lawful reason and have confirmed it is permitted. When in doubt, do not collect it.

## When an API Is the Better Choice

Many sites provide an **API** — a documented, official way to request their data, usually as JSON. When an API exists, it is almost always the better choice than scraping:

* It is explicitly permitted, so you are not working against the site's wishes.
* It returns clean, structured data instead of HTML you have to parse.
* It does not break when the site changes its page layout.

Check whether a site offers an API before you decide to scrape it. Scraping is the right tool when there is no API and the site's rules permit it.

---

## A Pre-Scraping Checklist

Before scraping a site, confirm:

1. Does an official **API** provide this data instead? If so, use it.
2. Does **`robots.txt`** allow the paths you need?
3. Do the **terms of service** permit automated collection?
4. Is any of the data **personal**? If so, reconsider.
5. Will you scrape at a **responsible rate**, with delays between requests?

---

### AI Prompt: Retrieval Practice

Understanding the ethics of scraping is as important as the code.

1. Open your preferred AI chatbot.
2. Explain what a `robots.txt` file is and why a developer should check it before starting a scraping project.
3. Ask the AI: "Can you give a scenario where ignoring `robots.txt` or a site's terms of service could cause problems for the website owner or for the person scraping?"

> **Example prompt:** "I'm learning about ethical web scraping. I understand that `robots.txt` is used for [your explanation]. Why is it important to follow these rules and a site's terms of service, and what is one real-world risk of ignoring them?"

---

## Check for Understanding

**1. What is the purpose of a site's `robots.txt` file?**

* A) It stores the site's data for scrapers to download
* B) It states which parts of the site automated programs may access
* C) It is required to run Selenium
* D) It blocks all scraping automatically

<details>
<summary>Answer</summary>

B) `robots.txt` tells automated programs which paths they are and are not allowed to access. You should read and respect it before scraping.

</details>

**2. A site's `robots.txt` allows the page you want, but its terms of service prohibit automated data collection. What should you do?**

* A) Scrape it anyway, since `robots.txt` allows it
* B) Do not scrape it — the terms of service also govern what is permitted
* C) Scrape it only once
* D) Ignore the terms of service

<details>
<summary>Answer</summary>

B) The terms of service are a separate, binding rule. If they forbid scraping, do not scrape the site even when `robots.txt` allows the path.

</details>

**3. A site offers an official API that returns the data you want as JSON. Why is that usually better than scraping the site's pages?**

* A) It is slower but more detailed
* B) It is permitted, returns structured data, and does not break when the page layout changes
* C) APIs are always free
* D) It avoids the need to write any code

<details>
<summary>Answer</summary>

B) An API is an approved, stable, structured source. Scraping is the right choice only when no API exists and the site's rules permit it.

</details>

---

## Further Reading

* [MDN: What is robots.txt?](https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt)
* [OWASP robots.txt](https://owasp.org/robots.txt) — an example to read.
