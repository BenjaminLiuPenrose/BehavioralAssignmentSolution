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
import matplotlib.backends.backend_pdf
import scipy.optimize as opt
import seaborn as sns
import csv

import Modules.config as config
from Modules.Strategy import *
from Modules.IntraDay import *
from Modules.Tools import *

CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
INSTRUMENTS = config.INSTRUMENTS
CONTRACTS = config.CONTRACTS
'''===================================================================================================
File content:
Strategy Class
==================================================================================================='''
@Timer
def XQW_model():
	'''==============================================================================================


	=============================================================================================='''
	# Preparation Phrase
	start = dt.datetime(2010, 1, 1); # depreciated
	end = dt.datetime(2010, 4, 30); # depreciated
	# ins_trail = "000300SH"; # depreciated

	intradays = {};
	# max_process_num = 8;
	process_num = 6;
	bool_test_mode = False;


	deltaS_range_hash = {
		"c": {10: (-0.1, -0.0), 37: (-0.027, -0.0), 52: (-0.0189, -0.0)},
		"p": {10: (0.0, 0.1), 37: (0.0, 0.027), 52: (0.0, 0.0189)},
	}
	flag_to_direction_hash = {
		"c": "Long",
		"p": "Short"
	}
	commission_rate_hash = {
		"000300SH": 2.5/10000,
		"000016SH": 2.5/10000,
		"000905SH": 2.5/10000,
	}


	# Handling Phrase
	for ins in INSTRUMENTS:
		if bool_test_mode and ins != ins_trail:
			continue;
		intraday = IntraDay(ins, start, end); ####
		intradays[ins] = intraday;

	INS_CONTRACTS=[(ins, contract) for ins in INSTRUMENTS for contract in CONTRACTS]

	for ins, contract in INS_CONTRACTS:
		if bool_test_mode and ins != ins_trail:
			continue;
		flag = contract["flag"][0].lower()  # get "c" or "p"
		direction = flag_to_direction_hash[flag]
		commission_rate = commission_rate_hash[ins]
		leverage = contract['leverage']
		fee_rate = contract['fee rate']
		(deltaS_low, deltaS_high) = deltaS_range_hash[flag][leverage]
		deltaS_ls = [round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)]
		strats = {
			"instrument": ins,
			"direction": direction,
			"commission rate": commission_rate,
			"leverage": leverage,
			"fee rate": fee_rate,
			"deltaS": deltaS_low
		};
		logging.info(strats)

		strats_ls = []
		for i in range(process_num):
			if bool_test_mode and i != process_num-1:
				continue
			tmp = strats.copy();
			tmp['deltaS'] = round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4);
			strats_ls.append(tmp)

		res = []
		for i in range(process_num):
			if bool_test_mode and i!= 0:
				break
			strategy = Strategy(intradays, strats);
			res.append( strategy.run_simulation(strats_ls[i]) ); ###


		# strategy = Strategy(intradays, strats)
		# res.append( strategy.run_simulation(strats) );
		# cum_profits= round(np.cumsum(res._profits)[-1]/100, 4);

		# logging.info("strats are {}".format(strats_ls))
		# res = []
		# for i in range(process_num/max_process_num):
			# res = multiProcess(max_process_num, Strategy(intradays, strats).run_simulation, strats_ls)

		Ys_profits = []; Ys_cum_profits = []; trades = [];
		cum_profit_final_ls = []; sharpe_ls = [];
		for i in range(process_num):
			if bool_test_mode and  i != 0:
				break
			Ys_profits.append( res[i]['profits ts'] );
			Ys_cum_profits.append( res[i]['cum profits ts'] );
			cum_profit_final_ls.append( res[i]['cum profit final'] );
			sharpe_ls.append( res[i]['sharpe'] );
			trades.append( res[i]['trades'] )
		Xs_dt = res[0]['datetimes'];
		# logging.info("{}".format(cum_profits))
		# with open("{}/output/{}/{}_{}_{}_pertrade.csv".format(CURRENT_PATH, CURRENT_TIME, ins, flag, leverage), "w", newline='') as file:

		str_path = "{}/output/{}/{}_{}_{}.pdf".format(CURRENT_PATH, CURRENT_TIME, ins, flag, leverage)
		with matplotlib.backends.backend_pdf.PdfPages(str_path) as pdf:
			# cum returns graph
			fig = plt.figure(figsize=(16, 12))
			for i in range(process_num):
				if bool_test_mode and i!= 0:
					break
				# plt.plot(Xs_dt, Ys_profits[i], label=str(strats_ls[i]['deltaS']));
				plt.plot(Xs_dt, Ys_cum_profits[i], label=str(strats_ls[i]['deltaS']));
			plt.legend(loc="upper left", ncol=int(process_num/10)+1)
			plt.title("Cumulative Returns")
			plt.xlabel("Days")
			plt.ylabel("Cumulative Returns")
			pdf.savefig(fig)
			# plt.show()

			# returns graph
			fig = plt.figure(figsize=(16, 12))
			for i in range(process_num):
				if bool_test_mode and i!= 0:
					break
				plt.plot(Xs_dt, Ys_profits[i], label=str(strats_ls[i]['deltaS']));
			plt.legend(loc="upper left", ncol=int(process_num/10)+1)
			plt.title("Daily PnL")
			plt.xlabel("Days")
			plt.ylabel("Daily PnL")
			pdf.savefig(fig)
			# plt.show()

			if not bool_test_mode:
				with open("{}/output/{}/{}_{}_{}_cumProfits.csv".format(CURRENT_PATH, CURRENT_TIME, ins, flag, leverage), "w", newline='') as file:
					writer = csv.writer(file);
					writer.writerow(tuple(round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)))
					for j in range(len(Ys_cum_profits[0])):
						writer.writerow(tuple(Ys_cum_profits[i][j] for i in range(process_num)))

			if not bool_test_mode:
				with open("{}/output/{}/{}_{}_{}_profits.csv".format(CURRENT_PATH, CURRENT_TIME, ins, flag, leverage), "w", newline='') as file:
					writer = csv.writer(file);
					writer.writerow(tuple(round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)))
					for j in range(len(Ys_cum_profits[0])):
						writer.writerow(tuple(Ys_profits[i][j] for i in range(process_num)))

			if not bool_test_mode:
				# training final_profits as cost function
				fig = plt.figure(figsize=(16, 12))
				plt.plot([round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)], cum_profit_final_ls, 'b--')
				plt.title("Training")
				plt.xlabel("deltaS")
				plt.ylabel("Final Profits")
				pdf.savefig(fig)
				# plt.show()

				# training  sharpe as cost function
				fig = plt.figure(figsize=(16, 12))
				plt.plot([round(deltaS_low+i*(deltaS_high-deltaS_low)/(process_num-1), 4) for i in range(process_num)], sharpe_ls, 'r--')
				plt.title("Training")
				plt.xlabel("deltaS")
				plt.ylabel("Sharpe Ratio")
				pdf.savefig(fig)
				# plt.show()
				with open("{}/output/{}/{}_{}_{}_trainingDeltaS.csv".format(CURRENT_PATH, CURRENT_TIME, ins, flag, leverage), "w", newline='') as file:
					writer = csv.writer(file);
					writer.writerow(('deltaS', 'cum profit final', 'sharpe'))
					for i in range(process_num):
						writer.writerow((deltaS_ls[i], cum_profit_final_ls[i], sharpe_ls[i]))

		logging.info("Delta S is {} \ncum profits is {}".format(strats['deltaS'], cum_profit_final_ls));




	# Checking Phrase

