# Py100 v3 Porting Notes

These are internal notes for porting Py100 v2 into v3. 

Essential links:
* v2 Curriculum Repo: https://github.com/Code-the-Dream-School/python-essentials-v2
* v2 Homework Repo: https://github.com/Code-the-Dream-School/python_homework
* Instructional Design Guidelines: https://docs.google.com/document/d/1u38QtHKfGeXwJf1yTYAyx0YK3yvit5dK6rhM0PZjx8c/edit?usp=sharing

## Planning

**Main Goal:** Revise the existing Python 100 curriculum to account for the new Python Intro course, which makes redundant the first three weeks of Python 100 v2. Replace those three weeks with new content.

**Sub-Goals**:
1. Spread out the final project, which is currently three separate assignments in the same week.
2. Adapt the repo structure to modern CTD standards (lesson sub-pages, contributing guidelines).
3. Make small improvements to language clarity, assessment design, and mentor resources.

## Planned Weekly Structure

| Week | Topic                                     | Description                                                                                                           | Status |
|------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------|
| 1    | Advanced Python and Regex                 | Focus on RegEx, file path handling, advanced data parsing, and review of GitHub workflows.                            | NEW    |
| 2    | Intro to Data Engineering with Pandas     | Load, preview, and inspect datasets (CSV, JSON, APIs). Basic selection, indexing, and handling simple missing values. | NEW    |
| 3    | Data Cleaning and Validation              | Standardize data, handle outliers, apply pattern matching (Regex in Pandas), and encode categorical features.         |        |
| 4    | Data Wrangling and Aggregation            | Multi-table joins/merges, grouping, aggregation, pivot tables, and reshaped data structures.                          |        |
| 5    | Exploratory Visualization                 | Static visualizations, chart selection, visual design principles, and exploratory data analysis (EDA).                |        |
| 6    | Web Scraping with Selenium                | HTML/DOM parsing, dynamic page interaction, ethical scraping (robots.txt), and saving unstructured web data.          |        |
| 7    | Databases and SQL                         | Relational schemas, basic SQL queries, and loading SQL query results directly into Pandas DataFrames.                 |        |
| 8    | Advanced SQL and Integration              | Complex JOINs, window functions, aggregation (HAVING), subqueries, and database writing pipelines.                    |        |
| 9    | Interactive Vizualization and Dashboards  | Building interactive charts with Plotly and assembling web applications/dashboards using Dash (or Streamlit).         |        |
| 10   | Final Project: Pipeline and Proposal      | Define scope, acquire data (Scraping/SQL/API), execute data cleaning, and perform core analysis.                      |        |
| 11   | Final Project: Dashboard and Presentation | Finalize analysis, build interactive Dash dashboard, document repository, and present findings.                       | NEW    |
