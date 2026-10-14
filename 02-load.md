# 02 — Load and normalize data

## Job and contract

Build a loader that reads the local LAPD NIBRS offenses CSV snapshot and
returns one normalized pandas DataFrame, `offenses`. One row represents one
charged offense on a police report. Later pieces receive this table and must
not reread or mutate the source CSV.

| Input | Output | Purpose |
|---|---|---|
| `data/lapd_nibrs_offenses_k7nn-b2ep.csv` | `offenses` | Incident-level offense analysis |
| `sample/offenses_sample.csv` | the same output | Development and loader checks before the full download is available |

Keep the raw CSVs unchanged and do not commit the downloaded `data/` folder.
Use pandas for the typed local CSV read. The full offenses file is about 143
MB with 471,285 rows, so later callers should pass the columns they need; use
`usecols` rather than loading unneeded columns.

## Required normalization

- Read `CaseNo`, `UniqueNIBRNo`, `Time OCC`, `AREA`, and `RPT Dist No` as
  strings. Do not coerce `CaseNo` to a number: leading zeros matter and one
  value is the literal `RFC CITATION`.
- Strip trailing whitespace from text fields, including `offenses["AREA NAME"]`.
- Normalize `AREA` to two digits and `RPT Dist No` to four digits with zero
  padding. Preserve the original fields or document clearly when a normalized
  field replaces one.
- Parse `Date Rptd` and `Date OCC` using the documented month-first format
  with invalid values coerced to missing. Do not silently discard missing or
  invalid dates; record their counts for the limitations/methodology piece.
- Do not fill a blank value with a substantive value such as zero, `No`, or
  `Unknown` unless a later piece explicitly defines that transformation.
- Remove unnecessary columns for the scope of the project **after** passing the raw CSV file as a variable.
- Consolidate the Type of Crime into a singular column rather than having multiple columns with yes/no values.

The loader only normalizes formats and reports quality checks. It does not
choose the tool's harm measures, remove plausible-looking records, impute
missing values, or create rankings. In particular, later metric pieces must
decide how to handle impossible `Date OCC` values, incomplete recent weeks,
and zero latitude/longitude values before using those fields in a chart or
map.

## Done when

1. The loader runs against the sample offenses CSV and the full offenses CSV
   using the same interface.
2. It reports input and output row counts, missing parsed-date counts, and
   the number of distinct normalized `AREA` and `RPT Dist No` values.
3. `UniqueNIBRNo` is unique in `offenses`; a failed check stops the build
   with an actionable error.
4. The full snapshot check reports 471,285 offense rows and 21 normalized
   areas (the row total may differ after a publisher refresh, so display the
   observed total and download date).
