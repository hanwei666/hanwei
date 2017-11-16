
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


