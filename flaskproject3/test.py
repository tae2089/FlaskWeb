import requests
import json
from ast import literal_eval

def  test():
    url_items = "http://localhost:5000/change-test"
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "id": int(3),
        "nickname": "big",
        "email": "tae2089@naver.com",
        "password": "1"
    }
    print(type(data))
    data = json.dumps(data)
    # print(type(data))
    # data = literal_eval(data)
    #requests.post(url_items, data=data, headers=headers)
    requests.post(url_items, data=data,headers = headers)
    
    

def test1():
    url_items = "http://localhost:5000/change-test"
    requests.post(url_items)

def test2():
    url_items = "http://localhost:5000/testing"
    a = requests.get(url_items)
    print(a.text)


def main():
    test()
    test2()
    #test1()

if __name__ == "__main__":
    main()
