from flask import Flask, render_template,request,jsonify
import pymysql
from simplejson import dumps
import json
import bsonjs
from ast import literal_eval
import requests

juso_db = pymysql.connect(
    user='root',
    passwd='z1x2a3s4@',
    host='127.0.0.1',
    db='mydb',
    charset='utf8'
)

app = Flask(__name__)
test = "3"

#값 포스트하기
@app.route('/request', methods=['POST'])
def query():
    curs = juso_db.cursor(pymysql.cursors.DictCursor)
    response = requests.get('http://localhost:5000/testing')
    if request.mimetype == "application/json":
        data = request.get_json()
        data = json.dumps(data, ensure_ascii=False)
        data = literal_eval(data)
        value = data['id']
    else:
        data = request.form['SensorID']
    value = response.text
    print(value)
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    # value = str(data['SensorID'])

    sql = "select * from Book where bookid ={}".format(value)
    curs.execute(sql)
    data_list = curs.fetchall()
    data1 = data_list[0]
    data1 = {
            'bookid': data1['bookid'],
            'bookname': data1['bookname'],
            'publisher': data1['publisher'],
            'price': data1['price']
            }

    jsondata = dumps(data1)
    return jsondata
    #return "1"

def chagne_test(value):
    global test
    test = value

#testing 페이지
@app.route('/testing')
def t1():
    global test
    return test

#값 변경하기
@app.route('/change-test',methods=['POST'])
def t2():
    data = request.get_json()
    data = json.dumps(data, ensure_ascii=False)
    data = literal_eval(data)
    value = data
    chagne_test(value)
    return "1"

#ajax페이지
@app.route('/request',methods=['GET'])
def query1():
    return render_template('test.html')


@app.route("/good")
def query2():
    return render_template("test2.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
