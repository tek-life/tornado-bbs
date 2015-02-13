__author__ = 'hfli'
import time
from pony.orm import *
from database import *

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    alias = Required(str)
    email = Required(str)
    passwd = Required(str)
    register_time =Required(int, default=int(time.time()))
    post = Set("Post")
    subpost = Set("SubPost")
