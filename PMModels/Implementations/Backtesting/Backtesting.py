# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/1/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from datetime import timedelta
from datetime import datetime
from Implementations.get_daily_returns import *
from Implementations.get_daily_dates import *
from Implementations.initialize_parameters import *
'''===================================================================================================
File content:
Write comments
==================================================================================================='''

def backtesting(weights, context):
	'''==============================================================================================
	Arguments:


	Returns:

	=============================================================================================='''
	# Preparation Phrase
	res = {}
	weights_markowitz = list(weights['Markowitz'].values())
	weights_blacklitterman = list(weights['Black Litterman'].values())
	weights_riskparity = list(weights['Risk Parity'].values())


	sta_date, end_date, assets_pool = context['end date'], context['end date backtest'], context['assets pool']
	daily_returns = get_daily_returns(sta_date, end_date, assets_pool);
	daily_returns_pct = daily_returns['percentage returns'];
	daily_returns_diff = daily_returns['diff returns'];
	# dates_range = get_daily_dates(sta_date, end_date, assets_pool);
	dates_range = daily_returns['dates range'][0]
	# dates_range = [datetime.strptime(x, '%Y-%m-%d') for x in dates_range]
	logging.debug('Markowitz_model: daily_returns is {}'.format(daily_returns))

	ax = context['canvas ax']
	ax = ax['canvas_ax_3']

	# Handling Phrase
	cumpnl_daily_markowitz = np.dot(weights_markowitz, np.cumsum(daily_returns_diff, axis=1))
	cumpnl_daily_blacklitterman = np.dot(weights_blacklitterman, np.cumsum(daily_returns_diff, axis=1))
	cumpnl_daily_riskparity = np.dot(weights_riskparity, np.cumsum(daily_returns_diff, axis=1))
	ax.plot(dates_range, cumpnl_daily_markowitz, 'g-')
	ax.plot(dates_range, cumpnl_daily_blacklitterman, 'r-')
	ax.plot(dates_range, cumpnl_daily_riskparity, 'b-')

	# pnl_daily_markowitz = np.dot(weights_markowitz, daily_returns_pct)
	# pnl_daily_blacklitterman = np.dot(weights_blacklitterman, daily_returns_pct)
	# pnl_daily_riskparity = np.dot(weights_riskparity, daily_returns_pct)
	# ax2 = ax.twinx()
	# ax2.plot(dates_range, pnl_daily_markowitz, 'g--')
	# ax2.plot(dates_range, pnl_daily_blacklitterman, 'r--')
	# ax2.plot(dates_range, pnl_daily_riskparity, 'b--')
	ax.set_ylabel('Cum PNL');
	ax.set_xlabel('Dates');
	ax.legend(['Markowitz', 'Black Litterman', 'Risk Parity'], loc='upper right');
	ax.figure.canvas.draw();



	# Checking Phrase
	logging.info('backtesting: Backtesting finished successfully')
