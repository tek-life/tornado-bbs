# coding: utf-8
from controller.manage import IndexHandler
__author__ = 'hfli'

# 各种路由

handlers=[
	(r"/",IndexHandler),
	(r"/post",IndexHandler),
	(r"/edit",IndexHandler),
	(r"/delete",IndexHandler),
]