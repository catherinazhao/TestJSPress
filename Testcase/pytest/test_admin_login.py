# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-28
# @IDE: Pycharm
# @File：test_admin_login.py

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from page.admin_login import AdminLoginPage
from util.ddt_read import ReadDDT
from util.constant import admin_login_ddt


@allure.feature("后台管理员界面")
class TestAdminLogin(object):
	def setup_class(self):
		self.driver = webdriver.Chrome()
		self.admin_page = AdminLoginPage(self.driver)
		self.admin_page.goto_login()

	def teardown_class(self):
		self.admin_page.quit()

	@allure.story("测试后台管理员登录功能")
	@pytest.mark.parametrize("user, password, code, expect", ReadDDT.read_data(admin_login_ddt))
	def test_user_login(self, user, password, code, expect):
		with allure.step("输入账号"):
			self.admin_page.input_user(user)

		with allure.step("输入密码"):
			self.admin_page.input_passowrd(password)

		with allure.step("输入验证码"):
			if code == "<VerifyCode>":
				self.admin_page.input_code(self.admin_page.get_code())
			else:
				self.admin_page.input_code(code)

		with allure.step("点击登录"):
			self.admin_page.click_btn()
			sleep(3)
			if expect != "JPress后台":
				WebDriverWait(self.driver, 5).until(EC.alert_is_present())
				alert = self.driver.switch_to.alert
				assert alert.text == expect, "后台管理员用户登录失败"
				alert.accept()
			else:
				assert self.driver.title == expect, "用户登录失败"


if __name__ == '__main__':
	pytest.main(['-s', '-v', '--alluredir', './report/'])





