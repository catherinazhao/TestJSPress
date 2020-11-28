# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @File：test_user_register.py

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page.user_register_page import RegisterPage
from util.ddt_read import ReadDDT
from util.constant import user_register_ddt


@allure.feature("用户注册界面")
class TestUserRegister(object):
	def setup_class(self):
		self.driver = webdriver.Chrome()
		self.register_page = RegisterPage(self.driver)
		self.register_page.goto_register()

	def teardown_class(self):
		self.register_page.quit()

	@allure.title("测试用户注册功能")
	@pytest.mark.parametrize('user, email, password, confirm_password, code, expect', ReadDDT.read_data(user_register_ddt))
	def test_user_register(self, user, email, password, confirm_password, code, expect):
		# step按步骤进行测试
		with allure.step("输入用户名"):
			self.register_page.input_user_name(user)

		with allure.step("输入邮箱"):
			self.register_page.input_email(email)

		with allure.step("输入密码"):
			self.register_page.input_pwd(password)

		with allure.step("输入确认密码"):
			self.register_page.input_confirm_pwd(confirm_password)

		with allure.step("输入验证码"):
			if code != '1234':
				self.register_page.input_code(self.register_page.get_code())
			else:
				self.register_page.input_code(code)

		with allure.step("点击注册"):
			self.register_page.click_btn()

		with allure.step('点击alert确定'):
			WebDriverWait(self.driver, 5).until(EC.alert_is_present())
			alert_handle = self.driver.switch_to.alert
			assert expect == alert_handle.text, "用户注册失败：%s" % alert_handle
			alert_handle.accept()

			pic = self.register_page.get_screenshot()
			allure.attach.file(pic, "用例截图", attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
	# pytest.main(['test_user_register.py'])
	pytest.main(['-s', "-q", "--alluredir", "./report/"])












