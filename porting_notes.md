# Py100 v3 Porting Notes

Internal notes for porting Py100 v2 into v3.

## Essential Links

* v2 Curriculum Repo: https://github.com/Code-the-Dream-School/python-essentials-v2
* v2 Homework Repo: https://github.com/Code-the-Dream-School/python_homework
* Python Intro v1 Repo (structure reference): https://github.com/Code-the-Dream-School/python-intro-v1
* Instructional Design Guidelines: https://docs.google.com/document/d/1u38QtHKfGeXwJf1yTYAyx0YK3yvit5dK6rhM0PZjx8c/edit?usp=sharing

## Goals

**Main Goal:** Revise the Python 100 curriculum to account for the new Python Intro
course, which makes redundant the first three weeks of Py100 v2. Replace those three
weeks with new content.

**Sub-Goals:**

1. Spread out the final project, which is currently three separate deliverables landing
   in the same week.
2. Adapt the repo structure to modern CTD standards (lesson sub-pages, contributing
   guidelines).
3. Make small improvements to language clarity, assessment design, and mentor resources.



## Page Structure and Conventions

Mirrors Python Intro v1.

```
lessons/
  01 - Advanced Python and Regex.md          <- week landing page
  01 - Advanced Python and Regex/            <- module folder
    01_setting_up_for_data_work.md
    02_regular_expressions.md
    03_working_with_file_paths.md
    04_comprehensions_lambdas_parsing.md
assignments/
  01AdvancedPythonAndRegex.md                <- one page per week, unchanged
```

**Landing page template**

```markdown
# Lesson N — Title

**Lesson Overview**

[Short narrative paragraph: why this week matters, what it unlocks.]

**Learning Objectives**

This week, I can...

* [objective]

## Topics

1. **[Module Title](link)**

   [One-line description of what the module covers.]

## Summary

[Wrap-up synthesis. NEW in v3 — Python Intro landing pages don't have this.]

## Check for Understanding

[Week-level CFU tying the modules together.]
```

**Module template**

```markdown
# Module Title

**Objective**: By the end of this lesson, you will be able to:
  * [objective]



## [Content sections, separated by ]

### AI Prompt: [Retrieval Practice | Predict-then-Check | Scaffold Removal]
[Placed mid-module where it fits, not appended at the end. Not every module.]

## Videos

## Check for Understanding
[4 multiple-choice questions with collapsible <details> answers.]

## Further Reading
```

**Project weeks (10 and 11) use an adapted module shape.** No Videos section, and the
Check for Understanding is replaced by a self-check list against the relevant rubric
section — a multiple-choice question about a student's own project doesn't make sense.
Each module carries: objective, guidance, a stage checklist, and common pitfalls.



## Planned Weekly Structure

| Week | Topic | Environment | Submission 1 | Submission 2 |
|---|---|---|---|---|
| 1 | Advanced Python and Regex | `python_homework` + Kaggle setup | PR | Kaggle (setup check) |
| 2 | Intro to Data Engineering with Pandas | Kaggle | Kaggle | — |
| 3 | Data Cleaning and Validation | Kaggle | Kaggle | — |
| 4 | Data Wrangling and Aggregation | Kaggle | Kaggle | — |
| 5 | Exploratory Visualization | Kaggle + project repo | Kaggle | PR (`proposal.md`) |
| 6 | Web Scraping with Selenium | `python_homework` | PR (mini project) | — |
| 7 | Databases and SQL | Kaggle | Kaggle | — |
| 8 | Advanced SQL and Integration | Kaggle | Kaggle (assignment) | Kaggle (project milestone) |
| 9 | Interactive Visualization and Dashboards | `python_homework` | PR | — |
| 10 | Final Project: Pipeline and Analysis | Kaggle + project repo | Kaggle (analysis) | PR (`summary.md` + cleaned data) |
| 11 | Final Project: Dashboard and Presentation | Project repo | PR | — |

**LMS constraint:** two URLs per week maximum, each must be a GitHub PR or a Kaggle
notebook. Weeks 5, 8, and 10 are at capacity — do not add a third deliverable to those
weeks without removing something.

Deployed app URLs and the presentation video URL go in the project repo (`service_urls.txt`
and the README), not in the submission form. This keeps every graded submission a PR or a
Kaggle link.

**Environments — three places, each set up once:**

