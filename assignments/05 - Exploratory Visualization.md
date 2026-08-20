## Lesson 5 Assignment — Exploratory Visualization

This week has **two submissions**:

- **Part A — Visualization Assignment:** a Kaggle notebook exploring the Diabetes Health Indicators dataset.
- **Part B — Final Project Proposal:** a short `proposal.md` submitted as a pull request, which also creates your project repository.

Both are described below. You will submit one Kaggle link (Part A) and one pull request link (Part B).

---

# Part A — Visualization Assignment

Complete Part A in a Kaggle notebook. As usual, mark the code for each task with a markdown cell, and use markdown cells to record what each chart shows.

### **Setup**

Create a Kaggle notebook named `CTD_Assignment_5`. Label each task with a markdown cell (a `## ` heading is added to the notebook's table of contents, which helps your reviewer navigate).

### **Task 1: Understand the Data**

1. In Kaggle, go to **Datasets** and search for **"Diabetes Health Indicators Dataset"** (from Alex Teboul).
2. In Data Explorer, click the file that starts with `diabetes_012`.
3. Read the column descriptions so you know what the data means. Note especially: `Diabetes_012` has three numeric values; `Age` is grouped into 13 buckets; `GenHlth` runs from 1 to 5 (5 is worst); `PhysHlth` counts days of poor physical health in the past month (higher is worse). You cannot interpret a chart unless you know what its numbers mean — this is the first step of exploratory data analysis (Module 5.4).

### **Task 2: Create the Notebook and Load the Data**

1. In your `CTD_Assignment_5` notebook, add the Diabetes Health Indicators dataset with **Add Input**. Run the first cell to list the file paths.
2. Load the `diabetes_012` file into a DataFrame called `diabetes`.
3. Print the first 5 rows.

### **Task 3: A Histogram of Age Distribution**

1. Use Matplotlib to create a histogram of `Age` from the `diabetes` DataFrame, with `Age` on the x-axis and count on the y-axis. Give the chart a meaningful title and label both axes.
2. Display the plot and check that it looks as you expect.

### **Task 4: General Health Over Age**

1. Create a `health_by_age` DataFrame by grouping `diabetes` by `Age` and aggregating `GenHlth` with `mean`.
2. Add a `Health` column equal to `5 - GenHlth`, so that higher values mean better health (easier to read on a chart).
3. Sort `health_by_age` by its index with `sort_index()`. (The index is `Age`, because of the `groupby`.)
4. Create a line plot with `Age` (the index) on the x-axis and `Health` on the y-axis. Add a title and axis labels, and display it.

### **Task 5: A Correlation Heatmap of All Columns**

1. Create a correlation matrix called `diabetes_corr` from all columns (use `.corr()`).
2. Use Seaborn to create a heatmap from it, and display it. (Seaborn may print deprecation warnings; you can ignore them.)
3. Notice that a heatmap of all 22 columns is hard to read — you will narrow it down in the next task.

### **Task 6: Subset Heatmaps**

Suppose the columns you care about most are `Diabetes_012`, `HeartDiseaseorAttack`, and `GenHlth`.

1. Create `diabetes_corr_subset` by selecting those columns from `diabetes_corr`.
2. Sort it in descending order on the `Diabetes_012` column.
3. Create a heatmap of the first 10 rows (the factors most positively correlated with diabetes) and display it with a title.
4. Create a heatmap of the last 10 rows (negatively or weakly correlated factors) and display it with a title.
5. Sort again on the `GenHlth` column, descending, and again show heatmaps of the first and last 10 rows.
6. In a markdown cell, describe the factors that appear most strongly related to diabetes and to general health.

### **Task 7: A Pair Plot — BMI vs. Age**

1. Using the `diabetes` DataFrame, create a Seaborn pair plot for `BMI` and `Age`, with `hue='Diabetes_012'`. The palette `['#FF5733', '#33FF57', '#3357FF']` displays the three groups clearly. Give the plot a descriptive title and display it.
2. This plot is hard to read because `BMI` has many distinct values. Group `BMI` into 10 quantiles and add the result to the DataFrame, then make the pair plot again using the grouped column:

   ```python
   diabetes['BMI_Quantile'] = pd.qcut(diabetes['BMI'], 10, labels=False)
   ```

3. Give the second pair plot a descriptive title and display it.

---

# Part B — Final Project Proposal

This week you begin the **final project**. The project runs in two phases later in the course:

- **Phase 1 (Week 10):** a data pipeline and analysis in a Kaggle notebook — load, clean, wrangle, visualize, and write up findings.
- **Phase 2 (Week 11):** an interactive dashboard built from your analysis and deployed to the web.

You have the tools for Phase 1 already — that is why the project starts now, while the load–clean–wrangle–visualize skills are fresh. This week's deliverable is a short **proposal** that commits you to a dataset and a question.

### **Choose a Dataset**

Choose one of these four curated datasets. All four are available on Kaggle, so you can add them to a notebook with **Add Input** and no downloading:

- **Global Superstore** — retail orders, sales, and profit across regions and categories.
- **TMDB 5000 Movie Dataset** — movies with budget, revenue, genres, and ratings.
- **Life Expectancy (WHO)** — health and economic indicators by country and year.
- **Seattle Airbnb Open Data** — listings, prices, availability, and reviews.

If you would prefer a different dataset, you may request approval for an alternative from your CIL before submitting your proposal. Class sizes make free dataset choice hard to support, and you will have full dataset choice in a later course.

### **Set Up Your Project Repository**

You will build the project in its own repository, set up the **same way you set up `python_homework` in Week 1**. Our starter **`python_final_project`** repository that contains the skeleton files you'll fill in across Weeks 5, 10, and 11 (a `proposal.md`, a `summary.md`, a `README.md`, a `requirements.txt`, and a dashboard stub).

1. Access the starter final project repository: https://github.com/reidrussom/python-for-data-analysis-final-project/tree/main
2. On GitHub, create your own public repository named `python_final_project`.
3. Clone Code the Dream's `python_final_project` starter, then reset the remotes so `origin` points at *your* repository (exactly as you did for `python_homework`), and push.

### **Write Your Proposal**

Open the `proposal.md` file already in your repository and fill in its four sections (about one page total):

1. **Dataset** — which dataset you chose.
2. **Question** — the main question you plan to answer with it. A good question is specific enough to answer with the columns available (for example, "Which product categories are most profitable by region?" rather than "What is interesting about sales?").
3. **Feasibility** — why the dataset can answer your question. Name a few columns you will use and confirm the dataset is large enough and clean enough to work with.
4. **Expected insights** — what you expect to find, or a hypothesis you want to test.

Your CIL will review the proposal to make sure the project is feasible before you invest more time in it.

### **Submit the Proposal as a Pull Request**

1. Create a branch, commit your completed `proposal.md`, and push it to your repository.
2. Open a pull request **in your own `python_final_project` repository** (the base repository should be your username, not `Code-the-Dream-School`).
3. Copy the pull request URL for submission.

---

## Submit Your Work

You submit **two links** this week:

1. **Part A (Kaggle):** Save Version on your `CTD_Assignment_5` notebook, then **Share → Public** with **Allow Comments** on, and copy the public URL.
2. **Part B (pull request):** the URL of the pull request containing your `proposal.md`.

Paste both URLs into the two link fields in the **assignment submission form**.

---
