# 00-vision.md

## Vision

The **Regional Loss Prevention Manager at CVS Health** in Los Angeles must decide, each quarter, **which five CVS stores should receive a second security guard on the evening shift (18:00–24:00)**. Today this decision relies on store managers' intuition and monthly total incident counts, which cannot separate evening from daytime risk or distinguish shoplifting inside a store from robbery on the surrounding street.

## What the tool is

A one-screen Streamlit page. The manager selects one LAPD Area from a sidebar dropdown, and the page shows:

- A ranked table of the top 10 RPT Dist Nos in that area by combined evening shoplifting (NIBR code 23C) and robbery (code 120) counts.
- A bar chart of the same top 10.
- A caption under both: "Reported offences, not actual crime. Evening = 18:00–24:00. January 2025 reporting break excluded."

## What the manager cares about

- Reducing shoplifting and robbery during the evening shift.
- Keeping the guard budget under control by putting the second guard where the risk is highest.
- Defending the allocation to regional leadership with a clear, data-backed shortlist.

## Use cases

1. Rank the top 10 RPT Dist Nos in one LAPD Area by combined evening 23C + 120 counts, to pick the five stores for a second guard.
2. Compare LAPD Areas by combined evening counts, to decide which area to prioritise this quarter.
3. Export the ranked table to justify the quarterly guard allocation to regional leadership.
4. Exclude the January 2025 NIBRS reporting break so the ranking is not distorted by the system migration.
