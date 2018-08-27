# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 5/29/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, glob, time, logging
import copy, math
import functools, itertools
import numpy as np
import pandas as pd
import Implementations.config as config
CURRENT_PATH=config.CURRENT_PATH
CURRENT_TIME =config.CURRENT_TIME
'''===================================================================================================
File content:
load the data
==================================================================================================='''

def load_data(assets_dict, sta_date, end_date, folder_path=CURRENT_PATH+'/input_data', file_ext='csv'):
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	# Preparation Phrase
	res=None
	os.chdir(folder_path);
	filename_ls=[i for i in glob.glob('*.{}'.format(file_ext))];
	logging.debug('file name list is {}'.format(filename_ls));
	thres=len(filename_ls)

	# Handling Phrase
	for i,fi in enumerate(filename_ls):
		if i==0:
			res=pd.read_csv(fi, encoding='utf-8');
			res['asset_type'] = pd.Series(os.path.splitext(fi)[0], index=res.index)
		elif i+1<=thres:
			re=pd.read_csv(fi, encoding='utf-8');
			re['asset_type'] = pd.Series(os.path.splitext(fi)[0], index=re.index)
			res=res.append(re);  #ignore index can be added
		else:
			break


	# Checking Phrase
	logging.debug('load_data finished!');
	if isinstance(res, type(None)):
		logging.warning('load_data line56: No data loaded, system will return None!')
	os.chdir(CURRENT_PATH)
	return res
