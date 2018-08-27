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
from Implementations.BlackLittermanModel.implied_equity_risk_premium import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
solve frontier, means, var, weights
==================================================================================================='''

def equilibrium_excess_return_view(PI, C, P, Q, tau=0.025):
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


	# Handling Phrase
	omega = np.dot(np.dot(np.dot(tau, P), C), P.T)	# omega=tau*(P*C*P.T)

	sub_a = np.linalg.inv(np.dot(tau, C))					# sub_a=(tau*C).I
	sub_b = np.dot(np.dot(P.T, np.linalg.inv(omega)), P)	# sub_b=P.T*omega.I*P
	sub_c = np.dot(np.linalg.inv(np.dot(tau, C)),PI)			# sub_c=(tau*C).I*PI
	sub_d = np.dot(np.dot(P.T, np.linalg.inv(omega)), Q)		# sub_d=P.T*omega.I*Q
	PI_new = np.dot(np.linalg.inv(sub_a+sub_b), (sub_c+sub_d))	# PI_new=(sub_a+sub_b).I*(sub_c+sub_d)


	# Checking Phrase
	res = PI_new
	return res
