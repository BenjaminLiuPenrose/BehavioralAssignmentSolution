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
from Implementations.RiskParityModel.risk_parity_equalized_weights import *

'''===================================================================================================
File content:
solve the weights for asset class based on vol
==================================================================================================='''

def solve_weights_assetinclass(V, context):
	'''==============================================================================================
	Arguments:
	V 	-- list, vols of the assets
	context 	-- the context of the model

	Returns:
	res -- dict, {'assetclass': {'asset': weights}}
	=============================================================================================='''
	# Preparation Phrase
	res = {}
	weights = {}
	V_asset = dict(zip(context['assets pool'], V))

	# Handling Phrase


	for assetclass in context['asset classes pool']:
		V_curr = []
		for asset in context['assets dict'][assetclass]:
			V_curr.append(V_asset[asset])
		weights[assetclass] = risk_parity_equalized_weights(zip(V_curr, context['assets dict'][assetclass]));

	# Checking Phrase
	logging.info('solve_weights_assetinclass finished successfully!')
	logging.info('W_assetinclass is {}'.format(weights))
	res = weights
	return res


