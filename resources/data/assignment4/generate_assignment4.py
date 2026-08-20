"""
Generator for the "Code the Dream Assignment 4" Kaggle dataset.

Produces four messy CSV files (records_part1.csv ... records_part4.csv, ~400 rows
each) for the Week 4 consolidation mini-project (Assignment 4, Task 14). Together
they describe ~400 unique people, each appearing once per file. Controlled noise
is added so the assignment's cleaning steps have something to fix:

  * Name / Address misspellings — for some people, exactly ONE of their four
    records has a small typo. The correct spelling therefore appears 3+ times
    (a "good" value), and the typo appears once (rare), so fuzzy matching snaps
    the typo back to the correct value.
  * Zip / Phone anomalies — for some people, ONE of their four records has a
    wrong value. The correct value is still the majority, so taking the mode
    per person restores it.
  * Residual nulls — a few people have a missing Phone in every record, so a
    handful of nulls survive cleaning (something for info() to report).

After the assignment's cleaning (fix names, fix addresses, fix zip/phone by mode,
drop duplicates), the ~1600 rows collapse to ~400 unique records.

Run:  python generate_assignment4.py
"""

import csv
import random
from itertools import product
from pathlib import Path

random.seed(42)   # reproducible
OUT = Path(__file__).parent

N_PEOPLE = 400
N_FILES = 4

FIRST = ["Alice", "Bob", "Carlos", "Dana", "Eve", "Frank", "Grace", "Hana",
         "Ivan", "Judy", "Karl", "Lena", "Mateo", "Nadia", "Omar", "Priya",
         "Quinn", "Rosa", "Sam", "Tara", "Umar", "Vera", "Will", "Xena",
         "Yuki", "Zane", "Amara", "Bianca", "Cyrus", "Diana", "Elias", "Farah",
         "Gabe", "Hugo", "Iris", "Jamal", "Kira", "Leo", "Mona", "Noah"]
LAST = ["Nguyen", "Smith", "Zhang", "Lee", "Martinez", "OConnor", "Kim", "Brown",
        "Garcia", "Wilson", "Davis", "Patel", "Chen", "Khan", "Lopez", "Silva",
        "Adams", "Baker", "Cruz", "Diaz", "Evans", "Ford", "Gomez", "Hall",
        "Ito", "Jones", "Kelly", "Long", "Meyer", "Novak", "Owens", "Perry",
        "Reed", "Shah", "Tran", "Ueda", "Vega", "Watts", "Yates", "Zimmer"]

STREETS = ["Oak", "Maple", "Pine", "Cedar", "Elm", "Birch", "Walnut", "Chestnut",
           "Willow", "Aspen", "Juniper", "Spruce", "Poplar", "Hickory", "Sycamore",
           "Magnolia", "Dogwood", "Cypress", "Redwood", "Hawthorn"]


def typo(s):
    """Return s with one small typo (swap two adjacent letters, or drop a letter)."""
    if len(s) < 4:
        return s + s[-1]  # double the last char
    i = random.randint(1, len(s) - 2)
    if random.random() < 0.5:
        # swap adjacent characters
        return s[:i] + s[i + 1] + s[i] + s[i + 2:]
    # drop a character
    return s[:i] + s[i + 1:]


def typo_address(addr):
    """Typo the street word only, keeping the unique house number intact so the
    misspelling stays unambiguously closest to this person's own address."""
    num, street, suffix = addr.split(" ")   # e.g. "234", "Oak", "St"
    return f"{num} {typo(street)} {suffix}"


# --- Build 400 canonical people ---------------------------------------------
combos = list(product(FIRST, LAST))
random.shuffle(combos)
chosen = combos[:N_PEOPLE]

people = []
for idx, (first, last) in enumerate(chosen):
    people.append({
        "Name": f"{first} {last}",
        "Address": f"{100 + idx} {random.choice(STREETS)} St",
        "Zip": str(random.randint(10000, 99999)),
        "Phone": f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
    })

# People whose Phone is missing in EVERY record (residual nulls after cleaning)
all_null_phone = set(random.sample(range(N_PEOPLE), 5))

# --- Build four records per person, with noise ------------------------------
# files[k] is the list of rows for records_part{k+1}.csv
files = [[] for _ in range(N_FILES)]

for idx, person in enumerate(people):
    # Decide which single record (if any) gets each kind of noise.
    name_bad = random.choice(range(N_FILES)) if random.random() < 0.35 else None
    addr_bad = random.choice(range(N_FILES)) if random.random() < 0.30 else None
    zip_bad = random.choice(range(N_FILES)) if random.random() < 0.30 else None
    phone_bad = random.choice(range(N_FILES)) if random.random() < 0.30 else None
    one_null = random.choice(range(N_FILES)) if random.random() < 0.15 else None

    for k in range(N_FILES):
        name = typo(person["Name"]) if k == name_bad else person["Name"]
        address = typo_address(person["Address"]) if k == addr_bad else person["Address"]
        zip_code = str(random.randint(10000, 99999)) if k == zip_bad else person["Zip"]
        phone = person["Phone"]
        if k == phone_bad:
            phone = f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        if idx in all_null_phone:
            phone = ""                      # missing in every record
        elif k == one_null:
            phone = ""                      # missing in one record (mode fills it back)
        files[k].append([name, address, zip_code, phone])

# --- Write the four files ----------------------------------------------------
header = ["Name", "Address", "Zip", "Phone"]
for k in range(N_FILES):
    path = OUT / f"records_part{k + 1}.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(files[k])
    print(f"Wrote {path} ({len(files[k])} rows)")

print(f"\n{N_PEOPLE} unique people across {N_FILES} files "
      f"({N_PEOPLE * N_FILES} rows total).")
