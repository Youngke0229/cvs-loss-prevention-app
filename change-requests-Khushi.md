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
