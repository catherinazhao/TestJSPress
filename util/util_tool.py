# -*- coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-23
# @IDE: Pycharm
# @Function： util_tool.py


import os
import time
import random
import string
import requests
# import pytesseract
from PIL import Image
from selenium import webdriver


# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from lib.ShowapiRequest import ShowapiRequest
from config import GetConfigParser

CONFIG = GetConfigParser()


# 截取图片
def get_screen_shot(driver, id):
	# 保存整个截图
	sc_path = CONFIG.screen_shot_path

	format_time = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())) + '.png'
	full_screenshot_name = os.path.join(sc_path, format_time)
	print(full_screenshot_name)
	driver.get_screenshot_as_file(full_screenshot_name)

	# 找到验证码图片的位置
	element = driver.find_element_by_id(id)
	rect_code = element.rect
	print(rect_code)
	left_top = rect_code['x']
	left_height = rect_code['y']
	right_end = rect_code['width'] + left_top
	right_height = rect_code['height'] + left_height

	# 抠图
	img = Image.open(full_screenshot_name)
	code_img = img.crop((left_top, left_height, right_end, right_height))

	code_pic_name = "code" + str(time.strftime("%Y-%m-%d - %H-%M-%S", time.localtime())) + '.png'
	pic_path = os.path.join(sc_path, code_pic_name)

	code_img.save(pic_path)
	code_str = get_string_from_api(pic_path)

	return code_str


# 第三方api解析验证码
def get_string_from_api(pic):
	# https://www.showapi.com/apiGateway/view/184/4  showapi接口文档说明
	r = ShowapiRequest("http://route.showapi.com/184-4", "447841", "8be0b4dc07c349f69c43b03c7b850089")
	r.addFilePara("image", pic)
	r.addBodyPara("typeId", "34")
	r.addBodyPara("convert_to_jpg", "0")
	r.addBodyPara("needMorePrecise", "0")
	res = r.post()
	print(res.text)
	code_str = res.json()['showapi_res_body']['Result']
	# print(res.text)  # 返回信息
	print(code_str)
	return code_str


# 生成随机字符串
def get_random_string():
	# 从a-zA-Z0-9生成指定数量的随机字符：
	ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
	print(ran_str, type(ran_str))
	return ran_str


if __name__ == '__main__':
	# driver = webdriver.Chrome(executable_path=r"C:\Users\yangzhao\AppData\Local\Programs\selenium_driver\chromedriver.exe")
	# driver.maximize_window()
	# get_string_from_api(get_screen_shot(driver))
	# driver.quit()
	st = get_random_string()
	print(st)