* `python_homework` (local, venv, created Week 1) — Weeks 1, 6, 9
* Kaggle notebooks (account verified Week 1) — Weeks 2–5, 7–8, 10
* Final project repo (created Week 5) — Weeks 5, 10, 11

v2 had four environments with two of them scaffolded mid-course, including a brand-new
repo built from scratch in the final week. Nothing in v3 is created after Week 5.



## Module Map

### Week 1 — Advanced Python and Regex `NEW`

Bridge week from Python Intro. Scoped against the Intro course's stated objectives:
students arrive with data structures, functions and scope, list comprehensions,
`try`/`except`, `requests` and JSON, file I/O via the `csv` module, and the full Git/PR
workflow. They do **not** arrive with regex, `pathlib`, lambdas, hands-on virtual
environments (Intro covers venv conceptually only), or any exposure to Jupyter notebooks.

1. **Setting Up for Data Work** — Kaggle notebooks as the primary environment (cells,
   kernels, execution order, `Add Input`, Save Version). The `python_homework` repo and
   venv as the secondary one. Git workflow refresher framed around the new repo.
2. **Regular Expressions** — Literals, character classes, quantifiers, anchors, capture
   groups. The `re` module: `search`, `findall`, `sub`. Greedy vs. non-greedy. Testing
   patterns in regex101 before writing code.
3. **Working with File Paths** — `pathlib.Path`, relative vs. absolute, cross-platform
   separators, globbing, reading a directory of files.
4. **Comprehensions, Lambdas, and Parsing Messy Data** — Dict comprehensions and lambdas
   taught in service of a real task: regex-extract fields from semi-structured text into a
   list of dicts, handle malformed rows, write results out. Ends with students holding
   something that looks exactly like a table, which Week 2 turns into a DataFrame.

### Week 2 — Intro to Data Engineering with Pandas

1. **Series and DataFrames** — The two structures, built from dicts, lists, and NumPy
   arrays. Why not a list of dicts. NumPy relationship, kept brief.
2. **Loading and Saving Data** — `read_csv` and its common parameters, `read_json`,
   DataFrame from a dict, the `sep` parameter, `to_csv`, and reading from an API.
3. **Inspecting a Dataset** — `head`, `tail`, `info`, `describe`, `shape`, `dtypes`,
   `value_counts`, framed as a repeatable first-look routine rather than isolated methods.
4. **Selecting and Filtering** — `.loc`, `.iloc`, `.at`, `.iat`, column selection, boolean
   filtering. The `&` vs. `and` and `.str.upper()` traps promoted from code comments into
   real teaching. Ends with `isna().sum()` as the handoff into Week 3.

### Week 3 — Data Cleaning and Validation

Busy week. Absorbs all cleaning material stripped out of old Lesson 4.1 plus the
column-transformation toolkit from old 6.6 and 6.7.

1. **Missing Data** — `isna`/`notna`, `dropna`, `fillna` with constant/mean/median,
   `ffill`/`bfill`, and the judgment call of drop vs. fill.
2. **Data Types and Dates** — `astype`, `to_numeric` and `to_datetime` with
   `errors="coerce"`, `NaT`, `format="mixed"`, and recognizing placeholder values
   (`"N/A"`, `"-"`, `"unknown"`) that hide missingness behind a valid string.
3. **Transforming Columns** — Add, replace, drop a column. Operators on a Series. `.map()`
   with a dict and with a function. Lambdas. NumPy functions on a Series. `.apply()` on a
   Series.
4. **Text Standardization and Regex** — `.str` methods, `map` vs. `replace` and the silent
   `NaN` trap, `.str.replace`/`.str.extract`/`.str.contains`, `df.filter(regex=)`. Week 1's
   regex pays off here.
5. **Validation, Duplicates, and Outliers** — Range and allowed-value checks,
   `duplicated`/`drop_duplicates`, simple outlier rules, and the discipline of keeping an
   untouched raw copy.

**Ordering note:** module 3 must precede 4 and 5. Old Lesson 5 uses `.apply(lambda ...)` in
its validation and outlier examples before ever teaching `apply` or lambdas. Invisible on
one long page, obvious once it's five linked modules.

### Week 4 — Data Wrangling and Aggregation

1. **Grouping and Aggregation** — `groupby`, standard aggregate functions, `agg` with a
   list vs. a dict and why those produce differently-shaped results.
