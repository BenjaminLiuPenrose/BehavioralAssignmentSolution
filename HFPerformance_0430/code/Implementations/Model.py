# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
Before running please install packages *numpy *pandas *datetime *matplotlib
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from Implementations.LoadData import *
from Implementations.GetTicker import *
from Implementations.SplitDataByStock import *
from Implementations.GetOneStock import *
from Implementations.DataAnalysis import *
logging.getLogger().setLevel(logging.INFO)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

def model(file_rank=None):
	'''==============================================================================================
	Arguments:
	file_rank -- rank of the file to be selected,
					e.g 3, 6, 9 ... , default is None which will load all files in the pat

	Returns:
	res -- dict,
				-- {winning_rate, pnl_avg, pnl_ratio, hold_t_avg,...}
	=============================================================================================='''
	### Preparation Phrase
	## load the data 
	current_path=os.getcwd();
	dat=load_data(folder_path=current_path+'\Mar', num_files=None, file_rank=file_rank, file_ext='csv');
	os.chdir(current_path)
	#dat=load_data(folder_path='C:\Users\Benjamin\Desktop\Ben\code\Mar', num_files=None, file_ext='csv');
	logging.debug(dat.head());
	col_name_ls=['ticker','s_name','buy_sell','trade_t','trade_vol','trade_price','trade_code','trade_cost','trade_date'];
	dat.columns=col_name_ls;
	dat['trade_T']=pd.Series([datetime.datetime.strptime('2018'+row['trade_date']+' '+row['trade_t'], '%Y%m%d %H:%M:%S') 
		for _, row in dat.iterrows()], index=dat.index)           #defulted to be 2018

	## get the ticker
	stock_pool=get_ticker(data_table=dat);
	logging.debug('stock_pool: {}'.format(stock_pool));

	## split the table
	split_table_dict=split_data_by_stock(data_table=dat, stock_pool=stock_pool);
	logging.debug('split_table: {}'.format(split_table_dict.itervalues().next()));

	## create stock_dict
	stock_dict={};
	for s in stock_pool:
		stock=get_one_stock(split_data_table=split_table_dict, ticker=s);
		stock_dict[str(s)]=stock;
	logging.debug('stock_dict: {}'.format(stock_dict.itervalues().next()));

	### Handling Phrase
	## exploratory data analysis
	re=data_analysis(dat, stock_dict, file_rank, display=False);

	res=re;


	### Checking Phrase
	'Finished'
	return res


