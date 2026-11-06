"""Run with: streamlit run app.py"""
from pathlib import Path
import streamlit as st
from src.data import load_prepared
from src.setup import load_defaults
from src.filter import filter_offenses
from src.rank import summarize_areas, rank_districts
from src.view import select_area, render_results

ROOT = Path(__file__).resolve().parent

@st.cache_data(show_spinner=False)
def area_summary(offenses, start, end):
    return summarize_areas(offenses, start, end)

def main():
    defaults = load_defaults(ROOT / 'configs/default.toml')
    offenses, metadata = load_prepared(ROOT / 'data/processed/offenses.parquet', ROOT / 'data/processed/metadata.json')
    areas = area_summary(offenses, defaults.start, defaults.end)
    selected = select_area(defaults, areas)
    districts = rank_districts(filter_offenses(offenses, selected, defaults.start, defaults.end))
    render_results(districts, areas, selected, defaults, metadata)

if __name__ == '__main__':
    main()
