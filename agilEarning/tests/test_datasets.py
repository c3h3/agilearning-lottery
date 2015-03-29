
import pandas as pd
from agilEarning.lottery import getHistoricalData


def test_fn_getHistoricalData():
    df = getHistoricalData(from_year=2004, to_year=2015, data_only=False)
    
    assert isinstance(df, pd.DataFrame)
    assert all(df.columns == pd.Index(["YN","TN","year","monthDay","x1","x2","x3","x4","x5","x6","s"], dtype='object'))
    assert df.shape == (1154, 11)
    
    
    
