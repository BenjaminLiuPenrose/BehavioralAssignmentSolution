# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 5/29/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matpotlib
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import Implementations.config as config
FREQ_CONVERSION=config.FREQ_CONVERSION

'''===================================================================================================
File content:
compute mean, covariance and variance of portfolio
==================================================================================================='''

def assets_mean_var(daily_returns, freq="daily"):
	'''==============================================================================================
	Arguments:
	daily_returns 	-- np.array of np.array, past returns of all assets

	Returns:
	res -- dict, {'mean', 'cov', 'var', 'std'}
	=============================================================================================='''
	# Preparation Phrase
	res = {}
	rows, cols = daily_returns.shape
	mean = [];
	cov = [];
	var = [];
	std = [];
	(_, conv_factor) = FREQ_CONVERSION[freq.lower()]
	# logging.debug("row: {}, cols: {}".format(rows, cols))

	# Handling Phrase
	for i in range(rows):
		mean.append(np.mean(daily_returns[i]))
	mean = np.array(mean)
	mean = (1+mean)**conv_factor-1

	cov = np.cov(daily_returns)
	cov = cov*conv_factor

	var = [cov[i][i] for i in range(rows)]
	var = np.array(var)

	std = np.sqrt(var)

	# Checking Phrase
	res['mean'] = mean
	res['cov'] = cov
	res['var'] = var
	res['std'] = std
	return res
