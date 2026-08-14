# 5.1 Choosing the Right Chart

**Objective**: By the end of this module, you will be able to:

* Start from the *question* you're asking, not the chart you want to make.
* Match the five common question types to the charts that answer them.
* Recognize and avoid common chart mismatches.

---

Before you write a single line of plotting code, answer one question: **what am I trying to show?** A chart is an answer, and different questions have different answers. Reaching for a chart type out of habit — a pie chart because it looks nice, a line because it's familiar — is the most common way visualizations end up misleading or confusing. This module has no code. It's about the thinking that comes *first*.

---

## Start from the Question

Almost every data question is one of five types. Name the type, and the chart follows:

| I want to show… | Question type | Reach for… |
|---|---|---|
| How categories compare | **Comparison** | Bar chart |
| How something changes over time | **Trend** | Line chart |
| How values are spread out | **Distribution** | Histogram, box plot |
| How two variables relate | **Relationship** | Scatter plot (heatmap for many pairs) |
| How parts make up a whole | **Composition** | Stacked bar (pie only for 2–3 parts) |

A few words on each:

* **Comparison** — "Which region sold the most?" A **bar chart** puts categories side by side so their heights are easy to compare. Bars are the workhorse of comparison.
* **Trend** — "How did revenue change over the year?" A **line chart** connects points in time order, so the shape of the line *is* the trend.
* **Distribution** — "What's the spread of customer ages?" A **histogram** buckets values into ranges and shows how many fall in each; a **box plot** summarizes the median, spread, and outliers compactly.
* **Relationship** — "Do higher-priced items get lower ratings?" A **scatter plot** puts one variable on each axis and lets you see whether the dots trend together. For many variables at once, a **correlation heatmap** shows every pair.
* **Composition** — "What share of sales came from each category?" A **stacked bar** shows the parts within each whole and still lets you compare totals.

---

## Common Mismatches

Choosing the wrong chart doesn't just look off — it can actively mislead. The usual offenders:

* **Pie charts with many slices.** People judge angles poorly, so a pie with eight near-equal wedges is unreadable. With more than 2–3 categories, a **bar chart** compares far more clearly.
* **Line charts on a categorical axis.** A line implies the x-axis is *ordered and continuous* (like time). Drawing a line across unordered categories — "Sales" → "HR" → "Engineering" — invents a trend that doesn't exist. Use **bars** for categories.
* **Dual y-axes.** Plotting two series against two different vertical scales lets you make them appear correlated (or not) just by choosing the scales. It's a common source of misleading charts — prefer two separate charts, or plot the values as indexed/percentage change on one axis.
* **Too many things at once.** A chart trying to answer three questions usually answers none. One chart, one point.

The test for any chart: *could a reasonable person misread this?* If the axis is truncated, the categories are falsely ordered, or the scales are doing the persuading, the chart is working against you.

---

### AI Prompt: Retrieval Practice

Matching a question to a chart is a skill you build by practicing out loud.

1. Open your preferred AI chatbot.
2. For each of these questions, name the chart you'd use and why: (a) "How have monthly signups changed this year?" (b) "Which of our five products sells best?" (c) "How is delivery time distributed?" (d) "Is there a relationship between ad spend and revenue?"
3. Give your reasoning for each.
4. Ask the AI whether your choices are sound and whether any question could reasonably take a *different* chart.

> **Example prompt:** "I'm learning to choose charts by the question I'm asking. For these four questions, here are the charts I'd pick and why: [your answers]. Did I match each question to an appropriate chart, and are there cases where another chart would work just as well?"

---

## Check for Understanding

**1. You want to show how website traffic changed over the past 12 months. Which chart fits best?**

* A) Pie chart
* B) Line chart
* C) Scatter plot
* D) Histogram

<details>
<summary>Answer</summary>

B) A line chart shows change over time — the ordered x-axis (months) and the connecting line make the trend visible.

</details>

**2. Why is a line chart a poor choice for comparing sales across unordered categories like "Sales," "HR," and "Engineering"?**

* A) Lines can't be colored
* B) A line implies the x-axis is ordered and continuous, inventing a trend between categories that has no meaning
* C) Line charts only work with two categories
* D) It isn't poor — it's the best choice

<details>
<summary>Answer</summary>

B) The connecting line suggests a progression from one category to the next that doesn't exist. Use a bar chart for comparing categories.

</details>

**3. You want to show how a single numeric variable (customer age) is spread across its range. Which chart type is designed for that?**

* A) Bar chart of each individual age
* B) Histogram
* C) Line chart
* D) Pie chart

<details>
<summary>Answer</summary>

B) A histogram buckets the values into ranges and shows how many fall in each — the standard tool for distribution.

</details>

---

## Further Reading

* [From Data to Viz](https://www.data-to-viz.com/) — an interactive guide that leads from your data type to appropriate chart choices (and warns about common mistakes).
* [The Data Visualisation Catalogue](https://datavizcatalogue.com/) — a browsable reference of chart types and what each is for.
