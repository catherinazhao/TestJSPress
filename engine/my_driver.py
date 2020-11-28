# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @File：driver.py

from selenium import webdriver
from time import sleep

from util.constant import chrome_driver


class Driver(object):

	@classmethod
	def __new__(cls, *agrs, **kwargs):
		cls.driver = webdriver.Chrome(executable_path=chrome_driver)
		# super(Driver, cls).__new__(cls)
		print(cls.driver)
		return cls.driver


if __name__ == '__main__':
	driver = Driver()
	print(driver)
	driver.get("http://www.baidu.com")
	sleep(3)
	driver.quit()
