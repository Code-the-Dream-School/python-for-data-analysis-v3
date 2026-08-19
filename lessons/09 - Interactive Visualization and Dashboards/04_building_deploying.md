# 9.4 Building and Deploying

**Objective**: By the end of this module, you will be able to:

* Assemble widgets, metrics, and charts into a single dashboard.
* Render a Plotly chart inside Streamlit with `st.plotly_chart`.
* Deploy a Streamlit app to Streamlit Community Cloud.

---

The previous modules covered the pieces: interactive charts, displaying data, widgets, and layout. This module puts them together into a dashboard and then deploys it to the web so anyone can use it.

## Assembling a Dashboard

A dashboard combines a filter, some headline numbers, and a chart into one coherent page. Render a Plotly chart inside Streamlit with `st.plotly_chart(fig)`:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Sales":   [420, 380, 210, 150],
    "Profit":  [80, 60, 45, 30],
})

st.title("Product Dashboard")

# A sidebar filter
product = st.sidebar.selectbox("Product", df["Product"].unique())
row = df[df["Product"] == product]

# Headline metrics, side by side
col1, col2 = st.columns(2)
col1.metric("Sales", f"${row['Sales'].values[0]:,}")
col2.metric("Profit", f"${row['Profit'].values[0]:,}")

# A chart of all products for context
st.subheader("All Products")
fig = px.bar(df, x="Product", y=["Sales", "Profit"], barmode="group")
st.plotly_chart(fig)
```

When the user picks a different product in the sidebar, the whole script reruns: `row` recomputes, the metrics update, and the chart redraws. This is the same rerun pattern from Module 9.3, now assembled into a full page. (Note the shorthand `col1.metric(...)`, which places content in a column without a `with` block.)

---

## Deploying to Streamlit Community Cloud

An app on your own computer is only visible to you. **Streamlit Community Cloud** hosts a Streamlit app for free and gives it a public URL. It deploys directly from a GitHub repository.

To deploy:

1. **Put your app in a public GitHub repository.** Your `python_homework` repo works for this practice app.
2. **Add a `requirements.txt`** listing the libraries the app imports, so the cloud can install them:
   ```text
   streamlit
   pandas
   plotly
   ```
3. **Go to [share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub.
4. **Create a new app**, choose your repository, branch, and the path to your app file (for example, `assignment9/dashboard_app.py`).
5. **Deploy.** After it builds, you get a public URL you can share.

Deploy the simple dashboard above now, confirm the public URL works, and note the steps. You will follow the same procedure for your project dashboard in Week 11.

---

## Optional: Dash

Streamlit is not the only Python dashboard framework. **Dash**, made by the company behind Plotly, is another. It is more configurable and is used for some large production dashboards, but it takes more setup.

The main difference is the execution model. Streamlit reruns the whole script on every interaction (Module 9.2). Dash instead uses **callbacks**: you write functions that are wired to specific inputs and outputs, and each one runs only when its input changes. That model gives finer control at the cost of more code.

This section is optional and not assessed. If you are curious, the [Dash documentation](https://dash.plotly.com/) is a good starting point. For this course and the final project, use Streamlit.

---

### AI Prompt: Scaffold Removal

Deployment is a common place to get stuck, often because of a missing dependency or a wrong file path. When your deployed app fails, ask for direction rather than a rewrite:

> "My Streamlit app runs locally but fails to deploy on Streamlit Community Cloud with a `ModuleNotFoundError`. Don't fix it for me — give me 3 things to check about my `requirements.txt` and repository that commonly cause this."

The goal is to learn to diagnose deployment problems yourself, since you will deploy again for the final project.

---

## Videos

* ["Build a Streamlit App in Python," Streamlit](https://youtu.be/p2pXpcXPoGk?si=npSmv3STz5dcM3E1)

---

## Check for Understanding

**1. How do you display a Plotly figure inside a Streamlit app?**

* A) `fig.show()`
* B) `st.plotly_chart(fig)`
* C) `fig.write_html()`
* D) `st.write(fig.data)`

<details>
<summary>Answer</summary>

B) `st.plotly_chart(fig)` renders the Plotly figure in the app. (`fig.show()` and `write_html` are for viewing outside Streamlit.)

</details>

**2. What does Streamlit Community Cloud deploy from, and what file tells it which libraries to install?**

* A) A local folder; `setup.py`
* B) A GitHub repository; `requirements.txt`
* C) A Kaggle notebook; `environment.yml`
* D) A ZIP file; `packages.txt`

<details>
<summary>Answer</summary>

B) It deploys from a GitHub repository and installs the libraries listed in `requirements.txt`.

</details>

**3. Why deploy a throwaway app this week when the graded dashboard is in the final project?**

* A) It is required for a grade this week
* B) So that deploying in the final week is a repeat of a known procedure rather than a first-time task under deadline
* C) Because local apps do not work
* D) To replace the final project

<details>
<summary>Answer</summary>

B) Practicing deployment now removes the risk of doing it for the first time when it counts. It is a deliberate rehearsal.

</details>

---

## Further Reading

* [Streamlit: Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud)
* [Streamlit: `st.plotly_chart`](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)
