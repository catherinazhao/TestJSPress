# -*-coding:utf-8 -*-
# @Author: yang
# @Time: 2020-11-27
# @IDE: Pycharm
# @File：main.py

import pytest

from util.constant import report


if __name__ == '__main__':
	'''参数说明
	
		-s: 输出print()里的内容
		-v: 显示每个测试用例的详细结果
		-q: 只显示整体的测试结果
		-h: 帮助信息
	'''

	# pytest.main(['-s', '-v', '需要执行的测试模块'])
	pytest.main(['-s', '-v', '--alluredir', '%s' % report])