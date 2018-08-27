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
from datetime import datetime

'''===================================================================================================
File content:
solve the weights for assets based on vol
==================================================================================================='''

def solve_weights_asset(W_asset, W_env, W_box, context):
	'''==============================================================================================
	Arguments:
	W_asset 	-- list, weights of the assets
	W_box 		-- list, weights of the boxes
	W_env 		-- list, weights of the envs
	context 	-- the context of the model

	Returns:
	res -- dict, {'assets':weights}
	=============================================================================================='''
	# Preparation Phrase
	res={}
	weights={}

	# Handling Phrase
	W_equity = W_env['GR'] * W_box['GR']['Equity'] + W_env['IF'] * W_box['IF']['Equity']
	W_commodity = W_env['GR'] * W_box['GR']['Commodity'] + W_env['IR'] * W_box['IR']['Commodity']
	W_nominal_bond = W_env['GF'] * W_box['GF']['Nominal Bond'] + W_env['IF'] * W_box['IF']['Nominal Bond']
	W_il_bond = W_env['IR'] * W_box['IR']['IL Bond'] + W_env['GF'] * W_box['GF']["IL Bond"]
	W_em_credit = W_env['IR'] * W_box['IR']['EM Credit'] + W_env['GR'] * W_box['GR']["EM Credit"]
	W_corporate_credit = W_env['GR'] * W_box['GR']['Corporate Credit']

	W_assetclass = {
		"Equity": W_equity,
		"Commodity": W_commodity,
		"Nominal Bond": W_nominal_bond,
		"IL Bond": W_il_bond,
		"EM Credit": W_em_credit,
		"Corporate Credit": W_corporate_credit
	}
	logging.info('W_assetclass is {}'.format(W_assetclass))


	for assetclass in context['asset classes pool']:
		for asset in context['assets dict'][assetclass]:
			weights[asset] = W_asset[assetclass][asset] * W_assetclass[assetclass]

	# Checking Phrase
	logging.info('solve_weights_asset finished successfully!')
	logging.info('W_asset is {}'.format(weights));
	res=weights
	return res

