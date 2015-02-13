# coding: utf-8
from controller.manage import *
__author__ = 'hfli'

# 各种路由

handlers=[
	(r"/",IndexHandler),
        (r"/add_post", PostHandler),
	(r"/post_content",PostHandler),
	(r"/add_sub_post",AddSubPostHandler),
	(r"/login",LoginHandler),
	(r"/logout",LogoutHandler),
	(r"/register",RegisterHandler),
	(r"/edit",IndexHandler),
	(r"/delete",IndexHandler),
	(r"/del",DelHandler),
]
