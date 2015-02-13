import tornado.web

import sys
import os

#import sqlalchemy
#import sqlalchemy.orm
#import sqlalchemy.ext.declarative
#from sqlalchemy.exc import OperationalError
# __DBHOST = "128.199.77.95"
from pony.orm import *
import MySQLdb
import time


__DBHOST = "127.0.0.1"
__DBPORT = 3306
__DBUSER = "root"
__DBPASSWD = ""
__DBNAME = "bbs"

db=Database('mysql',host=__DBHOST,user=__DBUSER,passwd=__DBPASSWD,db=__DBNAME)


def initialize_db():
#    temp = MySQLdb.Connect(host=__DBHOST,user=__DBUSER,passwd=__DBPASSWD)
#    temp_cursor = temp.cursor()
#    temp.set_character_set("utf8")
#    temp_cursor.execute("SET NAMES utf8;")
#    temp_cursor.execute("SET CHARACTER SET utf8;")
#    temp_cursor.execute("SET character_set_connection=utf8;")
#    temp_cursor.execute("SET character_set_database=utf8")
#    temp_cursor.execute("SET sql_notes=1;")
#    temp_cursor.execute("CREATE DATABASE IF NOT EXISTS %s CHARACTER SET utf8;"% __DBNAME)
#    temp_cursor.execute("SET sql_notes=1;")
#    temp_cursor.close()
#    temp.commit()
#    temp.close()
    sql_debug(True)
    db.generate_mapping(create_tables=True)

