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
