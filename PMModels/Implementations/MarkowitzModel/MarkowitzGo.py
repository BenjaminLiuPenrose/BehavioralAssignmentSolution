# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 5/29/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, scipy, matplotlib, PyQt5
Using cmd line py -3.6 -m pip install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import Implementations.config as config
from Implementations.GUI.UI_MainWindow import *
from Implementations.MarkowitzModel.Markowitz_model import *
CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH


'''===================================================================================================
File content:
the wrapped class of the markowitz model, the GUI, the model that computing the weights and graphs, etc
==================================================================================================='''

class MarkowitzGo(UI_MainWindow):
	'''==============================================================================================
	Members:
	weights 	-- weights, the ultimate weights


	Methods:
	basic_init() 	-- final setup of the buttons, etc, of the GUI
	setupUI() 		-- add items/widgets to the GUI
	runner()		-- run markowitz model and return weights and graphs
	=============================================================================================='''
	def __init__(self):
		init_dict = {'window title':'MarkowitzGo', 'window width': 3*550, 'window height': 550}
		super(MarkowitzGo, self).__init__(init_dict)
		self._weights = [];

		self._comboBox_ls = {}
		self._comboBox_ls['comboBox_1'] = ['5/30/2008', '6/9/2008'];
		self._comboBox_ls['comboBox_2'] = ['5/18/2018', '5/30/2018'];

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
			# logging.debug(self._centralLayout)
		self._centralWidget.setLayout(self._centralLayout);

		for i in range(1):
			self.newTextLogger()
			self._widgetLayout['widgetLayout_1'].addWidget(self._textLogger['textLogger_'+str(len(self._textLogger))]._widget, i, 1)
		self._widget['widget_1'].setLayout(self._widgetLayout['widgetLayout_1']);

		text_dict = {
		'label_1': "起始时间",
		'label_2': "结束时间",
		'label_3': "标的资产",
		'label_4': "null",
		'label_5': "null",
		'label_6': "null",
		'pushButton_1': "开始",
		'pushButton_2': "退出"}
		for i in range(7):
			if i<3:
				self.newLabel(text_dict['label_'+str(len(self._label)+1)])
				self.newComboBox()
				self._widgetLayout['widgetLayout_2'].addWidget(self._label['label_'+str(len(self._label))], i, 1)
				self._widgetLayout['widgetLayout_2'].addWidget(self._comboBox['comboBox_'+str(len(self._comboBox))], i, 2)
			elif i<6:
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

		for i in range(1):
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

	def runner(self):
		init_dict = {
		'canvas ax': self._canvas_ax,
		'start date': datetime.strptime(self._comboBox['comboBox_1'].currentText(), '%m/%d/%Y'),
		'end date': datetime.strptime(self._comboBox['comboBox_2'].currentText(), '%m/%d/%Y'),
		'assets dict': {
			"Equity": ['VTI', 'MSFT', 'AAPL', 'MMM', 'BIDU'],
			"Commodity": [],
			"Corporate Credit": [],
			'EM Credit': [],
			"Nominal Bond": [],
			"IL Bond": []
		},
		'risk adversion': 0.8}
		# init_dict={'canvas ax': self._canvas_ax, 'start date':'6/9/2008' , 'end date':'5/18/2018' , 'assets pool': self._comboBox['comboBox_2'].currentText(), 'risk adversion': 0.8}
		res = Markowitz_model(init_dict);
		self._weights = res['weights']


