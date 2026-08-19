# Scoping Your Analysis

**Objective**: Sharpen your project into a specific question, decide what will count as an insight, and plan the structure of your analysis notebook before you write code.

---

This week is Phase 1 of the final project: a Kaggle notebook that loads your dataset, cleans it, analyzes it, and presents your findings, ending with a written `summary.md`. This first module is about planning, which is where a good project is won or lost. Time spent scoping now saves you from rewriting analysis later.

You are not starting from scratch. You have two things to build on:

* Your **Week 5 proposal**, where you chose your dataset and stated a question.
* Your **Week 8 milestone**, where you loaded the data into SQLite and wrote a few analytical queries.

## Sharpen the Question

Reread your proposal, then restate your central question in one sentence. A good project question is **specific** and **answerable with your dataset**. Compare:

* Too broad: "What is interesting about the movies dataset?"
* Specific and answerable: "Which genres have the highest average return on budget, and has that changed over the last two decades?"

The specific version tells you exactly which columns you need (`genre`, `budget`, `revenue`, `year`) and what the output looks like. If you cannot name the columns your question depends on, the question is still too vague.

## Decide What Counts as an Insight

An **insight** is a finding supported by the data, stated in words — not just a chart. "Here is a bar chart of revenue by genre" is not an insight; "Action films earn the most total revenue, but documentaries have the highest return relative to their budget" is. The Phase 1 rubric asks for **at least three findings, each supported by a chart and by text**, so plan for three questions your analysis can actually answer.

## Plan the Notebook Structure

Sketch the sections your notebook will have before you write them. A dependable structure is:

1. **Load** the dataset and take a first look.
2. **Clean** it, documenting decisions (Module 10.2).
3. **Analyze** it — aggregations, derived features, and the queries from your Week 8 milestone (Module 10.3).
4. **Visualize** each finding.
5. **Summarize** the findings in `summary.md` (Module 10.4).

Having this outline means each later module fills in a section you have already planned.

---

## Stage Checklist

- [ ] Reread your Week 5 proposal and your Week 8 milestone queries.
- [ ] Restate your central question in one clear sentence.
- [ ] List three to five specific questions your analysis will answer, naming the columns each depends on.
- [ ] Confirm your dataset actually contains the fields those questions need.
- [ ] Sketch the sections of your notebook.

---

## Common Pitfalls

* **A question too broad to answer.** "What's interesting here?" has no endpoint. Narrow it until you can name the columns involved.
* **A question the data can't support.** Check that the fields you need exist and are populated before committing to a question.
* **Jumping straight to code.** Without a plan, you will write analysis you throw away. Outline first.
* **Ignoring the Week 8 milestone.** Your SQLite queries are a head start on the analysis — reuse them rather than starting over.

---

## Self-Check

This module supports the **Insights and Interpretation** and **Communication** categories of the [Phase 1 rubric](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md). Before moving on, confirm:

- [ ] I can state my project's question in one sentence.
- [ ] I have three or more specific questions my analysis will answer.
- [ ] Each question names the dataset columns it depends on.
- [ ] I have an outline of my notebook's sections.
