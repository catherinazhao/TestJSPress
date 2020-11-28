# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @File：user_register_page.py

from selenium.webdriver.common.by import By

from page.basepage import BasePage
from util.verify_code import VerifyCode


class RegisterPage(BasePage):
	def __init__(self, driver):
		BasePage.__init__(self, driver)
		self.user_name = (By.NAME, "username")
		self.email = (By.NAME, "email")
		self.pwd = (By.NAME, "pwd")
		self.confirm_pwd = (By.NAME, "confirmPwd")
		self.captcha = (By.ID, "captcha")
		self.captcha_img = (By.ID, "captchaimg")
		self.bt = (By.CLASS_NAME, "btn")

	def goto_register(self):
		self.driver.get('http://localhost:8080/jpress/user/register')
		self.driver.maximize_window()

	def input_user_name(self, text):
		self.clear(*self.user_name)
		self.input_text(text, *self.user_name)

	def input_email(self, text):
		self.clear(*self.email)
		self.input_text(text, *self.email)

	def input_pwd(self, text):
		self.clear(*self.pwd)
		self.input_text(text, *self.pwd)

	def input_confirm_pwd(self, text):
		self.clear(*self.confirm_pwd)
		self.input_text(text, *self.confirm_pwd)

	def input_code(self, text):
		self.clear(*self.captcha)
		self.input_text(text, *self.captcha)

	def click_btn(self):
		self.click(*self.bt)

	def get_code(self):
		return VerifyCode.get_code(self.driver, self.captcha_img)










