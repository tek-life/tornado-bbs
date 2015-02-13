import tornado.web

__author__ = 'hfli'

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")
	def is_login(self):
		return self.current_user != None
