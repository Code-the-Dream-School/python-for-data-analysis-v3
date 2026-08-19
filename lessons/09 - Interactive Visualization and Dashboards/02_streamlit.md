# Loading and Cleaning Your Dataset

**Objective**: Load your chosen dataset into your notebook, apply the cleaning skills from Week 3, and document every cleaning decision in markdown.

---

With your question scoped (Module 10.1), the next step is to get the data into shape. This is Week 3 applied to your own dataset — but with one addition that the rubric rewards heavily: **you document your decisions as you go**. A cleaning step that is not explained is worth less than the same step with a sentence saying why you made it.

## Load and Take a First Look

Add your dataset to the notebook with **Add Input**, read it into a DataFrame, and run your first-look routine from Week 2: `shape`, `head`, `info`, `describe`, and `value_counts` on the important categorical columns. The goal is to know what you have — how big it is, what the columns and types are, and where the problems are — before you change anything.

Keep an untouched copy of the raw data (`raw = df.copy()`) so you can always compare against the original, as in Week 3.

## Clean the Data, and Say Why

Work through the Week 3 toolkit as your data requires:

* **Missing values** — decide, per column, whether to drop or fill, and say which and why.
* **Data types** — convert numbers stored as text and parse dates; watch for placeholder values like `"N/A"` that hide missingness.
* **Text** — standardize casing and whitespace so categories group correctly.
* **Duplicates and validation** — remove duplicate rows and check that values fall in plausible ranges.

After each meaningful step, add a **markdown cell** explaining what you did and why — for example: *"`budget` had 812 zero values, which almost certainly mean 'not recorded' rather than a $0 budget. I replaced them with `NaN` so they don't distort the average."* This is exactly the kind of documented decision the Phase 1 rubric's "Data Preparation" category looks for.

## Save the Cleaned Data

You will need the cleaned dataset again in Phase 2, for the dashboard. Save it to a file (for example, `cleaned_data.csv`) so you can commit it to your project repository. Committing the cleaned data is part of this week's pull request submission.

---

## Stage Checklist

- [ ] Load your dataset and run the first-look routine.
- [ ] Save an untouched raw copy.
- [ ] Handle missing values, wrong types, messy text, and duplicates as needed.
- [ ] Add a markdown cell explaining each cleaning decision.
- [ ] Save the cleaned data to a file for use in Phase 2.

---

## Common Pitfalls

* **Cleaning without documenting.** Undocumented cleaning loses rubric credit and makes your work hard to trust. Explain each decision.
* **Over-cleaning.** Deleting outliers or rows without checking can remove real, meaningful data. Investigate before you remove (Week 3.5).
* **Placeholder values that look valid.** `"unknown"`, `"N/A"`, or `0` used as a stand-in will quietly distort your analysis if you don't convert them to `NaN` first.
* **Forgetting to save the cleaned data.** Phase 2's dashboard reads this file — if you don't save and commit it, you will redo the cleaning next week.

---

## Self-Check

This module supports the **Data Preparation** category of the [Phase 1 rubric](../../resources/final-project-overview.md). Before moving on, confirm:

- [ ] My dataset is loaded and I have inspected it.
- [ ] I have handled missing values, types, text, and duplicates as my data needed.
- [ ] Every cleaning decision has a short markdown explanation.
- [ ] The cleaned data is saved to a file for Phase 2.
