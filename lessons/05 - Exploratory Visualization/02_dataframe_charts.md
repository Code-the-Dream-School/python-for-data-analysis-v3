# 5.3 Matplotlib and Seaborn for Presentation

**Objective**: By the end of this module, you will be able to:

* Build a chart with Matplotlib's figure and axes objects.
* Add titles, axis labels, and legends, and arrange multiple plots with subplots.
* Save a finished chart to an image file.
* Create statistical plots with Seaborn (correlation heatmap, pair plot).
* Apply basic design rules that make a chart clear and honest.

---

The `df.plot()` charts from Module 5.2 are good for looking at data while you work. When you need to share a chart — in a report, a slide, or the final project — you need more control over its labels, layout, and appearance. Matplotlib provides that control, and Seaborn adds a set of statistical plots with sensible defaults. Pandas' `df.plot()` uses Matplotlib underneath, so these are the same tools at a lower level.

---

## The Figure and the Axes

Matplotlib separates two objects:

* A **figure** is the whole image — the canvas.
* An **axes** is a single plot inside that figure, with its own x-axis, y-axis, and title.

`plt.subplots()` creates both at once. You then call methods on the axes to build the chart:

```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [1000, 1200, 1500, 1700, 1600, 1800]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, revenue, marker='o')
ax.set_title('Monthly Revenue')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue (USD)')
```

This is the object-oriented style: `fig` is the figure, `ax` is the axes, and you configure the chart through `ax`. It is more explicit than calling `plt.plot()` and `plt.title()` directly, and it is the approach to use when a figure has more than one plot.

---

## Titles, Labels, and Legends

A chart that isn't labeled cannot be understood by anyone but its author. Set a title, label both axes (with units), and add a legend when there is more than one series:

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, revenue, marker='o', label='Revenue')
ax.plot(months, [800, 1000, 1300, 1400, 1500, 1600], marker='s', label='Expenses')
ax.set_title('Monthly Revenue and Expenses')
ax.set_xlabel('Month')
ax.set_ylabel('Amount (USD)')
ax.legend()
```

The `label` given to each `plot()` call is the text that appears in the legend.

---

## Multiple Plots with Subplots

Pass a row and column count to `plt.subplots()` to place several plots in one figure. It returns an array of axes, which you index to reach each plot:

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(['Region A', 'Region B'], [500, 700])
axes[0].set_title('Sales by Region')
axes[0].set_ylabel('Sales (USD)')

axes[1].hist([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5)
axes[1].set_title('Score Distribution')
axes[1].set_xlabel('Score')

fig.tight_layout()
```

`fig.tight_layout()` adjusts the spacing so that titles and labels do not overlap. Call it after creating the plots.

---

## Saving a Chart to a File

Use `savefig()` to write a chart to an image file — useful for reports and for the final project, where charts are saved and referenced:

```python
fig.savefig('revenue.png', dpi=150, bbox_inches='tight')
```

`dpi` sets the resolution, and `bbox_inches='tight'` trims extra whitespace around the chart. In Kaggle, save to the working directory (for example, `'/kaggle/working/revenue.png'`) so the file is available after the notebook runs.

---

## Seaborn for Statistical Plots

Seaborn is built on Matplotlib and works directly with DataFrames. It is most useful for statistical plots that would take more code in plain Matplotlib. The examples below use Seaborn's built-in Titanic dataset; in your own work you would load a DataFrame with Pandas.

**A correlation heatmap** shows how strongly each pair of numeric columns moves together. Correlation is a number between -1 and 1: a positive value means the two variables tend to rise together, a negative value means one rises as the other falls, and a value near 0 means little linear relationship.

```python
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

fig, ax = plt.subplots(figsize=(8, 6))
correlation = titanic.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title('Correlation Between Numeric Columns')
```

`annot=True` writes the numbers in each cell, and `fmt='.2f'` rounds them to two decimals.

**A pair plot** draws a grid of scatter plots for every pair of the columns you list, which is a fast way to scan for relationships:

