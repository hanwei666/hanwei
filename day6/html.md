position:fixed;

a.  fie ---> 固定再页面窗口

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .pg-hesder{
        height: 48px;
        background-color: black;
        color: #dddddd;
        position: fixed;
        top:0;
        right:0;
        left:0;
        }
        .pg-body{
        background-color:#dddddd;
        height:5000px;
        margin-top:50px;
        }
    </style>
</head>
<body>
      <div class="pg-hesder">头部</div>
      <div class="pg-body">内容</div>
</body>
</html>
```

b.  relative + absolute   固定每个位置或固定标签里面 

```
<body>
      <div style="position: relative;
      width:500px;height:200px;
      border:1px solid red;
      margin: 0 auto;">
          <div style="position: absolute;
          left:0;bottom:0;width: 50px;
          height:50px;
          background-color: 
          black;"></div>
      </div>
</body>
```

c. z-index:9 层级 ---- opacity:0.5 透明度

```
<body>
     <div style="z-index:10;position: fixed;
     top: 50%;left: 50%;
     margin-left: -250px;margin-top:
     -200px;background-color:
     white;height:400px;
     width:500px;">
         <input type="text" />
         <input type="text" />
     </div>
     <div style="z-index:9;position: fixed;background-color:black;
     top:0;
     bottom:0;
     right:0;
     left:0;
     opacity:0.5;
     "></div>
     <div style="height:5000px;background-color: green;">
         test
     </div>
</body>
```

####超过范围出现下拉框

overflow:hidden

超过范围不显示
overflow:hidden

<body>

     <div style="height: 100px;width: 200px;overflow:auto">
         <img src="88.jpg">
     </div>
     <div style="height: 100px;width: 200px;overflow:hidden">
         <img src="88.jpg">
     </div>

</body>

#### hover 当鼠标放在标签上面显示颜色

<head>

    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .pg-header{
        position: fixed;
        right: 0;
        left: 0;
        top: 0;
        height: 48px;
        background-color: #2459a2;
        line-height: 48px;
        }
        .pg-body{
        margin-top: 50px;
        }
        .w{
        width: 980px;
        margin: 0 auto;
        }
        .pg-header .menu{
        display: inline-block;
        padding: 0 10px 0 10px;
        color: white;
        }
        .pg-header .menu:hover{
        background-color: red;
        }
    </style>
</head>
<body>
     <div class="pg-header">
         <div class="w">
             <a class="logo">LOGO</a>
             <a class="menu">全部</a>
             <a class="menu">42区</a>
             <a class="menu">段子</a>
             <a class="menu">1024</a>
         </div>
         <div class="pg-body">
             <div class="w">test</div>
         </div>
     </div>
</body>
</html>

####图片设置背景,background-image

默认复制 x,y方向

```
repeat-y 复制 y 方向
```

```
repeat-x 复制 x 方向
```

```
no-repeat 不复制
```

```
<body>
   <div style="background-image: url('88.jpg');
   background-repeat:no-repeat;height: 500px;">
       test
   </div>
```

#### 移动图片background-position

```
<body>
   <div style="background-image: url('88.jpg');
   background-repeat:no-repeat;
   height: 350px;width:300px;
   border:1px solid red;
   background-position-x:-25px;
   background-position-y:-5px;
   ">
   </div>
</body>
```

简写background:transparent

```
<div style="
 height: 350px;width:300px;
background:transparent url('88.jpg')
no-repeat
scroll 5% 50%;
border:1px solid red;
">
</div>
```

登录框 设置图片背景

```
<body>
   <div style="height: 35px;width: 370px;position: relative;">
       <input type="text" style="height:
       35px;width: 370px;padding-right: 30px;">
       <span style="position:absolute;
       right: 60px;top: 10px;
       background-image: url('a.png'); height: 16px;
       width: 20px;display: inline-block;
       margin-right: -80px;
       "></span>
   </div>
</body>
```




#### js

<head>

    <meta charset="UTF-8">
    <title>Title</title>
    <script>
        alert(123);
    </script>
</head>



a.js
alert(123);


<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src='test.js'> </script>
</head>



a = "alex"

获取索引位置
a.charAt(0)

获取开始到结束位置
a.substring(1,3)

获取长度
a.length



charAt(0),ontent.substring,setInterval


<body>
     <div id="i1">欢迎老男孩指导</div>
     <script>
         function func(){
         //根据ID获取指定标签的内容，定于局部变量
         var tag = document.getElementById('i1');
         //获取标签内容的内容
         var content = tag.innerText;
         var f = content.charAt(0);
         var l = content.substring(1,content.length);
         var new_content = l + f;
         tag.innerText = new_content;
         }
         setInterval('func()',500);
     </script>
</body>
</html>



#### 字符串

```
obj.length                           长度
 
