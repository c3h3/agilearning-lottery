import pandas as pd

def getHistoricalData(from_year=2004, to_year=2015, data_only=False):
    years = range(from_year, to_year)

    get_hist_table = lambda year: pd.read_html("http://www.nfd.com.tw/lottery/49-year/49-%s.htm" % year)[0][1:]
    hist_tables = map(get_hist_table,years)
    
    df = pd.concat(hist_tables)
    df.columns = ["year","monthDay","YN","x1","x2","x3","x4","x5","x6","s","TN"]
    
    if data_only:
        df = df[["x1","x2","x3","x4","x5","x6","s"]]
    else:
        df = df[["YN","TN","year","monthDay","x1","x2","x3","x4","x5","x6","s"]]
    
    return df