# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-28
# @IDE: Pycharm
# @File：test_user_login.py

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from page.user_login import LoginPage
from util.ddt_read import ReadDDT
from util.constant import user_login_ddt


@allure.feature("用户登录界面")
class TestUserLogin(object):
	def setup_class(self):
		self.driver = webdriver.Chrome()
		self.login_page = LoginPage(self.driver)
		self.login_page.goto_login()

	def teardown_class(self):
		self.login_page.quit()

	@allure.story("测试用户登录功能")
	@pytest.mark.parametrize("user, password, expect", ReadDDT.read_data(user_login_ddt))
	def test_user_login(self, user, password, expect):
		with allure.step("输入账号"):
			self.login_page.input_user(user)

		with allure.step("输入密码"):
			self.login_page.input_passowrd(password)

		with allure.step("点击登录"):
			self.login_page.click_btn()
			sleep(3)
			if expect != "用户中心":
				WebDriverWait(self.driver, 5).until(EC.alert_is_present())
				alert = self.driver.switch_to.alert
				assert alert.text == expect, "用户登录失败"
				alert.accept()
			else:
				assert self.driver.title == expect, "用户登录失败"


if __name__ == '__main__':
	pytest.main(['-s', '-v', '--alluredir', './report/'])