obj.trim()                           移除空白
obj.trimLeft()
obj.trimRight)
obj.charAt(n)                        返回字符串中的第n个字符
obj.concat(value, ...)               拼接
obj.indexOf(substring,start)         子序列位置
obj.lastIndexOf(substring,start)     子序列位置
obj.substring(from, to)              根据索引获取子序列
obj.slice(start, end)                切片
obj.toLowerCase()                    大写
obj.toUpperCase()                    小写
obj.split(delimiter, limit)          分割
```



#### 布尔值

```
==      比较值相等
!=       不等于
===   比较值和类型相等
!===  不等于
||        或
&&      且
```

#### 数组

```
JavaScript中的数组类似于Python中的列表

常见功能：

obj.length          数组的大小
 
obj.push(ele)       尾部追加元素
obj.pop()           尾部获取一个元素
obj.unshift(ele)    头部插入元素
obj.shift()         头部移除元素
obj.splice(start, deleteCount, value, ...)  插入、删除或替换数组的元素
                    obj.splice(n,0,val) 指定位置插入元素
                    obj.splice(n,1,val) 指定位置替换元素
                    obj.splice(n,1)     指定位置删除元素
                    
obj.splice(1,1,"a")  删除索引1删除1个插入a

obj.slice( )        切片
obj.reverse( )      反转
obj.join(sep)       将数组元素连接起来以构建一个字符串
obj.concat(val,..)  连接数组
obj.sort( )         对数组元素进行排序
```

##### 循环数组

```
var a=["k1","k2"]

for(var item in a){
    console.log(a[item]);
}
 k1
 k2
```

##### 字典

```
var a={'k1':'v1','k2':'v2'}

for(var item in a){
    console.log(a[item],item);
}

v1 k1
v2 k2

```



##### for循环

````
for(var i=0;i<10;i+=1){
    console.log(i)
}


var a = [11,22,33,55]
for(var i=0;i<a.length;i+=1){
    console.log(i)
}

不支持字典循环
````

##### if体哦见语句

```
if(条件){
  
}else if(条件){
  
}else if(条件){
  
}else{
  
}
```

##### 函数

```
function test(a,b,c){
}
test(1,2,3)
```



##### 元素查找

直接查找

````
document.getElementById             根据ID获取一个标签
document.getElementsByName          根据name属性获取标签集合
document.getElementsByClassName     根据class属性获取标签集合
document.getElementsByTagName       根据标签名获取标签集合
````

间接查找

```
parentNode          // 父节点
childNodes          // 所有子节点
firstChild          // 第一个子节点
lastChild           // 最后一个子节点
nextSibling         // 下一个兄弟节点
previousSibling     // 上一个兄弟节点
 
parentElement           // 父节点标签元素
children                // 所有子标签
firstElementChild       // 第一个子标签元素
lastElementChild        // 最后一个子标签元素
nextElementtSibling     // 下一个兄弟标签元素
previousElementSibling  // 上一个兄弟标签元素
```

操作

```
<body>
    <div id="i1">我是i1</div>
    <a>test1</a>
    <a>test2</a>
    <a>test3</a>
</body>

document.getElementById('i1')   找到标签
document.getElementById('i1').innerText  获取内容
document.getElementById('i1').innerText = '新内容'  修改


document.getElementsByTagName('a')        取a标签
document.getElementsByTagName('a')[1]     取第一个a标签
document.getElementsByTagName('a')[1],innerText = 666;  修改

```

#####for循环修改标签

```
tags=document.getElementsByTagName('a');
for(var i=0;i<tags.length;i++){tags[i],innerText=777;}

```

##### 弹出框

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .hide{
             display: none;
        }
        .c1{
           position: fixed;
           left: 0;
           top: 0;
           right: 0;
           bottom: 0;
           background-color: black;
           opacity: 0.6;
           z-index: 9;
        }
        .c2{
        width: 500px;
        height: 400px;
        background-color: white;
        position: fixed;
        left: 50%;
        top: 50%;
        margin-left: -250px;
        margin-top: -200px;
        z-index: 10;
        }
    </style>
</head>
<body style="margin: 0;">

     <div>
         <input type="button" value="添加"  onclick="ShowModel();"/>
         <table>
             <thead></thead>
                    <tr>
                        <th>主机</th>
                        <th>端口</th>
                    </tr>
             <tbody>
                  <tr>
                      <td>1.1.1.3</td>
                      <td>190</td>
                  </tr>
             </tbody>
         </table>
     </div>
     
     <!--遮罩层-->
     <div id="i1" class="c1 hide">
     </div>
     <!--弹出框-->
     <div id="i2" class="c2 hide">
         <p><input type="text" /></p>
         <p><input type="text" /></p>
         <p>
             <input type="button" value="取消" onclick="HideModel()"/>
             <input type="button" value="确认"/>
         </p>

     </div>

     <script>
        function ShowModel(){
        document.getElementById('i1').classList.remove('hide');
        document.getElementById('i2').classList.remove('hide');
        }
        function HideModel(){
        document.getElementById('i1').classList.add('hide')
        document.getElementById('i2').classList.add('hide')
        }
    </script>
</body>
```

