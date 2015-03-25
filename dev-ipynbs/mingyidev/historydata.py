# coding: utf-8
get_ipython().magic('pylab inline')
import pandas as pd
from datetime import datetime,time,date
d=date.today()
y=d.year
#讀歷屆資料
years = range(2008, y+1)
#get_hist_table = lambda year: pd.read_html("http://www.nfd.com.tw/lottery/power-38/%s.htm" % year,infer_types=False)[0][1:]
get_hist_table = lambda year: pd.read_html("http://www.nfd.com.tw/lottery/power-38/{0}.htm".format(year),header=0,infer_types=False)[0]
t=map(get_hist_table,years)
#ignore_index忽略本來排序
dfs=pd.concat(list(t),ignore_index=True)
dfs
#keys可以拿來看index,columns
dfs.keys()
dfs.columns = ["year","monthDay","YN","x1","x2","x3","x4","x5","x6","s","TN"]
#df = df[["YN","TN","year","monthDay","x1","x2","x3","x4","x5","x6","s"]]
dfs['month']=dfs['monthDay'].map(lambda x:int(x.split("/")[0]))
dfs['day']=dfs['monthDay'].map(lambda x:int(x.split("/")[1]))
for i in ['year', 'YN', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 's', 'TN']:
    dfs[i]=dfs[i].map(int)
dfs.head()
dfs = dfs[["TN","YN","year","month","day","x1","x2","x3","x4","x5","x6","s"]]
