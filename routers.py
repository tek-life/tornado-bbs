# coding: utf-8
from controller.manage import *
__author__ = 'hfli'

# 各种路由

handlers=[
	(r"/",AddPostHandler),
        (r"/add_post", AddPostHandler),
	(r"/post_content",PostHandler),
	(r"/add_sub_post",AddSubPostHandler),
	(r"/post",IndexHandler),
	(r"/edit",IndexHandler),
	(r"/delete",IndexHandler),
]
