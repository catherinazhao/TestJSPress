# -*- coding:utf-8 -*-
# @Author: yang
# @Time:2020-11-28
# @IDE: Pycharm
# @File: admin_login.py
from selenium.webdriver.android import webdriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from util.verify_code import VerifyCode


class AdminLoginPage(BasePage):
	def __init__(self, driver):
		BasePage.__init__(self, driver)

		self.user = (By.NAME, "user")
		self.password = (By.NAME, "pwd")
		self.captcha = (By.NAME, "captcha")
		self.captchaImg = (By.ID, "captchaImg")
		self.btn = (By.CLASS_NAME, "btn")

	"""跳转到管理员登录界面"""
	def goto_login(self):
		self.driver.get("http://localhost:8080/jpress/admin/login")
		self.driver.maximize_window()

	def input_user(self, text):
		self.clear(*self.user)
		self.input_text(text, *self.user)

	def input_passowrd(self, text):
		self.clear(*self.password)
		self.input_text(text, *self.password)

	def click_btn(self):
		self.click(*self.btn)

	def input_code(self, text):
		self.clear(*self.captcha)
		self.input_text(text, *self.captcha)

	def get_code(self):
		return VerifyCode.get_code(self.driver, self.captchaImg)
