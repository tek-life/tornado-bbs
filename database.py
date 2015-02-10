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
#database = "mysql://%s:%s@%s/%s" %(__DBUSER,__DBPASSWD,__DBHOST,__DBNAME)

#db=Database('mysql',host=__DBHOST,user=__DBUSER,passwd=__DBPASSWD)
db=Database('mysql',host=__DBHOST,user=__DBUSER,passwd=__DBPASSWD,db=__DBNAME)


def initialize_db():
#     global db
#     print(db,__file__)
#     temp = MySQLdb.Connect(host=__DBHOST,user=__DBUSER,passwd=__DBPASSWD)
#     temp_cursor = temp.cursor()
#     temp_cursor.execute("SET sql_notes=0;")
#     temp_cursor.execute("CREATE DATABASE IF NOT EXISTS %s;"% __DBNAME)
#     temp_cursor.execute("SET sql_notes=1;")
#     temp_cursor.close()
#     temp.commit()
#     temp.close()
# #    print(db,__file__)
    db.generate_mapping(create_tables=True)
#    print(db,__file__)



#mysql_engine = sqlalchemy.create_engine(database,echo=True)
#
#mBase = sqlalchemy.ext.declarative.declarative_base()
#def initialize_db():
#        import model
#	try:
#		mBase.metadata.create_all(mysql_engine)
#	except OperationalError, err:
#		print("Error %s" % str(err))
#	print("Data Base Completed")

