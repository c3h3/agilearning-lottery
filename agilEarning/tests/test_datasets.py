
import pandas as pd
from agilEarning.lottery import getHistoricalData


def test_fn_getHistoricalData():
    df = getHistoricalData(from_year=2004, to_year=2015, data_only=False)
    
    assert isinstance(df, pd.DataFrame)
    assert all(df.columns == pd.Index([u'TN', u'YN', u'year', u'month', u'day', u'x1', u'x2', u'x3', u'x4', u'x5', u'x6', u's'], dtype='object'))
    assert df.shape == (1154, 12)
