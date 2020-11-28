# @Author: yang
# @Time: 2020-11-23
# @IDE: Pycharm
# @Function： util_tool.py


import os
import time
import requests
import pytesseract
from PIL import Image
from selenium import webdriver

# from ..config import GetConfigParser

# CONFIG = GetConfigParser()


# python方法截取截取并解析简单验证
def get_code_original_method():
	driver = webdriver.Chrome(executable_path
							  =r"C:\Users\yangzhao\AppData\Local\Programs\selenium_driver\chromedriver.exe")
	# driver.get(CONFIG.user_register_url)
	driver.get("http://localhost:8080/jpress/user/register")

	# 保存整个截图
	time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
	full_png_path = os.path.dirname(os.path.dirname(__file__)) + "\\screenshots\\" + str(time_stamp) + ".png"
	driver.get_screenshot_as_file(full_png_path)

	# 查找验证码图片
	element = driver.find_element_by_id("captchaimg")

	# 验证码图片坐标
	left = element.rect['x']
	top = element.rect['y']
	right = left + element.rect['width']
	height = top + element.rect['height']

	print(element.location)  # 返回左上角x, y 坐标
	print(element.rect)	 # 返回左上角x,y; 宽和高
	print(element.size)  # 返回宽和高

	# dpr = driver.execute_script('return window.devicePixelRatio')

	# 用PIL将需要截取的图片打开
	img = Image.open(full_png_path)
	# im = img.crop((left*dpr, top*dpr, right*dpr, height*dpr))

	# 截取图片对象
	im = img.crop((left, top, right, height))

	t = time.time()

	code_png = os.path.dirname(os.path.dirname(__file__)) + "\\screenshots\\" + str(t) + '.png'
	im.save(code_png)  # 截取到的验证码图片

	# python3.6.5
	# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
	from lib.ShowapiRequest import ShowapiRequest

	r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
	r.addFilePara("image", code_png)
	r.addBodyPara("typeId", "34")
	r.addBodyPara("convert_to_jpg", "0")
	r.addBodyPara("needMorePrecise", "0")
	res = r.post()
	print(1111, res.json['showapi_res_body']['Result'])  # 返回信息

	#
	# print(22222, code_png)
	# code_jpg = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test1.jpg")
	# print(11111111, code_jpg, type(code_jpg))
	# code_image = Image.open(code_jpg)
	# st = pytesseract.image_to_string(code_image)
	# print(str(st, 'cp1252', 'ignore'))


if __name__ == '__main__':
	get_code_original_method()



