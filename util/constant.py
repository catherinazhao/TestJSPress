# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @Function：constant.py

import os


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
report = project_path + os.sep + 'report' + os.sep
print(report)
testcase = os.path.join(project_path, "Testcase")
util = os.path.join(project_path, "util")
screen_shot = project_path + os.sep + 'screenshots'

user_register_ddt = project_path + os.sep + 'ddt' + os.sep + 'user_register.txt'
user_login_ddt = project_path + os.sep + 'ddt' + os.sep + 'user_login.txt'
admin_login_ddt = project_path + os.sep + 'ddt' + os.sep + 'admin_login.txt'
chrome_driver = r"C:\Users\yangzhao\AppData\Local\Programs\selenium_driver\chromedriver.exe"

user_register_url = 'http://localhost:8080/jpress/user/register'