```python
sns.pairplot(titanic, vars=['age', 'fare'], hue='survived')
```

The `hue` argument colors each point by a category (here, whether the passenger survived), which can reveal group differences.

---

<!-- ===== NEW MATERIAL (v3) — begin: design principles as concrete rules ===== -->
> **🆕 NEW in v3** — *The porting notes ask for design principles stated as concrete rules. Old Lesson 7 covered customization mechanics but no design guidance. Please review.*

## Design Rules for Clear, Honest Charts

Good customization is not decoration — it is making the chart accurate and easy to read. A few rules cover most cases:

* **Label every axis, with units.** A number with no unit (dollars? thousands? percent?) cannot be interpreted.
* **Keep tick labels readable.** Rotate or shorten labels that overlap rather than leaving them unreadable.
* **Do not truncate a bar chart's y-axis.** Bar charts should start at zero. Starting higher exaggerates small differences and misleads the reader. (A line chart showing change over time may start elsewhere, but say so clearly.)
* **Use a colorblind-friendly palette.** Avoid red/green as the only way to tell categories apart. Seaborn's default palettes and Matplotlib's `'viridis'` are safe choices.
* **Remove clutter.** Drop gridlines, borders, and decorations that do not help the reader understand the data. Every element should serve the message.

The test for a finished chart is whether someone unfamiliar with the data could read it correctly without your explanation.
<!-- ===== NEW MATERIAL (v3) — end ===== -->

---

### AI Prompt: Predict-then-Check

Reading a correlation is a skill worth checking. Consider this scenario:

> In a correlation heatmap of the Titanic dataset, you see a correlation of about -0.55 between `pclass` (passenger class, where 1 is first class) and `fare` (ticket price).

Before asking an AI:

1. Predict what this negative correlation means. Does a lower class *number* (first class) go with a higher or lower fare?
2. Explain your reasoning to an AI chatbot.
3. Ask: "Is my interpretation of this negative correlation correct, given that first class is coded as the number 1?"

> **Example prompt:** "In a Titanic correlation heatmap, `pclass` and `fare` have a correlation of about -0.55. I predict this means [your prediction] because [your reasoning]. Am I interpreting the negative correlation correctly, given that first class is coded as 1?"

---

## Videos

* [Matplotlib Tutorial (Part 1): Creating and Customizing Our First Plots](https://www.youtube.com/watch?v=UO98lJQ3QGI) — Corey Schafer on building and labeling Matplotlib charts.

---

## Check for Understanding

**1. In Matplotlib, what is the difference between a *figure* and an *axes*?**

* A) They are two names for the same thing
* B) The figure is the whole image; an axes is a single plot within it
* C) The axes is the whole image; the figure is one plot
* D) Only Seaborn uses axes

<details>
<summary>Answer</summary>

B) The figure is the overall canvas; each axes is an individual plot (with its own title and x/y axes) inside the figure.

</details>

**2. Your two-plot figure has overlapping titles and labels. Which call fixes the spacing?**

* A) `fig.tight_layout()`
* B) `plt.clear()`
* C) `ax.reset()`
* D) `fig.overlap(False)`

<details>
<summary>Answer</summary>

A) `fig.tight_layout()` adjusts spacing so titles and labels don't overlap. Call it after adding the plots.

</details>

**3. Why should a bar chart's y-axis start at zero?**

* A) It's required by Matplotlib
* B) Starting above zero exaggerates small differences and can mislead the reader
* C) Bars can't be drawn otherwise
* D) It makes the chart load faster

<details>
<summary>Answer</summary>

B) A truncated y-axis makes small differences between bars look large. Bar charts should start at zero so the bar heights represent the values honestly.

</details>

---

## Further Reading

* [Matplotlib: Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
* [Seaborn: An introduction](https://seaborn.pydata.org/tutorial/introduction.html)
* [Matplotlib: Choosing colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html) — including colorblind-friendly options.
