from django.shortcuts import render

# Create your views here.
import sys,os,hashlib
from django.shortcuts import HttpResponse
from django.shortcuts import render
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from db import web_db,data
from django.shortcuts import redirect


DB = web_db.DB_Control()
table = DB.Tables['user']
user_obj = DB.Session.query(table).filter_by(name='admin').all()
use = user_obj[0].name
passwd = user_obj[0].pwd


def Create_Pwd(pwd):
    return hashlib.md5(pwd.encode("utf8")).hexdigest()

def login(request):
    '''
    验证登录
    :param request:
    :return:
    '''
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        password = Create_Pwd(pwd)
        if passwd == password and use == user:
            return redirect('http://127.0.0.1:8000/excel')
        else:
            error_msg = "用户名或密码错误"
    return render(request,'login.html',{'error_msg': error_msg})


def excel(request):
    '''
    处理表格
    :param request:
    :return:
    '''
    if request.method == "POST":
        i = request.POST.get('')
        u = request.POST.get('username')
        z = request.POST.get('group')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'id': i,'username': u,'email':e,'gender': g,'group': z }
        data.USER_LIST.append(temp)
        #添加数据
        data.add_info(i,u,z,e,g)
    return render(request,'excel.html',{'user_list': data.USER_LIST})


def del_host(request):
    '''
    删除
    :param request:
    :return:
    '''
    nid = request.POST.get('nid')
    data.del_host(nid)
    return redirect('http://127.0.0.1:8000/excel')
