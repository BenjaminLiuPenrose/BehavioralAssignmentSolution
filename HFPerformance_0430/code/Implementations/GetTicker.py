# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
Before running please install packages *numpy, *pandas
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, glob, time, logging
import copy, math
import functools, itertools
import numpy as np 
import pandas as pd 
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File Content:
Write comments
==================================================================================================='''

def get_ticker(data_table):
	'''==============================================================================================
	Arguments:
	data_table -- a pandas dataframe, it contains all the data in a table
					e.g. 证券代码|证券名称|交易类型|交易时间|成交股数|成交价格|成交编号|交易费用
						69		69		卖出		14:55:44	160		8.72	xxxxxxxx	1.63

	Returns:
	ticker_ls -- list, it contains all stocks
	=============================================================================================='''
	# Preparation Phrase
	ticker_ls=[];
	dat=copy.deepcopy(data_table);

	# Handling Phrase
	trade_stock_ls=dat['ticker'].tolist();
	ticker_ls=set(trade_stock_ls);
	ticker_ls=[int(ticker) for ticker in ticker_ls];

	# Checking Phrase
	logging.debug('get_ticker finished!');
	if ticker_ls==[]:
		logging.warning('Cannot get any tickers from the given data, system will return None!')
	return ticker_ls
