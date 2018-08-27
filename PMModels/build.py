# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 6.8/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy
Using cmd line py -3.6 -m pip install [package_name]
'''
from distutils.core import setup
import py2exe

'''===================================================================================================
File content:
build python exe
==================================================================================================='''

setup(console = ['main.py'],
	zipfile = None,
	options = {
	'py2exe': {
		"bundle_files": 1,
		"dll_excludes": ["MSVCP90.dll", "w9xpopen.exe"]
	}
	})
