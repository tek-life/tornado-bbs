# coding: utf-8
import os.path
import tornado.web
import tornado.httpserver
import tornado.ioloop
import routers
from controller import manage
import database
import time

from model import *
import logging
#from config import initialize_db

# __author__ = 'hfli'


class Application(tornado.web.Application):
    def __init__(self):
        handlers=routers.handlers
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__),"view"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
	    cookie_secret="abc",
	    login_url="/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    database.initialize_db()
    logging.basicConfig(level=logging.INFO)
#    print(database.db,__file__)
#    db.generate_mapping(check_tables=True,create_tables=True)
    tornado.httpserver.HTTPServer(Application()).listen(8899)
    print("Web is running %d" %8899)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()
