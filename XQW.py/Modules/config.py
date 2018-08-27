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
CURRENT_TIME = datetime.datetime.now().strftime('%Y%m%d_%H%M%S');
INSTRUMENTS = ["000300SH", "000016SH", "000905SH"];
# INSTRUMENTS = ["000300SH"];
CONTRACTS = [{"leverage": 10, "fee rate": 0.01, "flag": "call"}, {"leverage": 10, "fee rate": 0.01, "flag": "put"}, {"leverage": 37, "fee rate": 0.05, "flag": "call"}, {"leverage": 37, "fee rate": 0.05, "flag": "put"}, {"leverage": 52, "fee rate": 0.09, "flag": "call"}, {"leverage": 52, "fee rate": 0.09, "flag": "put"}]
# CONTRACTS = [{"leverage": 10, "fee rate": 0.01, "flag": "put"}]
