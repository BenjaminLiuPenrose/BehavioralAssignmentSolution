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

def get_daily_dates(sta_date, end_date, assets_pool, freq="daily"):
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
	res = {}; dates = [];
	(period, _) = FREQ_CONVERSION[freq.lower()]
	DATABASE_LIST=["quandl", "google", "fred", "famafrench", "oecd", "stooq", "moex"]

	# Handling Phrase
	for asset in assets_pool:
		df = web.DataReader(asset, "morningstar", sta_date, end_date);
		df = df.reset_index();
		dates_ = df['Date'][period:].values   ##error prone
		# log_ret = (np.log(df['Close']) - np.log(df['Close'].shift(period))).values
		dates.append(dates_);
		break
	dates = np.array(dates)

	# Checking Phrase
	res['dates range'] = dates;
	logging.debug('get_daily_dates finished!');
	if res == {}:
		logging.warning('get_daily_returns: No data loaded, system will return None!')
	return res

