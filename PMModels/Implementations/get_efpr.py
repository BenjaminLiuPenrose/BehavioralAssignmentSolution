from selenium.webdriver.common.proxy import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
driver = webdriver.Firefox(executable_path="C:\\Python36\\selenium\\geckodriver")
#driver.implicitly_wait(30)
driver.get("http://www.epfr.com/")
elem = driver.find_element_by_xpath('//*[@id="loginBtn"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="M_CPH1_txtUsername"]')
elem.send_keys('TCUoHK.CUHK5')
elem = driver.find_element_by_xpath('//*[@id="M_CPH1_txtPassword"]')
elem.send_keys('epfrdata')
elem = driver.find_element_by_xpath('//*[@id="M_CPH1_cmdLogin"]')
elem.click()

elem = driver.find_element_by_xpath('//*[@id="M_A_cblAllEquity_0"]')
elem.click()
#mouseover

#output text
elem = driver.find_element_by_xpath('//*[@id="lnkOutput"]')
hover = ActionChains(driver).move_to_element(elem)
hover.perform()
elem = driver.find_element_by_xpath('//*[@id="M_B_rblOutput"]/tbody/tr[7]/td/label')
elem.click()

#level
elem = driver.find_element_by_xpath('//*[@id="lnkLevel"]')
hover = ActionChains(driver).move_to_element(elem)
hover.perform()
elem = driver.find_element_by_xpath('//*[@id="M_B_rblLevel"]/tbody/tr[4]/td/label')
elem.click()
time.sleep(50)
driver.maximize_window()


#date
year = 2016
month = 1
day = '01'
day_end = 31
month_dic = [0,31,28,31,30,31,30,31,31,30,31,30,31]
while(year<2017):
	'''============================================================================================='''
	try:
		sys.stderr.write(str(year)+' '+str(month)+' '+'gogogo~\n')
		elem = driver.find_element_by_xpath('//*[@id="divDateTop"]')
		time.sleep(1)
		hover = ActionChains(driver).move_to_element(elem)
		time.sleep(1)
		hover.perform()
	except:
		sys.stderr.write('first error')
		time.sleep(1)
		elem = driver.find_element_by_xpath('//*[@id="divDateTop"]')
		time.sleep(1)
		hover = ActionChains(driver).move_to_element(elem)
		time.sleep(1)
		hover.perform()
	time.sleep(1)
	if (month<10):
		'''========================================================================================='''
		try:
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateFrom"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
			elem.send_keys('0'+str(month)+'/'+'01/'+str(year))
		except:
			time.sleep(1)
			sys.stderr.write('2 error')
			elem = driver.find_element_by_xpath('//*[@id="divDateTop"]')
			time.sleep(1)
			hover = ActionChains(driver).move_to_element(elem)
			time.sleep(1)
			hover.perform()
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateFrom"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
			elem.send_keys('0'+str(month)+'/'+'01/'+str(year))
		'''========================================================================================'''
		try:
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateTo"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
		except:
			elem = driver.find_element_by_xpath('//*[@id="divDateTop"]')
			time.sleep(1)
			hover = ActionChains(driver).move_to_element(elem)
			time.sleep(1)
			hover.perform()
			time.sleep(1)
			sys.stderr.write('3 error')
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateTo"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
		'''========================================================================================='''
		try:
			if month == 2 and year%4==0:
				elem.send_keys('0'+str(month)+'/'+str(month_dic[month]+1)+'/'+str(year))
			else:
				elem.send_keys('0'+str(month)+'/'+str(month_dic[month])+'/'+str(year))
		except:
			time.sleep(1)
			sys.stderr.write('4 error')
			if month == 2 and year%4==0:
				elem.send_keys('0'+str(month)+'/'+str(month_dic[month]+1)+'/'+str(year))
			else:
				elem.send_keys('0'+str(month)+'/'+str(month_dic[month])+'/'+str(year))
		'''======================================================================================'''
		# try:
		# 	elem = driver.find_element_by_xpath('//*[@id="M_B_cblData_0"]')
		# 	time.sleep(1)
		# 	hover = ActionChains(driver).move_to_element(elem)
		# 	time.sleep(1)
		# 	hover.perform()
		# except :
		# 	time.sleep(1)
		# 	sys.stderr.write('4.5 error')
		# 	elem = driver.find_element_by_xpath('//*[@id="M_B_cblData_0"]')
		# 	time.sleep(1)
		# 	elem.click()
		'''======================================================================================'''
		try:
			elem = driver.find_element_by_xpath('//*[@id="M_B_btnSearch"]')
			time.sleep(1)
			elem.click()
		except:
			time.sleep(1)
			sys.stderr.write('5 error')
			elem = driver.find_element_by_xpath('//*[@id="M_B_btnSearch"]')
			time.sleep(1)
			elem.click()
	elif month<13:
		try:
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateFrom"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
			elem.send_keys(str(month)+'/'+'01/'+str(year))
		except:
			elem = driver.find_element_by_xpath('//*[@id="divDateTop"]')
			time.sleep(1)
			hover = ActionChains(driver).move_to_element(elem)
			time.sleep(1)
			hover.perform()
			time.sleep(1)
			sys.stderr.write('6 error')
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateFrom"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
			elem.send_keys(str(month)+'/'+'01/'+str(year))
		try:
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateTo"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
			if month == 2 and year%4==0:
				elem.send_keys(str(month)+'/'+str(month_dic[month]+1)+'/'+str(year))
			else:
				elem.send_keys(str(month)+'/'+str(month_dic[month])+'/'+str(year))
		except:
			elem = driver.find_element_by_xpath('//*[@id="divDateTop"]')
			time.sleep(1)
			hover = ActionChains(driver).move_to_element(elem)
			time.sleep(1)
			hover.perform()
			time.sleep(1)
			sys.stderr.write('7 error')
			elem = driver.find_element_by_xpath('//*[@id="M_B_txtDateTo"]')
			time.sleep(1)
			elem.clear()
			time.sleep(1)
			if month == 2 and year%4==0:
				elem.send_keys(str(month)+'/'+str(month_dic[month]+1)+'/'+str(year))
			else:
				elem.send_keys(str(month)+'/'+str(month_dic[month])+'/'+str(year))
		try:
			elem = driver.find_element_by_xpath('//*[@id="M_B_btnSearch"]')
			time.sleep(1)
			elem.click()
		except:
			time.sleep(1)
			sys.stderr.write('8 error')
			elem = driver.find_element_by_xpath('//*[@id="M_B_btnSearch"]')
			time.sleep(1)
			elem.click()
	month += 1
	if month==13:
		month = 1
		year += 1
		time.sleep(1)
	time.sleep(5+(year%2001)*1/2)
