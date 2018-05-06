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
	counter=0;

	# Object init
	def __init__(self, ticker):
		self._ticker=ticker;
		self._buy_inventory=[];
		self._buy_t=[];
		self._buy_price=[];
		self._buy_cost=[];

		self._sell_inventory=[];
		self._sell_t=[];
		self._sell_price=[];
		self._sell_cost=[];		
		
		self._pnl_ls=[];
		self._hold_t_ls=[];
		self._win_ls=[];
		self.counter+=1;

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
		self._buy_inventory.append(trade_vol);
		self._buy_t.append(trade_t);
		self._buy_price.append(trade_price);
		self._buy_cost.append(trade_cost);

	def sell(self, trade_vol, trade_t, trade_price, trade_cost):
		self._sell_inventory.append(trade_vol);
		self._sell_t.append(trade_t);
		self._sell_price.append(trade_price);
		self._sell_cost.append(trade_cost);

	def clearing(self):
		net_pos=0;
		while len(self._buy_inventory)>0 and len(self._sell_inventory)>0:
			buy_inven=self._buy_inventory.pop(0);
			sell_inven=self._sell_inventory.pop(0);
			net_pos=buy_inven-sell_inven;
			if net_pos>0:
				delta=sell_inven;

				buy_t=self._buy_t[0];
				buy_price=self._buy_price[0];
				buy_cost=self._buy_cost[0];

				sell_t=self._sell_t.pop(0);
				sell_price=self._sell_price.pop(0);
				sell_cost=self._sell_cost.pop(0);

				# compute win_ls
				if sell_price>buy_price:
					win=True;
				else:
					win=False;
				self._win_ls.append(win);

				# compute pnl_ls
				pnl=(sell_price-buy_price)*delta;
				pnl=pnl-sell_cost-buy_cost*delta/(1.*buy_inven);
				self._pnl_ls.append(pnl);

				# compute hold_t_ls
				hold_t=abs(sell_t-buy_t);
				self._hold_t_ls.append(hold_t);

				self._buy_inventory.insert(0, net_pos);

			elif net_pos<0:
				delta=buy_inven;

				sell_t=self._sell_t[0];
				sell_price=self._sell_price[0];
				sell_cost=self._sell_cost[0];

				buy_t=self._buy_t.pop(0);
				buy_price=self._buy_price.pop(0);
				buy_cost=self._buy_cost.pop(0);

				# compute win_ls
				if sell_price>buy_price:
					win=True;
				else:
					win=False;
				self._win_ls.append(win);

				# compute pnl_ls
				pnl=(sell_price-buy_price)*delta;
				pnl=pnl-sell_cost*delta/(1.*sell_inven)-buy_cost;
				self._pnl_ls.append(pnl);

				# compute hold_t_ls
				'not sure how to compute hold_t in this case'
				hold_t=abs(sell_t-buy_t);
				self._hold_t_ls.append(hold_t);

				self._sell_inventory.insert(0, -net_pos);

			else:                                                           # net_pos==0
				delta=sell_inven;

				sell_t=self._sell_t.pop(0);
				sell_price=self._sell_price.pop(0);
				sell_cost=self._sell_cost.pop(0);

				buy_t=self._buy_t.pop(0);
				buy_price=self._buy_price.pop(0);
				buy_cost=self._buy_cost.pop(0);			

				# compute win_ls
				if sell_price>buy_price:
					win=True;
				else:
					win=False;
				self._win_ls.append(win);

				# compute pnl_ls
				pnl=(sell_price-buy_price)*delta;
				pnl=pnl-sell_cost-buy_cost;
				self._pnl_ls.append(pnl);

				# compute hold_t_ls
				hold_t=abs(sell_t-buy_t);
				self._hold_t_ls.append(hold_t);



	def load_stock(self, stock_data_dict):
		self._buy_inventory=stock_data_dict.get('buy_inventory',[]);
		self._buy_t=stock_data_dict.get('buy_t',[]);
		self._buy_price=stock_data_dict.get('buy_price',[]);
		self._buy_cost=stock_data_dict.get('buy_cost',[]);

		self._sell_inventory=stock_data_dict.get('sell_inventory',[]);
		self._sell_t=stock_data_dict.get('sell_t',[]);
		self._sell_price=stock_data_dict.get('sell_price',[]);
		self._sell_cost=stock_data_dict.get('sell_cost',[]);

		self._pnl_ls=stock_data_dict.get('pnl_ls',[]);
		self._hold_t_ls=stock_data_dict.get('hold_t_ls',[]);
		self._win_ls=stock_data_dict.get('win_ls',[]);








