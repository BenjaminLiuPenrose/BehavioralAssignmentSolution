# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/5/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy
Using cmd line py -3.6 -m pip install [package_name]
'''
import logging
import copy
from scipy.stats import norm
from modules.price_BS import *
from modules.vega_BS import *

'''===================================================================================================
File content:
Write comments
==================================================================================================='''
def compute_implied_vol(option):
	"""
	"""
	# Preparation Phrase
	MAX_ITERATIONS = 1000;
	PRECISION = 1.0e-5;
	market_price = option['market price'];
	imag_option = option.copy();

	# Handling Phrase
	sigma = 0.5;
	for i in range(MAX_ITERATIONS):
		imag_option['sigma'] = sigma;

		price = price_BS(imag_option);
		vega = vega_BS(imag_option);

		diff = market_price - price;

		if (abs(diff)<PRECISION):
			break;

		sigma = sigma + diff/vega;

	# Checking Phrase
	return sigma
