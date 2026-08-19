# Lesson 9 — Interactive Visualization and Dashboards

**Lesson Overview**

Week 5 covered static charts for reports. This week you build **interactive** visualizations and the dashboards that hold them. You will start with Plotly for interactive charts, then learn Streamlit, a library that turns a Python script into a web app. The most important idea is Streamlit's execution model — the script reruns from top to bottom on every interaction — and once that clicks, building a dashboard is mostly assembling widgets, filters, metrics, and charts. You will finish by deploying an app to the web. That deployment is a deliberate practice run: doing it now, with a throwaway app, means the graded deployment in the final project is a repeat rather than a first attempt under deadline.

This week's work runs **locally in your `python_homework` repository**, not in Kaggle, because you build and run a Streamlit app on your computer. Your assignment is submitted as a pull request.

**Learning Objectives**

This week, I can...

* Create interactive charts with Plotly and display them.
* Explain Streamlit's rerun-from-top execution model.
* Build an interactive app with widgets, layout, and a DataFrame filter.
* Assemble a dashboard and deploy it to Streamlit Community Cloud.

## Topics

1. **[Interactive Charts with Plotly](<09 - Interactive Visualization and Dashboards/01_plotly.md>)**

   Making interactive charts with `plotly.express`, adding hover data, and displaying a chart from a script by writing it to HTML.

2. **[Your First Streamlit App](<09 - Interactive Visualization and Dashboards/02_first_streamlit_app.md>)**

   Running an app with `streamlit run`, the rerun-from-top execution model, and displaying text and data with `st.write`, `st.dataframe`, and `st.metric`.

3. **[Inputs, Layout, and State](<09 - Interactive Visualization and Dashboards/03_inputs_layout_state.md>)**

   Collecting input with widgets, arranging content with columns and a sidebar, and filtering a DataFrame from a widget's value.

4. **[Building and Deploying](<09 - Interactive Visualization and Dashboards/04_building_deploying.md>)**

   Assembling widgets, metrics, and charts into a dashboard, rendering Plotly with `st.plotly_chart`, and deploying to Streamlit Community Cloud (with an optional look at Dash).

## Summary

This week you learned to build interactive data apps. Plotly produces charts a reader can hover over, zoom, and pan. Streamlit turns a Python script into a web app, and its defining feature is that the whole script reruns on every interaction — which is why a widget value driving a DataFrame filter updates the page automatically, with no separate update code. You assembled these pieces into a dashboard with a sidebar filter, headline metrics, and a chart, and you deployed an app to Streamlit Community Cloud.

That deployment is the single most useful rehearsal in the course. In Week 11 you will deploy your final project's dashboard as a graded submission; having deployed a throwaway app this week, that step becomes a familiar procedure. The Streamlit skills from this week are exactly the ones the final project's dashboard is built from. Next week begins the final project itself: Week 10 is the analysis phase, and Week 11 is the dashboard and presentation.

## Check for Understanding

**1. You are running a Plotly chart from a plain Python script and it hangs on `fig.show()`. What is the reliable alternative?**

* A) `print(fig)`
* B) `fig.write_html("chart.html", auto_open=True)`
* C) `plt.show()`
* D) Restart Python

<details>
<summary>Answer</summary>

B) From a script, write the chart to an HTML file and open it. `fig.show()` can hang because it tries to start a local server. (Module 9.1.)

</details>

**2. In a Streamlit app, what happens when the user changes a widget?**

* A) Only that widget updates
* B) The entire script reruns from top to bottom with the new value
* C) The app waits for a submit button
* D) Nothing changes

<details>
<summary>Answer</summary>

B) Streamlit reruns the whole script on every interaction, so the page always reflects the current input values. (Module 9.2.)

</details>

**3. What is the core pattern that makes a Streamlit page a dashboard?**

* A) Using as many widgets as possible
* B) A widget value drives a DataFrame filter, which is recomputed and redisplayed on each rerun
* C) Deploying to the cloud
* D) Writing charts to HTML files

<details>
<summary>Answer</summary>

B) The dashboard pattern is a widget value filtering the data, recomputed automatically on every rerun. (Module 9.3.)

</details>

**4. Why deploy a throwaway app to Streamlit Community Cloud this week?**

* A) It is the graded final submission
* B) So that deploying the final project's dashboard later is a repeat of a known procedure, not a first-time task under deadline
* C) Because Streamlit only runs in the cloud
* D) To replace the final project

<details>
<summary>Answer</summary>

B) Practicing deployment now removes the risk of a first-time deployment when it counts in the final week. (Module 9.4.)

</details>
