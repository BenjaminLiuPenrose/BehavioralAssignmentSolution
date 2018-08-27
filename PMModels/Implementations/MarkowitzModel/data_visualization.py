# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date:

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, matplotlib
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import gridspec
import Implementations.config as config
CURRENT_TIME=config.CURRENT_TIME
CURRENT_PATH=config.CURRENT_PATH
logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
plot the data
==================================================================================================='''
context={'main_title': 'All dates',
		'height_ratios':[3,3,3]}
def data_visualization(context, display=False):
	'''==============================================================================================
	Arguments:
	context 	--

	Returns:
	fig 	--
	=============================================================================================='''

	# Preparation Phrase
	h_ratios=context['height_ratios'];
	main_title=context['main_title'];
	n=len(h_ratio);
	ax=[];
	fig=plt.figure(figsize=(2*n, 2*2*n), facecolor='white');
	fig.suptitle(main_title);
	gs=gridspec.GridSpec(n, 1, height_ratios=h_ratios);
	for i in range(n):
		ax.append(fig.add_subplot(gs[i]))

	# Handling Phrase
	ax[0].set_title('PnL');
	ax[0].hist(pnl_lst, bins=50, density=True, facecolor='g', alpha=0.75);

	ax[1].set_title('Hold t');
	ax[1].hist(hold_t_lst, bins=50, facecolor='g', alpha=0.2);

	ax[2].set_title('Trade vol');
	ax[2].bar(date, dat['trade_vol']);

	# Checking Phrase
	plt.subplots_adjust(hspace=.2);
	fig.autofmt_xdate()

	if display==True:
		plt.show();

	logging.info('data_analysis finished!');
	fig.savefig(CURRENT_PATH+'\\plt\\{}\\{}.png'.format(CURRENT_TIME, main_title));
	return fig


