# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
Before running please install packages *numpy, *pandas
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, glob, time, logging
import copy, math
import functools, itertools
import numpy as np 
import pandas as pd 
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File Content:
Class Stock
==================================================================================================='''

class Stock(object):
	# Class init
	_counter=0;

	# Object init
	def __init__(self, ticker):
		self._ticker=ticker;
		self._inventory=[];
		self._buy_t=[];
		self._buy_price=[];
		self._buy_cost=[];
		self._short_inventory=[];
		
		self._pnl_ls=[];
		self._hold_t_ls=[];
		self._win_ls=[];
		self._counter+=1;

	# Getter and setter
	@property
	def win_ls(self):
		return self._win_ls

	@property
	def hold_t_ls(self):
		return self._hold_t_ls

	@property
	def pnl_ls(self):
		return self._pnl_ls

	# @get.setter
	# def set(self, i):
	# 	pass

	# # Static method
	# @staticmethod
	# def myFunc():
	# 	pass

	# # Class method
	# @classmethod
	# def myFunc(cls):
	# 	pass

	# Object-level method
	def buy(self, trade_vol, trade_t, trade_price, trade_cost):
		self._inventory.append(trade_vol);
		self._buy_t.append(trade_t);
		self._buy_price.append(trade_price);
		self._buy_cost.append(trade_cost);

	def sell(self, trade_vol, trade_t, trade_price, trade_cost):
		while trade_vol>0:
			###################################################################
			'Not sure how to handle this case, this is a temp fix'
			if self._inventory==[]:
				#self._short_inventory.append(trade_vol);
				break
				# self.buy(trade_vol, trade_t, trade_price, trade_cost); # in case init inventory exists but not known
			###################################################################

			inven=self._inventory.pop(0);
			if trade_vol<inven:
				buy_t=self._buy_t[0];
				buy_price=self._buy_price[0];
				buy_cost=self._buy_cost[0];

				# compute win_ls
				if trade_price>buy_price:
					win=True;
				else:
					win=False;
				self._win_ls.append(win);

				# compute pnl_ls
				pnl=(trade_price-buy_price)*trade_vol;
				pnl=pnl-trade_cost-buy_cost*trade_vol/(1.*inven);
				self._pnl_ls.append(pnl);

				# compute hold_t_ls
				hold_t=trade_t-buy_t;
				self._hold_t_ls.append(hold_t);

				self._inventory.insert(0, inven-trade_vol);
				trade_vol=0;

			else:                                                       # trade_vol>=inven:
				buy_t=self._buy_t.pop(0);
				buy_price=self._buy_price.pop(0);
				buy_cost=self._buy_cost.pop(0);

				# compute win_ls
				if trade_price>buy_price:
					win=True;
				else:
					win=False;
				self._win_ls.append(win);

				# compute pnl_ls
				pnl=(trade_price-buy_price)*trade_vol;
				pnl=pnl-trade_cost-buy_cost;
				self._pnl_ls.append(pnl);

				# compute hold_t_ls
				hold_t=trade_t-buy_t;
				self._hold_t_ls.append(hold_t);

				trade_vol-=inven;

	def load_stock(self, stock_data_dict):
		inventory=stock_data_dict.get('inventory',[]);
		buy_t=stock_data_dict.get('buy_t',[]);
		buy_price=stock_data_dict.get('buy_price',[]);
		buy_cost=stock_data_dict.get('buy_cost',[]);

		pnl_ls=stock_data_dict.get('pnl_ls',[]);
		hold_t_ls=stock_data_dict.get('hold_t_ls',[]);
		win_ls=stock_data_dict.get('win_ls',[]);

		self._inventory=inventory;
		self._buy_t=buy_t;
		self._buy_price=buy_price;
		self._buy_cost=buy_cost;
		
		self._pnl_ls=pnl_ls;
		self._hold_t_ls=hold_t_ls;
		self._win_ls=win_ls;








