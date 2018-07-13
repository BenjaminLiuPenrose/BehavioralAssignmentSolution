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

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import csv

from modules.get_daily_options import *
from modules.compute_implied_vol import *
from modules.plot_vol_surface import *
'''===================================================================================================
File content:

==================================================================================================='''
def IV_model():
	'''===================================================================================================


	==================================================================================================='''
	# Preparation Phrase
	options = get_daily_options();

	# Handling Phrase

	for option in options:
		iv = compute_implied_vol(option);
		option['implied vol'] = iv;

	# plotting vol surface
	plot_vol_surface(options)

	# export result to csv
	# with open('demo.csv', 'wb') as file:
	# 	writer = csv.writer(file, delimiter=',')
	# 	# line0 = ['']
	# 	for option in options:
	# 		writer.writerow(option)

	# Checking Phrase
	for x, option in enumerate(options):
		logging.info('The option {} is {}'.format(x, option));

	return options

