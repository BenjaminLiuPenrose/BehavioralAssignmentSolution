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
from Implementations.compute_var import *
from Implementations.RiskParityModel.risk_parity_equalized_weights import *

'''===================================================================================================
File content:
solve the weights for envIRonment based on vol
==================================================================================================='''

def solve_weights_env(V, W_asset, W_box, context):
	'''==============================================================================================
	Arguments:
	V 		-- list, vols of the assets
	W_asset 	-- list, weights of the asset classes
	W_box 		-- list, weights of the boxes
	context 	-- the context of the model

	Returns:
	res -- dict, {'envs': weights}
	=============================================================================================='''
	# Preparation Phrase
	res = {}
	weights = {}
	V_asset = zip(context['assets pool'], V)
	V_assetclass = {'Equity': 0, 'Commodity': 0, 'Nominal Bond': 0, 'IL Bond':0, 'Corporate Credit': 0, 'EM Credit': 0}
	for fst, snd in V_asset:
		if fst in context['assets dict']['Equity'] :
			V_assetclass['Equity'] = V_assetclass['Equity'] + W_asset['Equity'][fst]*snd;
		elif fst in context['assets dict']['Commodity']:
			V_assetclass['Commodity'] = V_assetclass['Commodity'] + W_asset['Commodity'][fst]*snd;
		elif fst in context['assets dict']['Nominal Bond']:
			V_assetclass['Nominal Bond'] = V_assetclass['Nominal Bond'] + W_asset['Nominal Bond'][fst]*snd;
		elif fst in context['assets dict']['IL Bond']:
			V_assetclass['IL Bond'] = V_assetclass['IL Bond'] + W_asset['IL Bond'][fst]*snd;
		elif fst in context['assets dict']['Corporate Credit']:
			V_assetclass['Corporate Credit'] = V_assetclass['Corporate Credit'] + W_asset['Corporate Credit'][fst]*snd;
		else :
			V_assetclass['EM Credit'] = V_assetclass['EM Credit'] + W_asset['EM Credit'][fst]*snd;
	V_assetclass = V_assetclass

	vol_assetclass = V_assetclass

	# Handling Phrase
	vol_gr = W_box['GR']['Equity'] * vol_assetclass['Equity'] \
			+ W_box['GR']['Commodity'] * vol_assetclass['Commodity'] \
			+ W_box['GR']['EM Credit'] * vol_assetclass['EM Credit'] \
			+ W_box['GR']['Corporate Credit'] * vol_assetclass['Corporate Credit']
	vol_gf = W_box['GF']['Nominal Bond'] * vol_assetclass['Nominal Bond'] \
			+ W_box['GF']["IL Bond"] * vol_assetclass["IL Bond"]
	vol_ir = W_box['IR']["IL Bond"] * vol_assetclass["IL Bond"] \
			+ W_box['IR']['Commodity'] * vol_assetclass['Commodity'] \
			+ W_box['IR']['EM Credit'] * vol_assetclass['EM Credit']
	vol_if = W_box['IF']['Equity'] * vol_assetclass['Equity'] \
			+ W_box['IF']['Nominal Bond'] * vol_assetclass['Nominal Bond']

	W_env = risk_parity_equalized_weights([(vol_gr, 'GR'), (vol_gf, 'GF'), (vol_ir, 'IR'), (vol_if, 'IF')])

	weights = {
		"GR": W_env['GR'],
		"GF": W_env['GF'],
		"IR": W_env['IR'],
		"IF": W_env['IF']
	}


	# Checking Phrase
	logging.info('solve_weights_env finished successfully!')
	logging.info('W_env is {}'.format(W_env))
	res=weights
	return res

