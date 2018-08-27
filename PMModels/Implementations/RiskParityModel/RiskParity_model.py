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
import scipy.optimize as opt
from datetime import datetime
import matplotlib.pyplot as plt
from Implementations.initialize_parameters import *
from Implementations.get_daily_returns import *
from Implementations.assets_mean_var import *
from Implementations.RiskParityModel.solve_weights_assetinclass import *
from Implementations.RiskParityModel.solve_weights_box import *
from Implementations.RiskParityModel.solve_weights_env import *
from Implementations.RiskParityModel.solve_weights_asset import *

'''===================================================================================================
File content:
RiskParity Model, includes
initialize_params
get_daily_returns
assets_mean_var
solve_weights_assetinclass
solve_weights_box
solve_weights_env
solve_weights_asset
==================================================================================================='''

def RiskParity_model(context):
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	# Preparation Phrase
	res = {}
	# context = initialize_parameters(init_dict)
	logging.debug('RiskParity_model: context is {}'.format(context))

	sta_date, end_date, assets_pool = context['start date'], context['end date'], context['assets pool']
	# daily_returns = get_daily_returns(sta_date, end_date, assets_pool);
	# daily_returns = daily_returns['percentage returns'];
	daily_returns = context['daily returns']

	ax = context['canvas ax']
	# ax = ax['canvas_ax_3']


	# Handling Phrase
	mean_var = assets_mean_var(daily_returns)
	R, C, V = mean_var['mean'], mean_var['cov'], mean_var['var']
	logging.debug('RiskParity_model: mean_var is {}'.format(mean_var))

	W_asset = solve_weights_assetinclass(V, context)
	W_box = solve_weights_box(V, W_asset, context)
	W_env = solve_weights_env(V, W_asset, W_box, context)
	weights = solve_weights_asset(W_asset, W_env , W_box, context)
	logging.info('RiskParity_model: weights is {}'.format(weights))
	logging.info('RiskParity_model: sum of weights is {}'.format(sum(list(weights.values()))))

	# ax.clear();

	# ax.figure.canvas.draw();

	# Checking Phrase
	logging.info('RiskParity_model finished successfully')
	res['weights'] = weights
	res['date'] = datetime.now().strftime("%m/%d/%y")
	return res

