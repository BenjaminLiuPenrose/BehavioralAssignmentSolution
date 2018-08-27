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
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Calculate Markov Regime Switching portfolio weights
==================================================================================================='''

def MarkovRegimeSwitchingPort(return_ts):
	'''==============================================================================================
	Arguments:
	return_ts -- time series data of returns of all assets, list of list or dict of list

	Returns:
	weights -- weights of the portfolio, list or dict
	=============================================================================================='''

	print('\n====================================Exercise xyz=====================================\n');
	print('Running my myFunction function ... \n');
	myFunction();
	raw_input('Program pause. Press enter to continue.\n');
	# Preparation Phrase
	# Handling Phrase
	# Checking Phrase
