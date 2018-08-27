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
'''===================================================================================================
File content:
Bin Class
==================================================================================================='''

class Bin():
	'''==============================================================================================
	Members:
	open_time 	-- datetime object, open time of the bin
	close_time 	-- datetime object, close time of the bin
	open_price 	-- double, open bid of the bin
	high_price 	-- double, highest bid of the bin
	low_price 	-- double, lowest bid of the bin
	close_price 	-- double, close bid of the bin
	volume 	-- double, volume of the bin
	pnl 	-- double, pnl of the bin
	length 	-- deltatime/string, length of the bin


	Methods:
	=============================================================================================='''
	def __init__(self):
		self._open_time = 0;
		self._close_time = 0;

		self._open_price = 0.0;
		self._high_price = 0.0;
		self._low_price = 0.0;
		self._close_price = 0.0;


		self._volume = 0.0;

		self._pnl = 0.0;

		self._length = 0;

	@property
	def open_time(self):
		return self._open_time

	@open_time.setter
	def open_time(self, value):
		if isinstance(value, str):
			value = dt.datetime.strptime(value, "%Y-%m-%d %H:%M")
		self._open_time = value

	@property
	def close_time(self):
		return self._close_time

	@close_time.setter
	def close_time(self, value):
		if isinstance(value, str):
			value = dt.datetime.strptime(value, "%Y-%m-%d %H:%M")
		self._close_time = value


	@property
	def open_price(self):
		return self._open_price

	@open_price.setter
	def open_price(self, value):
		self._open_price = round(float(value), 6)

	@property
	def close_price(self):
		return self._close_price

	@close_price.setter
	def close_price(self, value):
		self._close_price = round(float(value), 6)

	@property
	def high_price(self):
		return self._high_price

	@high_price.setter
	def high_price(self, value):
		self._high_price = round(float(value), 6)

	@property
	def low_price(self):
		return self._low_price

	@low_price.setter
	def low_price(self, value):
		self._low_price = round(float(value), 6)

	@property
	def volume(self):
		return self._volume

	@volume.setter
	def volume(self, value):
		self._volume = round(float(value), 1)

	@property
	def pnl(self):
		return self._pnl

	@pnl.setter
	def pnl(self, value):
		self._pnl = value

	@property
	def length(self):
		return self._length

	@length.setter
	def length(self, value):
		self._length = value


	def to_string(self):
		logging.debug("")











