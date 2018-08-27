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
import matplotlib.pyplot as plt
from Implementations.compute_mean import *
from Implementations.compute_var import *
import Implementations.config as config
CURRENT_TIME=config.CURRENT_TIME
CURRENT_PATH=config.CURRENT_PATH

'''===================================================================================================
File content:
plot efficient frontier
==================================================================================================='''

def efficient_frontier(vols, rets, rf, ax=None):
	'''
	Arguments:
	vols	--vol of portfolio at the effcient frontier curve
	rets 	--return of portfolio at the efficient frontier curve

	Returns:
	'''
	# Preparation Phrase
	fig = plt.figure(figsize=(5, 3))
	if ax == None:
		ax = plt.subplot(111)

	# Handling Phrase
	scatter = ax.scatter(vols, rets, c=(rets-rf)/vols, marker='x')
	ax.grid = True
	ax.set_xlabel('expected vol')
	ax.set_ylabel('expected return')
	# fig.colorbar(scatter, ax=ax, label='Sharpe ratio')

	# Checking Phrase
	logging.info('efficient_frontier finished!')
	# fig.savefig(CURRENT_PATH+'\\plt\\{}\\{}.png'.format(CURRENT_TIME, 'efficient_frontier'));

