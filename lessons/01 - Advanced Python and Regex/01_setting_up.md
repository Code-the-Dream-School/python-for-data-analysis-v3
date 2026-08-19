# 1.1 Setting Up for Data Work

**Objective**: By the end of this module, you will be able to:

* Create and run a Kaggle notebook, and attach a dataset to it.
* Explain how a notebook's cells share state and why execution order matters.
* Set up the local `python_homework` repository with a virtual environment.
* Use the Git branch-and-pull-request workflow for your assignments.

---

Welcome to Python for Data Analysis!

You'll start by building on the core Python skills you learned in the Intro course: data structures, functions, `try`/`except`, `requests` and JSON, reading and writing files, and the Git workflow. This course applies those skills to **working with data** — loading it, cleaning it, analyzing it, and presenting it.

You'll work in two environments this term, and you set both up this week:

* **Kaggle notebooks** — a free, cloud-based environment where most of the course runs. Datasets and data libraries are already there, so you can focus on the analysis.
* **The `python_homework` repository** — a local project on your own computer, used for the weeks where you run Python scripts or a web app (Weeks 1, 6, and 9).

---

## Kaggle Notebooks

A **Kaggle notebook** runs Python in your browser, with the common data libraries (including Pandas) already installed. A notebook is made of **cells**, which come in two kinds: **code cells** that run Python, and **markdown cells** that hold formatted text. You run a cell by clicking the arrow beside it, and its output — text, a table, or a chart — appears directly below.

**Set up your account:**

1. Create a free account at [kaggle.com](https://www.kaggle.com).
2. **Verify your phone number** (in account settings). Verification unlocks the ability to attach datasets and enable internet access in a notebook, both of which the course requires.

**Two things about notebooks to understand now:**

* **Cells share one session.** All the code cells in a notebook run in the same Python session, so a variable or import from one cell is available in later cells. You only import Pandas once, for example.
* **Execution order matters.** Because cells share state, a cell that depends on an earlier one will fail if the earlier one hasn't run. If a session times out or you run cells out of order, use **Run All** (at the top) to run everything from the top in order.

**Two features you'll use often:**

* **Add Input** (upper right) attaches a Kaggle dataset to your notebook, so you can read its files. You'll use this from Week 2 on.
* **Save Version** saves your notebook and runs it top to bottom, which is also how you produce the shareable link you submit for assignments.

---

## The `python_homework` Repository and a Virtual Environment

Some weeks run Python on your own computer rather than in the cloud. For those, you use the **`python_homework`** repository. We'll it up once now.

Follow this link [LINK TBD]() to the homework repository. To use this repository:

1. Sign into your GitHub, and create a repository called python_homework. It must be a public repository. You don't need to create a `.gitignore` or a `README.md.`
2. On your computer, clone the repository. (Do not clone the repository you just created.)
3. Change to the python_homework directory you just cloned.  Enter the following commands:
```shell
# if you use ssh authentication:
git remote set-url origin git@github.com:your-github-id/python_homework.git
# if you use token based authentication:
git remote set-url origin https://github.com/your-github-id/python_homework

git remote add upstream https://github.com/Code-the-Dream-School/python_homework
git push origin main
```

A **virtual environment** is a private copy of Python and its packages for a single project, so one project's libraries don't interfere with another's. After cloning `python_homework`, from inside the project folder:

```bash
python -m venv .venv           # create the environment
source .venv/bin/activate      # activate it (macOS/Linux)
# .venv\Scripts\activate       # activate it (Windows)

pip install -r requirements.txt   # install the project's packages
```

The `requirements.txt` file lists the packages this course needs, including Pandas. Installing it once means those libraries are ready whenever you work locally — including when you build a Streamlit app in Week 9.

---

## The Git Workflow

You'll submit most local work as a **pull request**, the same workflow from the Intro course. For each assignment:

1. Create a branch: `git checkout -b assignment1`.
2. Do your work, then `git add` and `git commit` your changes.
3. Push the branch: `git push origin assignment1`.
4. Open a pull request on GitHub and submit its link.

Committing in small steps as you go gives you points to return to if something breaks.

---

### AI Prompt: Predict-then-Check

Notebook execution order is a common source of confusion. Imagine a notebook with two code cells:

```python
# Cell 1
total = 100

# Cell 2
print(total * 2)
```

Suppose you run **Cell 2 first**, before ever running Cell 1.

1. Predict what happens.
2. Explain to an AI chatbot why a notebook behaves this way, given that all cells share one session.
3. Ask: "Is my understanding of how notebook cells share state and why execution order matters correct?"

> **Example prompt:** "In a Kaggle/Jupyter notebook, I run a cell that uses a variable before running the cell that defines it. I predict [your prediction] because [your reasoning]. Am I right about how notebook cells share state?"

---

## Videos

* [Python Tutorial: virtualenv and why you should use virtual environments](https://www.youtube.com/watch?v=N5vscPTWKOk) — Corey Schafer on virtual environments.

---

## Check for Understanding

**1. In a Kaggle notebook, you run a cell that uses a variable defined in an earlier cell you never ran. What happens?**

* A) It works, because notebooks fill in variables automatically
* B) It raises an error, because the variable was never defined in the session
* C) The notebook runs the earlier cell for you
* D) The variable defaults to zero

<details>
<summary>Answer</summary>

B) Cells share one session, but a variable exists only after its cell runs. Use **Run All** to run everything from the top in order.

</details>

**2. What is the purpose of a virtual environment?**

* A) To make Python run faster
* B) To keep one project's packages separate from other projects'
* C) To connect to the internet
* D) To store your data files

<details>
<summary>Answer</summary>

B) A virtual environment gives a project its own private set of packages, so different projects don't interfere with each other.

</details>

**3. Which Kaggle feature attaches a dataset to your notebook so you can read its files?**

* A) Save Version
* B) Run All
* C) Add Input
* D) Commit

<details>
<summary>Answer</summary>

C) **Add Input** attaches a Kaggle dataset to the notebook. (Save Version saves and runs the notebook; Run All executes the cells in order.)

</details>

---

## Further Reading

* [Kaggle: How to Use Kaggle](https://www.kaggle.com/docs/notebooks) — the official guide to notebooks.
* [Python: venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
