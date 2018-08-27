# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 6/13/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3,6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np

'''===================================================================================================
File content:
equalize weights based on vol
==================================================================================================='''

def risk_parity_equalized_weights(V_pool_tuple_ls):
	'''==============================================================================================
	Arguments:
	V_pool_tuple 	-- tuple of (vol, pool)

	Returns:
	res -- dict, {'pool': weights}
	=============================================================================================='''
	# Preparation Phrase
	res = {}
	V_pool_tuple_ls=list(V_pool_tuple_ls)
	n=len(V_pool_tuple_ls)
	if n==0:
		return res

	# Handling Phrase
	(vol_last, pool_last) = V_pool_tuple_ls[n-1]
	vol_last_over_vol_other = [vol_last/vol_curr for (vol_curr, _) in V_pool_tuple_ls]
	weight_n = 1.0 / sum(vol_last_over_vol_other)
	weights = dict([(pool_curr, (vol_last/vol_curr)*weight_n) for (vol_curr, pool_curr) in V_pool_tuple_ls])

	# weights=map()

	# Checking Phrase
	res=weights
	return res


