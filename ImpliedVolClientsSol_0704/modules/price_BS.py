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

from scipy.stats import norm
import numpy as np

'''===================================================================================================
File content:
Write comments
==================================================================================================='''
def price_BS(option):
	"""
	"""
	# Preparation Phrase
	S, K, r, sigma, T = option['S'], option['K'], option['r'], option['sigma'], option['T'];
	opt_flag = option['flag'];
	d1 = (np.log(S/K)+(r+sigma*sigma/2.0)*T)/(sigma*np.sqrt(T));
	d2 = d1 - sigma*np.sqrt(T);

	# Handling Phrase
	if opt_flag[0].lower() == 'c':
		price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2);
	else:
		price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1);


	# Checking Phrase
	return price;
