# 01-design.md

1. Clear pieces
I suggest we split the tool into 5 pieces, one job each:

    Load: reads the LAPD CSV, fixes padding, parses dates.

    Filter: keeps rows by LAPD Area, 23C/120, evening hours, and after 2025-02-01.

    Rank: groups by RPT Dist No, counts, takes the top 10.

    View: the Streamlit sidebar, table, bar chart, and caption.

    Setup: the default LAPD Area and default time window.

2. Simple connections
Only Load touches the files. Only View touches the screen. Every other piece works on a pandas object in memory. Each piece receives one thing and returns one thing: Load returns a clean DataFrame, Filter returns a filtered DataFrame, Rank returns a sorted Series, View draws it. The evening window and the risk codes live only in Filter, so a later change touches one place.

3. Local changes
What we are most likely to change later:

    the evening window and risk codes → one constant in Filter;

    the default LAPD Area and default time window → Setup;

    a new chart (for example a line chart over months) → one new piece next to View.

That way a change touches one file, not three.

4. Real-world operation
The offenses file is 471,285 rows and 143.4 MB (from data_overview_lapd-nibrs.md, section 4). The tool loads it all at startup and caches it with @st.cache_data. Each click only runs the filter and the ranker on the cached DataFrame, no re-read from disk. That is about 300-400 MB in memory, fine on a laptop. If we later add the victims table, we switch to DuckDB to load only the rows we need.
