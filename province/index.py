# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:25:24 2018

@author: hong
"""

from flask import Flask,render_template,jsonify,request
import pymysql as MySQLdb

app = Flask(__name__)

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'',
          'db':'test',
          'charset':'utf8mb4',
          'cursorclass':MySQLdb.cursors.DictCursor,
          }

connection = MySQLdb.connect(**config)

def search(sql):
    with connection.cursor() as cursor:
    # 执行sql语句，进行查询
            
        cursor.execute(sql)
    # 获取查询结果
        result = cursor.fetchall()
        
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
    return result
        
#数据接口                   
@app.route("/num",methods=["GET"])
def add_numbers():
    a = int(request.args.get("a"))
    print(a)
    b = int(request.args.get("b"))
    print(b)
    if a == -1:
        pass
    elif a == 0:
        sql = 'SELECT ProvinceID,ProvinceName FROM S_Province'
        result = search(sql)
    else:
        sql = 'SELECT CityID,CityName FROM S_City where ProvinceID='+repr(a)
        result = search(sql)

    if b == -1:
        pass
    else:
        sql = 'SELECT DistrictID,DistrictName FROM s_district where CityID='+repr(b)
        result = search(sql)
    print(result)
    return jsonify(result=result)                    

#主页路由
@app.route("/")
def index():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=False)