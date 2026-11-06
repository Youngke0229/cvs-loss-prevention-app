"""All screen rendering and exports, without recomputing offense counts."""
from datetime import datetime
from zoneinfo import ZoneInfo
import altair as alt
import pandas as pd
import streamlit as st
from src.setup import Defaults

CAPTION = 'Reported offenses, not actual crime. Evening = 18:00–24:00. January 2025 reporting break excluded.'
RED = '#b5122b'
GRAY = '#a6adb7'

def select_area(defaults: Defaults, area_summary: pd.DataFrame) -> str:
    st.set_page_config(page_title='CVS | Evening Loss Prevention', page_icon='🔴', layout='wide')
    st.markdown('''<style>
    .stApp {background-color:#fafafa;} h1 {letter-spacing:-.035em;}
    [data-testid="stSidebar"] {background-color:#f1f2f4;}
    [data-testid="stSidebar"] h2 {font-size:1.2rem;}
    .block-container {padding-top:3.5rem;padding-bottom:1rem;}
    </style>''', unsafe_allow_html=True)
    with st.sidebar:
        st.markdown('**CVS HEALTH** · LOS ANGELES')
        st.header('Evening allocation')
        options = sorted(area_summary['AREA NAME'].tolist())
        selected = st.selectbox('LAPD Area', options, index=options.index(defaults.default_area))
        st.caption(f'Reporting window\n\n{defaults.start:%b %d, %Y} – {defaults.end:%b %d, %Y}')
        st.subheader('Area comparison')
        st.caption('All 21 Areas · combined reported offenses')
        chart = alt.Chart(area_summary).mark_bar(color=GRAY, cornerRadiusEnd=2).encode(
            x=alt.X('combined_incidents:Q', title='Combined offenses', axis=alt.Axis(tickCount=3)),
            y=alt.Y('AREA NAME:N', sort=area_summary['AREA NAME'].tolist(), title=None, axis=alt.Axis(labelOverlap=False, labelFontSize=10)),
            color=alt.condition(alt.datum['AREA NAME'] == selected, alt.value(RED), alt.value(GRAY)),
            tooltip=['AREA NAME:N', 'shoplifting_incidents:Q','robbery_incidents:Q','combined_incidents:Q']
        ).properties(height=430).configure_view(strokeWidth=0)
        st.altair_chart(chart, width='stretch')
        st.caption(CAPTION)
    return selected

def export_ranked_table(ranked: pd.DataFrame, area: str, defaults: Defaults) -> bytes:
    exported = ranked.copy()
    for key, value in {
        'applied_area': area, 'reporting_start': defaults.start.isoformat(),
        'reporting_end': defaults.end.isoformat(), 'evening_window': '18:00–24:00 (Time OCC)',
        'offense_codes': '23C; 120', 'exclusion_note': 'January 2025 reporting break excluded',
        'export_date': datetime.now(ZoneInfo('America/Los_Angeles')).date().isoformat(),
    }.items():
        exported[key] = value
    return exported.to_csv(index=False).encode('utf-8-sig')

def render_results(ranked: pd.DataFrame, area_summary: pd.DataFrame,
                   selected_area: str, defaults: Defaults, metadata: dict) -> None:
    st.title('Evening Loss-Prevention Navigator')
    st.write('Prioritize five reporting districts for a second evening guard. Assign individual stores using local knowledge.')
    st.subheader(f'{selected_area} · district priorities')
    st.caption(f'{defaults.start:%b %d, %Y} – {defaults.end:%b %d, %Y} · Date reported · Shoplifting 23C + robbery 120')
    st.markdown('**Red marks the first five priority districts** · ranks are based on charged offense rows.')
    left, right = st.columns([1.15, 1], gap='large')
    with left:
        st.markdown('**Top 10 reporting districts**')
        styled = ranked.style.apply(lambda row: ['background-color:#fce7eb;color:#85152a;font-weight:600' if row['rank'] <= 5 else '' for _ in row], axis=1)
        st.dataframe(styled, hide_index=True, width='stretch', height=390,
            column_config={'rank':st.column_config.NumberColumn('Rank', format='%d'),
                'RPT Dist No': st.column_config.TextColumn('RPT Dist No'),
                'shoplifting_incidents':st.column_config.NumberColumn('Shoplifting', format='%d'),
                'robbery_incidents':st.column_config.NumberColumn('Robbery', format='%d'),
                'combined_incidents':st.column_config.NumberColumn('Combined', format='%d')})
        st.caption(CAPTION)
        st.download_button('Download ranked CSV', export_ranked_table(ranked, selected_area, defaults),
            file_name=f'evening_priorities_{selected_area.lower().replace(" ", "_")}_{defaults.end}.csv',
            mime='text/csv', disabled=ranked.empty, type='primary')
    with right:
        st.markdown('**Evening reported offenses**')
        if ranked.empty:
            st.info('No qualifying offenses for this Area and reporting window.')
        else:
            chart = alt.Chart(ranked).mark_bar(cornerRadiusEnd=3).encode(
                y=alt.Y('RPT Dist No:N', sort=ranked['RPT Dist No'].tolist(), title='RPT Dist No'),
                x=alt.X('combined_incidents:Q', title='Combined reported offenses'),
                color=alt.condition(alt.datum.rank <= 5, alt.value(RED), alt.value(GRAY)),
                tooltip=[alt.Tooltip('rank:Q', title='Rank'), 'RPT Dist No:N',
                    'shoplifting_incidents:Q', 'robbery_incidents:Q', 'combined_incidents:Q']
            ).properties(height=350).configure_view(strokeWidth=0)
            st.altair_chart(chart, width='stretch')
        st.caption(CAPTION)
    quality = metadata['quality']
    st.caption(f"Source: LAPD NIBRS · downloaded {metadata['download_date']} · {quality['input_rows']:,} offense rows · {quality['distinct_AREA']} Areas")
    with st.expander('Methodology & data quality'):
        st.markdown(f"""[City of Los Angeles · LAPD NIBRS offenses]({metadata['source_url']}). Counts represent **charged offense rows**, not distinct reports, actual crime, CVS incidents, or store-level risk. Occurrence time determines the evening shift; reporting date determines inclusion in the configured range. Local Los Angeles clock time is assumed.

Districts sort by combined offenses, shoplifting, robbery (descending), then district number (ascending). The first five are the priority shortlist. Area comparison uses the same filters and includes Areas with zero matches. Missing districts cannot be ranked.

Full-source quality: **{quality['missing_Date_Rptd']:,}** missing/invalid report dates; **{quality['missing_Date_OCC']:,}** missing/invalid occurrence dates; **{quality['missing_or_invalid_Time_OCC']:,}** missing/invalid times. Missing report dates and times are excluded by the filters. Occurrence dates and coordinates are not used. No missing values are imputed.

January 2025 reporting is excluded. This fixed window can be changed in `configs/default.toml`. Recent months may be incomplete. There is no store count, foot traffic, loss amount, or causal evidence of a guard's impact. Use local store knowledge for assignments.""")
        check = metadata['configuration_check']
        st.write(f"Snapshot completeness check ({check['end'][:7]}): {check['end_month_count']:,} reports versus a prior-six-month median of {check['previous_six_month_median']:,.0f}. Next month: {check['next_month_count']:,} reports. Threshold: 90% of each month's prior-six-month median. This is a completeness heuristic, not a guarantee.")
