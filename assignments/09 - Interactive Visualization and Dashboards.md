## Lesson 9 Assignment — Interactive Visualization and Dashboards

### **Objective**

Build an interactive dashboard with Plotly and Streamlit, and deploy it to Streamlit Community Cloud. Deploying now — while the app is small and disposable — means the graded deployment in the final project will be a repeat of a known procedure.

### **Setup**

This assignment runs locally in your `python_homework` repository.

1. Create an `assignment9` git branch and an `assignment9` folder.
2. Make sure the libraries are installed, and that they are listed in your repo's `requirements.txt` (you will need this for deployment):
   ```bash
   pip install streamlit plotly
   ```
   `requirements.txt` should include at least:
   ```text
   streamlit
   pandas
   plotly
   ```

All tasks use Plotly's built-in **gapminder** dataset, so no data files are needed:

```python
import plotly.express as px
df = px.data.gapminder()   # columns: country, continent, year, lifeExp, pop, gdpPercap
```

---

### **Task 1: An Interactive Plotly Chart**

In a file called `chart.py`:

1. Load the gapminder dataset and filter it to a single year (for example, 2007).
2. Create an interactive **scatter plot** of `gdpPercap` (x) versus `lifeExp` (y), colored by `continent`, with the country name in the hover data. Give it a clear title.
3. Save it to an HTML file with `fig.write_html("gapminder.html", auto_open=True)`, and confirm the chart is interactive (hover, zoom).

### **Task 2: Build a Streamlit Dashboard**

In a file called `streamlit_app.py`, build a dashboard on the gapminder data:

1. Add a title and load the dataset.
2. Add a **sidebar filter** — for example, a `selectbox` to choose a continent (or a slider to choose a year).
3. Filter the DataFrame by the selected value.
4. Show at least **two `st.metric` values** computed from the filtered data (for example, average life expectancy and total population).
5. Add at least **one Plotly chart** of the filtered data, rendered with `st.plotly_chart` (for example, a bar chart of average life expectancy by country, or a scatter of `gdpPercap` vs `lifeExp`).
6. Confirm that changing the sidebar filter updates the metrics and the chart.

Run it locally with:

```bash
streamlit run streamlit_app.py
```

### **Task 3: Deploy to Streamlit Community Cloud**

1. Commit your work and push the `assignment9` branch to GitHub (your `python_homework` repository).
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub, and create a new app pointing at your repository, branch, and `assignment9/streamlit_app.py`.
3. Deploy, and confirm the public URL loads and works.
4. **Record the deployed URL in your repository** — add it to the `assignment9` `README.md` (or a `service_urls.txt` file) so your reviewer can open it. (The deployed URL lives in the repo, not the submission form.)

### **Optional: Reflection**

In a `reflection.md` file, write a few sentences on when an interactive dashboard is more useful than a static chart, and one thing you found tricky about Streamlit's rerun model.

---

### **Submit Your Assignment**

1. **Commit and push** your `assignment9` files (including the deployed URL in the README) to the `assignment9` branch.
2. **Open a pull request** for the `assignment9` branch.
3. **Submit the link.** Paste the pull request URL into the **assignment submission form**.

---
