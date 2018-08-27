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
import scipy.optimize as opt
from datetime import datetime
import matplotlib.pyplot as plt
from Implementations.initialize_parameters import *
from Implementations.get_daily_returns import *
from Implementations.assets_mean_var import *
from Implementations.BlackLittermanModel.equilibrium_excess_return import *
from Implementations.BlackLittermanModel.equilibrium_excess_return_view import *
from Implementations.solve_weights import *

'''===================================================================================================
File content:
Black Litterman Model
==================================================================================================='''

def BlackLitterman_model(context):
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	# Preparation Phrase
	res={};
	# context = initialize_parameters(init_dict);
	rf = context['rf']
	logging.debug('BlackLitterman_model: context is {}'.format(context))

	sta_date, end_date, assets_pool = context['start date'], context['end date'], context['assets pool']
	# daily_returns = get_daily_returns(sta_date, end_date, assets_pool);
	# daily_returns = daily_returns['percentage returns'];
	daily_returns = context['daily returns']

	ax = context['canvas ax']
	ax = ax['canvas_ax_1']


	# Handling Phrase
	mean_var = assets_mean_var(daily_returns);
	R, C = mean_var['mean'], mean_var['cov']
	logging.debug('BlackLitterman_model: mean_var is {}'.format(mean_var))

	weights_market = context['weights cap']
	PI = equilibrium_excess_return(weights_market, R, C, rf)
	logging.debug('BlackLitterman_model: PI is {}'.format(PI))

	implied = solve_weights(PI+rf, C, rf)
	weights_implied = implied['weights']
	mean = compute_mean(weights_implied, R)
	var = compute_var(weights_implied, C)
	P = np.zeros([2, len(assets_pool)])
	P[0][0] = 1; P[1][0] = 1; P[0][1] = -1; P[1][2] = -1;
	Q = np.array([0.03,0.02])
	PI_new = equilibrium_excess_return_view(PI, C, P, Q, tau=0.025)
	logging.debug('BlackLitterman_model: PI_new is {}'.format(PI_new))

	optima = solve_weights(PI_new+rf, C, rf)
	weights = optima['weights']
	weights = dict(zip(assets_pool, weights))
	logging.info('BlackLitterman_model: weights: weights is {}'.format(weights))
	logging.info('BlackLitterman_model: sum of weights is {}'.format(sum(list(weights.values()))))

	# ax.clear();

	# ax.figure.canvas.draw();

	# Checking Phrase
	logging.info('BlackLitterman_model finished successfully!')
	res['weights'] = weights;
	res['date'] = datetime.now().strftime("%m/%d/%y")
	return res

