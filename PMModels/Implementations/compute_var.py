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
compute expected variance of portfolio
==================================================================================================='''

def compute_var(W, C):
	'''==============================================================================================
	Arguments:
	W -- list, weights of assets
	C -- list, past covariance of returns of assets

	Returns:
	res -- double, expected variance of portfolio
	=============================================================================================='''
	# Preparation Phrase
	dim_W = len(W);
	dim_C1, dim_C2 = C.shape
	if (dim_W != dim_C1 or dim_W!=dim_C2):
		logging.error('compute_var: dimension mismatched!')

	# Handling Phrase
	res = np.dot(np.dot(W, C), W)

	# Checking Phrase
	return res

