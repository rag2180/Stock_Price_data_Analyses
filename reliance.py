import urllib3
import json
import matplotlib.pyplot as plt
import matplotlib.finance as fin
import datetime
from matplotlib.finance import date2num

http = urllib3.PoolManager()

f = http.request('GET',"https://www.quandl.com/api/v3/datasets/BSE/BOM532712.json?api_key=8k-uP7DvHsuDsLc6qBmg")
data = f.data.decode('utf-8')
#print(data)
json = json.loads(data)
#print(json)

column_names = [v for k,v in json['dataset'].items() if k=='column_names']
data = [v for k,v in json['dataset'].items() if k=='data']
dates = [x[0] for x in data[0]]
open = [x[1] for x in data[0]]
high = [x[2] for x in data[0]]
low = [x[3] for x in data[0]]
close = [x[4] for x in data[0]]
no_of_shares = [x[6] for x in data[0]]

print(dates[0])
year = [int(x[:4]) for x in dates]
month = [int(x[5:7]) for x in dates]
day = [int(x[8::]) for x in dates]
float_days=[]
for i in range(len(year)):
	float_days.append(date2num(datetime.datetime(year[i], month[i], day[i])))
#print(float_days)

quotes=[[]]
for i in range(len(year)):
	quotes.append([float_days[i],open[i],close[i],high[i],low[i]])

quotes = quotes[1::]
ax = plt.gca()
plt.title("RELIANCE COMMUNICATIONS STOCK PRICE TREND TILL TODAY")
plt.ylabel("Price")
plt.xlabel("Date(epoch)")
fin.candlestick_ochl(ax,quotes,width=0.2, colorup='k', colordown='r', alpha=1.0) 
'''
Plot the time, open, close, high, low as a vertical line ranging from low to high. Use a rectangular bar to represent the open-close span. 
If close >= open, use colorup to color the bar, otherwise use colordown
'''
plt.show()
