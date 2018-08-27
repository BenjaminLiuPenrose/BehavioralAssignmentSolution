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
from Implementations.solve_weights import *
from Implementations.MarkowitzModel.solve_frontier import *
from Implementations.MarkowitzModel.efficient_frontier import *
from Implementations.MarkowitzModel.tangent_to_frontier import *


'''===================================================================================================
File content:
Markowitz Model, includes
initialize_params
daily_returns
solve_frontiers
solve_weights
efficient_frontier
==================================================================================================='''
def Markowitz_model(context):
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	# Preparation Phrase
	res = {};
	# context = initialize_parameters(init_dict);
	rf = context['rf']
	risk_adversion = context['risk adversion']
	logging.debug('Markowitz_model: context is {}'.format(context))


	sta_date, end_date, assets_pool = context['start date'], context['end date'], context['assets pool']
	# daily_returns = get_daily_returns(sta_date, end_date, assets_pool);
	# daily_returns = daily_returns['percentage returns'];
	daily_returns = context['daily returns']

	ax = context['canvas ax']
	ax = ax['canvas_ax_2']


	# Handling Phrase
	mean_var = assets_mean_var(daily_returns);
	R, C = mean_var['mean'], mean_var['cov'];					#some problem to be solved
	logging.info('Markowitz_model: mean_var is {}'.format(mean_var));

	ef = solve_frontier(R, C)
	weights_frontier, rets, vols=ef['frontier_weights'], ef['frontier_mean'], ef['frontier_var']
	logging.debug('Markowitz_model: frontier_weights are {}'.format(weights_frontier))

	# ax.clear();							# some problem to be solved
	efficient_frontier(vols, rets, rf, ax)
	tangent = solve_weights(R, C, rf)
	weights_tangent = tangent['weights']
	mean_tangent = compute_mean(weights_tangent, R);
	vol_tangent = compute_var(weights_tangent, C);
	mean_end = (1/risk_adversion-1)*mean_tangent+(2-1/risk_adversion)*rf;
	vol_end = (1/risk_adversion-1)*vol_tangent
	tangent_to_frontier(xs = [0, vol_tangent, vol_end], ys = [rf, mean_tangent, mean_end], ax = ax)
	ax.figure.canvas.draw();
	logging.info('Markowitz_model: tangent_weights is {}'.format(weights_tangent))

	weights = weights_tangent
	weights = dict(zip(assets_pool, weights))
	logging.info('Markowitz_model: weights is {}'.format(weights))
	logging.info('Markowitz_model: sum of weights is {}'.format(sum(list(weights.values()))))


	# Checking Phrase
	logging.info('Markowitz_model finished successfully')
	res['weights'] = weights;
	res['date'] = datetime.now().strftime("%m/%d/%y")
	return res

