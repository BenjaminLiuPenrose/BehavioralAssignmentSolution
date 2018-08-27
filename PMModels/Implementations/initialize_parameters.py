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
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from Implementations.get_daily_returns import *
from datetime import datetime

'''===================================================================================================
File content:
initialize hyper-parameters in the model
==================================================================================================='''

def initialize_parameters(init_dict = None):
	'''==============================================================================================
	Arguments:
	init_dict 	--dict, input data, parqams and others to the model, some are optional

	Returns:
	context	--dict, context of backtesting
	=============================================================================================='''
	# Preparation Phrase
	context = {}

	# Handling Phrase
	## defaulted value
	### hyper perams
	training_set_window = 'N/A';
	validation_set_window = 'N/A';
	test_set_window = 'N/A';
	mean_var_window = 'N/A';
	rebalance_freq = 'N/A';
	max_notional = 1000000.1;
	min_notional = -1000000.0;
	commission = 0.001;
	slippery = 0;

	### params
	rf = 0.0;
	canvas_ax = None;

	risk_adversion = 0.8;
	start_date = datetime(2018, 1, 2)
	end_date = datetime(2018, 6, 1)
	end_date_backtest = datetime.now()
	assets_dict = {
		"Equity": ['SPY', 'FEZ', 'ASHR'], #, 'NKY', '2800.HK'
		"Commodity": ['DBC', 'DBV'], #
		"Nominal Bond": ['TLT', 'IEF', 'VWOB'], #
		"IL Bond": ['TIP', 'VTIP'], #
		"Corporate Credit": ['LQD', 'VCSH', 'VCIT'], #
		'EM Credit': ['CEMB', 'EMB'] #, 'CEHY'
	}
	env_assetclasses_dict = {
		"GR": ["Equity", "Commodity', 'EM Credit', 'Corporate Credit'"],
		"GF": ["Nominal Bond", "IL Bond"],
		"IR": ["IL Bond", "Commodity', 'EM Credit'"],
		"IF": ["Equity", "Nominal Bond"]
	}

	### misc params
	weights_file = "weight/weights.csv"

	## any updates from the user
	if init_dict != None:
		if init_dict.get('risk adversion', 'Not Found') != 'Not Found':
			risk_adversion = init_dict['risk adversion']
		if init_dict.get('start date', 'Not Found') != 'Not Found':
			start_date = init_dict['start date']
		if init_dict.get('end date', 'Not Found') != 'Not Found':
			end_date = init_dict['end date']
		if init_dict.get('end date backtest', 'Not Found') != 'Not Found':
			end_date_backtest = init_dict['end date backtest']
		if init_dict.get('rebalance frequency', 'Not Found') != 'Not Found':
			rebalance_freq = init_dict['rebalance frequency']
		if init_dict.get('assets dict', 'Not Found') != 'Not Found':
			for key in init_dict['assets dict']:
				assets_dict[key] = init_dict['assets dict'][key]
		if init_dict.get('canvas ax', 'Not Found') != 'Not Found':
			canvas_ax = init_dict['canvas ax']

	'HANDLING ASSETS HERE'
	assets_pool = []
	assetclasses_pool = []
	for clas in assets_dict:
		assets_pool.extend(assets_dict[clas])
		assetclasses_pool.append(clas)
	# assets_idx_to_tickers = dict([(i, x) for i, x in enumerate(assets_pool)])
	# assetclasses_idx_to_tickers = dict([(i, x) for i, x in enumerate(assetclasses_pool)])

	'HANDLING DATETIME HERE'
	training_set_window = (end_date - start_date).days;
	validation_set_window = 0;
	test_set_window = (end_date_backtest - end_date).days;
	rebalance_freq_days, rebalance_freq_numperyear = rebalance_freq;

	###================================Migrate Daily Returns Here=======================================================']
	daily_returns = get_daily_returns(start_date, end_date, assets_pool);
	daily_returns = daily_returns['percentage returns'];
	weights_cap = np.ones([len(assets_pool)])/len(assets_pool);
	###================================Migrate Daily Returns Here=======================================================']

	# Checking Phrase
	context = {
		'training set window': training_set_window,
		'validation set window': validation_set_window,
		'test set window': test_set_window,
		'mean var window': mean_var_window,
		'rebalance frequency': rebalance_freq_days,
		'rebalance_frequency_2': rebalance_freq_numperyear,
		'max notional': max_notional,
		'min notional': min_notional,
		'commission': commission,
		'slippery': slippery,
		'rf': rf,
		'canvas ax': canvas_ax,
		'risk adversion': risk_adversion,
		'start date': start_date,
		'end date': end_date,
		'end date backtest': end_date_backtest,
		'assets dict': assets_dict,
		'env assetclasses dict': env_assetclasses_dict,
		'assets pool': assets_pool,
		'asset classes pool': assetclasses_pool,
		'weights cap': weights_cap,
		'daily returns': daily_returns,
		'weights file': weights_file
	}
	# context['assets idx to tickers'] = assets_idx_to_tickers
	# context['asset classes idx to tickers'] = assetclasses_idx_to_tickers

	return context
