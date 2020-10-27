import pymysql
db =pymysql.connect("localhost","usr","usr","test",use_unicode=True,charset="utf-8")
cursor=db.cursor()