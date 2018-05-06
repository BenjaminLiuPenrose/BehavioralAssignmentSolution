# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
Before running please install packages *numpy, *pandas, *datetime
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, glob, time, logging
import copy, math
import functools, itertools
import numpy as np 
import pandas as pd 
import datetime
from Implementations.Stock_ import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File Content:
Write comments
==================================================================================================='''

def get_one_stock(split_data_table, ticker):
	'''==============================================================================================
	Arguments:
	split_data_table -- dict, dict of data splitted by ticker
					e.g {ticker: data_table}
					e.g. 证券代码|证券名称|交易类型|成交股数|成交价格|成交编号|交易费用
						69		69		卖出		14:55:44	8.72	xxxxxxxx	1.63
	ticker -- int, ticker for stock

	Returns:
	stock -- an object of class Stock
	=============================================================================================='''
	# Preparation Phrase
	stock=Stock(ticker);
	dat=split_data_table[str(ticker)];
	dat=dat.sort_values(['trade_T'], ascending=True);

	# Handling Phrase
	for _, row in dat.iterrows():
		#########################################needs improvement#################################
		buy_t=datetime.datetime.strptime(row['trade_date']+' '+row['trade_t'], '%m%d %H:%M:%S');
		if row['buy_sell'].lower()=='buy':
			stock.buy(int(row['trade_vol']), buy_t, float(row['trade_price']), float(row['trade_cost']))  # trade_vol, trade_t, trade_price, trade_cost
		else :                                                      # row['buy_sell']=='卖出'：
			stock.sell(int(row['trade_vol']), buy_t, float(row['trade_price']), float(row['trade_cost']))

	stock.clearing();

	# Checking Phrase
	logging.debug('get_one_stock finished for ticker {}!'.format(ticker))
	return stock
