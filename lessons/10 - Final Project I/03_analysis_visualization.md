# Analysis and Visualization

**Objective**: Answer your question with aggregations, derived features, and the SQL queries from your Week 8 milestone, and support each finding with a clear chart.

---

This is the core of Phase 1: turning clean data into findings. It applies Weeks 4, 5, and 8 to your own dataset. The target set by the Phase 1 rubric is concrete — **at least three findings, each supported by a chart and by text** — so let that guide how much analysis is enough.

## Explore, Then Focus

Start with the EDA loop from Week 5.4: look at distributions, missingness patterns, and relationships between variables. Exploration is how you discover what is actually in the data and which of your planned questions the data can answer well. Some questions will turn out to be more interesting than you expected, and some less; follow what the data supports.

## Analyze

Use the tools from Week 4 to answer each question:

* **Aggregations** — `groupby` with `sum`, `mean`, `count`, and `agg` to summarize by category.
* **Derived features** — new columns that make a pattern visible (a ratio, a band from `pd.cut`, a row-wise calculation with `apply`).
* **The Week 8 queries** — your SQLite milestone already contains real analytical queries (a grouped aggregate with `HAVING`, a window function). Bring those results into the notebook; they count toward the analysis and toward the rubric's "Exceeds" bar.

Aim for at least two aggregations or derived features that directly serve your question.

## Visualize Each Finding

Every finding should be backed by a chart. Apply Week 5:

* **Choose the right chart** for each question (comparison, trend, distribution, relationship, composition).
* **Label it fully** — title, axis labels with units, a legend where needed — and apply the design rules (readable ticks, honest axes, colorblind-friendly colors).
* **Explain it.** After each chart, add a markdown cell stating what the chart shows and how it answers your question. A chart without interpretation is not yet a finding.

Three well-chosen, well-explained charts beat ten unfocused ones. Each should earn its place by supporting a specific finding.

---

## Stage Checklist

- [ ] Run the EDA loop to understand distributions, missingness, and relationships.
- [ ] Produce at least two aggregations or derived features that serve your question.
- [ ] Bring in the analytical queries from your Week 8 milestone.
- [ ] Create at least three appropriate, fully labeled charts, one per finding.
- [ ] After each chart, write a markdown cell interpreting it.
- [ ] Confirm you have at least three findings supported by both a chart and text.

---

## Self-Check

This module supports the **Analysis and Aggregation**, **Visualization**, and **Insights and Interpretation** categories of the [Phase 1 rubric](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md). Before moving on, confirm:

- [ ] My analysis uses at least two aggregations or derived features.
- [ ] I have at least three charts, each appropriate and fully labeled.
- [ ] Each chart is followed by an explanation of what it shows.
- [ ] I can state at least three findings, each supported by a chart and text.
