# Deploying Your App

**Objective**: Deploy your dashboard to Streamlit Community Cloud and prepare your repository for submission.

---

Your dashboard runs locally; now make it public. This is the same procedure you practiced in Week 9.4 — that practice run was so that this step, which is graded, is a repeat rather than a first attempt. This module also covers what your repository needs to include for submission.

## Deploy to Streamlit Community Cloud

The steps are the ones from Week 9:

1. **Commit and push** your `streamlit_app.py`, your `cleaned_data.csv`, and a `requirements.txt` to your project repository on GitHub.
2. **Confirm `requirements.txt`** lists the libraries your app imports, so the cloud can install them:
   ```text
   streamlit
   pandas
   plotly
   ```
3. **Go to [share.streamlit.io](https://share.streamlit.io)**, sign in with GitHub, and create a new app pointing at your repository, branch, and `streamlit_app.py`.
4. **Deploy**, then open the public URL and confirm the dashboard loads and the filters work.

> **If deployment gives you trouble:** the presentation (Module 11.4) may demonstrate your app running locally instead. A deployment problem affects only the one Deployment line of the rubric, not your whole submission — so keep working toward a deployed URL, but do not let a last-minute cloud issue block you from finishing.

## Prepare the Repository

Your repository is what gets graded, so make it complete. The `README.md` should include:

* A **summary** of the project — the question and the main findings (you can draw from `summary.md`).
* **Setup steps** — how to install the requirements and run the app.
* A **screenshot** of the dashboard.
* The **deployed URL**.
* The **presentation video link** (added after Module 11.4).

Also record the deployed URL in a `service_urls.txt` file at the top level of the repository. Putting the URL in the repository, rather than the submission form, keeps your graded submission a single pull request.

---

## Stage Checklist

- [ ] Commit `streamlit_app.py`, `cleaned_data.csv`, and `requirements.txt` to the repository.
- [ ] Confirm `requirements.txt` lists every library the app imports.
- [ ] Deploy to Streamlit Community Cloud and confirm the public URL works.
- [ ] Add the deployed URL to `README.md` and `service_urls.txt`.
- [ ] Fill in the README: summary, setup steps, screenshot, deployed URL.

---

## Self-Check

This module supports the **Deployment** and **Repository and Documentation** categories of the [Phase 2 rubric](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md). Before moving on, confirm:

- [ ] My app is deployed with a working public URL (or I can demo it locally as a fallback).
- [ ] `requirements.txt` and `cleaned_data.csv` are committed.
- [ ] The README has a summary, setup steps, a screenshot, and the deployed URL.
- [ ] The deployed URL is recorded in `service_urls.txt`.