2. **Combining Datasets** — `merge` on one key and multiple keys, all four `how` values,
   `_x`/`_y` suffix collisions, `join` on index, `concat`.
3. **Reshaping with Pivot Tables** — `pivot_table` and its parameters, multi-level indices,
   long vs. wide. `set_index`/`reset_index`/`rename`/`sort_values` as the navigation tools
   (absorbs old 6.8, which pairs far better here than as a standalone utility grab-bag).
4. **Derived Features** — `apply(axis=1)` for logic spanning columns (the commission
   example), `pd.cut` binning, categorical encoding via `map` and `get_dummies`.

**Note:** `apply` appears in both 3.3 and 4.4 deliberately — Series-wise in Week 3,
row-wise with `axis=1` in Week 4. Make the progression explicit in the text so it doesn't
read as a repeat.

### Week 5 — Exploratory Visualization

Old Lesson 7 was the genuinely light week: four topics amounting to three plot types and
how to add a title. No chart-selection reasoning, no design principles, no EDA — all three
of which the v2 planning notes claimed for this week. Grows here with new content plus
`df.plot()` moved forward from old 11.1.

1. **Choosing the Right Chart** `NEW` — Start from the question: comparison, distribution,
   trend, relationship, composition, and what serves each. Common mismatches: pie charts
   with many categories, line charts on categorical axes, dual y-axes. No code in this
   module.
2. **Quick Charts from a DataFrame** — `df.plot()` and `df.plot(kind=...)` for line, bar,
   hist, scatter, box, straight off a DataFrame or a `groupby` result. Shortest path from
   Week 4's output to a picture.
3. **Matplotlib and Seaborn for Presentation** — Figure and axes, labels, titles, legends,
   subplots, `tight_layout`, saving to file. Seaborn for statistical plots (correlation
   heatmap, pairplot). Design principles applied as concrete rules: label axes with units,
   readable tick labels, colorblind-safe palettes, no truncated bar-chart y-axes, cut
   chart junk.
4. **Exploratory Data Analysis** `NEW` — EDA as a repeatable loop: shape and dtypes,
   distribution of each variable, missingness patterns, pairwise relationships, then what
   question that surfaces. Links back to Week 2's inspection routine and Week 3's cleaning
   so students see EDA as the thing that tells you what to clean. Ends on the habit of
   writing findings into markdown cells, which is what the project rubric rewards.

### Week 6 — Web Scraping with Selenium

1. **HTML and the DOM** — Document structure, key elements, the tree, inspecting a live
   page with devtools. Real teaching, not a refresher: Intro is pure Python and students
   arrive having never seen a tag.
2. **Scraping Ethically and Legally** — `robots.txt`, terms of service, rate limiting,
   identifying your scraper, personal data, when an API is the right answer. Moved
   deliberately *before* the tooling; it's section 8.3 in v2, after students have already
   scraped a site.
3. **Selenium Fundamentals** — Driver setup with WebDriver Manager, loading a page,
   locating elements by CSS selector and XPath, extracting text and attributes, waiting for
   dynamic content. Consolidates old 8.2 and 8.4, treating XPath as an alternative locator
   strategy rather than a separate topic. Durham Library site as the worked example.
