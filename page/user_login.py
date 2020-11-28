# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-28
# @IDE: Pycharm
# @File：user_login.py
from selenium.webdriver.common.by import By

from page.basepage import BasePage

from selenium import webdriver


class LoginPage(BasePage):
	def __init__(self, driver):  # 先继承在重构, 可以获得父类的属性
		# 定义了__init__方法, 就是在定义了构造函数进行了重构, 如果不先进行继承的话, 子类则不能继承父类的属性
		"""
			继承构造类的两种方法
			1. 经典类的写法： 父类名称.__init__(self, 参数1，参数2，...)
			2.新式类的写法：super(子类，self).__init__(参数1，参数2，....)
		"""
		BasePage.__init__(self, driver)  # 继承父类的构造方法
		self.user = (By.NAME, "user")
		self.password = (By.NAME, "pwd")
		self.btn = (By.CLASS_NAME, "btn")

	"""跳转到用户登录界面"""
	def goto_login(self):
		self.driver.get("http://localhost:8080/jpress/user/login")
		self.driver.maximize_window()

	def input_user(self, text):
		self.clear(*self.user)
		self.input_text(text, *self.user)

	def input_passowrd(self, text):
		self.clear(*self.password)
		self.input_text(text, *self.password)

	def click_btn(self):
		self.click(*self.btn)





