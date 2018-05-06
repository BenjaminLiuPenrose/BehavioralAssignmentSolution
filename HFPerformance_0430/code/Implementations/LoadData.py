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

def load_data(folder_path, num_files=None, file_rank=None, file_ext='csv'):
	'''==============================================================================================
	Arguments:
	folder_path -- string, path from which the program will load the data,
					e.g C:\Users\Benjamin\Desktop\Ben\Mar
	num_files -- int, number of files to be loaded,
					e.g 3, 6, 9 ... , default is None which will load all files in the path
	file_rank -- rank of the file to be selected,
					e.g 3, 6, 9 ... , default is None which will load all files in the path
	file_ext -- string, type of files to be load,
					e.g default is csv

	Returns:
	res -- a pandas dataframe, it contains all the data 
					e.g. 证券代码|证券名称|交易类型|交易时间|成交股数|成交价格|成交编号|交易费用
						69		69		卖出		14:55:44	160		8.72	xxxxxxxx	1.63
	=============================================================================================='''
	# Preparation Phrase
	res=None;
	os.chdir(folder_path);
	filename_ls=[i for i in glob.glob('*.{}'.format(file_ext))];
	logging.debug('file name list is {}'.format(filename_ls));

	if num_files==None or num_files>len(filename_ls):
		thres=len(filename_ls);
	else :
		thres=num_files;

	# Handling Phrase
	if file_rank!=None and isinstance(file_rank, int):
		if file_rank<len(filename_ls) and file_rank>=0:
			fi=filename_ls[file_rank];
			res=pd.read_csv(fi, encoding='utf-8');
			res['trade_date'] = pd.Series(filter(str.isdigit, fi), index=res.index)
			return res

	for i,fi in enumerate(filename_ls):
		if i==0:
			res=pd.read_csv(fi, encoding='utf-8');
			res['trade_date'] = pd.Series(filter(str.isdigit, fi), index=res.index)
		elif i+1<=thres:
			re=pd.read_csv(fi, encoding='utf-8')
			re['trade_date'] = pd.Series(filter(str.isdigit, fi), index=re.index)
			res=res.append(re);  #ignore index can be added
			#res=pd.concat([res, re]);
		else:
			break

	# Checking Phrase
	logging.debug('load_data finished!');
	if isinstance(res, type(None)):
		logging.warning('No data loaded, system will return None!')
	return res 

