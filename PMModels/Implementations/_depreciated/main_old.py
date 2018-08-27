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
from Implementations.MarkowitzModel.MarkowitzModel import *
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
Write comments
==================================================================================================='''

def main():
	'''==============================================================================================
	Arguments:
	A -- activations from previous layer (or input data): (size of previous layer, number of examples)
	W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)
	b -- bias vector, numpy array of shape (size of the current layer, 1)

	Returns:
	Z -- the input of the activation function, also called pre-activation parameter
	cache -- a python dictionary containing "A", "W" and "b" ; stored for computing the backward pass efficiently
	=============================================================================================='''
	return_ts=[]
	return_ts.append([0.2+8*np.random.random()+6*np.random.random() for x in range(152)])
	return_ts.append([np.random.random()+np.random.random()-0.1 for x in range(152)])
	# logging.debug(return_ts.items())
	risk_adversion=1.0
	master=MarkowitzModel(return_ts, risk_adversion);
	res=master.port_formulation()
	master.efficient_frontier(res['target_rets'], res['target_vols'])

	# Preparation Phrase
	# Handling Phrase
	# Checking Phrase

if __name__=='__main__':
	main()

