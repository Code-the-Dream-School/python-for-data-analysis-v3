# Lesson 5 — Exploratory Visualization

**Lesson Overview**

You can now load, clean, and wrangle data. This week you learn to *see* it. Visualization is how you find patterns during analysis and how you communicate them afterward. You will start by choosing the right chart for a question, then make quick charts directly from a DataFrame, then build and save presentation-quality charts with Matplotlib and Seaborn. The final module ties the week together with exploratory data analysis (EDA): a repeatable process for getting to know a dataset, which draws on everything from the past three weeks.

This week also begins the **final project**. Alongside the visualization assignment, you will write a short project proposal that selects your dataset and states the question you plan to answer. The proposal instructions and submission steps are on this week's assignment page.

This week's visualization work happens in **Kaggle notebooks**. You have two submissions this week: the Kaggle assignment and the project proposal (submitted as a pull request).

**Learning Objectives**

This week, I can...

* Choose an appropriate chart for a question about comparison, trend, distribution, relationship, or composition.
* Make quick charts directly from a DataFrame with `df.plot()`, including from a `groupby` result.
* Build, label, and save presentation-quality charts with Matplotlib and Seaborn, and apply basic design rules.
* Explore an unfamiliar dataset with a repeatable EDA process and document the findings.

## Topics

1. **[Choosing the Right Chart](<05 - Exploratory Visualization/01_choosing_the_right_chart.md>)**

   Starting from the question you are asking — comparison, trend, distribution, relationship, or composition — and matching it to the chart that answers it, while avoiding common mismatches.

2. **[Quick Charts from a DataFrame](<05 - Exploratory Visualization/02_quick_charts_dataframe.md>)**

   Making line, bar, histogram, scatter, and box charts with `df.plot()`, including plotting a `groupby` result directly for fast exploration.

3. **[Matplotlib and Seaborn for Presentation](<05 - Exploratory Visualization/03_matplotlib_seaborn.md>)**

   Building charts with the figure and axes model, adding titles, labels, legends, and subplots, saving to a file, creating statistical plots with Seaborn, and applying design rules.

4. **[Exploratory Data Analysis](<05 - Exploratory Visualization/04_exploratory_data_analysis.md>)**

   A repeatable process for getting to know a dataset — structure, distributions, missingness, and relationships — and recording findings as you go.

## Summary

This week completed the core analysis toolkit. You can now choose a chart based on the question you are asking, produce one quickly with `df.plot()` while exploring, and build a polished, correctly labeled chart with Matplotlib and Seaborn when it is time to present. The final module brought these together with exploratory data analysis: a repeatable loop of examining structure, distributions, missing values, and relationships that shows you both what a dataset contains and what it needs.

With load, clean, wrangle, and visualize now in place, you have the full set of tools for working with a dataset from start to finish. That is why the final project begins this week, with a proposal that commits you to a dataset and a question. Next week shifts to a new source of data: web scraping, a way to collect datasets that are not already available as files.

## Check for Understanding

**1. You want to show how monthly revenue changed over a year. Which chart is the best fit, and why?**

* A) A pie chart, because it shows proportions
* B) A line chart, because it shows change over an ordered time axis
* C) A histogram, because it shows distribution
* D) A scatter plot, because it shows two variables

<details>
<summary>Answer</summary>

B) A line chart connects points in time order, so it shows the trend across the year. (Module 5.1.)

</details>

**2. You have a `groupby` result and want a bar chart of it for quick exploration. What is the simplest approach?**

* A) Export it to a spreadsheet
* B) Call `.plot(kind='bar')` on the grouped result
* C) Rebuild the data as lists first
* D) Use Seaborn's `pairplot`

<details>
<summary>Answer</summary>

B) A `groupby` result is a Series or DataFrame, so `.plot(kind='bar')` works directly on it. (Module 5.2.)

</details>

**3. Why should a bar chart's y-axis start at zero?**

* A) Matplotlib requires it
* B) A truncated y-axis exaggerates small differences and can mislead the reader
* C) It makes the chart render faster
* D) So the bars fit on the screen

<details>
<summary>Answer</summary>

B) Starting the axis above zero makes small differences look large. Bars should start at zero so their heights represent the values honestly. (Module 5.3.)

</details>

**4. During EDA you find that one column is missing 15% of its values. What is the appropriate response?**

* A) Ignore it, since EDA is only about charts
* B) Note the missingness, consider whether it is random or patterned, and decide how to handle it as part of cleaning
* C) Immediately delete the column
* D) Delete every row of the dataset

<details>
<summary>Answer</summary>

B) EDA surfaces the missingness; you then decide, using the Week 3 tools, whether to fill or drop, based on how much is missing and why. (Module 5.4.)

</details>
