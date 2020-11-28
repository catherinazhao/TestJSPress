# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-25
# @IDE: Pycharm
# function： test_user_login.py

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from config import GetConfigParser
from util import util_tool

conf = GetConfigParser()

USER_NAME_NAME = 'user'
PASSWORD_NAME = 'pwd'
LOGIN_BTN_CLASS = 'btn'


class TestUserLogin(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(
			executable_path=r"C:\Users\yangzhao\AppData\Local\Programs\selenium_driver\chromedriver.exe")

		cls.driver.get(conf.user_login_url)
		cls.driver.maximize_window()
		print("This is setUpClass function ")

	def setUp(self):
		self.driver.find_element_by_name(USER_NAME_NAME).clear()
		self.driver.find_element_by_name(PASSWORD_NAME).clear()
		print("This is setUp function")

	# 还原测试环境
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		print("This is tearDownClass function ")

	# @unittest.skip
	def test_case_1_user_login_null(self):
		expected = '账号不能为空'
		self.driver.find_element_by_class_name(LOGIN_BTN_CLASS).click()

		WebDriverWait(self.driver, 5).until(EC.alert_is_present())

		ar = self.driver.switch_to.alert

		# unittest的断言
		self.assertEqual(ar.text, expected)

		sleep(3)
		ar.accept()

	# @unittest.skip
	def test_case_2_user_password_null(self):
		expected = '密码不能为空'
		user = 'test01'
		self.driver.find_element_by_name(USER_NAME_NAME).send_keys(user)
		self.driver.find_element_by_class_name(LOGIN_BTN_CLASS).click()

		WebDriverWait(self.driver, 5).until(EC.alert_is_present())

		ar = self.driver.switch_to.alert

		# unittest的断言
		self.assertEqual(ar.text, expected)

		sleep(3)
		ar.accept()

	def test_case_3_user_login_successful(self):
		user = 'test01'
		password = '123456'
		expected = "用户中心"

		self.driver.find_element_by_name(USER_NAME_NAME).send_keys(user)
		self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)
		self.driver.find_element_by_class_name(LOGIN_BTN_CLASS).click()

		print(self.driver.title)
		# 右键单击查看源码的网页titile
		WebDriverWait(self.driver, 5).until(EC.title_is(expected))

		sleep(3)
		assert self.driver.title == expected, "没有登录成功"


if __name__ == '__main__':
	unittest.main()