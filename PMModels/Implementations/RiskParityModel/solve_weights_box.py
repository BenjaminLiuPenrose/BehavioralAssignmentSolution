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
from Implementations.compute_mean import *

'''===================================================================================================
File content:
solve the weights for box based on vol
==================================================================================================='''

def solve_weights_box(V, W_asset, context):
	'''==============================================================================================
	Arguments:
	V 		-- list, vols of the assets
	W_asset 	-- list, weights of the asset classes
	context 	-- the context of the model

	Returns:
	res -- dict, {'env': {'assetclass': weights}}
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
	V_assetclass = list(V_assetclass.values());

	vol_assetclass = V_assetclass

	# Handling Phrase

	# growth rising
	W_gr = risk_parity_equalized_weights(zip(vol_assetclass, ['Equity', 'Commodity', 'EM Credit', 'Corporate Credit']))
	W_gr_equity = W_gr['Equity']
	W_gr_commodity = W_gr['Commodity']
	W_gr_em_credit = W_gr['EM Credit']
	W_gr_corp_credit = W_gr['Corporate Credit']

	# growth falling
	W_gf = risk_parity_equalized_weights(zip(vol_assetclass, ['Nominal Bond', 'IL Bond']))
	W_gf_nominal_bond = W_gf['Nominal Bond']
	W_gf_il_bond = W_gf['IL Bond']

	# inflation rising
	W_ir = risk_parity_equalized_weights(zip(vol_assetclass, ['IL Bond', 'Commodity', 'EM Credit']))
	W_ir_il_bond = W_ir['IL Bond']
	W_ir_commodity = W_ir['Commodity']
	W_ir_em_credit = W_ir['EM Credit']

	# inflation falling
	W_if = risk_parity_equalized_weights(zip(vol_assetclass, ['Equity', 'Nominal Bond']))
	W_if_equity = W_if['Equity']
	W_if_nominal_bond = W_if['Nominal Bond']

	weights = {
		"GR": {"Equity": W_gr_equity, "Commodity": W_gr_commodity, "EM Credit": W_gr_em_credit, "Corporate Credit": W_gr_corp_credit},
		"GF": {"Nominal Bond": W_gf_nominal_bond, "IL Bond": W_gf_il_bond},
		"IR": {"IL Bond": W_ir_il_bond, "Commodity": W_ir_commodity, "EM Credit": W_ir_em_credit},
		"IF": {"Nominal Bond": W_if_nominal_bond, "Equity": W_if_equity}
	}

	# Checking Phrase
	logging.info('solve_weights_box finished successfully!')
	logging.info('W_box is {}'.format(weights))
	res = weights
	return res


