# coding: utf-8
from pony.orm import *
from .base import BaseHandler
from tornado.web import *
from model import *
import time
import datetime

# __author__ = 'hfli'

# class VendorManageHandler(BaseHandler):
# 	def get(self):
# 		self.write("This is Vendor Manage dashboard")

def format_date(date):
#TODO:
#        date = time.localtime(date)
        return datetime.datetime.utcfromtimestamp(date).strftime("%Y-%m-%d:%H:%M:%S")

class IndexHandler(BaseHandler):
	@db_session
	def get(self):
                posts = select(p for p in Post)
		self.render("index.html",posts=posts, format_date=format_date)
	def post(self):
		pass
	def edit(self):
		pass
	def remove(self):
		pass

class AddPostHandler(BaseHandler):
    @db_session
    def get(self):
            posts = select(p for p in Post).order_by(Post.created_date.desc())
            # posts = select((p,u) for p in Post for u in p.user)[:]
            # print(posts[0][0].title,posts[0][1].alias)
            self.render("index.html",posts=posts, format_date=format_date)

    @db_session
    def post(self, *args, **kwargs):
        title=self.get_argument("submit_title")
        content=self.get_argument("submit_post_content")
        author=User.get(id=1)
        create_time=int(time.time())
        post=Post(title=title,content=content,user=author)
        self.redirect("/")

class PostHandler(BaseHandler):
    @db_session
    def get(self):
        post_id = self.get_argument("id")
        post = get(p for p in Post if p.id == post_id)
        subpost = select(p for p in SubPost if p.post == post).order_by(SubPost.created_date.desc())
        self.render("post.html",post=post,subposts=subpost,format_date=format_date)

class AddSubPostHandler(BaseHandler):
    @db_session
    def post(self):
        post_id = self.get_argument("post_id")
        title=self.get_argument("submit_title")
        content=self.get_argument("submit_post_content")
        author=User.get(id=1)
        create_time=int(time.time())
        post = get(p for p in Post if p.id==post_id)
        if(post != None):
            SubPost(title=title,user=author,post=post,content=content)
        else:
            self.write("滚")
            return
        self.redirect("/post_content?id=%s"% (post_id))
#        subposts = select (p for p in SubPost if p.post==post)