##### 全选，反选。取消

```
<body style="margin: 0;">

       <div>
           <input type="button" value="添加" onclick="ShwModel();" />
           <input type="button" value="全选" onclick="ChooseAll();" />
           <input type="button" value="取消" onclick="CancleAll();" />
           <input type="button" value="反选" onclick="ReverseAll();" />

           <table>
               <thead>
                      <tr>
                          <th>选择</th>
                          <th>主机名</th>
                          <th>端口</th>
                      </tr>
               </thead>

               <tbody id="tb">
               <tr>
                   <td><input type="checkbox" /></td>
                   <td>1.1.1.1</td>
                   <td>190</td>
               </tr>
               <tr>
                   <td><input type="checkbox" /></td>
                   <td>1.1.1.3</td>
                   <td>193</td>
               </tr>
               </tbody>
           </table>
       </div>

       <script>
           function ChooseAll(){
               //获取id
               var tbody = document.getElementById('tb');
               //获取孩子
               var tr_list = tbody.children;
               //循环孩子
               for(var i=0;i<tr_list.length;i++){
                   var current_tr = tr_list[i]
                   var checkbox = current_tr.children[0].children[0];
                   //修改
                   checkbox.checked = true;
               }
           }

           function CancleAll(){
                var tbody = document.getElementById('tb');

                var tr_list = tbody.children;
                for(var i=0;i<tr_list.length;i++){

                    var current_tr = tr_list[i];
                    var checkbox = current_tr.children[0].children[0];
                    checkbox.checked = false;
                }
           }

           function ReverseAll(){
                var tbody = document.getElementById('tb');

                var tr_list = tbody.children;
                for(var i=0;i<tr_list.length;i++){
                    var current_tr = tr_list[i];
                    var checkbox = current_tr.children[0].children[0];

                    if(checkbox.checked){
                        checkbox.checked = false;
                    }else{
                        checkbox.checked = true;
                    }
                }
           }

       </script>
</body>
```

##### 左测菜单

```
head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
          .hide{
            display: none;
        }
        .item .header{
            height: 35px;
            background-color: #2459a2;
            color: white;
            line-height: 35px;
        }
    </style>
</head>
<body>
     <div style="height: 48px;"></div>
     <div style="width: 300px;">
         <div class="item">
             <div id='i1' class="header" onclick="ChangeMenu('i1');">菜单1</div>
             <div>
                 <div>内容1</div>
                 <div>内容2</div>
                 <div>内容3</div>
             </div>
         </div>
         <div class="item">
             <div id='i2' class="header" onclick="ChangeMenu('i2');">菜单2</div>
             <div class="hide">
                 <div>内容1</div>
                 <div>内容2</div>
                 <div>内容3</div>
             </div>
         </div>
         <div class="item">
             <div id='i3' class="header" onclick="ChangeMenu('i3');">菜单3</div>
             <div class="hide">
                 <div>内容1</div>
                 <div>内容2</div>
                 <div>内容3</div>
             </div>
         </div>
     </div>

<script>
    function ChangeMenu(nid){
        var current_header = document.getElementById(nid);

        var item_list = current_header.parentElement.parentElement.children;

        for(var i=0;i<item_list.length;i++){
            var current_item = item_list[i]
            current_item.children[1].classList.add('hide');
            }
            current_header.nextElementSibling.classList.remove('hide');

    }
</script>
</body>
```

#### 总结

````
css 补充
      - position
	  - background
	  - hover
	  - overflow
	  - z-index
	  - opacity
	  
	  
JavaScript:
    局部变量 var
	基本数据类型
	     数字
		 字符串
		 数组
		 字典
		 布尔值
		 for循环
		 
		 if条件语句
		    ==
			!=
			===
			!==
		    ||
			&&
Dom
    招标签
        - 直接找 $('#id') $('c1').siblings()
        - 简介找
    操作：
	    innerText
		checkbox:
		     checked
	    className
		classList
		
	事件：
	     <div onclick='函数(123)'><div>
		 
	定时器
         setInterval('函数()',4000)

    其他：
         
         alert()
         console.log()

实例：
     亲临指导
     多选
     模态对话框
     左侧菜单
     返回顶部	 
````

