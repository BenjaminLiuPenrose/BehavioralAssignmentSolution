# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/5/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy
Using cmd line py -3.6 -m pip install [package_name]
'''
import logging
import copy
import numpy as np
import datetime

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

'''===================================================================================================
File content:

==================================================================================================='''
def plot_vol_surface(options):
	'''===================================================================================================


	==================================================================================================='''
	K = [option['K'] for option in options]
	T = [option['T'] for option in options]
	IV = [option['implied vol'] for option in options]
	Ks, Ts = np.meshgrid(K, T)
	IVs = griddata(np.array([K, T]).T, np.array(IV), (Ks, Ts), method='linear')

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(K, T, IV, color='r')
	# surf = ax.plot_surface(Ks, Ts, IVs, color='white', cmap=cm.jet)
	# fig.colorbar(surf)
	ax.set_xlabel('Strike K');
	ax.set_ylabel('Time to maturity T')
	ax.set_zlabel('Implied Vol IV')
	ax.set_title('Volatility Surface')
	fig.tight_layout()
	plt.show()
