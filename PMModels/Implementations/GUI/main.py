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
import os, time, logging, sys
import copy, math
import functools, itertools
import numpy as np
from PyQt5 import QtWidgets
from Implementations.UI_MainWindow import *
logging.getLogger().setLevel(logging.INFO)


'''===================================================================================================
Main program:
Create demo for gui

Implementations:
Write comments
==================================================================================================='''

def main():
	app = QtWidgets.QApplication(sys.argv);
	master = UI_MainWindow();
	master.setupUI();
	master.show();
	sys.exit(app.exec_());




if __name__=='__main__':
	main()
