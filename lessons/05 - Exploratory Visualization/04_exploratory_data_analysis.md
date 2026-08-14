# 5.4 Exploratory Data Analysis

**Objective**: By the end of this module, you will be able to:

* Describe what exploratory data analysis (EDA) is and why it comes before formal analysis.
* Follow a repeatable EDA loop on a new dataset.
* Use EDA to decide what needs cleaning and what to investigate next.
* Record your findings in markdown cells as you work.

---

**Exploratory data analysis (EDA)** is the work of getting to know a dataset before you try to answer a specific question with it. You examine its size and structure, look at how each variable is distributed, find where data is missing, and check how variables relate to one another. The goal is to understand what you have — including its problems — so that later analysis rests on a clear picture of the data.

EDA brings together skills from the past three weeks. The inspection routine from Week 2, the cleaning tools from Week 3, and the charts from this week are all part of it. EDA is the process that connects them: it is how you discover what a dataset contains and what needs to be fixed.

---

## A Repeatable EDA Loop

EDA is not a fixed checklist, but the following loop works for almost any new dataset. Each step can send you back to an earlier one.

**1. Shape and structure.** Start with the size and the column types, using the routine from Week 2:

```python
df.shape        # how many rows and columns
df.info()       # column names, types, and non-null counts
df.head()       # what a few rows look like
```

**2. Distribution of each variable.** Look at each column on its own. For numeric columns, use `describe()` and a histogram to see the range and shape. For categorical columns, use `value_counts()` and a bar chart to see which values appear and how often:

```python
df['age'].describe()
df['age'].plot(kind='hist', bins=20)

df['category'].value_counts()
```

**3. Missingness.** Find where data is missing, and consider whether it is missing at random or in a pattern:

```python
df.isna().sum()
```

A column missing a few values at random is different from a column missing values only for a certain group. Both matter, and both were the subject of Week 3.

**4. Relationships.** Look at how variables relate. A scatter plot compares two numeric variables; a correlation heatmap (Module 5.3) compares many pairs at once; a `groupby` compares a measure across categories:

```python
df.plot(kind='scatter', x='income', y='spending')
df.groupby('region')['spending'].mean()
```

**5. What question does this raise?** Each finding suggests the next thing to look at. A surprising gap in one column, an unexpected relationship, an outlier group — these point you toward the next step. This is why EDA is a loop rather than a line.

---

## EDA Tells You What to Clean

Week 3 taught cleaning tools, but not *which* cleaning a given dataset needs. EDA answers that. You often do not know a column has placeholder values, an impossible range, or an inconsistent category until you look at its distribution and its missing-value count. In practice, exploration and cleaning happen together: you explore, find a problem, clean it, and explore again to confirm the fix and to see what it reveals.

---

## Write Down What You Find

As you explore, record your observations in **markdown cells** in the notebook, next to the code that produced them. For example: "Age has 62 missing values, all from the 2019 records," or "Income and spending are positively correlated, except for one group of high earners who spend little."

This habit has two benefits. It keeps your own analysis organized, and it produces the written findings that a reader — or a grader — needs to follow your reasoning. The final project rubric rewards clearly documented insights, so building the habit now will pay off directly.

---

### AI Prompt: Retrieval Practice

Being able to describe the EDA process shows you understand it.

1. Open your preferred AI chatbot.
2. Describe, in your own words, the steps you would take to explore a dataset you have never seen before.
3. Explain how EDA helps you decide what to clean.
4. Ask the AI whether your process is complete and what step, if any, you left out.

> **Example prompt:** "I'm learning exploratory data analysis. Here is the process I would follow on a new dataset: [your steps]. I also think EDA helps me decide what to clean because [your reasoning]. Is my process reasonable, and is there a step I should add?"

---

## Check for Understanding

**1. What is the main purpose of exploratory data analysis?**

* A) To produce the final, formatted charts for a report
* B) To understand a dataset's structure, distributions, gaps, and relationships before formal analysis
* C) To train a machine learning model
* D) To delete unnecessary columns

<details>
<summary>Answer</summary>

B) EDA is about understanding what you have — its shape, distributions, missing values, and relationships — so later work is grounded in a clear picture of the data.

</details>

**2. How does EDA relate to the cleaning you learned in Week 3?**

* A) They are unrelated
* B) EDA reveals which cleaning a dataset needs; cleaning and exploration happen together
* C) You must finish all cleaning before any EDA
* D) EDA replaces cleaning

<details>
<summary>Answer</summary>

B) Exploration surfaces the problems (placeholders, impossible ranges, missing patterns) that tell you what to clean, so the two steps interleave.

</details>

**3. Why should you record findings in markdown cells as you explore?**

* A) It makes the notebook run faster
* B) It keeps your analysis organized and produces the documented insights a reader or grader needs
* C) Markdown cells are required for code to run
* D) It hides the code from the reviewer

<details>
<summary>Answer</summary>

B) Written findings keep your reasoning organized and communicate your insights — which the final project rubric rewards.

</details>

---

## Further Reading

* [Pandas: Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) — practice applying the inspection and plotting tools together.
* [Seaborn: Statistical data visualization](https://seaborn.pydata.org/tutorial.html) — plots that support the relationship step of EDA.