4. **Building a Reliable Scraper** — Error handling, delays and retries, why scrapers break
   (old 8.7's "frailty"), writing results to CSV, JSON, and SQLite.

**Assignment change:** Week 6's assignment becomes a self-contained scraping mini project
(choose a site, scrape a dataset, clean it, save to CSV and SQLite, document in a README).
The Durham Library guided tasks that make up v2's Assignment 8 move into modules 3 and 4 as
worked practice. Students who enjoy their scraper may carry the data forward into the final
project, but it's optional and not assumed.

**Small cleanup:** old 8.2 apologizes mid-example for using a list comprehension ("we
haven't talked about those"). Intro now covers them and Week 1 reinforces them — delete the
aside.

### Week 7 — Databases and SQL

Busy week. Old Lesson 9 is the largest file in the course (32KB, twelve sections).

1. **Relational Thinking** — Why a relational database beats a folder of CSVs. Tables,
   rows, primary keys, one-to-many and many-to-many. Constraints as the database enforcing
   data quality, connecting back to Week 3's manual validation. Transactions conceptually.
2. **Creating and Populating a Database** — `sqlite3` connections, `with` blocks and
   commit/rollback, `CREATE TABLE` with types and constraints, `INSERT`, `executemany`,
   foreign keys. Parameterized inserts taught as the only way, with a forward reference to
   Week 8 for why.
3. **Querying with SELECT** — SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, aggregate
   functions, GROUP BY.
4. **Joins, Updates, and Deletes** — INNER and LEFT joins over the tables built in module
   2, then UPDATE and DELETE with the missing-`WHERE` warning.
5. **SQL and Pandas Together** — `pd.read_sql_query`, `df.to_sql`, and the judgment call of
   what belongs in SQL vs. Pandas. Short, but for a data course it's the most consequential
   idea of the week; burying it as section 9.11 of twelve badly undersold it.

**This module stays on a raw `sqlite3` connection deliberately.** Students should feel the
plain version before Week 8 shows the upgrade. Do not introduce SQLAlchemy here.

**`sqlcommand.py`** becomes an optional extension page for students who want more SQL
practice. Since the week now runs in Kaggle, the notebook-native equivalent is a helper
function that takes a query string and returns a DataFrame — worth providing inline for
everyone, with the interactive CLI version as the optional deeper path.

### Week 8 — Advanced SQL and Integration

Five modules. Grew from four to accommodate SQLAlchemy.

1. **Aggregation in Depth** — GROUP BY on multiple columns, `HAVING` vs. `WHERE`,
   aggregating across joins, joining to get readable names instead of ids.
2. **Subqueries and Complex Joins** — Subqueries in `WHERE` and `FROM`, correlated
   subqueries, multi-table joins, self-joins (the manager example).
3. **Window Functions and Dates** — `ROW_NUMBER`, `RANK`, running totals with
   `SUM() OVER`, `PARTITION BY`, plus SQLite date and time functions. Grouped because both
   are "SQL does more analysis than you assumed" and both feed the final project.
4. **Connecting with SQLAlchemy** — `create_engine()`, database URLs, why the connection
   string is the only thing that changes when a project outgrows SQLite, `pd.read_sql_query`
   and `df.to_sql` against an engine, and `engine.connect()` vs. `engine.begin()`. Closes
   with the ORM preview (see below).
5. **Safe and Reliable Queries** — Parameterization and SQL injection shown in both dialects,
   transactions and rollbacks, indexing and when it helps.

**The framing for SQLAlchemy must be accurate.** Pandas has *not* dropped support for raw
`sqlite3` connections — they work with no error and no deprecation warning on current pandas.
Do not write "modern Pandas expects a SQLAlchemy engine"; a student who later uses `sqlite3`
and watches it work will conclude the lesson was wrong. The accurate motivation is stronger:
pandas special-cases SQLite, and SQLAlchemy is the path that works for every database.

**SQLAlchemy is not automatically safe from injection.** An f-string interpolated into
`text()` injects exactly as readily as one interpolated into a `sqlite3` call — verified,
see below. Safety comes from binding parameters, not from choosing the library. Module 5
teaches parameterization as the technique, with the syntax shown in both dialects.

**The ORM appears as a demonstration only.** Show the Week 7 `CREATE TABLE` and its
`DeclarativeBase` equivalent side by side, then run `Base.metadata.create_all(engine)` and
inspect the generated tables. The point is that the class is a second notation for something
students already built, not a new abstraction. It is **not** in the assignment, **not** in
the rubric, and **not** a prerequisite for the Week 8 project milestone or the final project.
Nothing downstream may assume it.

**Rationale for that constraint:** there is no OOP anywhere in this track. Python Intro's
objectives contain no classes, and Py100 v2 contains no class definitions at all. A student
reaching Week 8 has never written `class Anything:`. A read-only demonstration is fine; a
requirement would be cargo-cult programming.

**Note:** transactions appear conceptually in 7.1 and practically in 8.5. Have the modules
reference each other explicitly so it doesn't read as duplication.

### Week 9 — Interactive Visualization and Dashboards

With `df.plot()` moved to Week 5, this week has room to actually teach Streamlit instead of
sprinting through three libraries.

1. **Interactive Charts with Plotly** — `plotly.express` for scatter, line, bar; hover
   data; what interactivity buys you; writing to HTML. Includes the `fig.show()` hang that
   v2 warns about in a code comment — it deserves real text.
2. **Your First Streamlit App** — Reusing the Week 1 local repo. The
   script-reruns-top-to-bottom execution model, which is the biggest conceptual hurdle and
   gets almost no airtime in v2. Text and data display, `st.dataframe`, `st.metric`,
   `streamlit run`.
3. **Inputs, Layout, and State** — Widgets, columns, expanders, sidebar, and filtering a
   DataFrame from widget values. The module that turns a page into a dashboard.
4. **Building and Deploying** — Assembling filters, metrics, and charts into a coherent
   layout, then deploying a throwaway app to Streamlit Community Cloud. Ends with a clearly
   marked optional section on Dash: what it is, how its callback model differs, a pointer
   for the curious. Optional and unassessed.

**Why the practice deployment matters:** in v2, the first deployment a student ever attempts
is the graded one, in the final week, with the app URL as a required submission field and no
slack behind it. Deploying something trivial a week early converts the highest-risk step in
the course into a repeat of a known procedure. This is the single highest-leverage change in
the revision.

### Week 10 — Final Project: Pipeline and Analysis `NEW`

1. **Scoping Your Analysis** — Revisit the Week 5 proposal, sharpen the question, decide
   what counts as an insight, plan the notebook's structure.
2. **Loading and Cleaning Your Dataset** — Week 3 applied to the chosen dataset, with
   cleaning decisions documented in markdown cells as the rubric requires.
3. **Analysis and Visualization** — Weeks 4, 5, and 8 applied: aggregations, derived
   features, the SQL queries written in the Week 8 milestone, and the charts that support
   each insight.
4. **Writing Up Your Findings** — `summary.md`: the question, the data, what you found,
   what the limitations are. Becomes the script for the Week 11 video, so the recording is
   demoing something already articulated rather than composing under deadline.

### Week 11 — Final Project: Dashboard and Presentation

1. **Planning Your Dashboard** — What questions the dashboard answers that the notebook
   can't, sketching the layout, choosing which filters matter.
2. **Building the Dashboard** — Streamlit applied, reading from the stored data, wiring
   filters to charts, layout and labeling.
3. **Deploying Your App** — A repeat of Week 9's procedure. README requirements: summary,
   setup steps, screenshot, deployed URL, video link.
4. **Recording and Submitting** — Presentation guidance using `summary.md` as the script,
   and the submission checklist.



## Content Moves and Cuts

Old Lessons 4, 5, and 6 overlapped substantially. Lesson 4.1 taught `fillna` strategies,
forward/backward fill, `str.strip()`, case normalization, and `to_datetime` with
`errors="coerce"` — all of which Lesson 5 then taught again as its main content. Lesson 6.1
re-taught `.loc`/`.iloc` selection already covered in 4.1, and was marked "Optional," which
reads as an admission of redundancy.

| Content | From | To |
|---|---|---|
| `fillna` strategies, `ffill`/`bfill` | L4.1 | Week 3.1 |
| `str.strip()`, case normalization | L4.1 | Week 3.4 |
| `to_datetime`, `errors="coerce"` | L4.1 | Week 3.2 |
| Pandas Review & Deep Dive (Optional) | L6.1 | Cut — dissolves into Week 2.4 |
| Data Selection (`.loc`/`.iloc`) | L6.2 | Week 2.4 |
| Data Transformation, `apply()` | L6.6, L6.7 | Week 3.3 (Series-wise) and Week 4.4 (row-wise) |
| Utility Methods (rename, sort, index) | L6.8 | Week 4.3 |
| Categorical Encoding | L6.9 | Week 4.4 |
| Feature Engineering / binning | L6.10 | Week 4.4 |
| Plotting with Pandas (`df.plot()`) | L11.1 | Week 5.2 |
| Ethical scraping | L8.3 | Week 6.2 (moved earlier, before the tooling) |
| SQL from Pandas | L9.11 | Week 7.5 (promoted from buried subsection) |

**Net effect:** Weeks 2, 3, and 4 land at comparable weight instead of Lesson 4 being the
largest file in the Pandas block. Week 5 grows from genuinely light to substantial. Week 9
gains room for Streamlit depth.

**Gaps filled with new content:** `describe`/`shape`/`dtypes`/`value_counts` (Week 2.3),
reading from an API (Week 2.2), chart selection reasoning (Week 5.1), visual design
principles (Week 5.3), EDA workflow (Week 5.4).



## Final Project Design

**One project, two phases.** v2 ran two concurrent capstones — a Kaggle data pipeline
project (started old Week 5, finished old Week 7) and a web scraping plus dashboard project
(started old Week 8, finished old Week 11). That structure split the work by *technique*
rather than by *phase*, which is why the final week had to reconcile them and why the video
demo covered two disjoint things in three minutes. v3 splits by phase instead.

**What v2's final week actually asked for** — the problem being solved:

1. Assignment 11 itself, in a brand-new repo requiring ten setup steps (fresh venv,
   `requirements.txt`, seven packages, interpreter config, remote, branch).
2. The Streamlit dashboard for the scraping capstone, plus first-ever deployment.
3. Final submission of both capstones against their full rubrics.
4. A 3–5 minute video demoing both projects, uploaded to YouTube.

Four deliverables across three repositories, two of them first-time activities under
deadline. The Kaggle project was also *finished* in old Week 7 but not submitted until Week
11, so students returned to polish something a month old while actively building something
else.

**v3 structure:**

* **Weeks 10 and 11 have no separate weekly assignment.** The project is the submission,
  which satisfies the per-week participation check.
* **Week 5 milestone — scope proposal.** One page: the question, the dataset, why it's
  feasible, expected insights. Submitted as `proposal.md` via PR, which also creates the
  project repo. Week 5 is the right moment: students have just finished the
  load-clean-wrangle-visualize arc and can judge what's realistic. Cheap for a mentor to
  sanity-check, so infeasible projects surface with five weeks left.
* **Week 8 milestone — data in SQLite plus analytical queries.** Load the curated dataset,
  do initial cleaning, write it to a SQLite table, then run two or three real queries
  against it (a grouped aggregate with `HAVING`, a window function). Exercises Week 8's
  content on the student's own data instead of a toy employees database, and the results
  feed directly into Phase 1.
* **Week 10 — Phase 1.** Cleaned data, core analysis, visualizations, `summary.md`.
* **Week 11 — Phase 2.** Dashboard, deployment, recorded presentation.

**Datasets.** Four curated options, retained from v2: Global Superstore, TMDB 5000 Movie
Dataset, Life Expectancy (WHO), Seattle Airbnb Open Data. All already exist as Kaggle
Datasets, so students use `Add Input` with no downloading. Alternative datasets allowed with
CIL approval. Class sizes make free choice too costly to support, and students get full
dataset choice in the later capstone course.

**Where the project lives.** Phase 1 analysis is a Kaggle notebook — that's where the
datasets are, and GitHub is a poor place to review notebook diffs (v2's Assignment 5 says so
outright). Phase 2 must be a GitHub repo because Streamlit Community Cloud deploys from
GitHub. The handoff is the cleaned data committed to the repo for the dashboard to read.

**Resilience detail.** Let the presentation demo a locally-running app if deployment
misbehaves. In v2 the deployed URL is a hard submission requirement, so a Streamlit Cloud
problem in the last 48 hours cascades into a missing presentation. Decoupling them means a
deployment issue costs a rubric line, not a graduation.



## Verified Code Patterns (SQLAlchemy)

**Do not draft this section's code from tutorials, blog posts, or an AI assistant's memory.**
SQLAlchemy 1.4 and 2.0 differ in ways that produce code which either fails outright or
silently teaches the wrong thing, and the older style dominates the material that's findable
online. Everything below was executed and confirmed against **SQLAlchemy 2.0.52 / pandas
3.0.2**.

### Version hazards

| Hazard | 1.4 and earlier | 2.0+ |
|---|---|---|
| Executing SQL | `engine.execute(...)` works | **`engine.execute()` does not exist** — raises `AttributeError`. Use a connection context manager |
| Declarative base | `Base = declarative_base()` | `class Base(DeclarativeBase): pass` — `DeclarativeBase` does not exist before 2.0 |
| Column definitions | `Column(Integer, primary_key=True)` | `mapped_column(...)` |

**Verify the SQLAlchemy version in the current Kaggle image before writing any of this,** and
pin it in the lesson if it isn't 2.0+. If Kaggle ships 1.4, every snippet below needs the
older spelling and the `DeclarativeBase` demo is impossible as written. One cell settles it:

```python
import sqlalchemy; print(sqlalchemy.__version__)
```

### Engine and pandas

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///db/project.db")
# The only thing that changes for a different database is this string:
# create_engine("postgresql://user:pass@host:5432/dbname")

df.to_sql("sales", engine, if_exists="replace", index=False)
df = pd.read_sql_query("SELECT * FROM sales", engine)
```

Use `engine.connect()` for reads and `engine.begin()` for writes — `begin()` commits when the
block exits, `connect()` does not.

```python
from sqlalchemy import text

with engine.begin() as conn:                      # commits on exit
    conn.execute(text("CREATE TABLE users (id INTEGER, name TEXT)"))

with engine.connect() as conn:                    # read-only
    rows = conn.execute(text("SELECT * FROM users")).fetchall()
```

### Parameterization and injection

Confirmed behavior with `evil = "1 OR 1=1"` against a two-row table:

```python
# VULNERABLE — returns both rows. SQLAlchemy does not save you here.
conn.execute(text(f"SELECT * FROM users WHERE id = {evil}"))

# SAFE — returns zero rows. The bound parameter is never parsed as SQL.
conn.execute(text("SELECT * FROM users WHERE id = :uid"), {"uid": evil})
```

The `sqlite3` equivalent, for the side-by-side comparison:

```python
cur.execute("SELECT * FROM users WHERE id = ?", (evil,))
```

### ORM demonstration

Both the annotated and non-annotated forms generate identical tables. **Use the
non-annotated form** — the 2.0 documented default relies on `Mapped[]` type annotations, and
type hints are another concept absent from the Intro course. One new idea is enough.

```python
from sqlalchemy import create_engine, Integer, String, ForeignKey, inspect
from sqlalchemy.orm import DeclarativeBase, mapped_column

engine = create_engine("sqlite:///db/demo.db")

class Base(DeclarativeBase):
    pass

class Magazine(Base):
    __tablename__ = "magazines"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(80), nullable=False)

class Publisher(Base):
    __tablename__ = "publishers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(80), nullable=False)
    magazine_id = mapped_column(ForeignKey("magazines.id"))

Base.metadata.create_all(engine)          # this is what generates the CREATE TABLE
print(inspect(engine).get_table_names())  # ['magazines', 'publishers']
```

Pair this with the `CREATE TABLE` statement students wrote in Week 7.2 so the mapping between
the two notations is visible line by line, and use `create_all` plus `inspect` to prove the
class produced the same table.



## Open Work Items

1. **Rubric rewrite.** One project means one rubric, split so Phase 1 and Phase 2 are each
   independently gradeable. v2's Kaggle rubric has good coverage — especially its criteria
   on insights, limitations, and data-story quality — but nine categories is unwieldy for
   graders. Build on the scraping rubric's tighter five-category shape and fold in the
   Kaggle rubric's conclusions and interpretation criteria.
2. **Strip capstone increments from Weeks 3–9 assignments.** v2 wove project work into
   Assignment 5 (Task 10), 6 (Task 13), 7 (Task 8), 8 (Task 7), 9 (Task 6), 10 (Task 5), and
   11 (Task 6). All of that goes; only the Week 5 and Week 8 milestones remain.
3. **Replace `sqlcommand.py` with a notebook-native helper** for Weeks 7–8, keeping the CLI
   version as an optional extension.
4. **Rewrite Week 6's assignment** as the scraping mini project.
5. **Standardize the "run this in the Python interactive shell" framing.** It appears
   throughout old Lessons 4, 5, and 6 while every assignment is a notebook. Now that modules
   are separate pages, the inconsistency will be visible on nearly every one.
6. **Contributing guidelines** for the repo, per sub-goal 2.
7. **Confirm the SQLAlchemy version in the Kaggle image** before drafting Week 8, and pin it
   in the lesson. Everything in Verified Code Patterns assumes 2.0+.
8. **Track the OOP gap at the track level.** Python Intro teaches no classes, Py100 teaches
   no classes, and the planned follow-up course has ML content — scikit-learn's interface is
   class-based, and writing a custom transformer means subclassing. OOP needs a home somewhere
   in Python for Cloud & AI or the Data Practicum. Not this course's problem to solve, but it
   is the reason the ORM here has to stay a demonstration, and it will block more than the
   ORM if it goes unaddressed.
