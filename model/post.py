__author__ = 'hfli'

import time
import sqlalchemy
import database
from pony.orm import *
#from database import mBase

class Post(database.db.Entity):
    title= Required(str)
    content=Required(str)
    created_dat=Required(int,default=int(time.time()))
    update_date=Required(int,default=int(time.time()))
    # __tablename__ = 'Post'
    # __table_args__ = {'extend_existing':True}
    #
    # id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True, autoincrement = True)
    # title = sqlalchemy.Column(sqlalchemy.String(64))
    # content = sqlalchemy.Column(sqlalchemy.Text)
    # created_date = sqlalchemy.Column(sqlalchemy.Integer)
    # update_date = sqlalchemy.Column(sqlalchemy.Integer)
    #
    # def __init__(self, title=title, content=content,
    #              created_date = None, update_date = None):
    #     self.title=title
    #     self.content = content
    #
    #     if created_date == None:
    #         created_data = time.time()
    #     else:
    #         self.update_date = update_date
    #
    #     if update_date == None:
    #         update_date = time.time()
    #     else:
    #         self.update_date = update_date
