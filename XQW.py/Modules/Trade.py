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
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

'''===================================================================================================
File content:
Trade Class
==================================================================================================='''

class Trade():
	'''==============================================================================================
	Members:
	uuid 	-- string, a unique string like ID of trade
	instrument 	-- string, name of the instrument being trade
	entry_price 	-- double, the entry price of the trade
	exit_price 		-- double, the exit price of the trade
	stop_loss_price 	-- double, the stop loss price of the trade
	profit_target_price 	-- double, the profit target price of the trade
	commission_rate 	-- double, the commission rate of the trade
	commission 		-- double, the commission of the trade
	profit 		-- double, the profit of the trade
	quantity 		-- int, the quantity of the trade
	entry_time 	-- datetime object, the entry time of the trade
	exit_time 	-- datetime object, the exit time of the trade
	direction 	-- string, the direction of the trade

	Methods:
	close 	-- close the trade
	=============================================================================================='''
	def __init__(self):
		self._uuid = "";

		self._instrument = "";

		self._entry_price = 0.0;
		self._exit_price = 0.0;
		self._stop_loss_price = 0.0;
		self._profit_target_price = 0.0;

		self._commission_rate = 0.0;
		self._commission_rate_open = 2.5/10000;
		self._commission = 0.0;

		self._init_cost = 0.0;
		self._profit = 0.0;

		self._quantity = 0
		self._entry_time = [];
		self._exit_time = [];

		self._direction = "";

	@property
	def uuid(self):
		return self._uuid

	@uuid.setter
	def uuid(self, value):
		self._uuid = value

	@property
	def instrument(self):
		return self._instrument

	@instrument.setter
	def instrument(self, value):
		self._instrument = value

	@property
	def entry_price(self):
		return self._entry_price

	@entry_price.setter
	def entry_price(self, value):
		self._entry_price = value

	@property
	def exit_price(self):
		return self._exit_price

	@exit_price.setter
	def exit_price(self, value):
		self._exit_price = value

	@property
	def stop_loss_price(self):
		return self._stop_loss_price

	@stop_loss_price.setter
	def stop_loss_price(self, value):
		self._stop_loss_price = value

	@property
	def profit_target_price(self):
		return self._profit_target_price

	@profit_target_price.setter
	def profit_target_price(self, value):
		self._profit_target_price = value

	@property
	def commission_rate(self):
		return self._commission_rate

	@commission_rate.setter
	def commission_rate(self, value):
		self._commission_rate = value

	@property
	def commission(self):
		return self._commission

	@commission.setter
	def commission(self, value):
		self._commission = value

	@property
	def profit(self):
		return self._profit

	@profit.setter
	def profit(self, value):
		self._profit = round(float(value), 6)

	@property
	def init_cost(self):
		return self._init_cost

	@profit.setter
	def init_cost(self, value):
		self._init_cost = round(float(value), 6)

	@property
	def quantity(self):
		return self._quantity

	@quantity.setter
	def quantity(self, value):
		self._quantity= value

	@property
	def entry_time(self):
		return self._entry_time

	@entry_time.setter
	def entry_time(self, value):
		self._entry_time = value

	@property
	def exit_time(self):
		return self._exit_time

	@exit_time.setter
	def exit_time(self, value):
		self._exit_time = value

	@property
	def direction(self):
		return self._direction

	@direction.setter
	def direction(self, value):
		self._direction = value

	def open(self, order):
		self.uuid = order['uuid']
		self.instrument = order['instrument']
		self.entry_price = order['entry price']
		self.quantity = order['quantity']
		self.entry_time = order['entry time']
		self.direction = order['direction']
		self.stop_loss_price = order.get('stop loss price', 0.0)
		self.profit_target_price = order.get('profit target price', 0.0)
		self.commission_rate = order['commission rate']
		if self.direction == "Long":
			self.init_cost = self.entry_price*self.quantity*(1+self._commission_rate_open);
		else :
			self.init_cost = -self.entry_price*self.quantity*(1-self._commission_rate_open);

	def close(self, order):
		self.exit_price = order['exit price']
		self.exit_time = order['exit time']
		if self.direction == "Long":
			self.profit = self.exit_price*self.quantity*(1-self.commission_rate) - self.entry_price*self.quantity*(1+self._commission_rate_open);
		else :
			self.profit = self.entry_price*self.quantity*(1-self._commission_rate_open) - self.exit_price*self.quantity*(1+self.commission_rate);
		self.direction = "Neutural"

	def to_string(self):
		logging.debug('\nThe Trade:\nuuid: {}\ninstrument: {}\nentry_price: {}\nexit_price: {}\nstop_loss_price: {}\nprofit_target_price: {}\ncommission_rate: {}\ncommission: {}\nprofit: {}\nquantity: {}\nentry_time: {}\nexit_time: {}\ndirection: {}\n'.format(self.uuid, self.instrument, self.entry_price, self.exit_price, self.stop_loss_price, self.profit_target_price, self.commission_rate, self.commission, self.profit, self.quantity, self.entry_time, self.exit_time, self.direction));





