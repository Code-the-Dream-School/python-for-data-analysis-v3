# 1.3 Working with File Paths

**Objective**: By the end of this module, you will be able to:

* Build file paths with `pathlib.Path` that work on any operating system.
* Distinguish relative from absolute paths.
* Read a file through a `Path`, and inspect a path's parts.
* List and process a directory of files with globbing.

---

Working with data means working with files — reading a CSV, writing results, processing a whole folder of them. Doing this reliably is harder than it looks, because operating systems disagree about how paths are written: macOS and Linux separate folders with a forward slash (`data/sales.csv`), while Windows uses a backslash (`data\sales.csv`). Building paths by joining strings yourself leads to code that breaks on someone else's computer.

Python's **`pathlib`** module solves this. Its `Path` object represents a file path and handles the differences between operating systems for you.

---

## Building Paths

Create a `Path` from a string, and join parts with the `/` operator — which works regardless of the operating system:

```python
from pathlib import Path

data_dir = Path("data")
file_path = data_dir / "sales.csv"   # data/sales.csv  (or data\sales.csv on Windows)
```

Using `/` to join is the main reason to prefer `pathlib`: you write the same code everywhere, and Python inserts the correct separator.

A `Path` can tell you about its parts:

```python
file_path.name     # 'sales.csv'  — the file name
file_path.stem     # 'sales'      — the name without the extension
file_path.suffix   # '.csv'       — the extension
file_path.parent   # Path('data') — the containing folder
file_path.exists() # True or False — whether it exists on disk
```

---

## Relative vs. Absolute Paths

A **relative** path is interpreted from the **current working directory** — the folder your program is running in. `Path("data/sales.csv")` means "a `data` folder here, wherever *here* is." An **absolute** path starts from the root of the filesystem and names the exact location, like `/Users/you/project/data/sales.csv`.

```python
Path.cwd()                          # the current working directory
Path("data/sales.csv").resolve()    # the absolute version of a relative path
Path.home()                         # your home directory
```

Relative paths are shorter and more portable, but they depend on *where the program is run from*. A relative path that works when you run a script from the project folder will fail if you run it from somewhere else — a common source of "file not found" errors.

---

## Reading Files Through a Path

A `Path` works anywhere a filename does, including `open()` and Pandas:

```python
import pandas as pd

df = pd.read_csv(Path("data") / "sales.csv")   # Pandas accepts a Path

text = Path("notes.txt").read_text()            # read a whole text file
Path("output.txt").write_text("done")           # write a text file
```

---

## Processing a Directory of Files

**Globbing** lists the files in a folder that match a pattern. `glob("*.csv")` finds every file ending in `.csv`:

```python
for csv_path in Path("data").glob("*.csv"):
    print(csv_path.name)
```

This is how you process many files at once. For example, reading every CSV in a folder into a list of DataFrames (using a list comprehension from the Intro course):

```python
frames = [pd.read_csv(p) for p in Path("data").glob("*.csv")]
```

To search subfolders too, use `rglob` (recursive glob) instead of `glob`.

---

### AI Prompt: Predict-then-Check

Relative paths depend on where a program runs, which surprises people. Consider a script saved at `project/scripts/load.py` containing:

```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data/sales.csv"))
```

The `data` folder is at `project/data/`, not `project/scripts/data/`.

1. Predict whether this works when you run the script from inside the `project/scripts` folder, and why.
2. Explain to an AI chatbot how the current working directory affects a relative path.
3. Ask: "Is my understanding of why a relative path can fail depending on where the script is run correct?"

> **Example prompt:** "I have a script that reads `Path('data/sales.csv')`, but the data folder isn't next to the script. I predict it will [work/fail] when run from [location] because [your reasoning]. Am I right about how the current working directory affects a relative path?"

---

## Videos

* ["Pathlib - the Modern Way to Handle File Paths," Corey Schafer](https://youtu.be/yxa-DJuuTBI?si=1E3dqfbmc72NtTcC)

---

## Check for Understanding

**1. Why build paths with `Path("data") / "sales.csv"` instead of the string `"data/sales.csv"`?**

* A) It is shorter to type
* B) `pathlib` inserts the correct folder separator for the operating system, so the code works everywhere
* C) Strings cannot represent file paths
* D) It makes the file load faster

<details>
<summary>Answer</summary>

B) The `/` operator on a `Path` uses the right separator on each operating system, so the same code runs on Windows, macOS, and Linux.

</details>

**2. What is the difference between a relative and an absolute path?**

* A) Relative paths are for text files; absolute paths are for data
* B) A relative path is interpreted from the current working directory; an absolute path names the full location from the filesystem root
* C) There is no difference
* D) Absolute paths only work on Windows

<details>
<summary>Answer</summary>

B) A relative path depends on where the program runs; an absolute path specifies the exact location regardless of the working directory.

</details>

**3. How do you get every `.csv` file in a `data` folder?**

* A) `Path("data").read_text()`
* B) `Path("data").glob("*.csv")`
* C) `Path("data").suffix`
* D) `Path("data").exists()`

<details>
<summary>Answer</summary>

B) `glob("*.csv")` lists the files matching the pattern. Use `rglob` to include subfolders.

</details>

---

## Further Reading

* [Python `pathlib` documentation](https://docs.python.org/3/library/pathlib.html)
* [Python HOWTO: Working with files with pathlib](https://realpython.com/python-pathlib/)
