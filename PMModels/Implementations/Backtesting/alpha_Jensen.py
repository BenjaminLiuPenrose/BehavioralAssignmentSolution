# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/5/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3,6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from Implementations.compute_mean import *
from Implementations.compute_var import *
### Assume only computing a single value
## params like freq and time window are generally ignored
'''===================================================================================================
File content:
provide optimization target function fitness_sharpe, like cost
==================================================================================================='''

def alpha_Jensen(R, freq='annually'):
	'''==============================================================================================
	Arguments:
	R 	-- list, past expected returns of strategy
	freq 	-- string, the frequency of computation

	Returns:
	res -- double,
	=============================================================================================='''
	# Preparation Phrase
	res = 0.0

	# Handling Phrase

	# Checking Phrase
	return res

