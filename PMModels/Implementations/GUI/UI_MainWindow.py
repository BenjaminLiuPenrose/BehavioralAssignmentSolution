# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Student name: Beier (Benjamin) Liu
Date:

Remark:
Python 2.7 is recommended
Before running please install packages *numpy
Using cmd line py -2.7 -m install [package_name]
'''
import os, time, logging
import copy, math
import functools, itertools
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import Implementations.config as config
CURRENT_TIME = config.CURRENT_TIME
CURRENT_PATH = config.CURRENT_PATH

'''===================================================================================================
File content:
Class UI_MainWindow
==================================================================================================='''

class UI_MainWindow(object):
	'''
	Members:
	mainWindow 	-- QMainWindow object,
	centralWidget 	-- QWidget obeject,
	label 	-- dict of QLabel
	comboBox 	-- dict of QComboBox
	lineEdit 	-- dict of QLineEdit
	textBrowser -- dict of QTextBrowser
	pushButton 	-- dict of QPushButton
	canvas 	-- dict of QCanvas

	Methods:
	newWidget 	-- add a new widget
	newLabel -- add a new label
	newComboBox -- add a new combobox
	newLineEdit -- add a new lineedit
	newTextBrowser	-- add a new text browser
	newPushButton 	-- add a new push button
	newCanvas 	-- add a new canvas with a tool bar and a ax
	show 	-- display the main window
	close 	-- close the main window
	'''
	def __init__(self, init_dict=None):
		if init_dict == None:
			init_dict = {'window title':'MainWindow', 'window width': 3*550, 'window height': 550}
		self._mainWindow = QtWidgets.QMainWindow();
		self._mainWindow.setWindowTitle(init_dict['window title'])
		self._mainWindow.setObjectName("MainWindow");
		self._mainWindow.resize(init_dict['window width'], init_dict['window height']);
		self._mainWindow.setWindowIcon(QtGui.QIcon(CURRENT_PATH+'\\plt\\icon.png'))
		self._centralWidget = QtWidgets.QWidget();
		self._centralWidget.setObjectName("centralWidget");
		self._mainWindow.setCentralWidget(self._centralWidget)
		self._centralLayout = QtWidgets.QGridLayout();

		self._label = {};
		self._comboBox = {};
		self._lineEdit = {};
		self._textBrowser = {};
		self._pushButton = {};
		self._widget = {};
		self._widgetLayout = {};
		self._canvas = {};
		self._toolbar = {};
		self._canvas_ax = {};
		self._textLogger = {};
		self._menuBar = None;
		self._menu = None;
		self._action = None;

		self._translate = QtCore.QCoreApplication.translate;

	def newWidget(self):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._widget)+1;
		new_name = "widget_"+str(number);
		new_name_layout = "widgetLayout_"+str(number)

		# Handling Phrase
		widget = QtWidgets.QWidget(self._mainWindow);
		# label.setGeometry(QtCore.QRect(geo_ul, geo_ur, geo_ll, geo_lr));
		widget.setObjectName(new_name);
		widgetLayout = QtWidgets.QGridLayout();
		# widget.setLayout(widgetLayout);

		# Checking Phrase
		logging.debug("UI_MainWindow: newWidget -- {} is added successfully!".format(new_name));
		self._widget[new_name] = widget;
		self._widgetLayout[new_name_layout] = widgetLayout

	def newLabel(self, text_name='null'):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._label)+1;
		new_name = "label_"+str(number);

		# Handling Phrase
		label = QtWidgets.QLabel();
		# label.setGeometry(QtCore.QRect(geo_ul, geo_ur, geo_ll, geo_lr));
		label.setObjectName(new_name);
		label.setText(self._translate("MainWindow", text_name));

		# Checking Phrase
		logging.debug("UI_MainWindow: newLabel -- {} is added successfully!".format(new_name));
		self._label[new_name]=label;


	def newComboBox(self):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._comboBox)+1;
		new_name = "comboBox_"+str(number);

		# Handling Phrase
		comboBox = QtWidgets.QComboBox();
		# comboBox.setGeometry(QtCore.QRect(geo_ul, geo_ur, geo_ll, geo_lr));
		comboBox.setObjectName(new_name);

		# Checking Phrase
		logging.debug("UI_MainWindow: newComboBox -- {} is added successfully!".format(new_name));
		self._comboBox[new_name] = comboBox;

	def newLineEdit(self):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._lineEdit)+1;
		new_name = "lineEdit_"+str(number);

		# Handling Phrase
		lineEdit = QtWidgets.QLineEdit();
		# lineEdit.setGeometry(QtCore.QRect(geo_ul, geo_ur, geo_ll, geo_lr));
		lineEdit.setObjectName(new_name);

		# Checking Phrase
		logging.debug("UI_MainWindow: newLineEdit -- {} is added successfully!".format(new_name));
		self._lineEdit[new_name] = lineEdit;

	def newTextBrowser(self):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._textBrowser)+1;
		new_name = "textBrowser_"+str(number);

		# Handling Phrase
		textBrowser = QtWidgets.QTextBrowser();
		# textBrowser.setGeometry(QtCore.QRect(geo_ul, geo_ur, geo_ll, geo_lr));
		textBrowser.setObjectName(new_name);

		# Checking Phrase
		logging.debug("UI_MainWindow: newTextBrowser -- {} is added successfully!".format(new_name));
		self._textBrowser[new_name] = textBrowser;

	def newPushButton(self, text_name='null'):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._pushButton)+1;
		new_name = "pushButton_"+str(number);

		# Handling Phrase
		pushButton = QtWidgets.QPushButton();
		# pushButton.setGeometry(QtCore.QRect(geo_ul, geo_ur, geo_ll, geo_lr));
		pushButton.setObjectName(new_name);
		pushButton.setText(self._translate("MainWindow", text_name));

		# Checking Phrase
		logging.debug("UI_MainWindow: newPushButton -- {} is added successfully!".format(new_name));
		self._pushButton[new_name] = pushButton;

	def newCanvas(self):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._canvas)+1;
		new_name = "canvas_"+str(number);
		new_name_ax = "canvas_ax_"+str(number);
		new_name_toolbar = "toolbar_"+str(number);


		# Handling Phrase
		canvas = FigureCanvas(Figure(figsize=(5,3)));
		toolbar = NavigationToolbar(canvas, self._centralWidget)

		# Checking Phrase
		logging.debug("UI_MainWindow: newCanvas -- {} is added successfully!".format(new_name));
		self._canvas[new_name] = canvas;
		# self._canvas_ax[new_name_ax] = canvas.figure.subplots();
		self._canvas_ax[new_name_ax] = canvas.figure.add_subplot(111);
		self._toolbar[new_name_toolbar] = toolbar;

	def newTextLogger(self):
		'''
		Arguments:
		Returns:
		'''
		# Preparation Phrase
		number = len(self._textLogger)+1;
		new_name = "textLogger_"+str(number);

		# Handling Phrase
		textLogger = QTextLogger()
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		textLogger.setFormatter(formatter)
		logging.getLogger().addHandler(textLogger)
		# logging.getLogger().setLevel(logging.DEBUG)
		textLogger._widget.setObjectName(new_name);

		# Checking Phrase
		logging.debug("UI_MainWindow: newTextLogger -- {} is added successfully!".format(new_name));
		self._textLogger[new_name]=textLogger;

	def setupUI_test(self):
		'''
		Arguments:
		Returns:
		'''
		for i in range(3):
			self.newWidget()
			if i == 1:
				self._centralLayout.addWidget(self._widget['widget_'+str(i+1)], 1, i)
			else :
				self._centralLayout.addWidget(self._widget['widget_'+str(i+1)], 1, i, 1, 3)
			# logging.debug(self._centralLayout)
		self._centralWidget.setLayout(self._centralLayout);

		for i in range(2):
			self.newTextBrowser()
			self._widgetLayout['widgetLayout_1'].addWidget(self._textBrowser['textBrowser_'+str(len(self._textBrowser))], i, 1)
		self._widget['widget_1'].setLayout(self._widgetLayout['widgetLayout_1']);

		for i in range(3):
			self.newLabel()
			self.newComboBox()
			self._widgetLayout['widgetLayout_2'].addWidget(self._label['label_'+str(len(self._label))], i, 1)
			self._widgetLayout['widgetLayout_2'].addWidget(self._comboBox['comboBox_'+str(len(self._comboBox))], i, 2)
		for i in range(3):
			self.newLabel()
			self.newLineEdit()
			self._widgetLayout['widgetLayout_2'].addWidget(self._label['label_'+str(len(self._label))], i+3, 1)
			self._widgetLayout['widgetLayout_2'].addWidget(self._lineEdit['lineEdit_'+str(len(self._lineEdit))], i+3, 2)
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
		self._action = QtWidgets.QAction(self._mainWindow)
		self._action.setObjectName("action")
		self._action.setText("退出")
		self._menu.addAction(self._action)
		self._menuBar.addAction(self._menu.menuAction())

		QtCore.QMetaObject.connectSlotsByName(self._mainWindow)
		logging.debug("UI_MainWindow: setup UI successfully")

	def show(self):
		self._mainWindow.show();
		logging.debug("UI_MianWindow: show successfully!");

	def close(self):
	 	self._mainWindow.close();
	 	logging.debug("UI_MainWindow: close successfully!")

class QTextLogger(logging.Handler):
	def __init__(self, parent=None):
		super().__init__()

		self._widget = QtWidgets.QPlainTextEdit(parent)
		self._widget.setReadOnly(True)

	def emit(self, record):
		msg=self.format(record)
		self._widget.appendPlainText(msg)
