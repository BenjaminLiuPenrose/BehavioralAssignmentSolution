# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Name: Beier (Benjamin) Liu
Date: 7/5/2018

Remark:
Python 3.6 is recommended
Before running please install packages *numpy, pandas, scipy, datetime, matplotlib, pyqt5
Using cmd line py -3.6 -m pip install [package_name]
'''
import logging
import datetime
import copy
from scipy.stats import norm
import numpy as np
from modules.compute_implied_vol import *
from modules.IV_model import *

logging.getLogger().setLevel(logging.DEBUG)

'''===================================================================================================
File content:
main program
==================================================================================================='''

def main():
	'''==============================================================================================
	Arguments:

	Returns:

	=============================================================================================='''
	IV_model();

	# input('Hello sir, welcome! please press any key to proceed...\n');
	# flag = input('The type of option is? [C for call and P for put]\n');
	# while True:
	# 	try :
	# 		market_price = input('The market price of option is? [please enter a number]\n');
	# 		market_price = float(market_price);
	# 		break;
	# 	except Exception as e:
	# 		logging.error('Error message: '+str(e));
	# 		logging.error('Invalid input. Please enter a number and do not enter space or nothing.');
	# while True:
	# 	try :
	# 		S = input('The price of the underlying is? [please enter a number]\n');
	# 		S = float(S);
	# 		break;
	# 	except Exception as e:
	# 		logging.error('Error message: '+str(e));
	# 		logging.error('Invalid input. Please enter a number and do not enter space or nothing.');

	# while True:
	# 	try :
	# 		K = input('The strike of the option is? [please enter a number]\n');
	# 		K = float(K);
	# 		break;
	# 	except Exception as e:
	# 		logging.error('Error message: '+str(e));
	# 		logging.error('Invalid input. Please enter a number and do not enter space or nothing.');
	# while True:
	# 	try :
	# 		T = input('The time to maturity (in years) is? [please enter a number ]\n');
	# 		T = float(T);
	# 		break;
	# 	except Exception as e:
	# 		logging.error('Error message: '+str(e));
	# 		logging.error('Invalid input. Please enter a number and do not enter space or nothing.');
	# while True:
	# 	try :
	# 		r = input('The risk-free rate is? [please enter a number]\n');
	# 		r = float(r);
	# 		break;
	# 	except Exception as e:
	# 		logging.error('Error message: '+str(e));
	# 		logging.error('Invalid input. Please enter a number and do not enter space or nothing.');

	# # T = (datetime.date(2018, 10, 18)-datetime.date(2018, 4, 18)).days / (datetime.date(2018, 12,31)-datetime.date(2018, 1, 1)).days;
	# option ={
	# 	'S': S,
	# 	'K': K,
	# 	'T': T,
	# 	'r': r,
	# 	'market price': market_price,
	# 	'flag': flag
	# };

	# vol = compute_implied_vol(option)
	# logging.info("\n=================Implied Vol Demo=======================\n OPTION INFO:\n Option flag: {flag},\n Market price: {market_price},\n Underlying asset price: {S},\n Strike price: {K},\n Time to maturity(in years): {T},\n Risk free rate: {r}\n\n COMPUTED RESULTS:\n Implied vol is {iv}\n=========================================================".format(flag=flag, market_price=market_price, S=S, K=K, T=T, r=r, iv=vol))
	# input('Hello sir! hope to serve you next time, please press anykey to exit...\n')

# def compute_implied_vol(option):
# 	"""
# 	"""
# 	# Preparation Phrase
# 	MAX_ITERATIONS = 1000;
# 	PRECISION = 1.0e-5;
# 	market_price = option['market price'];
# 	imag_option = option.copy();

# 	# Handling Phrase
# 	sigma = 0.5;
# 	for i in range(MAX_ITERATIONS):
# 		imag_option['sigma'] = sigma;

# 		price = price_BS(imag_option);
# 		vega = vega_BS(imag_option);

# 		diff = market_price - price;

# 		if (abs(diff)<PRECISION):
# 			break;

# 		sigma = sigma + diff/vega;

# 	# Checking Phrase
# 	return sigma

# def price_BS(option):
# 	"""
# 	"""
# 	# Preparation Phrase
# 	S, K, r, sigma, T = option['S'], option['K'], option['r'], option['sigma'], option['T'];
# 	opt_flag = option['flag'];
# 	d1 = (np.log(S/K)+(r+sigma*sigma/2.0)*T)/(sigma*np.sqrt(T));
# 	d2 = d1 - sigma*np.sqrt(T);

# 	# Handling Phrase
# 	if opt_flag[0].lower() == 'c':
# 		price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2);
# 	else:
# 		price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1);


# 	# Checking Phrase
# 	return price

# def vega_BS(option):
# 	"""
# 	"""
# 	# Preparation Phrase
# 	S, K, r, sigma, T = option['S'], option['K'], option['r'], option['sigma'], option['T'];
# 	opt_flag = option['flag'];
# 	d1 = (np.log(S/K)+(r+sigma*sigma/2.0)*T)/(sigma*np.sqrt(T));

# 	# Handling Phrase
# 	vega = S*np.sqrt(T)*norm.pdf(d1)

# 	# Checking Phrase
# 	return vega;





if __name__=='__main__':
	main()

