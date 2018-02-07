#### js正则表达式

- test

```
匹配到返回true
rep = /\d+/
/\d+/
rep.test("asdsdf")
false

rep.test("asd12")
true

^$ 精确匹配
rep = /^\d+$/;
/^\d+$/
rep.test("112sdf")
false
rep.test("11")
true


```



- exec

```
分组匹配和匹配所有(\W*) g
text = "JavaScript is more fun than \nJava or JavaBeans!"
var rep = /^Java(\W*)/g;
rep.exec(text)

匹配所有行m
text = "JavaScript is more fun than \nJava or JavaBeans!"
var rep = /^Java(\W*)/gm;
rep.exec(text)
```

#### 提交时间

```
-登录注册验证
	默认事件先执行
		checkbox
	自定义事件先执行
		a
		submit
		
		<form>
			<input type='type'/>
			<input type='password' />
			<input type='submit' />
		<form>
		
		$(':submit').click(function(){
          $(':text,:password').each(function(){
            retuen false;
          })
          return false;
		})

```

#### web模板

```
Ajax操作
http://www.jeasyui.com/

jqyeryui
http://jqueryui.com/

bootstrap
http://www.bootcss.com/
https://v3.bootcss.com/

bootstrap 模板
http://www.cssmoban.com/tags.asp?page=3&n=Bootstrap


```

#### bootstrap

响应式

@media

```
   <style>
        .c1{
            background-color:red;
            height:50px;
        }
        @media(min-width:900px){
            .c2{
                background-color:grey;
            }
        }
    </style>
</head>
<body>
    <div class="c1 c2"></div>
</body>
```

!important

强制样式生效

```
<style>
	.no-radus{
      border-radius: 0 !important;
	}
<style>
<link rel="stylesheet" href="bootstrap-3.3.0-dist/bootstrap.css"/>
```

##### 轮播图

- 1下载bxslider插件
- 2 https://bxslider.com/ 
- 3复制代码https://www.helloweba.net/demo/bxslider/demo3.html

```
<head>

    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="jquery.bxslider.css"/>
</head>
<body>
     <ul class="bxslider">
         <li><img src="images/1.jpg" /></li>
         <li><img src="images/2.jpg" /></li>
         <li><img src="images/3.jpg" /></li>
         <li><img src="images/4.jpg" /></li>
     </ul>

    <script src="jquery.js"></script>
    <script src="jquery.bxslider.js"></script>
    <script>
        // $(document).ready(function(){
        //     $('.bxslider').bxSlider();
        // });

        $(function(){
            $('.bxslider').bxSlider({
                auto: true,
                autoControls: true
            });
        });
    </script>
</body>
```

#### WEB：mvc mtv

```
MVC
    Model   View     Controller
    数据库   模板文件 业务处理
    
MTV 
	Model    temolates    Controller
    数据库    模板文件 业务处理
    
```

#### Django安装

```
1.pip3 install dango 

2.设置环境变量
D:\Programs\Python\Python35\Scripts

3.创建文件夹
django-admin startproject mysite

4.启动django 
cd mysite
python manage.py runserver 127.0.0.1:8001

```

```
mysite
      - mysite     
      - init       #对整个程序进行配置
      - settings   #配置文件
      - url        #URL对应关系
      - wsgi       #遵循WSIG规范， uwsgi + nginx 
      - manage.py  #管理Django程序：
                      - python  manage.py
                      - python  manage.py startapp xx
                      - python  manage.py makemigrations
                      - python  manage.py migrate
```

```
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello</h1>')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('h.html/', home),
]
```

创建APP

```
python manage.py startapp cmdb

from django.contrib import admin
from django.urls import path
from cmdb import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('h.html/', views.home),
]
```

APP文件

```
app:
	migrations    数据修改表结构记录文件
	admin         Django为我们提供的后台管理
	apps          配置当前app
	models        ORM，写指定的类 通过命令可以创建数据库结构
	tests         单元测试
	views         业务代码
```

URL调用

```
urls.py

from django.contrib import admin
from django.urls import path
from cmdb import views
from django.conf.urls import url
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('h.html/', views.home),
    url(r'login',views.login),
]

cmdb/views.py

from django.shortcuts import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'login.html')

templates/login.html

from django.shortcuts import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'login.html')


```

Django静态文件以及模板文件顺序

1.urls.py

```
from django.contrib import admin
from django.urls import path
from cmdb import views
from django.conf.urls import url
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('h.html/', views.home),
    url(r'login',views.login),
]
```

2.cmdb/views.py

```
from django.shortcuts import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'login.html')
```

3.templates/login.html

```
 <title>Title</title>
    <link rel="stylesheet" href="/static/commons.css">
    <style>
        label{
            width: 80px;
            text-align: right;
            display: inline-block;
        }
    </style>
</head>
<body>
    <form action="/login" method="post">
        <p>
            <label for="username">用户名</label>
            <input id="username" type="text"/>
        </p>
        <p>
            <label for="password">密码:</label>
            <input id="password" type="text" />
            <input type="submit" value="提交" />
        </p>
    </form>
    <script src="/static/jquery.js"></script>
</body>
```

4.settings.py

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]    ####
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

```

#### django验证用户密码是否正确

1.settings.py

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',   注释掉
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

2.templates/login.html

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/commons.css">
    <style>
        label{
            width: 80px;
            text-align: right;
            display: inline-block;
        }
    </style>
</head>
<body>
    <form action="/login" method="post">
        <p>
            <label for="username">用户名</label>
            <input id="username" name="user" type="text"/>
        </p>
        <p>
            <label for="password">密码:</label>
            <input id="password" name="pwd" type="password" />
            <input type="submit" value="提交" />
            <span style="color: red;">{{ error_msg }}</span>  ####
        </p>
    </form>
    <script src="/static/jquery.js"></script>
</body>
```

3.cmdb/views.py

```
def login(request):

    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == "root" and pwd == "123":
            return redirect('http://www.baidu.com')
        else:
            error_msg = "用户名或密码错误"

    return render(request,'login.html', {'error_msg': error_msg})

```

#### input添加示例

1.urls.py

```
urlpatterns = [
    url(r'home',views.home),
```

2.templates/home.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body style="margin: 0">
    <div style="height: 48px;background-color: #dddddd"></div>
    <div>
        <form action="/home" method="post">
            <input type="text" name="username" placeholder="用户名"/>
            <input type="text" name="email" placeholder="邮箱"/>
            <input type="text" name="gender" placeholder="性别"/>
            <input type="submit" value="添加"/>
        </form>
    </div>
    <div>
        <table>
            {% for row in user_list %}
                <tr>
                    <td>{{ row.username }}</td>
                    <td>{{ row.gender }}</td>
                    <td>{{ row.email }}</td>
                </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
```

3.cmdb/views.py

```
USER_LIST = [
    {'username': 'zhang','email': 'zhang@163.com','gender': 'man'},
    {'username': 'li','email': 'li@163.com','gender': 'man'},
    {'username': 'wang','email': 'wang@163.com','gender': 'man'}
]
def home(request):
    if request.method == "POST":

        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username': u, 'email': e,'gender': g}
        USER_LIST.append(temp)
    return render(request,'home.html',{'user_list': USER_LIST})
```

