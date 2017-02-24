import csv
import pandas as pd
import urllib3
import json
import matplotlib.pyplot as plt

stock_name_code={}
def get_stock_code():
	stocks_file=open('stocks_code.txt','r')
	stocks_data = stocks_file.readlines()
	for d in stocks_data:
		stock_name_code[d.rpartition('|')[0]]=d.rpartition('|')[2]	
	stock_name = input("Enter Stock Name:\n")
	stock_name = stock_name.lower()
	print(stock_name)
	stock_code = [stock_name_code[x] for x in stock_name_code if(stock_name in x.lower())]
	stock_code = stock_code[0].rpartition("\n")[0]
	quandl_code = "BSE/{0}".format(stock_code)
	return quandl_code

def get_data(code):
	http = urllib3.PoolManager()
	f = http.request('GET',"https://www.quandl.com/api/v3/datasets/{0}.json?api_key=8k-uP7DvHsuDsLc6qBmg".format(code))
	data = f.data.decode('utf-8')
	json1 = json.loads(data)
    #print(json)
	dates,open,high,low,close = filter_data(json1)
	return dates,open,high,low,close
	
def filter_data(json):
	column_names = [v for k,v in json['dataset'].items() if k=='column_names']
	data = [v for k,v in json['dataset'].items() if k=='data']
	dates = [x[0] for x in data[0]]
	#print(column_names)
	#print(dates[0])
	open = [x[1] for x in data[0]]
	high = [x[2] for x in data[0]]
	low = [x[3] for x in data[0]]
	close = [x[4] for x in data[0]]
	if(len(column_names[0])>5):
		no_of_shares = [x[6] for x in data[0]]
	#print(dates[0])
	year = [int(x[:4]) for x in dates]
	month = [int(x[5:7]) for x in dates]
	day = [int(x[8::]) for x in dates]
	return dates,open,high,low,close
	
def make_df(dates,open,high,low,close):
	stock_df = pd.DataFrame({
	'date':dates,	
	'open':open,
	'high':high,
	'low':low,
	'close':close
	})
	stock_df = stock_df.set_index(stock_df['date'])
	stock_df = stock_df.dropna() #Drop all the Rows having NaN value
	return stock_df

def plot(df):
	df.plot(kind='line',grid=True,rot=45)
	plt.show()
	
if __name__ == '__main__':
	code = get_stock_code()
	print(code)
	dates,open,high,low,close = get_data(code)
	stock_df = make_df(dates,open,high,low,close)
	print(stock_df)
	plot(stock_df)