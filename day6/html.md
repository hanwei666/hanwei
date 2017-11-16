
# html

1.一套规则，浏览器认识的规则

2.开发者：

​             学习HTML规则

​             开发后台程序

​                            写HTML文件(充当模板的作用)

​                             数据库获取数据，然后替换到html文件的指定位置(web框架)

3.本地测试

​           找到文件路径，直接浏览器打开

​            pycharm打开测试

4.编写html文件

​            doctype对应关系

​             html标签，标签内部可以写属性 ===>  只能有一个

 ```
<!DOCTYPE html>           <!-- 定义规则(有多个版本)-->
<html lang="en">          <!--标签和标--签属性 -->
<head>                     <!--头 -->
    <meta charset="UTF-8">
    <title>han</title>
</head>
<body>                       <!--身 -->
     <a href="http://www.phicomm.com">斐讯</a>   <!--定义超链接 -->
</body>
</html>
 ```



​   5.input系列

​       input   type='text'                  - name属性，value='张三'

​       input   type='password'        -name属性    value='张三'

​       input type='submit'              -value=‘提交’   提交按钮,表单

​       input type='button'               -value='登录'   按钮

​        input type='radio'                 -单选框 value, checked='checked',name 属性(name相同侧互诉)

​        input type='checkbox'          -复选框 value checked='checked',name属性 (批量获取数据)

​        input type='file'                     -依赖form表单的一个属性 enctype='multipart/form-data' 

​         input type='reset'                -重置       


```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>斐讯</title>
</head>
<body>
     # <form action="http://localhost:8888/index" method="POST> POST方法
     <form enctype="multipart/form-data">
         <div>
              请输入用户名
             <input type="text" name="user" />
             请输入密码
             <input type="password" name="pass" />
             <input type="button" value="登录1"/>
             <input type="submit" value="登录2"/>
             <p> 请选择性别：</p>
             男: <input type="radio" name="gender" value="1" />
             女：<input type="radio" name="gender" value="2" checked="checked"/>
             未知：<input type="radio" name="gender" value="3"/>
             <p>爱好</p>
             篮球：<input type="checkbox" name="favor" value="1"/>
             足球：<input type="checkbox" name="favor" value="2" checked="checked"/>
             台球: <input type="checkbox" name="favor" value="3"/>
             <p>技能</p>
             撩妹：<input  type="checkbox" name="skill" checked="checked"/>
             写代码：<input type="checkbox" name="skill" />
             <p>上传文件</p>
             <input type="file" name="fname"/>
         </div>
         <input type="submit" value="提交"/>
         <input type="reset" value="重置"/>
     </form>
</body>
</html>
```



```
import tornado.ioloop
import tornado.web
#pip install tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u = self.get_argument('user')
        p = self.get_argument('pass')
        if u == 'abc' and p == '123':
            self.write('OK')
        else:
            self.write('NO')

    def post(self,*args,**kwargs):
        u = self.get_argument('user')
        p = self.get_argument('pass')
        print(u,p)
        self.write('POST')
application = tornado.web.Application([
    (r"/index",MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
```



6.select标签         -name，内部option value,提交到后台size,muiltip

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
      <form enctype="multipart/form-data">
          <div>
              #框内输入多行
              <textarea name="meno" >asdasdasd</textarea>
              
              #设置框大小
              <select name="ctiy" size="5" multiple="multiple">
                  <option value="1">北京</option>
                  <option value="2">上海</option>
                  #默认选中
                  #分组</optgroup lable=河南省>_</optgroup>
                  <option value="3" selected="selected">南京</option> 
                  <option value="4">深圳</option>
              </select>
          </div>
      </form>

</body>
</html>
```



7.a标签

- 跳转

- 锚    href='#某个标签的id' 标签的id不允许重复

  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  </head>
  <body>
       <!--超链接，target="_blank在新窗口打开-->
       <!--<a href="http://www.baidu.com" target="_blank">百度</a>-->
       <a href="#i1">第一章</a>
       <a href="#i2">第二章</a>
       <a href="#i3">第三章</a>

       <div id="i1" style="height:600px;">第一章内容</div>
       <div id="i2" style="height:600px;">第二章内容</div>
       <div id="i3" style="height:600px;">第三章内容</div>
  </body>
  </html>
  ```

  ​


