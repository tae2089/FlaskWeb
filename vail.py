import re

#비밀번호 유효성 검사
def passwrodVaild(data):
    pswd = data
    reg = re.compile(r'^[A-Za-z0-9@#$!%^&%*~]{6,12}$')
    spec_reg = re.compile(r'[@#$]+')
    pswd_mat = reg.search(pswd)
    spec_mat = spec_reg.search(pswd)
    if pswd_mat and spec_mat:
        print(f"{pswd} is a valid password")
    else:
        print("Please check password requirements")

#login확인하기
def loginVaild():
    print("login")


def idVaild(data):
    reg = re.compile(r'[A-Za-z0-9]{4,20}$')
    id_mat = reg.search(data)
    if id_mat:
        print("good")
    else:
        print("not good")


#이멜이 체크하기
def emailVaild(data):
    reg = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    m = reg.search(data)
    if m:
        print("good")
    else:
        print("not good")

#비밀번호확인과 비밀번호 동일 한지  이중체크
def passwordDoubleVaild(data1,data2):
    if data1 == data2:
        print("good")
    else:
        print("password Double")


#공백 체크
def notblank():
    print("blank check")

#null 체크
def nullCkeck(data):
    if data == None:
        return "null"
    else:
        return data
