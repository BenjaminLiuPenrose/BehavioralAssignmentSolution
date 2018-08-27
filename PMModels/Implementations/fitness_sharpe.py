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
from Implementations.compute_mean import *
from Implementations.compute_var import *

'''===================================================================================================
File content:
provide optimization target function fitness_sharpe, like cost
==================================================================================================='''

def fitness_sharpe(W, R, C, rf):
	'''==============================================================================================
	Arguments:
	W 	-- list, weights of assets
	R 	-- list, past expected returns of asset
	C 	-- list, past covariance of returns of assets
	rf 	--	double, risk-free return rate

	Returns:
	res -- double, -u, u=(mean-rf)/sqrt(var)
	=============================================================================================='''
	# Preparation Phrase
	mean = compute_mean(W, R)
	var = compute_var(W, C)

	# Handling Phrase
	utility = (mean-rf)/var
	res = -utility

	# Checking Phrase
	return res

