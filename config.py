import tornado.web

import sys
import os
#import sqlalchemy
#import sqlalchemy.orm
#import sqlalchemy.ext.declarative
#from sqlalchemy.exc import OperationalError
# __DBHOST = "128.199.77.95"
import pony.orm
__DBHOST = "127.0.0.1"
__DBPORT = 3306
__DBUSER = "root"
__DBPASSWD = ""
__DBNAME = "bbs"
database = "mysql://%s:%s@%s/%s" %(__DBUSER,__DBPASSWD,__DBHOST,__DBNAME)

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

