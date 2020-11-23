from flask import Flask,render_template,make_response
from flask import Blueprint, request, flash, redirect, url_for
from module.dbModule import Database
from module.elasticsearchModule import Elastic

app = Flask(__name__)

@app.route('/')
def index():
    # Set a same-site cookie for first-party contexts
    #resp.set_cookie('cookie1', 'http://3.35.113.255:5601/', samesite='None')
    # Set a cross-site cookie for third-party contexts
    #resp.set_cookie('cookie2', 'value2', samesite='None', secure=True);
    return render_template('intro.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/info1')
def info1():
    return render_template('index1.html')

@app.route('/select', methods=['GET'])
def select():
    db_class = Database()
    es = Elastic()
    res = es.searchAPI()
    #print(res)
    #print(res['hits']['hits'])
    sql = "SELECT * FROM Book"
    row = db_class.executeAll(sql)
    rows = res['hits']['hits']
    #print(row)
    a = render_template('db.html',
                        test=res,
                        rows=rows,
                        resultData=row[1],
                        resultUPDATE=None)
    resp = make_response(a)
    # Set a same-site cookie for first-party contexts
    resp.set_cookie('sid', "value1", samesite='Strick')
    # Set a cross-site cookie for third-party contexts
    resp.set_cookie('sid', 'value2', samesite='Strick', secure=True)
    #resp.headers.add('Set-Cookie', 'cookie2=value2; SameSite=None; Secure')
    return a


@app.route('/select2', methods=['GET'])
def select2():
    db_class = Database()
    sql = "SELECT * FROM Book"
    rows = db_class.executeAll(sql)
    return render_template('db2.html',rows=rows)


# @app.route('/test', method=['GET', 'POST'])
# def test():
#     if request.method == 'GET':
#         return render_template('post.html')
#     elif request.method == 'POST':
#         value = request.form['test']
#         return render_template('default.html')

if  __name__ =='__main__':
    app.run(debug=True,port=5001)
