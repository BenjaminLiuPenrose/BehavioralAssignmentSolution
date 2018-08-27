# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 5/29/2018

Remark:
Python 2.7 is recommended
Before running please install packages *numpy, scipy
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from Implementations.compute_mean import *
from Implementations.compute_var import *


'''===================================================================================================
File content:
solve frontier, means, var, weights
==================================================================================================='''

def implied_equity_risk_premium(W, R, C, rf):
	'''==============================================================================================
	Arguments:
	W 	-- list, market cap weights of the assets
	R 	-- list, past expected returns of assets
	C 	-- list, past covariance of returns of assets
	rf 	-- double, risk-free rate

	Returns:
	res -- double, implied equity risk premium
	=============================================================================================='''
	# Preparation Phrase
	market_mean = compute_mean(W, R)
	market_var = compute_var(W, C)

	# Handling Phrase
	utility = (market_mean-rf)/market_var
	res = utility

	# Checking Phrase
	return res
