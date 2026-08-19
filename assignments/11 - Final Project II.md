# Assignment 11 — Final Project II: Dashboard and Presentation

This is Phase 2 of the final project. Before you begin, review the [Final Project Overview](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md) and both rubrics. This week is graded against the **Phase 2 rubric**.

## Requirements

Work in your project repository, using the cleaned data you committed in Week 10.

### Dashboard

- Build a Streamlit dashboard in `streamlit_app.py` that reads your committed cleaned data.
- Include at least one **meaningful filter** (selectbox, slider, or multiselect) that updates what is shown.
- Show **headline metrics** for the current selection with `st.metric`.
- Include at least **three relevant, labeled visualizations** that respond to the filters.
- Give the dashboard a clear title and a sentence describing what it shows.

### Deployment

- Deploy the app to **Streamlit Community Cloud** and confirm the public URL works.
- Record the deployed URL in `README.md` and in a `service_urls.txt` file.
- *If deployment fails near the deadline, you may demonstrate the app locally in your presentation — this affects only the Deployment rubric line, not the whole submission.*

### Repository

Your repository must include:

- `streamlit_app.py` — the dashboard
- `cleaned_data.csv` — the data it reads
- `requirements.txt` — the dependencies (`streamlit`, `pandas`, `plotly`, …)
- `README.md` — summary, setup steps, a screenshot, the deployed URL, and the video link
- `service_urls.txt` — the deployed URL

### Presentation

- Record a **3–5 minute** video using your `summary.md` as the script.
- Cover the question, the key findings (demonstrated live on the dashboard), and the limitations.
- Upload to YouTube (unlisted) or Loom, and add the link to your `README.md`.

## Submission

Phase 2 is a **single pull request** to your project repository. Because the deployed URL and video link are recorded in the repository, the pull request is the only link you submit.

Open the pull request and paste its link into the **assignment submission form**.

## Rubric

This week is graded against the **Phase 2 rubric** in the [Final Project Overview](../resources/final-project-overview.md#phase-2-rubric--week-11-dashboard-and-presentation). Review it before submitting — it covers Dashboard and Interactivity, Dashboard Visualizations, Deployment, Repository and Documentation, and Presentation.
