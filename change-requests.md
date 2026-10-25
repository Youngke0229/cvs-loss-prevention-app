# Change requests

Our team's log of what we found and what should change, kept in the top folder of our team repo
from Module 9 to Module 13. Pull before you edit it and push soon after.

- For each finding, copy the request template below to the end of this file, give it the next
  number and fill in every field.
- Never delete a request. When it is built, set its status to `built` with the commit; when the
  team decides against it, `declined` with the reason.
- When this file gets long, ask Codex to move the built and declined requests into a dated file
  in `change-requests-archive/` (for example `change-requests-archive/2026-11-02.md`) and leave
  only the open ones here. Numbers continue; never reuse one.

Request template:

```markdown
### CR-NN: short title

- **From:** name, YYYY-MM-DD
- **Part:** the feature, number or function
- **Evidence:** what you did and saw: the input, what you expected, what the tool gave
- **Change:** what should change, in a sentence or two
- **Priority:** high, medium or low
- **Status:** open
```

A filled request (from the class lottery app):

```markdown
### CR-01: chance above 100% with two slots

- **From:** Ana, 2026-10-21
- **Part:** `odds` (the chance of selection by wage level)
- **Evidence:** one person at Level I and one at Level IV, two slots. Both must be selected,
  so each chance is 1. `odds` gave 0.4 and 1.6.
- **Change:** select each person at most once (without replacement), so no chance passes 1.
- **Priority:** high
- **Status:** open
```

## Requests

<!-- Add new requests below this comment, at the end of the file, newest last. -->
### CR-01: Let managers rank robbery separately or weight it more heavily

- **From:** Deenal Ahir, 2026-10-23
- **Part:** District-priority ranking
- **Evidence:** In Part 1, the app ranks districts with a simple combined count of shoplifting (23C) and robbery (120) offenses. This gives each robbery the same weight on the rank as each shoplifting offense does. This is not ideal since robberies may create greater danger and risk for CVS employees and customers than an average shoplifting offense.
- **Change:** Add ranking options for combined counts, robbery-first, and a weighted score. Keep the shoplifting and robbery breakdown visible for every option so the manager can assess.
- **Priority:** medium
- **Status:** open

### CR-02: Let managers choose a reporting period

- **From:** Deenal Ahir, 2026-10-23
- **Part:** Area comparison and district-priority ranking
- **Evidence:** In Part 2, we see that the Topanga area's displayed total of 660 was correct for the fixed reporting window of February 1, 2025 through September 30, 2026. However, the manager is making a quarterly guard-allocation decision and cannot use the app to compare a recent quarter with the longer historical period.
- **Change:** Add reporting-period options such as the most recent complete quarter, the previous 12 months, and the full available period. Update the area comparison, district ranking, chart, and CSV to use the selected period.
- **Priority:** high
- **Status:** open

### CR-03: Connect reporting districts to CVS stores

- **From:** Khushi Ahir, 2026-10-23
- **Part:** Download ranked CSV / five-store allocation decision
- **Evidence:** With Hollywood selected for 2025-02-01 through 2026-09-30, the export contained 10 ranked reporting districts; the top five were 0645, 0638, 0648, 0668, and 0646. It had no CVS store IDs, addresses, or mapping from stores to districts, although the manager's decision concerns five stores.
- **Change:** Allow the manager to load or maintain a verified CVS store-to-reporting-district mapping. Show candidate stores alongside ranked districts in the app and export; if the mapping is unavailable, show that no store-level recommendation can be made. Keep final guard assignments subject to manager review.
- **Priority:** high
- **Status:** open

### CR-04: Add a store-exposure comparison next to raw Area totals

- **From:** Khushi Ahir, 2026-10-23
- **Part:** Area comparison / Hollywood combined offenses
- **Evidence:** The Hollywood tooltip reported 383 combined evening offenses, and an independent row-by-row Python count also gave 383 (172 shoplifting, 211 robbery). This is a correct raw total, but the app has no CVS store counts or foot-traffic information. An Area with more stores could have a larger total without having a higher average store exposure.
- **Change:** If validated store counts are supplied, add a clearly named offenses-per-CVS-store comparison alongside raw Area totals. If reliable store exposure is unavailable, explicitly suppress the normalized value and warn against interpreting raw Area totals as store-level risk. Do not replace the raw count.
- **Priority:** medium
- **Status:** open

### CR-05: App footer shows inflated row count due to data duplication

- **From:** Youngke Li, 2026-10-25
- **Part:** Data Load / Source footer
- **Evidence:** At the bottom of the app page, the footer says "498,741 offense rows". However, the official dataset documentation states the offenses CSV has exactly 471,285 rows. This indicates a fan-out error (likely a many-to-many merge) that duplicated about 27,000 rows, inflating every single number on the screen.
- **Change:** Fix the Load piece to deduplicate the data (e.g., on `UniqueNIBRNo`) before passing it to the Filter. Ensure the total row count exactly matches the raw CSV (471,285).
- **Priority:** high
- **Status:** open

### CR-06: Remove contradictory hardcoded sample values in the Setup check

- **From:** Youngke Li, 2026-10-25
- **Part:** Setup check (Prompt instructions)
- **Evidence:** The `one-shot-prompt.md` contains a check that hardcodes sample values (expecting the default Area to be "Mission" and the end date to be July 2026). This contradicts the actual rule that the default Area should dynamically be the one with the highest offenses. If the data updates, the hardcoded test will fail.
- **Change:** Rewrite the first Setup check in the prompt to test the logical rule (e.g., "assert that the default Area equals the first row of the Area Summary for the configured window") instead of hardcoding the sample's Mission/July values.
- **Priority:** medium
- **Status:** open

### CR-07: Rank the top five districts across selected Areas

- **From:** Christian Cabello, 2026-10-25
- **Part:** Area selection / district-priority ranking
- **Evidence:** The app’s single-Area selection prevents managers from seeing one prioritized district list across multiple Areas. Comparing separate rankings manually makes it harder to allocate guards across Area boundaries.
- **Change:** Allow managers to select multiple Areas and rank the top five districts overall across those selections, using the chosen reporting period and ranking measure. Show each district’s Area and offense breakdown, and label the results as a combined ranking.
- **Priority:** medium
- **Status:** open

### CR-08: Show Area offense totals without hover
- **From:** Christian Cabello, 2026-10-25
- **Part:** Area comparison / district priorities
- **Evidence:** The Area comparison shows incident counts only in bar tooltips, so users must hover to see the selected Area’s shoplifting, robbery, and combined totals.
- **Change:** Display the selected Area’s shoplifting, robbery, and combined incident totals beneath its district-priorities heading.
- **Priority:** medium
- **Status:** open
