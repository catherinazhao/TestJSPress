# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @File：basepage.py
"""
	base page function mode
"""

import os
import time
from selenium import webdriver

from util.constant import screen_shot
"""selenium页面基本操作"""


class BasePage(object):
	def __init__(self, driver):
		self.driver = driver

	def get_element(self, *loc):
		""" 获取页面元素 """
		return self.driver.find_element(*loc)

	def input_text(self, text, *loc):
		""" 输入内容 """
		self.driver.find_element(*loc).send_keys(text)

	def clear(self, *loc):
		""" 清除数据 """
		self.driver.find_element(*loc).clear()

	def click(self, *loc):
		""" 点击确认 """
		self.driver.find_element(*loc).click()

	def quit(self):
		""" 退出浏览器 """
		self.driver.quit()

	def get_screenshot(self):
		""" 截图 """
		file_name = screen_shot + os.sep + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.png'
		self.driver.save_screenshot(file_name)
		return file_name