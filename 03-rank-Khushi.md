# 03 — Rank reporting districts

## What this piece does

Rank identifies the **top 10 reporting districts (`RPT Dist No`)** in the selected LAPD Area based on the combined number of evening shoplifting (NIBR code `23C`) and robbery (code `120`) offense reports. This gives the manager a clear shortlist to consider when allocating additional security guards.

## Receives

A **filtered pandas DataFrame** from Filter. Each row is a qualifying offense, and Filter has already applied these rules:

- `AREA NAME` matches the LAPD Area selected in the sidebar.
- `NIBR Code` is `"23C"` or `"120"`.
- `Time OCC` is between `"1800"` and `"2359"`.
- `Date Rptd` is on or after `2025-02-01`.

Rank needs the **`RPT Dist No`** column (stored as four-character text). It does not read the CSV or repeat Filter's work.

## Returns

A **pandas Series** of up to **10 reporting districts**, sorted from the highest to the lowest combined offense count.

| Part of result | Meaning |
|---|---|
| **Index** | `RPT Dist No` (reporting district) |
| **Values** | Number of qualifying offense rows in that district |
| **Order** | Highest count first |
| **Destination** | View uses the Series for the ranked table and bar chart |

If fewer than 10 districts have qualifying reports, Rank returns all of them. If there are no matching rows, it returns an empty Series.

## Definitions and why

Rank follows four simple pandas steps:

```python
ranked = (
    filtered.groupby("RPT Dist No")
    .size()
    .sort_values(ascending=False)
    .head(10)
)
```

| Choice | Why |
|---|---|
| `groupby("RPT Dist No")` | Compares reports at the reporting-district level. |
| `.size()` | Counts all qualifying offense rows in each district. |
| `.sort_values(ascending=False)` | Puts the districts with the most reports at the top. |
| `.head(10)` | Matches the project's top-10 shortlist. |
| Combine codes `23C` and `120` | The manager needs a single combined measure of these two reported offense types. |
| Return a Series | Keeps the output simple for View to display. |

**Boundary:** Filter decides which reports qualify; Rank only groups, counts, sorts, and selects the top 10. Counts are **reported offenses**, not unique stores or a direct measure of actual crime risk.

## How to check it works

1. **Top 10:** Confirm the result has no more than 10 districts.
2. **Correct order:** Check that counts go from highest to lowest.
3. **Unique districts:** Verify that each `RPT Dist No` appears only once.
4. **Correct counts:** Manually count the qualifying rows for one district and compare with its result.
5. **Small test:** Try a sample where district `0101` has 3 reports and `0102` has 2; `0101` should rank first.
6. **Empty input:** Confirm that a filtered DataFrame with no rows returns an empty Series without an error.

**Handoff to View:** Pass the ranked Series directly to View for its table and bar chart.
