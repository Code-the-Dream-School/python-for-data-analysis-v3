# Final Project Overview

The final project is one project in two phases, one per week. Each week is its own graded submission.

* **Week 10 — Phase 1: Pipeline and Analysis.** In a Kaggle notebook, load your dataset, clean it, analyze it, and visualize the results, then write your findings in a `summary.md`. **Submissions:** the Kaggle notebook link, and a pull request to your project repository containing `summary.md` and your cleaned data.
* **Week 11 — Phase 2: Dashboard and Presentation.** In your project repository, build a Streamlit dashboard from your analysis, deploy it, and record a short presentation. **Submission:** a pull request, with the deployed URL and the presentation video link recorded in the repository.

Your project repository was created with the Week 5 proposal, and the Week 8 milestone (your data in SQLite, with analytical queries) feeds directly into Phase 1.

---

## Choosing Your Dataset

You committed to one of these four datasets in your Week 5 proposal. All are available on Kaggle via **Add Input**:

* **Global Superstore** — retail orders, sales, and profit across regions and categories.
* **TMDB 5000 Movie Dataset** — movies with budget, revenue, genres, and ratings.
* **Life Expectancy (WHO)** — health and economic indicators by country and year.
* **Seattle Airbnb Open Data** — listings, prices, availability, and reviews.

You work with your chosen dataset across both phases. You will have full freedom to choose your own dataset in the follow-on data pipeline course; for this project, the four options keep the analysis focused and make consistent mentor support possible.

---

## Phase 1 Rubric — Week 10 (Pipeline and Analysis)

Graded from your Kaggle notebook and `summary.md`.

| Category | Does Not Meet | Meets | Exceeds |
|---|---|---|---|
| **Data Preparation** | Data is not loaded, or cleaning is missing and problems remain in the data. | Loads the dataset with Pandas and handles missing, duplicate, and malformed values with sensible strategies; cleaning steps are shown. | Cleaning decisions are documented in markdown with brief rationale, and the before/after effect of cleaning is clear. |
| **Analysis and Aggregation** | Little analysis beyond displaying the data. | Uses grouping/aggregation and at least one derived feature to address the question; includes at least two aggregations. | Analysis is layered (multiple aggregations, derived features, and/or the SQL queries from the Week 8 milestone), and each step connects to the question. |
| **Visualization** | No charts, or charts are unlabeled or inappropriate for the data. | At least three appropriate, clearly labeled charts (title, axis labels, legend) that support the findings. | Chart types are chosen deliberately for each question, design principles are applied (readable ticks, honest axes, colorblind-friendly), and each chart is explained. |
| **Insights and Interpretation** | No conclusions, or conclusions not supported by the data. | States at least three findings, each supported by a chart and by text, and connects them to the original question. | Interprets findings in context, discusses limitations and possible biases, and communicates a clear data story. |
| **Communication and Reproducibility** | No `summary.md`, or the notebook does not run or is disorganized. | `summary.md` states the question, the data, the findings, and the limitations; the notebook is organized with markdown narration and runs top to bottom. | The notebook reads as a clear narrative, and the data source and dependencies are specified well enough for another person to reproduce it. |

---

## Phase 2 Rubric — Week 11 (Dashboard and Presentation)

Graded from your project repository, deployed app, and presentation video.

| Category | Does Not Meet | Meets | Exceeds |
|---|---|---|---|
| **Dashboard and Interactivity** | No working dashboard, or no user interaction. | A Streamlit dashboard displays the data and insights, and at least one meaningful filter or widget updates what is shown. | Multiple coordinated filters, a clean and guided layout with clear titles and instructions, and interactions that respond correctly and intuitively. |
| **Dashboard Visualizations** | Fewer than three charts, or charts are unlabeled or irrelevant. | At least three relevant, well-labeled visualizations that support the data story and respond to the filters. | Visualizations are polished and varied, and each clearly advances the story the dashboard tells. |
| **Deployment** | The app does not run, and no working local or deployed version is shown. | The app runs and is demonstrated — deployed to Streamlit Community Cloud, or run locally if deployment is unavailable — with the URL or run instructions recorded in the repository. | Deployed to Streamlit Community Cloud with a working public URL recorded in the README and `service_urls.txt`. |
| **Repository and Documentation** | No README or setup instructions; the project cannot be run from the repository. | The README includes a summary, setup steps, a screenshot, the deployed URL, and the video link; `requirements.txt` lists dependencies; the cleaned data is committed. | The repository is well-organized, and another person could set it up and run it from the README alone. |
| **Presentation** | No video, or the video does not demonstrate the project. | A 3–5 minute video demonstrates the dashboard and communicates the project's question and key findings. | The presentation is clear and well-structured, uses `summary.md` as its throughline, and explains decisions and insights rather than only features. |

> **On deployment (resilience):** the presentation may demonstrate a locally-running app if deployment misbehaves. A deployment problem costs the one **Deployment** rubric line (dropping from Exceeds to Meets), not the whole submission — so a last-minute Streamlit Cloud issue never blocks a passing grade.
