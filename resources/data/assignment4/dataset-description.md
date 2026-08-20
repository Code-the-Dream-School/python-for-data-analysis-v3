# Code the Dream Assignment 4

Teaching dataset for the Week 4 (Data Wrangling and Aggregation) consolidation mini-project of Code the Dream's **Python for Data Analysis** course. Upload the four files as a single CTD-owned Kaggle dataset titled **"Code the Dream Assignment 4"**.

## Files

`records_part1.csv`, `records_part2.csv`, `records_part3.csv`, `records_part4.csv` — four messy exports of the same ~400 people (each person appears once per file, so ~1,600 rows in total).

| Column | Type | Notes |
|---|---|---|
| `Name` | text | some records have a small misspelling |
| `Address` | text | some records have a small misspelling (house number always intact) |
| `Zip` | integer | some records have a wrong value |
| `Phone` | text | some records have a wrong value; a few people are missing it entirely |

## How the noise is engineered

The files are designed so the assignment's cleaning steps produce a clean result:

* **Name / Address misspellings** appear in at most one of a person's four records, so the correct spelling appears 3+ times (a "good" value) and the misspelling is rare. Fuzzy matching snaps the rare misspelling back to the correct value.
* **Zip / Phone anomalies** appear in at most one record, so the correct value is the majority and the per-person **mode** restores it.
* **A few people have no phone in any record**, so a small number of nulls survive cleaning.

**Expected result after cleaning** (fix names, fix addresses, fix Zip/Phone by mode, drop duplicates): **400 unique records, with 5 rows still missing a phone number.** This has been verified against the assignment's cleaning code.

## Regenerating

The files are produced by `generate_assignment4.py` in this folder (seeded, reproducible):

```bash
python generate_assignment4.py
```

Edit that script to change the size or noise rates; it is the source of truth for these fixtures.