8.img标签

```
<body>
      #图片超链接
      <a href="http://www.baidu.com"> 
      #设置图片，名字，图片大小。
      <img src="a.jpg" title="测试" style="height:200px;width:200px;" alt="测">
      </a>
</body>
```

9.列表ul,ol,dl,dd标签

```
<body>
     <ul>
         <li>abc</li>
         <li>abc</li>
         <li>abc</li>
     </ul>

     <ol>
         <li>abc</li>
         <li>abc</li>
         <li>abc</li>
     </ol>

     <dl>
         <dt>123</dt>
         <dd>abc</dd>
         <dd>abc</dd>
     </dl>
</body>
```

10.table标签

```
<body>
      <table border="1">  #网格
          <tr>#换行
              <td>主机名</td>
              <td>端口</td>
              <td>操作</td>
          </tr>
          <tr>
              <td>1.1.1.1</td>
              <td>80</td>
              <td>
                  <a href="s9.html">查看详细信息</a>
                  <a href="$">修改</a>
              </td>
          </tr>
          <tr>
               <td>1.1.1.1</td>
               <td>80</td>
              <td>第二行，第三列</td>
          </tr>
      </table>
</body>
```

table 标准写法和合并单元格

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<table border="1">
    <thead>       #表头
    <tr>
        <th>表头1</th>
        <th>表头2</th>
        <th>表头3</th>
        <th>表头4</th>
    </tr>
    </thead>
    <tbody>       #表身
    <tr>
        <td>1</td>
        <td colspan="3">2</td>  #横合并单元格
    </tr>
    <tr>
        <td rowspan="2">1</td> #竖合并单元格
        <td>2</td>
        <td>3</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2</td>
        <td>3</td>
        <td>4</td>
    </tr>
    </tbody>
</table>
<body>

</body>
</html>
```
11.id选择器

```
<body>
  <fieldset> 加框
      <label for="username">用户名:</label>
      <input id="username" type="text" name="user"/>
      <br />
      <label for="pwd">密码:</label>
      <input id="pwd" type="text" name="user"/>
  </fieldset> 加框
</body>
```
12.写在head里面，style标签中写样式

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
          #i3{
             background-color: #660033;
             height;48px;
             }
           #i2{
             background-color: #66FF99;
             height;48px;
             }
      </style>
</head>
<body>
      <div style="background-color: #2459a2;height;48px;">ff</div>
      <div id="i3">test1</div>
      <div id="i2">test1</div>

</body>
```

12.class选择器

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
          .c1{
             background-color: #660033;
             height;48px;
             }
      </style>
</head>
<body>
      <div style="background-color: #2459a2;height;48px;">ff</div>
      <div class="c1">test1</div>
      <div class="c1">test1</div>

</body>
```

13.标签选择器

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
          div{
             background-color: #660033;
             height;48px;
             }
      </style>
</head>
<body>
      <div style="background-color: #2459a2;height;48px;">ff</div>
      <p style="background-color: #FF3399;height;48px;">abc,abc</p>
      <div class="c1">test1</div>
      <div class="c1">test1</div>

</body>
```

14.层级选择器

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
          .c1{
             background-color: #660033;
             height;48px;
             }
          .c2{
             background-color: #66CC99;
             height;48px;
             }
          div span{
             background-color: #6600CC;
             height;48px;
             }
      </style>

</head>
<body>
      <!--<div style="background-color: #2459a2;height;48px;">ff</div>-->
      <!--<p style="background-color: #FF3399;height;48px;">abc,abc</p>-->
      <!--<div class="c1">test11</div>-->
      <div class="c2">test12
          <span>test2</span>
          <span>test3</span>
      </div>
</body>
```

15.组合选择器

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
          #i1,#i2{
             background-color: #660033;
             height;48px;
             }
      </style>

</head>
<body>
      <div id="i1">test11</div>
      <div id="i2">test12</div>
</body>
```

16.属性选择器

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
           input[type='text']{ width:100px; height:200px;}
    </style>
</head>
<body>
      <input type="text">
      <input type="password">
</body>
```