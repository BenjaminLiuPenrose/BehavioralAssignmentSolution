# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 5/29/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3,6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import scipy.optimize as opt
from Implementations.fitness import *
from Implementations.fitness_sharpe import *
from Implementations.fitness_bible import *

'''===================================================================================================
File content:
solve the optimal weights
==================================================================================================='''

def solve_weights(R, C, rf):
	'''==============================================================================================
	Arguments:
	R 	-- list, past expected returns of asset
	C 	-- list, past covariance of returns of assets
	rf 	--	double, risk-free return rate

	Returns:
	res -- dict, {'weights'}
	=============================================================================================='''
	# Preparation Phrase
	n = len(R)
	W = np.ones([n])/n
	b_ = tuple((0.,1.) for i in range(n))
	c_ = ({'type':'eq', 'fun':lambda W: np.sum(W)-1.})
	res = {}

	# Handling Phrase
	optimized = opt.minimize(fitness_sharpe, W, (R, C, rf), method='SLSQP', bounds=b_, constraints=c_)
	logging.debug('solve_weights: optimized value is {}'.format(optimized.fun))
	if not optimized.success:
		logging.error("solve_weights: {}".format(optimized.message))


	# Checking Phrase
	logging.info('solve_weights finished!')
	res['weights'] = np.array(optimized.x)
	return res

