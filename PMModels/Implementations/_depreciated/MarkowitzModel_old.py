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
import os
import time
import logging
import copy
import math
import functools
import itertools
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Class MarkowitzModel
==================================================================================================='''


class MarkowitzModel(object):
	def __init__(self, return_ts, risk_adversion=1.0):
		self._return_ts=return_ts
		self._risk_adversion=risk_adversion

		self._n=len(return_ts)
		self._weights=self._n*[1./self._n,]

	@property
	def n(self):
		return self._n

	@property
	def weights(self):
		return self._weights

	@property
	def risk_adversion(self):
		return self._risk_adversion

	@risk_adversion.setter
	def risk_adversion(self, iRisk_adversion):
		self._risk_adversion=iRisk_adversion

	# @return_ts.setter
	# def return_ts(self, iReturn_ts):
	# 	self._return_ts=iReturn_ts
	# 	self._n=len(return_ts)
	# 	self._weights=self._n*[1./self._n,]

	def port_market(self):
		'''==============================================================================================
		Arguments:
		return_ts -- time series data of returns of all assets, list of list or dict of list
		risk_adversion -- a measure of risk adversion, double

		Returns:
		weights -- weights of the portfolio, list or dict
		=============================================================================================='''
		# Preparation Phrase
		n=self._n
		bnds=tuple((0,1) for x in range(n))
		target_rets=np.linspace(0.0, 0.25, 50)
		target_vols=[]
		target_weights=[];
		res={}

		# Handling Phrase
		for target_ret in target_rets:
			cons=({'type':'eq', 'fun': lambda x: self.port_return(x)-target_ret},
				{'type': 'eq', 'fun': lambda x: np.sum(x)-1})
			re=opt.minimize(self.port_vol, n*[1./n,], method='SLSQP', bounds=bnds, constraints=cons)
			target_vols.append(re['fun'])
			target_weights.append(re['x'])
		target_vols=np.array(target_vols)
		target_weights=np.array(target_weights)

		# Checking Phrase
		res['target_rets']=target_rets
		res['target_vols']=target_vols
		res['target_weights']=target_weights
		return res


	def port_return(self, weights):
		'''=============================================================================================
		Arguments:
		weights -- list, weights for different assets in one portfolio

		Returns:
		port_ret--double, expected portfolio return
		============================================================================================='''
		# Preparation Phrase
		weights=np.array(weights)
		return_ts=self._return_ts
		return_ts=np.array(return_ts)

		# Handling Phrase
		port_ret=np.sum(np.dot(np.mean(return_ts), weights))

		# Checking Phrase
		return port_ret

	def port_vol(self, weights):
		'''
		Arguments:
		weights -- list, weights for different assets in one portfolio

		Returns:
		port_vol--double, expected portfolio volatility
		'''
		# Preparation Phrase
		weights=np.array(weights)
		return_ts=self._return_ts
		return_ts=np.array(return_ts)

		# Handling Phrase
		port_vol=np.sqrt(np.dot(weights.T, np.dot(np.cov(return_ts), weights)))

		# Checking Phrase
		return port_vol

	def efficient_frontier(self, rets, vols):
		'''
		Arguments:

		Returns:
		'''
		# Preparation Phrase
		plt.figure(figsize=(8,4))

		# Handling Phrase
		plt.scatter(vols, rets, c=rets/vols, marker='x')
		plt.grid=True
		plt.xlabel('expected vol')
		plt.ylabel('expected return')
		plt.colorbar(label='Sharpe ratio')

		# Checking Phrase
		plt.show()

	def port_formulation(self):
		'''==============================================================================================
		Arguments:
		return_ts -- time series data of returns of all assets, list of list or dict of list
		risk_adversion -- a measure of risk adversion, double

		Returns:
		weights -- weights of the portfolio, list or dict
		=============================================================================================='''
		# Preparation Phrase

		# Handling Phrase
		# Checking Phrase



