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

'''===================================================================================================
File content:
compute expected return of portfolio
==================================================================================================='''

def compute_mean(W, R):
	'''==============================================================================================
	Arguments:
	W -- list, weights of assets
	R -- list, past expected returns of assets

	Returns:
	res -- double, expected return of portfolio
	=============================================================================================='''
	# Preparation Phrase
	dim_R = len(R)
	dim_W = len(W)
	if dim_R != dim_W:
		logging.error('compute_mean: dimension mismatched!')

	# Handling Phrase
	res = np.dot(R, W)

	# Checking Phrase
	return res

