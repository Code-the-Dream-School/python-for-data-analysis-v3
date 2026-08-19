# 9.2 Your First Streamlit App

**Objective**: By the end of this module, you will be able to:

* Run a Streamlit app with `streamlit run`.
* Explain Streamlit's rerun-from-top execution model.
* Display text and data with `st.title`, `st.write`, `st.dataframe`, and `st.metric`.

---

Plotly makes an interactive chart. **Streamlit** turns a Python script into an interactive web app — a page with titles, text, tables, charts, and controls, all written in Python. It is the tool you will use to build your final project's dashboard.

Streamlit runs from your local `python_homework` repository (the environment you set up in Week 1), where you installed `streamlit` in the previous module.

## Running an App

A Streamlit app is just a Python script. Create a file called `app.py` and add:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello from Streamlit.")
```

Run it from the terminal:

```bash
streamlit run app.py
```

Streamlit starts a local web server and opens the app in your browser at `http://localhost:8501`.

---

## The Most Important Idea: the Script Reruns from the Top

This is the concept that makes Streamlit click, and it surprises almost everyone at first. **Every time the user interacts with the app — moves a slider, picks from a dropdown, clicks a button — Streamlit reruns your entire script from top to bottom**, using the new values.

There is no separate "event handler" or callback as in most user-interface tools. You write a straight-through script that reads inputs and produces output, and Streamlit re-executes the whole thing on every interaction. The page you see is always the result of running the current script with the current input values.

This has two practical consequences you will rely on in the next modules:

* Because the whole script reruns, the app always reflects the latest input values — you do not manually update the page.
* Because the whole script reruns, any plain Python variable is recreated from scratch each time. Values do not persist between reruns on their own.

While developing, you can turn on **"Always rerun"** (top-right of the app) so the app re-executes automatically each time you save the file.

---

## Displaying Text and Data

Streamlit provides functions for putting content on the page. For text and structure:

```python
st.title("Dashboard")
st.header("Section 1")
st.subheader("Details")
st.markdown("**Bold** and *italic* text")
st.write("Streamlit's flexible display — handles strings, numbers, and DataFrames.")
```

`st.write` is the general-purpose display function: pass it almost anything and Streamlit renders it sensibly.

For data, two functions matter most. `st.dataframe` displays a DataFrame as an interactive table, and `st.metric` shows a single number as a labeled statistic — the kind of figure a dashboard highlights:

```python
import pandas as pd

df = pd.DataFrame({"Product": ["A", "B", "C"], "Sales": [120, 340, 210]})

st.dataframe(df)
st.metric(label="Total Sales", value=f"${df['Sales'].sum():,}")
```

Streamlit renders output in the order your code runs, so the position of each `st.` call on the page follows its position in the script.

---

### AI Prompt: Retrieval Practice

The rerun model is worth being able to explain in your own words.

1. Open your preferred AI chatbot.
2. Explain how Streamlit runs a script differently from a normal program — specifically, what happens when a user interacts with a control.
3. Explain why this means an ordinary Python variable does not keep its value between interactions.
4. Ask the AI for feedback on your explanation.

> **Example prompt:** "I'm learning how Streamlit executes an app. Here is my explanation of what happens when a user interacts with a widget, and why a normal variable resets each time: [your explanation]. Is my understanding of the rerun-from-top model correct?"

---

## Videos

* ["Code Your First Streamlit Web App with Python," Maggie in Data](https://youtu.be/6MpGhlVXUiw?si=glzoLaEB7naEPLA6)
* ["Build a Streamlit App in Python," Streamlit](https://youtu.be/p2pXpcXPoGk?si=npSmv3STz5dcM3E1)

---

## Check for Understanding

**1. How do you start a Streamlit app named `app.py`?**

* A) `python app.py`
* B) `streamlit run app.py`
* C) `run streamlit app.py`
* D) `streamlit app.py`

<details>
<summary>Answer</summary>

B) `streamlit run app.py` starts the local server and opens the app in your browser.

</details>

**2. What happens when a user moves a slider or picks from a dropdown in a Streamlit app?**

* A) Only the changed widget updates
* B) Streamlit reruns the entire script from top to bottom with the new values
* C) Nothing until you click a "submit" button
* D) The app closes

<details>
<summary>Answer</summary>

B) Streamlit re-executes the whole script on every interaction. The page is always the result of running the current script with the current input values.

</details>

**3. Which function displays a single labeled number, like a dashboard statistic?**

* A) `st.dataframe`
* B) `st.metric`
* C) `st.title`
* D) `st.markdown`

<details>
<summary>Answer</summary>

B) `st.metric(label=..., value=...)` shows one number as a labeled statistic. `st.dataframe` displays a whole table.

</details>

---

## Further Reading

* [Streamlit: Get started](https://docs.streamlit.io/get-started)
* [Streamlit: Main concepts (app model)](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
