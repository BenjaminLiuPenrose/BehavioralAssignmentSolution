# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date:

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import scipy.optimize as opt
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Calculate Markowitz portfolio weights
==================================================================================================='''

def MarkowitzPort(return_ts, risk_adversion):
	'''==============================================================================================
	Arguments:
	return_ts -- time series data of returns of all assets, list of list or dict of list
	risk_adversion -- a measure of risk adversion, double

	Returns:
	weights -- weights of the portfolio, list or dict
	=============================================================================================='''
	# Preparation Phrase
	n=len(return_ts);
	bnds=tuple((0,1) for x in range(n))
	target_rets=np.linspace(0.0, 0.25, 50)
	target_vols=[]
	target_weights=[];
	res={}

	# Handling Phrase
	for target_ret in target_rets:
		cons=({'type':'eq', 'fun': lambda x: port_return(x)-target_ret},
			{'type': 'eq', 'fun': lambda x: np.sum(x)-1})
		re=opt.minimize(port_vol, n*[1./n,], method='SLSQP', bounds=bnds, constraints=cons)
		target_vols.append(re['fun'])
		target_weights.append(re['x'])
	target_vols=np.array(target_vols)
	target_weights=np.array(target_weights)

	# Checking Phrase
	res['target_rets']=target_rets
	res['target_vols']=target_vols
	res['target_weights']=target_weights
	return res


def port_return(weights):
	'''=============================================================================================
	Arguments:
	weights	-- list, weights for different assets in one portfolio

	Returns:
	port_ret--double, expected portfolio return
	============================================================================================='''
	# Preparation Phrase
	weights=np.array(weights)
	return_ts=np.array(return_ts)

	# Handling Phrase
	port_ret=np.sum(np.dot(return_ts.mean(), weights))

	# Checking Phrase
	return port_ret

def port_vol(weights):
	'''
	Arguments:
	weights	-- list, weights for different assets in one portfolio

	Returns:
	port_vol--double, expected portfolio volatility
	'''
	# Preparation Phrase
	weights=np.array(weights)
	return_ts=np.array(return_ts)

	# Handling Phrase
	port_vol=np.sqrt(np.dot(weights.T, np.dot(return_ts.cov(), weights)))

	# Checking Phrase
	return port_vol
