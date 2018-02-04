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
	Model    View    Controller
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

