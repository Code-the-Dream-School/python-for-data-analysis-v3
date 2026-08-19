# 9.1 Interactive Charts with Plotly

**Objective**: By the end of this module, you will be able to:

* Create interactive charts with `plotly.express`.
* Add hover information and choose what interactivity provides.
* Display a Plotly chart from a script by writing it to an HTML file.
* Explain why `fig.show()` can hang when run from a plain script.

---

Week 5 covered static charts with Matplotlib and Seaborn, the kind of charts you put in a printed report. This week is about **interactive** charts and the dashboards built from them. An interactive chart lets the reader hover for exact values, zoom into a region, and pan around, which turns a fixed picture into something a user can explore. **Plotly** is the library for making them.

> **Environment note:** This week's work runs locally in your `python_homework` repository, not in Kaggle, because you will build and run a Streamlit app on your computer. Install the libraries you need:
>
> ```bash
> pip install plotly streamlit
> ```

---

## Making a Chart with Plotly Express

`plotly.express` (imported as `px`) creates charts from a DataFrame with one function call, much like `df.plot`, but the result is interactive. The main chart types match the ones from Week 5: `px.scatter`, `px.line`, `px.bar`, and others.

Plotly includes sample datasets, so this example needs no file:

```python
import plotly.express as px
import plotly.data as pldata

df = pldata.iris(return_type="pandas")

fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="Iris: Sepal vs. Petal Length",
    hover_data=["petal_width"],
)
```

* `color="species"` gives each species its own color and a legend.
* `hover_data=["petal_width"]` adds `petal_width` to the tooltip that appears when the reader hovers over a point.

The chart object is stored in `fig`. Nothing is displayed yet — the next step is to show it.

---

## Displaying a Chart from a Script

In a notebook (like Kaggle), `fig.show()` displays a Plotly chart inline. From a **plain Python script**, the reliable way to view a chart is to write it to an HTML file and open it in your browser:

```python
fig.write_html("iris.html", auto_open=True)
```

`auto_open=True` opens the file in your browser automatically. The resulting `iris.html` is a self-contained interactive chart — it embeds the chart's data and the JavaScript that makes it interactive, so you can share the file or embed it elsewhere.

> **Why not `fig.show()` in a script?** When you call `fig.show()` from a plain script (rather than a notebook), Plotly tries to start a small local web server to display the chart, and depending on your environment this often hangs instead of opening the chart. Writing to an HTML file with `write_html` avoids the problem. Inside a Streamlit app, you will use `st.plotly_chart(fig)` instead — covered in the next modules.

---

## What Interactivity Provides

Open `iris.html` and try it: hover over a point to see its values, drag to zoom into a region, and use the toolbar to pan or reset. Interactivity is useful when the reader benefits from exploring the data themselves — checking exact values, focusing on a subset, or comparing groups. A static chart is still the better choice for a printed report or a slide, where nothing can be clicked. The next modules build these interactive charts into a full dashboard with Streamlit.

---

### AI Prompt: Retrieval Practice

Static and interactive charts each have their place.

1. Open your preferred AI chatbot.
2. Explain, in your own words, the main difference between a static chart (Matplotlib/Seaborn) and an interactive one (Plotly), in terms of what the reader can do.
3. Give one situation where a static chart is the better choice, and one where interactivity is genuinely useful.
4. Ask the AI for feedback on your explanation.

> **Example prompt:** "I'm learning the difference between static and interactive charts. Here is my explanation of when I would use a static Matplotlib chart versus an interactive Plotly chart: [your explanation]. Does this accurately reflect the strengths of each?"

---

## Videos

* ["Introduction to Plotly Data Visualization," Charming Data](https://youtu.be/_b2KXL0wHQg?si=U0QxCz-HXbamNLXK)

---

## Check for Understanding

**1. Which library creates interactive charts with hover, zoom, and pan?**

* A) Matplotlib
* B) Seaborn
* C) Plotly
* D) NumPy

<details>
<summary>Answer</summary>

C) Plotly (via `plotly.express`) makes interactive charts. Matplotlib and Seaborn produce static images.

</details>

**2. From a plain Python script, what is a reliable way to view a Plotly chart?**

* A) `fig.show()`
* B) `fig.write_html("chart.html", auto_open=True)`
* C) `print(fig)`
* D) `plt.show()`

<details>
<summary>Answer</summary>

B) Writing to an HTML file and opening it avoids the hang that `fig.show()` can cause when run from a script. (In a notebook, `fig.show()` works inline.)

</details>

**3. When is an interactive chart a better choice than a static one?**

* A) For a printed report
* B) When the reader benefits from exploring — hovering for values, zooming, or filtering
* C) Interactive charts are always better
* D) When the data has only one row

<details>
<summary>Answer</summary>

B) Interactivity helps when the reader explores the data. For fixed media like print or slides, a static chart is more appropriate.

</details>

---

## Further Reading

* [Plotly Express in Python](https://plotly.com/python/plotly-express/)
* [Plotly: Interactive HTML export](https://plotly.com/python/interactive-html-export/)
