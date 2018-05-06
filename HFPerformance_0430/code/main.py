'''===================================================================================================
Benjamin's Python programming template file
You can ignore this file
==================================================================================================='''

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
from Implementations.Model import *
# logging.getLogger().setLevel(logging.INFO)
CURRENT_PATH=os.getcwd();
CURRENT_TIME=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
if not os.path.exists(CURRENT_PATH+'/log/'):
    os.makedirs(CURRENT_PATH+'/log/')
if not os.path.exists(CURRENT_PATH+'/plt/'+CURRENT_TIME):
    os.makedirs(CURRENT_PATH+'/plt/'+CURRENT_TIME)

logger = logging.getLogger();
hdlr = logging.FileHandler(CURRENT_PATH+'/log/{}.log'.format(CURRENT_TIME));
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)



'''===================================================================================================
Main program:
Write comments
==================================================================================================='''

def main():
	# Preparation Phrase
	os.chdir(CURRENT_PATH+'\Mar');
	filename_ls=[i for i in glob.glob('*.{}'.format('csv'))];
	os.chdir(CURRENT_PATH);
	plot_data=[];

	# Handling Phrase
	logging.info('=================================================================================');
	logging.info('Analyzing data for aggregate {}'.format(filename_ls));
	model();
	logging.info('=================================================================================');

	for idx, fi in enumerate(filename_ls):
		logging.info('=================================================================================');
		logging.info('Analyzing data for {}'.format(fi));
		plot_data.append(model(file_rank=idx));
		logging.info('=================================================================================');

	plot_winning_rate=[];
	plot_pnl_ratio=[];
	plot_pnl_avg=[];
	plot_trade_vol=[];
	for dic in plot_data:
		plot_winning_rate.append(dic['winning_rate']);
		plot_pnl_ratio.append(dic['pnl_ratio']);
		plot_pnl_avg.append(dic['pnl_avg']);
		plot_trade_vol.append(dic['trade_vol']);
	plot_date=[filter(str.isdigit, fi) for fi in filename_ls];

	fig=plt.figure(figsize=(6, 12), facecolor='white');
	fig.suptitle('Summary stats')
	gs=gridspec.GridSpec(2,2, height_ratios=[3,3]);
	ax0=fig.add_subplot(gs[0]);
	ax1=fig.add_subplot(gs[1]);
	ax2=fig.add_subplot(gs[2]);
	ax3=fig.add_subplot(gs[3]);

	ax0.set_title('winning rate');
	ax0.plot(plot_date, plot_winning_rate);

	ax1.set_title('pnl ratio');
	ax1.plot(plot_date, plot_pnl_ratio);

	ax2.set_title('pnl avg');
	ax2.plot(plot_date, plot_pnl_avg);

	ax3.set_title('trade vol');
	ax3.bar(plot_date, plot_trade_vol);
	
	# Checking Phrase
	plt.subplots_adjust(hspace=.2);
	fig.autofmt_xdate()
	plt.savefig(CURRENT_PATH+'\plt\{}\Summary_stats.png'.format(CURRENT_TIME))
	plt.show()
	'Finished!'

if __name__=='__main__':
	main()
