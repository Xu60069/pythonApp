#http://stackoverflow.com/questions/13272528/bottle-py-http-auth
#https://gist.github.com/thinkxl/8296214
from bottle import request, route, run, template, auth_basic
#need to install pywin32 from sourceforge
import win32security
#import win32api

def win32check(user, pw):
    try:
        token = win32security.LogonUser(
        user, "ezesoft", pw,
        win32security.LOGON32_LOGON_NETWORK,
        win32security.LOGON32_PROVIDER_DEFAULT)
        authenticated = bool(token)
        print("authenticated %r"% (authenticated))
        return authenticated
    except:
        return False

userList={"TEST":"TOPsecrete"}    
def check(user, pw):
    # Check user/pw here and return True/False
    user = user.upper()
    password = ""
    if user in userList.keys():
        password = userList[user]
    else:
        print("not found: "+user+" / "+pw)
        return False
    if pw==password and pw != "":
        return True
    print("no match: "+user+" / "+pw)
    return False

@route('/hello/<name>')
@auth_basic(check)
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
@auth_basic(check)
def home():
    print(request.auth)
    print(request.remote_addr)
    return { 'data': request.auth }

run(host='localhost', port=8080)
