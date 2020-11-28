# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-23
# @IDE: Pycharm
# function： test_user_register.py

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config import GetConfigParser
from util import util_tool
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

conf = GetConfigParser()

USER_NAME_NAME = 'username'
MAIL_NAME = 'email'
PASSWORD_NAME = 'pwd'
CONFIRM_PASSWORD_NAME = 'confirmPwd'
CODE_ID = 'captcha'
CODE_PIC_ID = 'captchaimg'
REGISTER_BTN_CLASS = 'btn'

'''
p：parameter 参数
m：method 方法
c：class 类
v：variable 变量
f：function 函数
'''


class TestUserRegister(unittest.TestCase):
	# setup & teardown分为类方法和实例方法
	# 类方法仅执行一次，实例方法每个测试用例都执行一次
	# 环境初始化
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(
			executable_path=r"C:\Users\yangzhao\AppData\Local\Programs\selenium_driver\chromedriver.exe")

		cls.driver.get(conf.user_register_url)
		cls.driver.maximize_window()
		print("This is setUpClass function ")

	def tearDown(self):
		self.driver.find_element_by_name(USER_NAME_NAME).clear()
		self.driver.find_element_by_name(MAIL_NAME).clear()
		self.driver.find_element_by_name(PASSWORD_NAME).clear()
		self.driver.find_element_by_name(CONFIRM_PASSWORD_NAME).clear()
		self.driver.find_element_by_name(CODE_ID).clear()
		print("This is teardown function")

	# 还原测试环境
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		print("This is tearDownClass function ")



	# 注册信息全为空
	def test_case_1_user_register_null(self):
		expected = "用户名不能为空"
		bt = self.driver.find_element_by_class_name(REGISTER_BTN_CLASS)
		bt.click()

		WebDriverWait(self.driver, 5).until(EC.alert_is_present())
		alert = self.driver.switch_to.alert
		sleep(3)
		self.assertEqual(alert.text, expected)

		# 判断完之后要恢复要原样,所以要点确定
		alert.accept()

	# 注册邮箱为空
	def test_case_2_user_register_email_null(self):
		expected = "邮箱不能为空"

		user = self.driver.find_element_by_name(USER_NAME_NAME)
		user.send_keys(util_tool.get_random_string())

		self.driver.find_element_by_class_name(REGISTER_BTN_CLASS).click()
		WebDriverWait(self.driver, 5).until(EC.alert_is_present())

		alert = self.driver.switch_to.alert
		sleep(3)

		self.assertEqual(alert.text, expected)
		alert.accept()

	# 密码填写不一致
	def test_case_4_password_changeful(self):
		expected = "两次输入密码不一致"
		password = "123456"
		confirm_password = "123458"
		self.driver.find_element_by_name(USER_NAME_NAME).send_keys(util_tool.get_random_string())
		self.driver.find_element_by_name(MAIL_NAME).send_keys(util_tool.get_random_string() + "@qq.com")
		self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)
		self.driver.find_element_by_name(CONFIRM_PASSWORD_NAME).send_keys(confirm_password)

		self.driver.find_element_by_class_name(REGISTER_BTN_CLASS).click()

		WebDriverWait(self.driver, 5).until(EC.alert_is_present())

		alert = self.driver.switch_to.alert

		self.assertEqual(alert.text, expected)

		sleep(3)
		alert.accept()

	# 验证码填写错误
	def test_case_5_code_error(self):
		expected = "验证码不正确"
		password = "123456"
		confirm_password = "123456"
		code = "ss"

		self.driver.find_element_by_name(USER_NAME_NAME).send_keys(util_tool.get_random_string())
		self.driver.find_element_by_name(MAIL_NAME).send_keys(util_tool.get_random_string() + "@qq.com")
		self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)
		self.driver.find_element_by_name(CONFIRM_PASSWORD_NAME).send_keys(confirm_password)
		self.driver.find_element_by_id(CODE_ID).send_keys(code)

		self.driver.find_element_by_class_name(REGISTER_BTN_CLASS).click()

		WebDriverWait(self.driver, 5).until(EC.alert_is_present())

		alert = self.driver.switch_to.alert

		self.assertEqual(alert.text, expected)

		sleep(3)
		alert.accept()

	# 用户注册成功
	# @unittest.skip('暂时跳过用户注册成功的测试')
	def test_case_6_register_successful(self):
		user_name = "test01"
		expected = "注册成功，点击确定进行登录。"
		password = "123456"
		confirm_password = "123456"

		self.driver.find_element_by_name(USER_NAME_NAME).send_keys(user_name)
		self.driver.find_element_by_name(MAIL_NAME).send_keys(user_name + "@qq.com")
		self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)
		self.driver.find_element_by_name(CONFIRM_PASSWORD_NAME).send_keys(confirm_password)
		self.driver.find_element_by_id(CODE_ID).send_keys(util_tool.get_screen_shot(self.driver, CODE_PIC_ID))

		self.driver.find_element_by_class_name(REGISTER_BTN_CLASS).click()

		WebDriverWait(self.driver, 5).until(EC.alert_is_present())

		alert = self.driver.switch_to.alert

		self.assertEqual(alert.text, expected, "Register Successful")

		sleep(3)

		alert.accept()


if __name__ == '__main__':

	report_title = 'Example用例执行报告'
	desc = '用于展示修改样式后的HTMLTestRunner'
	report_file = 'ExampleReport.html'

	# 加载测试用例的几种方法
	# 第一种，最常用
	# unittest.main()

	# 第二种测试方法
	# 构建一个测试套件, 测试case执行顺序, 按照测试case加载顺序执行
	testsuit = unittest.TestSuite()
	# testsuit.addTest(TestUserLogin('test_case_1_user_register_null'))
	# testsuit.addTest(TestUserLogin('test_case_2_user_register_email_null'))
	#
	# # 第三种测试方法
	# cases = [TestUserLogin('test_case_1_user_register_null'), TestUserLogin('test_case_2_user_register_email_null')]
	# testsuit.addTests(cases)

	# 第四种
	loader = unittest.TestLoader()  # 用例加载器
	# 通过测试类的方式加载
	test_class = loader.loadTestsFromTestCase(TestUserRegister)
	testsuit.addTest(test_class)

	# 第五种
	# 通过测试模块的方式加载
	# testsuite.addTest(test_module = loader.loadTestsFromModule())

	# 第六种
	# 通过路径的方式加载
	# path =
	# testsuit.addTest(loader.discover(path))
	#
	# discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='unittest*.py')
	# runner = unittest.TextTestRunner()
	# runner.run(discover)


	# 执行测试用例
	# runner = unittest.TextTestRunner()
	# runner.run(testsuit)

	with open(report_file, 'wb') as report:
		runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
		runner.run(testsuit)




