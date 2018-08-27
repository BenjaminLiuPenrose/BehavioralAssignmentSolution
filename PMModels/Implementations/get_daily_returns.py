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
import pandas_datareader.data as web
import Implementations.config as config
CURRENT_PATH=config.CURRENT_PATH
CURRENT_TIME =config.CURRENT_TIME
FREQ_CONVERSION=config.FREQ_CONVERSION
'''===================================================================================================
File content:
get the daily returns
==================================================================================================='''

def get_daily_returns(sta_date, end_date, assets_pool, freq="daily"):
	'''==============================================================================================
	Arguments:
	sta_date 		--datetime object, start date
	end_date 		--datetime object, end date
	assets_pool		--list of string, list of assets
	freq 			--string, used to look up periods in FREQ_CONVERSION={"daily": (1, 252),"weekly": (5, 					50),"monthly": (20, 12),"yearly": (252, 1),"annually": (252, 1)}

	Returns:
	res 			--dict of np.array,
					e.g. {'percentage returns': np.array
							'log returns': np.array }
	=============================================================================================='''
	# Preparation Phrase
	res = {}; R_pct = []; R_log = []; R_diff = []; dates = [];
	(period, _) = FREQ_CONVERSION[freq.lower()]
	DATABASE_LIST=["quandl", "google", "fred", "famafrench", "oecd", "stooq", "moex"]
	switch = True;

	# Handling Phrase
	for asset in assets_pool:
		try:
			df = web.DataReader(asset, "morningstar", sta_date, end_date);
			pct_ret = df['Close'].pct_change(period).values
			log_ret = (np.log(df['Close']) - np.log(df['Close'].shift(period))).values
			diff_ret = df['Close'].diff(period).values;
			R_pct.append(pct_ret[~np.isnan(pct_ret)]);
			R_log.append(log_ret[~np.isnan(log_ret)]);
			R_diff.append(diff_ret[~np.isnan(diff_ret)]);
			if switch:
				df = df.reset_index();
				dates_ = df['Date'][period:].values;
				dates.append(dates_);
				switch = False;
			# logging.info('get_daily_returns: {} begins'.format(asset))
		except Exception as e:
			logging.error('Error message: {}\nError occurred! Asset {} data cannot be pulled!'.format(e, asset))
	R_pct = np.array(R_pct)
	R_log = np.array(R_log)
	R_diff = np.array(R_diff)
	dates = np.array(dates)

	# Checking Phrase
	res['percentage returns'] = R_pct;
	res['log returns'] = R_log;
	res['diff returns'] = R_diff;
	res['dates range'] = dates;
	logging.debug('get_daily_returns finished!');
	if res == {}:
		logging.warning('get_daily_returns: No data loaded, system will return None!')
	return res


# depreciated method and need to be modified
def get_daily_returns2(sta_date, end_date, assets_pool, folder_path=CURRENT_PATH+'/input_data', file_ext='csv'):
	'''==============================================================================================
	Arguments:
	assets_pool		--list of string, list of assets
	sta_date 		--datetime object, start date
	end_date 		--datetime object, end date
	folder_path		--string, path of the input data folder
					defaulted under CURRENT_PATH+'/input_data'
	file_ext 		--string, type of the file extensive
					defaulted of type csv

	Returns:
	res 			--np array, daily returns
	=============================================================================================='''
	# Preparation Phrase
	res = {}
	ress = []
	os.chdir(folder_path);
	filename_ls = [i for i in glob.glob('*.{}'.format(file_ext))];
	logging.debug('file name list is {}'.format(filename_ls));
	thres = len(filename_ls)

	# Handling Phrase
	for i,fi in enumerate(filename_ls):
		re = pd.read_csv(fi, encoding = 'utf-8')
		re['Date'] = pd.to_datetime(re['Date'])
		mask = (re['Date'] >= sta_date) &(re['Date'] <= end_date)
		re = re.loc[mask]
		re_diff = np.array(re['Close']/re['Close'].shift(-1))
		re_change = np.log(re_diff)
		re_change = re_change[~np.isnan(re_change)]
		ress.append(re_change)

		# re['asset_type'] = pd.Series(os.path.splitext(fi)[0], index=re.index)
	res['percentage returns'] = np.array(ress)


	# Checking Phrase
	logging.debug('get_daily_returns finished!');
	if isinstance(res, type(None)):
		logging.warning('get_daily_returns: No data loaded, system will return None!')
	os.chdir(CURRENT_PATH)
	return res
