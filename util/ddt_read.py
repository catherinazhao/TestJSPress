# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @File： ddt_read.py

import os
import re
import sys

from util.constant import user_register_ddt
from util.constant import user_login_ddt

'''通过DDT的方式读取测试用例'''


class ReadDDT(object):

	@staticmethod
	def read_data(data_file):
		test_cases = []
		with open(data_file, encoding='utf-8') as f:
			for line in f.readlines():
				case = []
				if line.startswith("#"):
					continue
				else:
					for val in line.split(','):
						# match = re.findall(r'[<](.*)[>]', val.strip())
						case.append(val.strip())

					test_cases.append(case)
					print(line.strip())

		print(test_cases)
		return test_cases


if __name__ == '__main__':
	rd = ReadDDT()
	rd.read_data(user_login_ddt)
