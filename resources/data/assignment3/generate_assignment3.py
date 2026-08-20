"""
Generator for the "Code the Dream Assignment 3" Kaggle dataset.

Produces two teaching fixtures used in the Week 3 (Data Cleaning and Validation)
assignment:

  employees.csv  — Task 1 (Handling Missing Data): Name, Age, Salary, Join Date,
                   City, with missing values engineered so that filling Name/Age/
                   Salary/Join Date leaves only City missing, and three rows are
                   dropped for a missing City.

  eclipses.csv   — Task 2 (Data Types and Dates) and Task 4 (Duplicates):
                   pipe-delimited ('|'), with a few deliberately invalid dates
                   (so to_datetime raises, and errors='coerce' produces NaT) and
                   a few exact duplicate rows (so drop_duplicates has something
                   to remove).

Run:  python generate_assignment3.py
"""

import csv
from pathlib import Path

OUT = Path(__file__).parent

# --- employees.csv -----------------------------------------------------------
# "" represents a missing value. Missing cells are spread across every column;
# rows 4, 10, and 16 are missing City (these get dropped after the fills).
EMP_HEADER = ["Name", "Age", "Salary", "Join Date", "City"]
EMP_ROWS = [
    ["Alice", "25", "50000", "2020-01-01", "New York"],
    ["Bob", "", "60000", "", "Los Angeles"],
    ["", "35", "", "2020-03-15", "Chicago"],
    ["David", "40", "80000", "2020-04-20", ""],
    ["Eva", "30", "55000", "", "Miami"],
    ["Frank", "45", "90000", "2019-11-05", "Seattle"],
    ["Grace", "", "62000", "2021-02-14", "Boston"],
    ["Hana", "28", "", "2020-07-30", "Denver"],
    ["", "33", "58000", "2018-05-22", "Austin"],
    ["Ivan", "52", "75000", "2017-09-01", ""],
    ["Julia", "38", "67000", "2022-01-11", "Portland"],
    ["Ken", "41", "", "2020-12-03", "Chicago"],
    ["Lena", "29", "53000", "", "New York"],
    ["Mateo", "", "71000", "2019-06-18", "Miami"],
    ["Nadia", "47", "88000", "2016-03-25", "Dallas"],
    ["Omar", "36", "64000", "2021-08-09", ""],
]

with open(OUT / "employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(EMP_HEADER)
    writer.writerows(EMP_ROWS)

# --- eclipses.csv (pipe-delimited) -------------------------------------------
# Eclipses observed in Arkansas. Three Date values are invalid on purpose.
ECL_HEADER = ["Date", "Type", "Location", "Coverage"]
ECL_ROWS = [
    ["2017-08-21", "Partial", "Little Rock", "88"],
    ["2017-08-21", "Partial", "Fayetteville", "86"],
    ["2023-10-14", "Annular", "Texarkana", "62"],
    ["2023-10-14", "Annular", "Hot Springs", "58"],
    ["2024-04-08", "Total", "Little Rock", "100"],
    ["2024-04-08", "Total", "Jonesboro", "100"],
    ["2024-04-08", "Total", "Russellville", "100"],
    ["2024-04-08", "Total", "Conway", "100"],
    ["2024-02-30", "Partial", "Fort Smith", "45"],       # invalid: Feb 30 does not exist
    ["2012-05-20", "Annular", "Fayetteville", "40"],
    ["2014-10-23", "Partial", "Little Rock", "50"],
    ["not recorded", "Partial", "Bentonville", "30"],    # invalid: not a date
    ["1994-05-10", "Annular", "Pine Bluff", "70"],
    ["1979-02-26", "Total", "Jonesboro", "95"],
    ["2023-13-05", "Partial", "Springdale", "35"],       # invalid: month 13
    ["2045-08-12", "Total", "Hot Springs", "100"],
    ["2017-08-21", "Partial", "Jonesboro", "84"],
    ["2024-04-08", "Total", "Hot Springs", "100"],
    ["2023-10-14", "Annular", "Little Rock", "60"],
    ["2001-06-21", "Partial", "Conway", "20"],
    ["2048-06-11", "Annular", "Fort Smith", "68"],
    ["2052-03-30", "Total", "Texarkana", "100"],
    ["2017-08-21", "Partial", "Rogers", "85"],
    ["2024-04-08", "Total", "Paragould", "100"],
]
# Add a few EXACT duplicate rows (for the drop_duplicates task).
ECL_ROWS += [
    ["2017-08-21", "Partial", "Little Rock", "88"],   # dup of row 0
    ["2024-04-08", "Total", "Little Rock", "100"],    # dup of row 4
    ["2023-10-14", "Annular", "Texarkana", "62"],     # dup of row 2
    ["2024-04-08", "Total", "Jonesboro", "100"],      # dup of row 5
]

with open(OUT / "eclipses.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(ECL_HEADER)
    writer.writerows(ECL_ROWS)

print(f"Wrote {OUT / 'employees.csv'} ({len(EMP_ROWS)} rows)")
print(f"Wrote {OUT / 'eclipses.csv'} ({len(ECL_ROWS)} rows)")
