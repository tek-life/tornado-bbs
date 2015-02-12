# coding: utf-8

__author__ = 'hfli'

import time
import sqlalchemy
from database import *
from pony.orm import *
from .post import *
from .user import *
#from database import mBase

class SubPost(db.Entity):
    # 设置主键
    id=PrimaryKey(int, auto=True)
    # 从属到哪个post
    post = Required(Post)
    user = Required(User)
    title= Required(str)
    content=Required(str)
    created_date=Required(int,default=int(time.time()))
    updated_date=Required(int,default=int(time.time()))
    # 设置对Post,User的外键

