from pathlib import Path
from datetime import date
from io import BytesIO
from unittest.mock import patch
import json
import pandas as pd
import streamlit as st
from pandas.testing import assert_frame_equal
from streamlit.testing.v1 import AppTest
from src.data import load_prepared
from src.setup import load_defaults
from src.filter import filter_offenses
from src.rank import summarize_areas, rank_districts
from src.view import export_ranked_table

def test_config_fits_full_snapshot():
    df, meta = load_prepared('data/processed/offenses.parquet','data/processed/metadata.json')
    defaults = load_defaults()
    areas = summarize_areas(df, defaults.start, defaults.end)
    assert len(areas) == 21 and areas.iloc[0]['AREA NAME'] == defaults.default_area
    check = meta['configuration_check']
    assert check['end'] == str(defaults.end)
    assert check['end_month_complete'] and not check['next_month_complete']

def test_screen_selection_cache_chart_and_export():
    load_prepared.clear()
    with patch('src.data.pd.read_parquet', wraps=pd.read_parquet) as read, patch('src.view.st.altair_chart', wraps=st.altair_chart) as charts:
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=30)
        assert not app.exception
        defaults = load_defaults()
        assert app.selectbox[0].value == defaults.default_area
        assert len(app.dataframe) == 1
        first = app.dataframe[0].value.copy()
        assert len(app.get('vega_lite_chart')) == 2
        assert_frame_equal(charts.call_args_list[1].args[0].data, first)
        app.selectbox[0].select('Mission' if defaults.default_area != 'Mission' else 'Topanga').run()
        assert not app.exception
        assert not first.equals(app.dataframe[0].value)
        assert read.call_count == 1
        assert_frame_equal(charts.call_args_list[3].args[0].data, app.dataframe[0].value)
    ranked = app.dataframe[0].value
    exported = pd.read_csv(BytesIO(export_ranked_table(ranked, app.selectbox[0].value, defaults)), dtype={'RPT Dist No':'string'})
    assert exported['RPT Dist No'].tolist() == ranked['RPT Dist No'].tolist()
    assert exported['combined_incidents'].tolist() == ranked['combined_incidents'].tolist()
    for key in ['applied_area','evening_window','offense_codes','exclusion_note','export_date','reporting_start','reporting_end']:
        assert key in exported and exported[key].notna().all()

def test_empty_result_renders():
    df, meta = load_prepared('data/processed/offenses.parquet','data/processed/metadata.json')
    with patch('src.data.load_prepared', return_value=(df.iloc[:0],meta)):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=30)
    assert not app.exception
    assert app.dataframe[0].value.empty
    assert any('No qualifying offenses' in item.value for item in app.info)
