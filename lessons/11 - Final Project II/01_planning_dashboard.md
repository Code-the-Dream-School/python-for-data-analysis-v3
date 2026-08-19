# Planning Your Dashboard

**Objective**: Decide what your dashboard is for (the questions it answers, the filters that matter, and the layout) before you build it.

---

This is Phase 2 of the final project. Last week you produced an analysis and a `summary.md`; this week you turn that analysis into an interactive **dashboard**, deploy it, and present it. As with Phase 1, planning first saves rework.

## What a Dashboard Adds

A notebook and a dashboard do different jobs. A notebook presents *your* analysis in a fixed order — the reader follows the story you wrote. A dashboard lets *the reader* explore: they choose a filter and see the numbers and charts update for their selection. So the first planning question is: **what will a user want to explore in your data?**

Do not try to move your whole notebook into the dashboard. Pick the two or three questions from your analysis where letting the reader change a filter genuinely adds something — a region, a year, a category they can select and compare.

## Choose Your Filters

For each question you want the dashboard to answer, decide which input drives it. A filter should map to a real column in your cleaned data:

* A **selectbox** for a category (region, genre, country).
* A **slider** for a numeric range or a year.
* A **multiselect** when the reader should compare several values at once.

Keep the number of filters small. Two or three well-chosen filters make a focused dashboard; ten make a confusing one.

## Sketch the Layout

Before writing code, sketch the page on paper or in a comment:

* A **title** and a sentence saying what the dashboard shows.
* A **sidebar** for the filters.
* A row of **metrics** (the headline numbers for the current selection).
* One or more **charts** that update with the filters.

Having this sketch means building the dashboard (Module 11.2) is filling in a layout you have already decided.

---

## Stage Checklist

- [ ] Reread your `summary.md` and pick the two or three questions worth making interactive.
- [ ] For each, choose the filter (selectbox, slider, multiselect) and the column it maps to.
- [ ] Decide the headline metrics for the current selection.
- [ ] Sketch the page layout: title, sidebar, metrics, charts.

---

## Common Pitfalls

* **Recreating the whole notebook.** A dashboard is not your analysis pasted into Streamlit. Choose the few views that benefit from interaction.
* **Too many filters.** Each filter adds complexity for the user. Keep to two or three that matter.
* **Filters with no data behind them.** Every filter must map to a real column in your cleaned dataset. Confirm the column exists before planning around it.
* **No plan.** Building without a layout sketch leads to a cluttered page you rearrange repeatedly.

---

## Self-Check

This module supports the **Dashboard and Interactivity** category of the [Phase 2 rubric](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md). Before moving on, confirm:

- [ ] I know the two or three questions my dashboard will let users explore.
- [ ] Each has a filter mapped to a real column in my data.
- [ ] I have chosen the headline metrics.
- [ ] I have a sketch of the page layout.
