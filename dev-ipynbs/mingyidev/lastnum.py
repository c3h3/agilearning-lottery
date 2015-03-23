# coding: utf-8
get_ipython().magic('pylab inline')
import pandas as pd
# 今天日期
from datetime import datetime,time,date
today_date = date.today()
print (today_date)
#抓現有樂透。。。先試著抓下來就好
df= pd.read_html("http://www.nfd.com.tw/lottery/power-38/2015.htm",parse_dates=[])
#要把那唯一的一個抓下來
len(df)
#到了py3就把單純的數字視作了日期，以下先暫時弄出來
df= pd.read_html("http://www.nfd.com.tw/lottery/power-38/2015.htm",header=0,infer_types=False)[0]
df.head()
l=len(df)-1
last=df.ix[l]
last
last=pd.DataFrame(last)
last.index
print ("上一期號碼 "+last.ix['球號 1'].values+","+last.ix['球號 2'].values+","+last.ix['球號 3'].values+","+last.ix['球號 4'].values+","+last.ix['球號 5'].values+","+last.ix['球號 6'].values)
#print ("上一期開獎時間 "+last.ix['年份'].values+"/ "+last.ix['日期'].values)
#顯示星期幾用weekday()
today_date.weekday()
#把日期弄成看得懂的方式去辨識
u=str(last.ix['日期'].values).strip("[']")
u=u.split("/ ")
int(u[0])
y=str(last.ix['年份'].values).strip("[']")
y
#d=",".join((y,u[0],u[1]))
w=date(int(y),int(u[0]),int(u[1])).weekday()
def weekday(x):
    n=({0:u"一",1:u"二",2:u"三",3:u"四",4:u"五",5:u"六",6:u"日"})
    return (n[x])
print ("上一期開獎時間 "+last.ix['年份'].values+"/ "+last.ix['日期'].values+" ("+str(weekday(w))+")")
