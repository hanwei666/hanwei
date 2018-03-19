from django.shortcuts import render

# Create your views here.
import sys,os,hashlib
from django.shortcuts import HttpResponse
from django.shortcuts import render
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from db import web_db
from django.shortcuts import redirect


DB = web_db.DB_Control()
table = DB.Tables['user']
user_obj = DB.Session.query(table).filter_by(name='admin').all()
use = user_obj[0].name
passwd = user_obj[0].pwd


def Create_Pwd(pwd):
    return hashlib.md5(pwd.encode("utf8")).hexdigest()

def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        password = Create_Pwd(pwd)
        if passwd == password and use == user:
            return redirect('http://www.baidu.com')
        else:
            error_msg = "用户名或密码错误"
    return render(request,'login.html',{'error_msg': error_msg})

