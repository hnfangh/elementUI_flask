import json
import requests
import pymysql
url = 'https://api.muxiaoguo.cn/api/tianqi'
params = {"city": "长沙", "type": "1"}
res = requests.post(url, data=params)
# print(res.json())

sql='SELECT * FROM sys.userinfo'
SQL = "INSERT INTO sys.userinfo (id,name,age,date) values('5','wusong','89','1961-01-01')"
SQL1 = "UPDATE sys.userinfo set age='76',date='1950-09-15' WHERE  id ='4'"
from app import mysql
b = mysql.DataBase()
p = b.selectSQL(sql)
# m = b.insertSQL(SQL)
# n = b.updateSQL(SQL1)
print(p)


