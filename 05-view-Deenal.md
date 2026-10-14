## VIEWS

All views will use recorded incidents in the LAPD Area that are reported between 18:00 and 24:00, 
with NIBRS crime codes 23C (shoplifting) or 120 (robbery). Exclude January 2025.


- **Ranked RPT Dist Nos** (`top10_districts`): a table of the top 10 RPT Dist Nos ranked by combined count of qualifying evening offences. 
Columns: rank, RPT Dist No, shoplifting incidents, robbery incidents, combined incidents. The first five rows are visually marked as the recommended second-guard shortlist. Option: `k`, default 10.

- **Evening-risk bar chart** (`evening_risk_chart`): horizontal bar chart of the ranked top 10 RPT Dist Nos, sort values in descending order of incident count. 
X-axis: combined reported offences
Y-axis: RPT Dist No. 
Tooltip shows the shoplifting and robbery breakdown.

- **Area comparison** (`area_comparison`): bar chart ranking every LAPD Area by combined qualifying evening offences. This supports quarterly prioritisation before the manager selects an area. Clicking an area sets the sidebar Area filter.

- **Export** (`export_ranked_table`): downloads the current ranked table as CSV, including the applied area, time window, offence codes, exclusion note, and export date.

Every results view shows this caption: “Reported offenses, not actual crime. Evening = 18:00–24:00. Drop data from January 2025 reporting.”