#http://stackoverflow.com/questions/13272528/bottle-py-http-auth
#https://gist.github.com/thinkxl/8296214
from bottle import request, route, run, template, auth_basic
#need to install pywin32 from sourceforge

userList={"TEST":"TOPsecrete"}
def check(user, pw):
    # Check user/pw here and return True/False
    user = user.upper()
    password = ""
    if user in userList.keys():
        password = userList[user]
    if pw==password and pw != "":
        return True
    print("not found: "+user+" / "+pw)
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
