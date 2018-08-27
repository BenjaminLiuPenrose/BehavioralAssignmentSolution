'''
Name: Beier (Benjamin) Liu
Date: 6/30/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging, sys
import copy, math
import functools, itertools
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import csv
from Modules.Bin import *
import Modules.config as config

CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
INSTRUMENTS = config.INSTRUMENTS
'''===================================================================================================
File content:
DataRepo Class
==================================================================================================='''
class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kargs):
		if cls not in cls._instances:
			cls._instances[cls]=super(Singleton, cls).__call__(*args, **kargs)
		return cls._instances[cls]

# metaclass=Singleton

class IntraDay():
	'''==============================================================================================
	Members:
	bins_m1 	-- list of bin objects, bin.length == M1


	Methods:
	=============================================================================================='''
	def __init__(self, ins, start="NA", end="NA"):
		self._instrument = ins;
		self._start = start;
		self._end = end;
		self._bins_m1 = [];
		self.compute_intraday();

	def compute_intraday(self):
		sta = self._start;
		end = self._end;
		ins = self._instrument
		curr = "NA"
		with open('{0}/database/{1}.csv'.format(CURRENT_PATH, ins.replace('.', ''), 'r')) as file:
			reader = csv.reader(file, delimiter=',');
			first_line_bool = True
			bins = []
			for row in reader:
				if first_line_bool == True:
					first_line_bool = False;
					continue;

				try :
					tmp = dt.datetime.strptime(row[0], "%Y-%m-%d %H:%M")
				except :
					tmp = dt.datetime.strptime(row[0], "%Y/%m/%d %H:%M")
					row[0]=row[0].replace('/', '-')
				if curr == "NA":
					curr = tmp;
					continue;

				if tmp.month != curr.month or tmp.day != curr.day:
					curr = tmp;
					# logging.debug("{}".format(bins))
					self.add_bins_m1(bins);
					bins = []
					# logging.info("{}".format(self._bins_m1[0]))
				elif tmp.month == curr.month or tmp.day == curr.day:
					pass
				else:
					pass
				bin = Bin();
				bin.close_time, bin.open_price, bin.close_price= row;
				bins.append(bin)
				# logging.info("bins is {}".format(bins))

		logging.debug("{}".format(self.bins_m1[1]))
		return self




	@property
	def bins_m1(self):
		return self._bins_m1

	@property
	def instrument(self):
		return self._instrument

	@instrument.setter
	def instrument(self, value):
		self._instrument = value

	def add_bins_m1(self, value):
		val = value.copy()
		self._bins_m1.append(val)

	def to_string(self):
		logging.debug('\nThe datarepo is: \nbins_m1: {}'.format(self.bins_m1));
