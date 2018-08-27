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
import scipy.optimize as opt
from Implementations.fitness import *
from Implementations.compute_var import *
from Implementations.compute_mean import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
solve frontier, means, var, weights
==================================================================================================='''

def solve_frontier(R, C):
	'''==============================================================================================
	Arguments:
	R 	-- list, past expected returns of asset
	C 	-- list, past covariance of returns of assets

	Returns:
	res -- dict, {'frontier_mean','frontier_var','frontier_weights'}
	=============================================================================================='''
	# Preparation Phrase
	n = len(R)
	frontier_mean, frontier_var, frontier_weights=[], [], []
	res = {}

	# Handling Phrase
	for r in np.linspace(min(R), max(R), num=20):
		W = np.ones([n])/n
		b_ = tuple((0.,1.) for i in range(n))
		c_=({'type':'eq', 'fun': lambda W: np.sum(W)-1.},
			{'type':'eq', 'fun': lambda W, R=R: compute_mean(W, R)-r})
		optimized = opt.minimize(fitness, W, (R, C, r), method='SLSQP', bounds=b_, constraints=c_)
		if not optimized.success:
			logging.error("solve_frontier : {}".format(optimized.message))
		if r==max(R):
			logging.debug('solve_weights: optimized value is {}, {}, {}'.format(r/optimized.fun, r, optimized.fun))
		frontier_mean.append(r)
		frontier_var.append(optimized.fun) # compute_var(optimized.x, C)
		frontier_weights.append(optimized.x)

	# Checking Phrase
	logging.info('solve_frontier finished!')
	frontier_mean = np.array(frontier_mean)
	frontier_var = np.array(frontier_var)
	frontier_weights = np.array(frontier_weights)
	res['frontier_mean'] = frontier_mean
	res['frontier_var'] = frontier_var
	res['frontier_weights'] = frontier_weights
	return res

