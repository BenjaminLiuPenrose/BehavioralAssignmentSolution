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
from Implementations.Stock import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File Content:
Write comments
==================================================================================================='''

def split_data_by_stock(data_table, stock_pool=None):
	'''==============================================================================================
	Arguments:
	data_table -- pandas dataframe, it contains all the data in a table
					e.g. 证券代码|证券名称|交易类型|成交股数|成交价格|成交编号|交易费用
						69		69		卖出		14:55:44	8.72	xxxxxxxx	1.63

	Returns:
	res -- dict, dict of data splitted by ticker
					e.g {ticker: data_table}
	=============================================================================================='''
	# Preparation Phrase
	res={};
	dat=copy.deepcopy(data_table);
	if stock_pool==None:
		stock_pool=get_ticker(data_table);

	# Handling Phrase
	for s in stock_pool:
		re=dat[dat['ticker']==s];
		res[str(s)]=re;
	

	# Checking Phrase
	logging.debug('split_data_by_stock finished!');
	if res=={}:
		logging.warning('split_data_by_stock: the return dict is empty!');
	return res
