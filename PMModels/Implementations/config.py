# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 6/1/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import datetime

'''===================================================================================================
File content:
global variables of the whole program
==================================================================================================='''

CURRENT_PATH = os.getcwd();
CURRENT_TIME = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
FREQ_CONVERSION = {
	"daily": (1, 252),
	"weekly": (5, 50),
	"monthly": (20, 12),
	"quaterly": (60, 4),
	"semiannually": (120, 2),
	"yearly": (252, 1),
	"annually": (252, 1)
	}



