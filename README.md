# Stock_Price_data_Analyses
Scripts related to stock market

Libraries and Packages used : JSON,MATPLOTLIB, URLLIB3 <break>
API USED : quandl (visit : www.quandl.com)

<b>"reliance.py"</b> --> Shows stock trend plot('reliance.png' is the output of the script) of RELIANCE COMMUNICATION BSE stocks from the day it started till the day you will run the script. The time, open, close, high, low values are plotted as a vertical line ranging from low to high. A rectangular bar represent the open-close span. If close >= open,the bar is of color black, otherwise bar is of color red.

<b>"data_acquisation.py"</b> --> Shows stock trend plot of any stock listed in BSE. User is asked for stock name. It's HIGH,LOW,CLOSE,OPEN values are extracted from quandl and dataframe is made with those values. Then these values are plotted to see general trend of that stock till now.
