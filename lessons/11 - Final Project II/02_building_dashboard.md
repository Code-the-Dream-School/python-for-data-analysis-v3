# Building the Dashboard

**Objective**: Build your planned dashboard in Streamlit, reading your cleaned data and wiring filters to metrics and charts.

---

With the layout planned (Module 11.1), this module builds it. You are applying Week 9 to your own data, so the tools are familiar: `st` display functions, widgets, layout, and `st.plotly_chart`. The one new element is reading your real data.

## Set Up the Project and Read the Data

Work in your project repository, in a file such as `streamlit_app.py`. Read the cleaned data you committed in Week 10 rather than re-cleaning it:

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("cleaned_data.csv")
```

Because the file is in your repository, it will also be available when you deploy (Module 11.3). Reading the already-cleaned data keeps the dashboard code focused on presentation, not cleaning.

## Wire Filters to Output

Build the page in the order you sketched: title, sidebar filters, metrics, then charts. The core pattern is the one from Week 9.3 — a filter value selects rows, and everything below recomputes from the filtered data:

```python
st.title("...")

# Sidebar filter
choice = st.sidebar.selectbox("Region", df["region"].unique())
filtered = df[df["region"] == choice]

# Metrics for the current selection
col1, col2 = st.columns(2)
col1.metric("Total sales", f"${filtered['sales'].sum():,}")
col2.metric("Average rating", round(filtered["rating"].mean(), 2))

# A chart of the filtered data
import plotly.express as px
fig = px.bar(filtered, x="category", y="sales")
st.plotly_chart(fig)
```

Remember the rerun model from Week 9: when the user changes the filter, the whole script reruns, `filtered` recomputes, and the metrics and chart update on their own. You do not write update logic.

## Label and Guide

A dashboard is used by someone who did not write it, so make it self-explanatory: a clear title, a sentence describing what the dashboard shows, and labeled charts. Run it locally with `streamlit run streamlit_app.py` and check that every filter changes the output as you expect.

---

## Stage Checklist

- [ ] Create `streamlit_app.py` in your project repository.
- [ ] Read the cleaned data committed in Week 10.
- [ ] Add the title and a one-sentence description.
- [ ] Add the sidebar filter(s) and compute the filtered DataFrame.
- [ ] Add the metrics and at least one chart, all driven by the filtered data.
- [ ] Run it locally and confirm the filters update the output.

---

## Self-Check

This module supports the **Dashboard and Interactivity** and **Dashboard Visualizations** categories of the [Phase 2 rubric](https://github.com/Code-the-Dream-School/python-for-data-analysis-v3/blob/main/resources/final_project_overview.md). Before moving on, confirm:

- [ ] The app reads my committed cleaned data.
- [ ] At least one filter drives the metrics and charts.
- [ ] There are at least three relevant, labeled visualizations across the dashboard.
- [ ] The app runs locally and the filters update the output.
