# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date:

Remark:
Python 2.7 is recommended
Before running please install packages *numpy, pandas, scipy, datetime, matplotlib, pyqt5
Using cmd line py -2.7 -m pip install [package_name]
these words are used interchangeablle:
(variance, vol)
(assets, assets pool, tickers)
'''
import os, time, logging, sys
import copy, math
import functools, itertools
import numpy
import datetime
import pandas
import matplotlib.pyplot
import scipy.optimize
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from Implementations.MarkowitzModel.Markowitz_model import *
from Implementations.MarkowitzModel.MarkowitzGo import *
from Implementations.BlackLittermanModel.BlackLittermanGo import *
from Implementations.RiskParityModel.RiskParityGo import *
from Implementations.CURLGo.CURLGo import *
import Implementations.config as config
CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH

if not os.path.exists(CURRENT_PATH+'/log/'):
	os.makedirs(CURRENT_PATH+'/log/')
if not os.path.exists(CURRENT_PATH+'/plt/'+CURRENT_TIME):
	os.makedirs(CURRENT_PATH+'/plt/'+CURRENT_TIME)
if not os.path.exists(CURRENT_PATH+'/weight/'+CURRENT_TIME):
	os.makedirs(CURRENT_PATH+'/weight/'+CURRENT_TIME)
# if not os.path.exists(CURRENT_PATH+'/backtest/'+CURRENT_TIME):
# 	os.makedirs(CURRENT_PATH+'/backtest/'+CURRENT_TIME)

logger = logging.getLogger();
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr = logging.FileHandler(CURRENT_PATH+'/log/{}.log'.format(CURRENT_TIME));
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

console=logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
logger.setLevel(logging.INFO)

'''===================================================================================================
File content:
main program
==================================================================================================='''

def main():
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	# daily_returns=[]
	# dummy=np.array([.08*np.random.random()+.06*np.random.random() for x in range(152)])
	# daily_returns.append(dummy)
	# daily_returns.append(0.6*dummy)
	# daily_returns.append(dummy+1)
	# daily_returns.append(np.array([.08*np.random.random() for x in range(152)]))
	# daily_returns.append(np.array([.16*np.random.random() for x in range(152)]))
	# daily_returns=np.array(daily_returns)

	# Markowitz_model(daily_returns);
	# Markowitz_model()
	try:
		input('press any key to start')
		app = QtWidgets.QApplication(sys.argv);
		# master = MarkowitzGo();
		# master = BlackLittermanGo();
		# master = RiskParityGo();
		master = CURLGo();
		master.show();
		sys.exit(app.exec_());
		input('press any key to exit')
	except :
		logging.error('Unexpected error: {}'.format(sys.exc_info()))
		input('press any key to exit')




	# Preparation Phrase
	# Handling Phrase
	# Checking Phrase

if __name__=='__main__':
	main()

