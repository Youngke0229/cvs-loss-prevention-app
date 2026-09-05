# How these samples were drawn

Seed: 0.576. Tool: DuckDB.

**This is a sample. Counts and proportions here are not population figures.** Every number you want to report about Los Angeles crime must come from the full files, not from these two CSVs.

## Method

The two tables share a case number, so an independent random sample of each table would leave almost no case with both its offense rows and its victim rows present, and the join a team most wants to practice would not work. The sample is therefore drawn one whole case at a time, not one row at a time. That means the rows in these files are not an independent random draw, so a proportion computed here can be further from the true one than the row count suggests.

1. Build the set of all distinct case numbers appearing in either full table. There are 423,257 of them.
2. Draw 22,000 of those case numbers uniformly at random with seed 0.576.
3. Keep every offense row whose case number is in the draw. That gives `offenses_sample.csv`.
4. Keep every victim row whose case number is in the draw. That gives `victims_sample.csv`.

Because whole cases are kept, the two sample files join on `CaseNo` exactly the way the full files do. 20,305 of the 22,000 sampled cases appear in both files; the rest are cases with offense rows but no victim row, which is normal in this data.

You can reproduce this from the full download described in section 4 of the data overview. DuckDB is a small database engine that runs inside Python and reads CSV files directly, which is why it was used here rather than pandas. To get it, run `uv run --with duckdb python your_script.py`, which installs it for that one run. In DuckDB the draw is:

```
SELECT setseed(0.576);

CREATE TABLE picked AS
SELECT CaseNo FROM (
  SELECT CaseNo FROM read_csv_auto('lapd_nibrs_offenses_k7nn-b2ep.csv')
  UNION
  SELECT CaseNo FROM read_csv_auto('lapd_nibrs_victims_gqf2-vm2j.csv'))
ORDER BY random() LIMIT 22000;

COPY (SELECT * FROM read_csv_auto('lapd_nibrs_offenses_k7nn-b2ep.csv')
      WHERE CaseNo IN (SELECT CaseNo FROM picked))
TO 'offenses_sample.csv' (HEADER, DELIMITER ',');
```

The same last line, with the victims table, writes the second file. This was drawn with DuckDB version 1.x. A different DuckDB version may order the draw differently, in which case you will get a different but equally valid 22,000 cases.

## Files

| File | Full file it comes from | Rows in the full file | Rows in the sample | Columns | Size |
|---|---|---|---|---|---|
| `offenses_sample.csv` | `lapd_nibrs_offenses_k7nn-b2ep.csv` | 471,285 | 24,575 | 31 | 7.5 MB |
| `victims_sample.csv` | `lapd_nibrs_victims_gqf2-vm2j.csv` | 432,047 | 22,435 | 17 | 4.4 MB |

All 31 and all 17 columns are present, in the same order and with the same names and spellings as the full exports. No column was dropped, renamed or truncated. Values are copied exactly, including the trailing spaces in `AREA NAME` and the unpadded values in the victims table.

The files are plain ASCII text, which is a subset of UTF-8, comma-delimited, quoted where a field contains a comma, with one header row. Sizes here are counted the ordinary way, one megabyte being one million bytes, the same convention as section 4 of the data overview.

## Coverage of the sample

Report dates in the offense sample run from 6 April 2010 to 31 August 2026, and the same in the victim sample. The handful of rows before 2024 are old cases that were typed into the new system later, and they are described in section 5 of the data overview.

## What to watch when you open it

Both files re-open cleanly with a plain read in pandas, with no parse errors and no mixed-type warnings. Two things still go wrong if you accept the guessed types:

- `Time OCC`, `AREA` and `RPT Dist No` are read as integers, which strips the leading zeros. Reporting district `0101` becomes `101` and area `01` becomes `1`. Read these three columns as text.
- `Vict Age` is read as a decimal number because it is blank on many rows. That is harmless, but the blanks are meaningful and are explained in the data overview.

Full column meanings, coverage, quirks and the list of what the data does not contain are in `../data_overview_lapd-nibrs.md`.
