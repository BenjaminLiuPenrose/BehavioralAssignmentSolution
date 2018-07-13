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
import numpy as np
import datetime

'''===================================================================================================
File content:

==================================================================================================='''
def get_daily_options():
	'''===================================================================================================


	==================================================================================================='''
	options = [];
	option = {};

	starttime = [datetime.datetime(2018, 1, 1) for x in range(100)];
	endtime = [datetime.datetime(2018, 12, 30)  for x in range(100)];
	K = np.random.rand(50)*9.0+100;
	spottime = [datetime.datetime(2018, np.random.randint(low=1, high=13), 15) for x in range(100)];
	market_price = np.random.rand(50)*2.0+5.0;
	S = np.random.rand(50)*10.0+80.0;
	T = [(endtime[x]-spottime[x]).days/252 for x in range(100)]
	# T = np.random.randint(low=1, high=13, size=50)/12;
	r = np.ones([50])*0.05;

	for x in range(50):
		option = {}
		option['flag'] = 'c'
		option['start time'] = starttime[x]
		option['end time'] = endtime[x]
		option['K'] = K[x]
		option['spot time'] = spottime[x]
		option['market price'] = market_price[x]
		option['S'] = S[x]
		option['T'] = T[x]
		option['r'] = r[x]
		options.append(option)

	return options
