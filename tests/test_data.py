import pandas as pd
import pytest
from src.data import load_offenses

def write_source(tmp_path, duplicate=False):
    frame = pd.DataFrame({
        'CaseNo':['00012','RFC CITATION','00014'], 'UniqueNIBRNo':['a','a' if duplicate else 'b','c'],
        'Date Rptd':['02/01/2025 11:59:59 PM','bad',None],
        'Date OCC':['01/01/1800 12:00:00 AM',None,'invalid'],
        'Time OCC':['5','2460',None], 'AREA':['1','02',None],
        'AREA NAME':['Central    ','Rampart  ',None], 'RPT Dist No':['101','201',None],
        'NIBR Code':['23C','120','220'], 'Hate Crime':['Yes','No',None],
        'Domestic Violence Crime':['Yes','No',None], 'Unused':['x']*3})
    path = tmp_path / 'offenses.csv'
    frame.to_csv(path,index=False)
    return path

def test_normalization_and_quality(tmp_path):
    df = load_offenses(write_source(tmp_path))
    assert len(df) == 3
    assert df['CaseNo'].tolist() == ['00012','RFC CITATION','00014']
    assert df.iloc[0]['Time OCC'] == '0005'
    assert df['Time OCC'].isna().sum() == 2
    assert df.iloc[0]['RPT Dist No'] == '0101' and df.iloc[0]['AREA'] == '01'
    assert df.iloc[0]['AREA NAME'] == 'Central'
    assert df.iloc[0]['Type of Crime'] == 'Hate Crime; Domestic Violence Crime'
    assert 'Hate Crime' not in df and 'Unused' not in df
    assert df.attrs['quality']['missing_Date_Rptd'] == 2
    assert df.attrs['quality']['missing_Date_OCC'] == 2
    assert df['RPT Dist No'].isna().sum() == 1

def test_duplicate_stops_with_actionable_message(tmp_path):
    with pytest.raises(ValueError, match='UniqueNIBRNo.*duplicate'):
        load_offenses(write_source(tmp_path, True))
