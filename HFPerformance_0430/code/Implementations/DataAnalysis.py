# -*- coding: utf-8 -*- 
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np 
import datetime
import matplotlib.pyplot as plt
from matplotlib import gridspec
logging.getLogger().setLevel(logging.DEBUG)
CURRENT_PATH=os.getcwd();
CURRENT_TIME=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

'''===================================================================================================
File content:
Write comments
==================================================================================================='''
def data_analysis(dat, stock_dict, file_rank, display=True):
	'''==============================================================================================
	Arguments:
	dat -- a pandas dataframe, it contains all the data 
					e.g. 证券代码|证券名称|交易类型|交易时间|成交股数|成交价格|成交编号|交易费用
						69		69		卖出		14:55:44	160		8.72	xxxxxxxx	1.63	
	stock_dict	-- a dict of objects of class Stock

	Returns:
	res -- dict,
				-- {winning_rate, pnl_avg, pnl_ratio, hold_t_avg, ...}
	=============================================================================================='''

	# Preparation Phrase
	res={}
	cnt=0;
	win_lst, hold_t_lst, pnl_lst=[], [], [];
	for ticker, stock in stock_dict.iteritems():
		cnt+=1;
		if cnt%5==0:
			logging.debug('Ticker {}: the win_ls {}; the hold_t_ls {}; the pnl_ls {}'.format(
				ticker, stock.win_ls, stock.hold_t_ls, stock.pnl_ls))
		win_lst.extend(stock.win_ls);
		hold_t_lst.extend(stock.hold_t_ls);
		pnl_lst.extend(stock.pnl_ls);
	logging.debug('win_lst: {}\nhold_t_lst": {}\npnl_lst: {}'.format(win_lst, hold_t_lst, pnl_lst))

	fig=plt.figure(figsize=(6, 12), facecolor='white');
	if file_rank!=None and isinstance(file_rank, int):
		fig.suptitle('Date: {}'.format(dat['trade_date'][0]));
	else:
		fig.suptitle('All dates');
	gs=gridspec.GridSpec(3,1, height_ratios=[3,3,3]);
	ax0=fig.add_subplot(gs[0]);
	ax1=fig.add_subplot(gs[1]);
	ax2=fig.add_subplot(gs[2]);


	# Handling Phrase
	# 胜率
	winning_rate=reduce(lambda x,y: x+y, win_lst)/(1.*len(win_lst));
	logging.info('winning rate: {}'.format(winning_rate));
	logging.debug(len(win_lst));

	# 每笔盈亏
	pnl_avg=reduce(lambda x,y: x+y, pnl_lst)/(1.*len(pnl_lst));
	logging.info('PnL avg: {}'.format(pnl_avg));
	ax0.set_title('PnL');
	ax0.hist(pnl_lst, bins=50, density=True, facecolor='g', alpha=0.75);

	#盈亏比
	(sum_p, sum_l)=sum_pos_neg(pnl_lst);
	pnl_ratio=sum_p/(-1.*sum_l);
	logging.info('pnl ratio: {}'.format(pnl_ratio));

	# 持仓周期
	hold_t_lst=[item.total_seconds() for item in hold_t_lst];
	hold_t_avg=reduce(lambda x,y: x+y, hold_t_lst)/(1.*len(hold_t_lst));
	logging.info('hold_t_avg: {}'.format(hold_t_avg));
	ax1.set_title('Hold t');
	ax1.hist(hold_t_lst, bins=50, facecolor='g', alpha=0.2);

	# 交易量统计
	# print(dat['trade_T'])
	# for d in dat['trade_T']:
	# 	print(d.hour)
	# date=[datetime.datetime(d.month, d.day, min(d.hour,23), d.minute, d.second) for d in dat['trade_T']]
	date=[d for d in dat['trade_T']]
	trade_vol=dat['trade_vol'];
	ax2.set_title('Trade vol');
	ax2.bar(date, dat['trade_vol']);
	trade_vol=reduce(lambda x,y: x+y, dat['trade_vol'])
	# plt.fill_between(dat['trade_T'], 0, dat['trade_vol'], facecolor='blue', alpha=0.5);

	res['winning_rate']=winning_rate;
	res['pnl_ratio']=pnl_ratio;
	res['pnl_avg']=pnl_avg;
	res['trade_vol']=trade_vol;

	# Checking Phrase
	plt.subplots_adjust(hspace=.2);
	fig.autofmt_xdate()
	if display==True:
		plt.show();
	else:
		pass
	logging.debug('data_analysis finished!');
	if file_rank!=None and isinstance(file_rank, int):
		fig.savefig(CURRENT_PATH+'\plt\{}\{}.png'.format(CURRENT_TIME, dat['trade_date'][0]));
	else:
		fig.savefig(CURRENT_PATH+'\plt\{}\\all_dates.png'.format(CURRENT_TIME));
	return res 
	
def sum_pos_neg(ls):
	s_pos, s_neg=0, 0;
	for x in ls:
		if x>0:
			s_pos+=x;
		elif x<0:
			s_neg+=x;
		else:
			pass
	return (s_pos, s_neg)

	