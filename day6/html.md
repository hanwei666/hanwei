
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

