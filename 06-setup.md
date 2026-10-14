# 06 — Setup (`configs/default.toml`, `src/setup.py`)

**Job.** Read the starting defaults (the LAPD Area shown when the page opens, and the time window) from one config file, check them, and return them as one object. Setup runs once, at startup. It reads only its own config file: never the LAPD CSV (Load) and never the screen (View).

## Config file — `configs/default.toml`

```toml
default_area = "Mission"     # Area preselected in the sidebar: the most evening 23C + 120 offences
start        = 2025-02-01    # after the January 2025 NIBRS reporting break
end          = 2026-07-31    # last complete month; August 2026 is still being entered
```

**Why Mission.** The page should open on the Area the manager is most likely to act on. In the team's sample (2025-02-01 to 2026-07-31, 18:00–23:59), Mission has the most evening 23C + 120 offences (33: 28 shoplifting, 5 robbery), just ahead of Pacific and Wilshire (32 each). The full data decides: if another Area ranks first there, that Area becomes the default (check 4).

A new quarter means editing `end` (and `start`, if the window should move) in this file only; no code changes.

## Contract — `src/setup.py`

```python
@dataclass(frozen=True)
class Defaults:
    default_area: str   # one of the 21 LAPD Area names, stripped ("77th Street", "N Hollywood")
    start: date         # first day counted, inclusive, on Date Rptd
    end: date           # last day counted, inclusive, on Date Rptd

def load_defaults(path: Path = Path("configs/default.toml")) -> Defaults: ...
    # Reads and checks the file; raises ValueError naming the field and value on any problem.
```

| Field | Passed to | Use |
|---|---|---|
| `default_area` | View | initial choice in the sidebar dropdown |
| `start`, `end` | Filter | keeps rows with `start ≤ Date Rptd ≤ end` |

## Checks

`load_defaults` raises a `ValueError` naming the field and the bad value when:
- `default_area` is not one of the 21 Area names: Central, Rampart, Southwest, Hollenbeck, Harbor, Hollywood, Wilshire, West LA, Van Nuys, West Valley, Northeast, 77th Street, Newton, Pacific, N Hollywood, Foothill, Devonshire, Southeast, Mission, Olympic, Topanga;
- `start` is before 2025-02-01, or `end` is not after `start`;
- a key is missing or unknown (catches typos such as `default_aera`).

## Done when

1. `load_defaults()` on the default file returns `Defaults("Mission", date(2025, 2, 1), date(2026, 7, 31))`.
2. A test file with `default_area = "Hollywod"` raises a `ValueError` whose message contains `Hollywod`; one with `start = 2024-06-01` raises one naming `start`.
3. On the downloaded data, the month of `end` is complete: its count of reports (`Date Rptd`) is at least 90% of the median of the six months before it, and the month after it is not. In the team's sample, July 2026 has 991 reports against 870–1,004 in each of the six months before, and August 2026 has 663.
4. On the full downloaded data, `default_area` is the Area with the most offences coded 23C or 120 with `Time OCC` from 1800 to 2359 and `Date Rptd` from `start` to `end`. If not, replace it with that Area.
