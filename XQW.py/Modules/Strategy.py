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

from Modules.Trade import *
from Modules.Tools import *
'''==================================================================================================-=
File content:
Strategy Class
==================================================================================================='''

class Strategy():
	'''==============================================================================================
	Members:
	params_1
	params_2
	params_3


	Methods:
	run_simulation 		-- run the simulation
	run_realtime		-- run the realtime
	cost_function 		-- cost function
	compute_cost_fucntion 	-- compute the cost function
	trades 			--
	=============================================================================================='''
	def __init__(self, intradays, strats):
		self._direction = strats.get("direction", "Long");
		self._instrument = strats['instrument'];
		self._leverage = strats.get('leverage', 10);
		self._fee_rate = strats.get('fee rate', 0.01);
		self._commission_rate = strats.get("commission rate", 0.0);
		self._intraday = intradays[self._instrument];

		self._params = {};

		# self._principals = np.random.randint(1000000, 10000000, len(self._intraday.bins_m1))
		self._principals = [strats.get('principal', 100)]*len(self._intraday.bins_m1)

	@Timer
	def run_simulation(self, strats={}):  ### need to be improved, this function is too heavy


		self._params['deltaS'] = strats.get('deltaS', -0.0);

		# Preparation Phrase
		res = {}
		intraday = self._intraday;
		instrument = self._instrument;
		principals = self._principals;
		leverage = self._leverage;
		fee_rate = self._fee_rate;
		commission_rate = self._commission_rate;
		direction = self._direction;
		deltaS = self._params['deltaS'];
		datetimes = []
		trades = []
		profits = [];
		cum_profit_final = 0;
		sharpe = 0;

		# Handling Phrase
		days = 0
		for bins_m1 in intraday.bins_m1: # for one day (intraday)
			cnt = 0;
			cum_chg_log = 0.0;
			pnl_contract = 0.0;
			principal = principals[days];
			profit = principal;
			# profit += principal*fee_rate;
			# logging.info("after init: profit is {}".format(profit))

			opn = bins_m1[cnt].close_price;
			datetimes.append( dt.datetime(bins_m1[cnt].close_time.year, bins_m1[cnt].close_time.month, bins_m1[cnt].close_time.day))

			offer_price = opn;
			order = {
				"uuid": bins_m1[cnt].close_time.strftime("%Y%m%d%H%M"),
				"instrument": instrument,
				"entry price": offer_price,
				"entry time": bins_m1[cnt].close_time,
				"quantity": principal*leverage/offer_price,
				"commission rate": commission_rate,
				"direction": direction
			}
			trade = Trade();
			trade.open(order);
			bool_full_pos = True;

			cnt += 1
			for bin in bins_m1[1:]:
				prev_price = bins_m1[cnt-1].close_price;
				cum_chg_log += np.log(bin.close_price/prev_price);

				if direction == "Long":
					if cnt == len(bins_m1)-1:
						pnl_contract = - max(0, (1+cum_chg_log*leverage)*principal)
						# logging.info("pnl contract is {}".format(pnl_contract))
						profit += pnl_contract;
						# logging.info("after pnl: profit is {}".format(profit))


					if bool_full_pos and (cum_chg_log<=deltaS):
						offer_price = np.exp(deltaS)*opn;
						# offer_price = bin.close_price;
						order = {
							"exit price": offer_price,
							"exit time": bin.close_time,
						}
						trade.close(order);
						profit += trade.profit;
						# logging.info("after trade: profit is {}".format(profit))
						trade.to_string();
						trades.append( trade );

						trade = None;
						bool_full_pos = False;
						cnt += 1
						continue;

					if (not bool_full_pos) and (cum_chg_log>deltaS):
						offer_price = np.exp(deltaS)*opn;
						# offer_price = bin.close_price;
						order = {
							"uuid": bin.close_time.strftime("%Y%m%d%H%M"),
							"instrument": instrument,
							"entry price": offer_price,
							"entry time": bin.close_time,
							"quantity": principal*leverage/offer_price,
							"commission rate": commission_rate,
							"direction": direction
						}
						trade = Trade();
						trade.open(order);
						bool_full_pos = True;
						cnt += 1
						continue;

					if (bool_full_pos) and cnt==len(bins_m1)-1:
						offer_price = bin.close_price;
						order = {
							"exit price": offer_price,
							"exit time": bin.close_time,
						}
						trade.close(order);
						profit += trade.profit;
						trade.to_string();
						# logging.info("after clearing: profit is {}".format(profit))
						trades.append( trade );

						trade = None;
						bool_full_pos = False;
						cnt += 1
						continue;
				else :
					if cnt == len(bins_m1)-1:
						pnl_contract = - max(0, (1-cum_chg_log*leverage)*principal)
						# logging.info("pnl contract is {}".format(pnl_contract))
						profit += pnl_contract;
						# logging.info("after pnl: profit is {}".format(profit))


					if bool_full_pos and (cum_chg_log>=deltaS):
						offer_price = np.exp(deltaS)*opn;
						# offer_price = bin.close_price;
						order = {
							"exit price": offer_price,
							"exit time": bin.close_time,
						}
						trade.close(order);
						profit += trade.profit;
						# logging.info("after trade: profit is {}".format(profit))
						trade.to_string();
						trades.append( trade );

						trade = None;
						bool_full_pos = False;
						cnt += 1
						continue;

					if (not bool_full_pos) and (cum_chg_log<deltaS):
						offer_price = np.exp(deltaS)*opn;
						# offer_price = bin.close_price;
						order = {
							"uuid": bin.close_time.strftime("%Y%m%d%H%M"),
							"instrument": instrument,
							"entry price": offer_price,
							"entry time": bin.close_time,
							"quantity": principal*leverage/offer_price,
							"commission rate": commission_rate,
							"direction": direction
						}
						trade = Trade();
						trade.open(order);
						bool_full_pos = True;
						cnt += 1
						continue;

					if (bool_full_pos) and cnt==len(bins_m1)-1:
						offer_price = bin.close_price;
						order = {
							"exit price": offer_price,
							"exit time": bin.close_time,
						}
						trade.close(order);
						profit += trade.profit;
						trade.to_string();
						# logging.info("after clearing: profit is {}".format(profit))
						trades.append( trade );

						trade = None;
						bool_full_pos = False;
						cnt += 1
						continue;
				cnt += 1
			# logging.info("final: profit is {}".format(profit))
			profits.append(profit)
			days += 1
		# logging.info(profits)
		# logging.info(np.cumsum(profits))

		# Checking Phrase
		res['deltaS']=deltaS;
		res['instrument']=instrument;
		res['leverage']=leverage;
		res['trades']=trades;
		res['datetimes']=datetimes;
		res["profits ts"] = np.array(profits);
		res["cum profits ts"] = np.cumsum(res.get("profits ts", [0, 1]));
		res["cum profit final"] = round(res.get("cum profits ts", [0, 1])[-1], 4);
		res["sharpe"]= res.get("profits ts", [0, 1]).mean()/res.get("profits ts", [0, 1]).var();
		return res



	def compute_cost_function(self):
		pass

	def compute_perf_metrics(self):
		pass

	def to_string(self):
		logging.debug('\nThe Strategy is ...')
