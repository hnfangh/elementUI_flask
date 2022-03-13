# coding=utf-8
import json
from app import mysql
import requests
from flask import request,jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask Web Project!'

@app.after_request
def cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Method'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return  response

@app.route('/test',methods=['POST','GET'])
def test():
    return_dict = {"status_code":200,"messge":"success"}
    if request.method == 'POST':
        res = request.get_data()
        result = json.loads(res)
        return  json.dumps({"user":result["username"],"messge":"用户信息提交成功","status_code":200})
    else:
        return return_dict

@app.route('/weather',methods=['POST'])
def search():
    url = 'https://api.muxiaoguo.cn/api/tianqi'
    res = requests.post(url,data=request.get_json())
    return jsonify(res.json())

# 添加用户
@app.route('/adduser',methods=['POST'])
def adduser():
    if request.method == 'POST':
        res = request.get_json()
        sql = "INSERT INTO sys.userinfo (id,name,age,date) values('{}','{}','{}','{}')".format(res['id'],res['name'],res['age'],res['date'])
        mysql.DataBase().insertSQL(sql)
        return {"user": res['id'], "msg": "用户添加成功", "status": "ok"}
    else:
        return {"msg": "用户添加失败", "status": "error"}

# 删除用户
@app.route('/deleteuser',methods=['POST'])
def deleteuser():
    if request.method == 'POST':
        res = request.get_json()
        sql = "DELETE FROM sys.userinfo WHERE id={}".format(res['id'])
        mysql.DataBase().deleteSQL(sql)
        return  {"user": res['id'], "msg": "用户删除成功", "status": "ok"}
    else:
        return {"msg": "用户删除失败", "status": "error"}

# 编辑用户
@app.route('/updateuser',methods=['POST'])
def updateuser():
    if request.method == 'POST':
        res = request.get_json()
        sql = "UPDATE sys.userinfo set name='{}',age='{}',date='{}' WHERE id ={}".format(res['name'],res['age'],res['date'],res['id'])
        mysql.DataBase().updateSQL(sql)
        return  {"user": res['id'], "msg": "用户更新成功", "status": "ok"}
    else:
        return {"msg": "用户更新失败", "status": "error"}

# 查询用户列表
@app.route('/userlist',methods=['POST'])
def userlist():
    if request.method == 'POST':
        sql = "SELECT * FROM sys.userinfo"
        result = mysql.DataBase().selectSQL(sql)
        print(str(result))
        return str(result)
    else:
        return {"msg": "查询用户失败", "status": "error"}