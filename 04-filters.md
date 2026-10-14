# 04-filter.md

## What this piece does

This piece keeps only the rows the manager cares about: evening shoplifting (NIBR code 23C) and robbery (code 120) in one LAPD Area, after the January 2025 reporting break.

## Receives

A cleaned pandas DataFrame from Load, with these columns:
- `RPT Dist No` (4-character text)
- `Time OCC` (4-character text)
- `NIBR Code` (text)
- `AREA NAME` (text)
- `Date Rptd` (parsed as a date)

Plus one user choice from the sidebar: the LAPD Area name.

## Returns

A filtered DataFrame with the same columns, containing only rows where:
1. `AREA NAME` equals the chosen area.
2. `NIBR Code` is `"23C"` or `"120"`.
3. `Time OCC` is between `"1800"` and `"2359"`.
4. `Date Rptd` is on or after `2025-02-01`.

## Definitions and why

All three definitions live in this file, in one place, as constants:

```python
EVENING_START = "1800"
EVENING_END = "2359"
RISK_CODES = ["23C", "120"]
START_DATE = "2025-02-01"
