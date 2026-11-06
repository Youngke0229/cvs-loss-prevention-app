"""Count charged offense rows; never count distinct police reports."""
from datetime import date
import pandas as pd
from src.filter import qualifying_mask
from src.setup import AREAS

COUNTS = ['shoplifting_incidents', 'robbery_incidents', 'combined_incidents']
DISTRICT_COLUMNS = ['rank', 'RPT Dist No', *COUNTS]

def _counts(rows: pd.DataFrame, key: str) -> pd.DataFrame:
    counts = rows.groupby([key, 'NIBR Code']).size().unstack(fill_value=0)
    counts = counts.reindex(columns=['23C', '120'], fill_value=0)
    counts.columns = COUNTS[:2]
    counts['combined_incidents'] = counts.sum(axis=1)
    return counts.reset_index()

def summarize_areas(offenses: pd.DataFrame, start: date, end: date) -> pd.DataFrame:
    counts = _counts(offenses.loc[qualifying_mask(offenses, start, end)], 'AREA NAME')
    counts = counts.set_index('AREA NAME').reindex(AREAS, fill_value=0).reset_index()
    return counts.sort_values(['combined_incidents', 'AREA NAME'], ascending=[False, True]).reset_index(drop=True)

def rank_districts(filtered: pd.DataFrame, k: int = 10) -> pd.DataFrame:
    if isinstance(k, bool) or not isinstance(k, int) or k <= 0:
        raise ValueError(f'k must be a positive integer; got {k!r}')
    counts = _counts(filtered, 'RPT Dist No')
    counts = counts.sort_values(
        ['combined_incidents','shoplifting_incidents','robbery_incidents','RPT Dist No'], ascending=[False,False,False,True])
    counts = counts.head(k).reset_index(drop=True)
    counts.insert(0, 'rank', range(1, len(counts) + 1))
    return counts[DISTRICT_COLUMNS]
