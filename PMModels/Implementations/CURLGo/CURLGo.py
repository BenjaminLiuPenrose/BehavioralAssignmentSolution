# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/1/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib, PyQt5
Using cmd line py -3.6 -m pip install [package_name]
'''
### Change one centralized clear[with duck typing] and delete sharperatio colorbar
### Change date dict
### Split into training/testing/cv phrase, add more methods in class
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from datetime import timedelta
import Implementations.config as config
from Implementations.GUI.UI_MainWindow import *
from Implementations.MarkowitzModel.Markowitz_model import *
from Implementations.BlackLittermanModel.BlackLitterman_model import *
from Implementations.RiskParityModel.RiskParity_model import *
from Implementations.Backtesting.Backtesting import *
CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH
FREQ_CONVERSION = config.FREQ_CONVERSION

'''===================================================================================================
File content:
the wrapped class of the markowitz model, black litterman model, risk parity model, the GUI, the model that computing the weights and graphs, etc
==================================================================================================='''

class CURLGo(UI_MainWindow):
	'''==============================================================================================
	Members:
	weights 	-- weights, the ultimate weights


	Methods:
	basic_init() 	-- final setup of the buttons, etc, of the GUI
	setupUI() 		-- add items/widgets to the GUI
	runner()		-- run markowitz model and return weights and graphs
	=============================================================================================='''
	_DATE_LIST = ['4/1/2018', '1/1/2008', '6/1/2008','1/1/2009', '6/1/2009','1/1/2010', '6/1/2010','1/1/2011', '6/1/2011','1/1/2012', '6/1/2012','1/1/2013', '6/1/2013','1/1/2014', '6/1/2014','1/1/2015', '6/1/2015','1/1/2016', '6/1/2016','1/1/2017', '6/1/2017','1/1/2018', '6/1/2018'];
	_DATE_LIST.append((datetime.now()-timedelta(days=1)).strftime('%m/%d/%Y'));
	_FREQ = ["annually", "semiannually", "quaterly", "monthly", "weekly", "daily"]

	def __init__(self):
		init_dict = {'window title':'CURLGo', 'window width': 3*550, 'window height': 550}
		super(CURLGo, self).__init__(init_dict)
		self._weights = {};

		self._comboBox_ls = {}
		self._comboBox_ls['comboBox_1'] = self._DATE_LIST[:-1];
		self._comboBox_ls['comboBox_2'] = reversed(self._DATE_LIST[:-1]);
		self._comboBox_ls['comboBox_3'] = reversed(self._DATE_LIST[-3:]);
		self._comboBox_ls['comboBox_4'] = self._FREQ;

		self._init_dict = {}
		self._context = {};

		self.setupUI();
		self.basic_init();

	def setupUI(self):
		'''
		Arguments:
		Returns:
		'''
		for i in range(3):
			self.newWidget()
			if i == 0:
				self._centralLayout.addWidget(self._widget['widget_'+str(i+1)], 1, 1, 6, 6)
			elif i == 1:
				self._centralLayout.addWidget(self._widget['widget_'+str(i+1)], 1, 7, 6, 2)
			else :
				self._centralLayout.addWidget(self._widget['widget_'+str(i+1)], 1, 10, 6, 6)
		self._centralWidget.setLayout(self._centralLayout);

		for i in range(1):
			self.newTextLogger()
			self._widgetLayout['widgetLayout_1'].addWidget(self._textLogger['textLogger_'+str(len(self._textLogger))]._widget, i, 1)
		for i in range(1):
			self.newCanvas()
			self._widgetLayout['widgetLayout_1'].addWidget(self._toolbar['toolbar_'+str(len(self._toolbar))],2, 1 )
			self._widgetLayout['widgetLayout_1'].addWidget(self._canvas['canvas_'+str(len(self._canvas))], 2+1, 1)
		self._widget['widget_1'].setLayout(self._widgetLayout['widgetLayout_1']);


		text_dict = {
		'label_1': "训练起始日期",
		'label_2': "训练结束日期(回测开始日期)",
		'label_3': "回测结束日期",
		'label_4': "调仓周期",
		'label_5': "标的资产Equity",
		'label_6': "标的资产Commodity",
		'label_7': "标的资产Nominal Bond",
		'label_8': "标的资产IL Bond",
		'label_9': "标的资产Corporate Credit",
		'label_10': "标的资产EM Credit",
		'pushButton_1': "开始",
		'pushButton_2': "退出"}
		for i in range(11):
			if i<4:
				self.newLabel(text_dict['label_'+str(len(self._label)+1)])
				self.newComboBox()
				self._widgetLayout['widgetLayout_2'].addWidget(self._label['label_'+str(len(self._label))], i, 1)
				self._widgetLayout['widgetLayout_2'].addWidget(self._comboBox['comboBox_'+str(len(self._comboBox))], i, 2)
			elif i<9:
				self.newLabel(text_dict['label_'+str(len(self._label)+1)])
				self.newLineEdit()
				self._widgetLayout['widgetLayout_2'].addWidget(self._label['label_'+str(len(self._label))], i, 1)
				self._widgetLayout['widgetLayout_2'].addWidget(self._lineEdit['lineEdit_'+str(len(self._lineEdit))], i, 2)
			else :
				self.newPushButton(text_dict['pushButton_'+str(len(self._pushButton)+1)])
				self._widgetLayout['widgetLayout_2'].addWidget(self._pushButton['pushButton_'+str(len(self._pushButton))], i, 1)
				self.newPushButton(text_dict['pushButton_'+str(len(self._pushButton)+1)])
				self._widgetLayout['widgetLayout_2'].addWidget(self._pushButton['pushButton_'+str(len(self._pushButton))], i, 2)
		self._widget['widget_2'].setLayout(self._widgetLayout['widgetLayout_2']);

		for i in range(2):
			self.newCanvas()
			self._widgetLayout['widgetLayout_3'].addWidget(self._toolbar['toolbar_'+str(len(self._toolbar))],2*i, 1 )
			self._widgetLayout['widgetLayout_3'].addWidget(self._canvas['canvas_'+str(len(self._canvas))], 2*i+1, 1)
		self._widget['widget_3'].setLayout(self._widgetLayout['widgetLayout_3']);

		self._menuBar = QtWidgets.QMenuBar(self._mainWindow)
		self._menuBar.setGeometry(QtCore.QRect(0,0,857,28))
		self._menuBar.setObjectName("menuBar")
		self._menu = QtWidgets.QMenu(self._menuBar)
		self._menu.setObjectName("menu")
		self._menu.setTitle("菜单")

		self._mainWindow.setMenuBar(self._menuBar)
		self._action=QtWidgets.QAction(self._mainWindow)
		self._action.setObjectName("action")
		self._action.setText("退出")
		self._menu.addAction(self._action)
		self._menuBar.addAction(self._menu.menuAction())

		QtCore.QMetaObject.connectSlotsByName(self._mainWindow)
		logging.debug("UI_MainWindow line225: setup UI successfully")

	def basic_init(self):
		self._pushButton['pushButton_1'].clicked.connect(self.runner)
		self._pushButton['pushButton_2'].clicked.connect(self.close)
		self._action.triggered.connect(self.close)
		for s in self._comboBox_ls['comboBox_1']:
			self._comboBox['comboBox_1'].addItem(s)
		for s in self._comboBox_ls['comboBox_2']:
			self._comboBox['comboBox_2'].addItem(s)
		for s in self._comboBox_ls['comboBox_3']:
			self._comboBox['comboBox_3'].addItem(s)
		for s in self._comboBox_ls['comboBox_4']:
			self._comboBox['comboBox_4'].addItem(s)

	def runner(self):
		self.training();
		logging.info('training session finished successfully!');
		self.testing();
		logging.info('testing session finished successfully!');

	def training(self):
		# Preparation Phrase
		res = {}
		self._init_dict = {
		'canvas ax': self._canvas_ax,
		'start date': datetime.strptime(self._comboBox['comboBox_1'].currentText(), '%m/%d/%Y'),
		'end date': datetime.strptime(self._comboBox['comboBox_2'].currentText(), '%m/%d/%Y'),
		'end date backtest': datetime.strptime(self._comboBox['comboBox_3'].currentText(), '%m/%d/%Y'),
		'rebalance frequency': FREQ_CONVERSION[self._comboBox['comboBox_4'].currentText()],
		'risk adversion': 0.8}
		# init_dict={'canvas ax': self._canvas_ax, 'start date':'6/9/2008' , 'end date':'5/18/2018' , 'assets pool': self._comboBox['comboBox_2'].currentText(), 'risk adversion': 0.8}
		self._context = initialize_parameters(self._init_dict);                         ###not a good solution
		context = self._context
		for axs in context['canvas ax']:
			try :
				context['canvas ax'][axs].clear();
			except Exception as e:
				logging.error('Illegal method Error message: {}'.format(e))
				try :
					logging.info('WARNING {}'.format(ontext['canvas ax'][axs].images))
					im = context['canvas ax'][axs].images[-1]
					im.colorbar.remove();
				except Exception as e:
					logging.error('Illegal method Error message: {}'.format(e))

		# Handling Phrase
		res = Markowitz_model(context);
		self._weights['Markowitz'] = res['weights'];
		res = BlackLitterman_model(context);
		self._weights['Black Litterman'] = res['weights'];
		res = RiskParity_model(context);
		self._weights['Risk Parity'] = res['weights'];

		self.weights_chart();

		# Checking Phrase
		logging.info("weights are respectively {}".format(self._weights));

	def cross_validation(self):
		logging.debug("cross_validation is not available")

	def testing(self):
		# Preparation Phrase
		res = {}
		context = self._context;
		rebalance_freq = context['rebalance frequency'];
		test_set_window = context['test set window'];

		# Handling Phrase
		assets_pool = self._context['assets pool']
		# int(test_set_window/rebalance_freq)
		backtesting(self._weights, self._context)
		# for adj in range(1):
		# 	if adj==0:
		# 		backtesting(self._weights, self._context);
		# 		continue;
		# 	start_date = self._context['start date'] + timedelta(days = rebalance_freq)
		# 	end_date = self._context['end date'] + timedelta(days = rebalance_freq)
		# 	self._context['daily returns'] = get_daily_returns(start_date, end_date, assets_pool)['percentage returns'];
		# 	context = self._context;
		# 	res = Markowitz_model(context);
		# 	self._weights['Markowitz'] = res['weights'];
		# 	res = BlackLitterman_model(context);
		# 	self._weights['Black Litterman'] = res['weights'];
		# 	res = RiskParity_model(context);
		# 	self._weights['Risk Parity'] = res['weights'];
		# 	backtesting(self._weights, self._context);

		# Checking Phrase

	def weights_chart(self):
		# Preparation Phrase
		context = self._context
		ax = context['canvas ax']
		ax = ax['canvas_ax_1']

		weights_markowitz, weights_blacklitterman, weights_riskparity = list(self._weights['Markowitz'].values()), list(self._weights['Black Litterman'].values()), list(self._weights['Risk Parity'].values())
		cumweights_markowitz, cumweights_blacklitterman, cumweights_riskparity = np.cumsum(weights_markowitz), np.cumsum(weights_blacklitterman), np.cumsum(weights_riskparity)
		logging.debug('WARNING: {}, {}, {}'.format(weights_markowitz, weights_blacklitterman, weights_riskparity))
		assets_pool = context['assets pool']
		xtick_ls = ('Markowitz', 'Black Litterman', 'Risk Parity')

		# Handling Phrase
		ax.bar(xtick_ls, (weights_markowitz[0], weights_blacklitterman[0], weights_riskparity[0]))
		for x in range(1, len(assets_pool)):
			ax.bar(xtick_ls, (weights_markowitz[x], weights_blacklitterman[x], weights_riskparity[x]), bottom=(cumweights_markowitz[x-1], cumweights_blacklitterman[x-1], cumweights_riskparity[x-1]))
			logging.debug('WARNING: {}, {}, {}'.format(weights_markowitz[x], weights_blacklitterman[x], weights_riskparity[x]))
		ax.set_ylabel('Weights');
		ax.set_xlabel('Portfolio Model');
		ax.legend(assets_pool, loc='upper right');
		ax.figure.canvas.draw();

		# Checking Phrase


