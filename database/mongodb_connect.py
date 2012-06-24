#!/usr/bin/python
#-*- coding:utf-8 -*-

#mongodb 连接

from pymongo import Connection

connection = Connection("localhost",27017)

#选择数据库
db = connection.test_database

#相当于关系数据库中的表
table = db.table

data = table.find()

print data


