#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","username","password","databasename")

#准备cursor

cursor = db.cursor()

cursor.execute("select version()")

#获得版本信息

info = cursor.fetchone()
print info


db.close()

