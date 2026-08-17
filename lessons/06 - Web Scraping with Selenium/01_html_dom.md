# 6.1 HTML and the DOM

**Objective**: By the end of this module, you will be able to:

* Describe how a web page is built from HTML elements.
* Identify the three parts of an element: tag, attributes, and content.
* Explain what the DOM is and how it forms a tree.
* Inspect a live page with your browser's developer tools.

---

So far, every dataset in this course arrived as a file or an API response. This week you learn to collect data from web pages themselves, a technique called **web scraping**. Before you can extract data from a page, you need to understand how a page is built.

When you open a URL in a browser, the browser sends a request to a web server, and the server returns an **HTML** document. HTML (HyperText Markup Language) describes the structure and content of the page. The browser reads that document and displays the page. When you scrape a page, you read the same document, not to display it, but to pull specific data out of it. Understanding HTML and the page's structure is the foundation of scraping.

> [!Note]
> If you have taken Code the Dream's Intro to Programming (via JavaScript) course, some of this will be a review. If you're new to HTML and need extra support, check out [The Odin Project's excellent free resources on HTML and CSS](https://www.theodinproject.com/lessons/foundations-introduction-to-html-and-css). For this track, you don't need to be proficient with HTML, but it's quick to learn and useful for any developer.

---

## The Parts of an HTML Element

A web page is made of **elements**. Each element has three parts:

* A **tag** — the name of the element type, written in angle brackets. A paragraph is `<p>`, a link is `<a>`, an image is `<img>`.
* **Attributes** — name-value pairs that give extra information about the element. A link's `href` attribute holds the address it points to; an image's `src` attribute holds the image file; a `class` attribute names a style group.
* **Content** — what the element contains. This may be text, or it may be other elements nested inside it.

Here is a single link element with all three parts:

```html
<a href="https://example.com">Example Link</a>
```

The tag is `a`, the attribute is `href="https://example.com"`, and the content is the text `Example Link`.

Some elements you will see often:

| Element | Purpose |
|---|---|
| `<title>` | The page's title |
| `<h1>`, `<h2>`, `<h3>` | Headings, from most to least important |
| `<p>` | A paragraph of text |
| `<a>` | A link (with an `href` attribute) |
| `<img>` | An image (with a `src` attribute) |
| `<div>`, `<span>` | Generic containers used to group other elements |

---

## The DOM: a Tree of Elements

Because elements contain other elements, a page forms a hierarchy. When the browser parses the HTML, it builds this hierarchy in memory as the **Document Object Model (DOM)** — a tree of elements. Your scraping code will navigate this tree to find the data you want.

```html
<html>
  <head>
    <title>Web Scraping</title>
  </head>
  <body>
    <h1>Introduction</h1>
    <p>This is an example paragraph.</p>
    <a href="https://example.com">Example Link</a>
  </body>
</html>
```

In this tree, `<html>` is the root. It contains `<head>` and `<body>`. `<head>` contains `<title>`; `<body>` contains the heading, paragraph, and link. An element that contains another is its **parent**; the contained element is a **child**. Elements with the same parent are **siblings**. These relationships matter when you locate data, because you often find one element and then move to its parent, child, or sibling to reach the data you actually want.

---

## Inspecting a Live Page

Every browser includes **developer tools** that show the DOM of the page you are viewing. This is how you find where your target data lives before you write any code.

**Activity:**

1. Open the Wikipedia page for [Web scraping](https://en.wikipedia.org/wiki/Web_scraping).
2. Open your browser's developer tools. In Chrome, press `Ctrl-Shift-J` (Windows) or `Cmd-Option-J` (Mac), then click the **Elements** tab. This tab shows the page's DOM.
3. Explore the tree to find:
   - the page `<title>`,
   - the first `<p>` paragraph and how it is structured,
   - the headings (`<h1>`, `<h2>`, `<h3>`) and links (`<a>`).

Looking at the page in developer tools is usually the first step when writing a scraper. You find the element that holds the data you want, note its tag, attributes, and position in the tree, and then write code to reach it. The next modules cover the ethics and the tools for doing that.

---

## Videos

> * ["Inspecting Web Pages with HTML," Alex the Analyst](https://youtu.be/q-kbzWjyPak?si=dBVM93DwYSnS8V-m)

---

## Check for Understanding

**1. In the element `<a href="https://example.com">Docs</a>`, what is `href`?**

* A) The tag
* B) An attribute
* C) The content
* D) A separate element

<details>
<summary>Answer</summary>

B) `href` is an attribute — a name-value pair giving the link's address. The tag is `a`, and the content is the text `Docs`.

</details>

**2. What is the DOM?**

* A) A Python library for scraping
* B) The tree of elements a browser builds from an HTML document
* C) A type of web server
* D) A file format for saving data

<details>
<summary>Answer</summary>

B) The Document Object Model is the tree of elements the browser creates from the HTML. Scraping code navigates this tree.

</details>

**3. In the DOM, two elements that share the same parent are called:**

* A) Children
* B) Ancestors
* C) Siblings
* D) Roots

<details>
<summary>Answer</summary>

C) Siblings. An element that contains another is the parent; the contained element is the child; elements sharing a parent are siblings.

</details>

---

## Further Reading

* [W3Schools HTML Tutorial](https://www.w3schools.com/html/) — a beginner reference for HTML elements.
* [MDN: Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
