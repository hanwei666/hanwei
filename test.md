### 布局1

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
        position: fixed;
        top:48px;
        bottom:0;
        left:0;
        width:200px;
        background-color: red;

        }
        .c2{
        position: fixed;
        top: 48px;
        bottom: 0;
        left: 200px;
        right: 0;
        background-color: #FF9900;
        overflow: auto;
        }
    </style>
</head>
<body style="margin:0 auto;">
      <div style="height:48px;background-color:#dddddd;"></div>
      <div class="c1"></div>
      <div class="c2">
          <div>test</div>
          <div>test</div>
      <div>    
```



### 布局2

如果是p标签请去掉背景色 外面套div标签在加背景颜色

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
        position: absolute;
        top:48px;
        bottom:0;
        left:0;
        width:200px;
        background-color: red;

        }
        .c2{
        position: absolute;
        top: 48px;
        bottom: 0;
        left: 200px;
        right: 0;
        background-color: #FF9900;
        overflow: auto;
        }
    </style>
</head>
<body style="margin:0 auto;">
      <div style="height:48px;background-color:#dddddd;"></div>
      <div class="c1"></div>
      <div class="c2">
          <div>test</div>
          <div>test</div>
          <div>test</div>
      <div>   
```

### 鼠标放到头像显示资料

```
head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .left{
        float:left;
        }
        .right{
        float:right;
        }
        .logo{
        background-color: #787878;
        height:48px;width:200px;
        line-height:48px;
        text-align:center;
        }

        .user{
        height:48px;
        width:150px;
        background-color: #009933;
        position:relative;
        }

        .c1{
        position: absolute;
        left:0;
        width:200px;
        top:48px;
        bottom:0;
        background-color:#FF9900;
        }

        .c2{
        position: absolute;
        top:48px;
        bottom:0;
        right:0;
        left:200px;
        background-color: red;
        overflow: auto;
        z-index: 9;

        }
        .user:hover{                              ####
        background-color: #00CCCC;
        }
        .user .ww{                                ####
        position:absolute;
        background-color:#660066;
        top:48px;right:50px;
        z-index:20;
        width:120px;
        display: none;
        }
        .user .ww a{                              ####
        display: block;
        }

        .user:hover .ww{                         ####
        display:block;
        }
    </style>
</head>
<body style="margin:0 auto;">
      <div style="height:48px;background-color:#dddddd;">
          <div class="logo left">
              PHICOMM
          </div>
          <div class="user right">
              <a>
                  <img style="height:40px;width:40px;margin-top:4px;border-radius:50%;" src="h.png">
              </a>
              <div class="ww">
                  <a>资料</a>
                  <a>注销</a>
              </div>
          </div>
      </div>
      <div style="clear:both"></div>
      <div class="c1"></div>
      <div class="c2"></div>

</body>
</html>
```

### 布局3

http://fontawesome.io/icons/

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="Font-Awesome-master/css/font-awesome.min.css"/>
    <style>
        .left{
        float:left;
        }
        .right{
        float:right;
        }
        .c1{
        height:48px;
        background-color: #dddddd;
        }
        .c2{
        padding-right:20px;
        }
        .c3{
        display: inline-block;
        padding: 4px; 7px;
        background-color:red;
        border-radius: 50%;
        }
    </style>
</head>
<body style="margin:0 auto;">
       <div class="c1">
           <div class="c2 right">
               <i class="fa fa-envelope-o" aria-hidden="true"></i>
           </div>
           <div class="c2 right">
               <i class="fa fa-commenting" aria-hidden="true"></i>
               <span class="c3">5</span>
           </div>
       </div>
</body>
</html>
```

### js函数

```
普通函数
   function func(){
     
   }

匿名函数
   function func(arg){
   
     return arg+1
   }
   
   steInterval("func()",5000);
   
   setInterval(function()){
       console.log(123);
   },5000)
   
  自执行函数(创建函数并且自动执行)；
    function func(arg){
      console.log(arg);
    }
    func(1)
    
    (function(arg){
      console.log(arg);
    })(1)
```

### 序列化

```
JSON.stringify()  将对象转换为字符串
JSON.pares()      将字符串转换为对象类型
```

### 转义

```
客户端(cookie) => 服务端
将数据经过转义后，保存在cookie

url="https://www.sogou.com/web?query=理解"
encodeURI(url)
"https://www.sogou.com/web?query=%E7%90%86%E8%A7%A3"
decodeURI(url)
encodeURIComponent(url)

```

eval

```
python：
      val = eval(表达式)
            exec(执行代码)
            
       JavaSCript:
             eval

```

### 时间

```
Date类

var d = new Date()

d.getxxx 获取
d.setXXX 设置



var d = new Date()
undefined
d
Sat Dec 30 2017 14:53:53 GMT+0800 (中国标准时间)
n = d.getMinutes() + 4
57
d.setMinutes(n)
1514617073984
d
Sat Dec 30 2017 14:57:53 GMT+0800 (中国标准时间)
```

### 作用域

- JavaScript:    以函数作为作用域
- 函数的作用域在函数未被调用之前，已经创建
- 函数的作用域存在作用域链，并且也是在未被调用之前创建

```
xo = "alex"
"alex"
"alex"

function func(){
    var xo = ‘eric’;
    function inner(){
      console.log(xo);
    
   }
   return inner;
}
var ret = func()
ret()
```



### 原型

```
function Foo(){
  this.name = n;
}
# F00的原型
Foo.prototype = {
  'sayName': function(){
    console.log(this.name)
  }
}

obj1 = new Foo('we');
obj.satName()

obj2 = new Foo('wee');
```

### dom

```
获取ID
obj = document.getElementById('i1');

innerText 
获取标签内容
obj.innerText 
修改
obj.innerText = "张三"
obj.innerText = "<a herf='http://www.baidu.com'>百度</a>";

innerHTML
获取标签
obj.innerHTML 
修改
obj.innerHTML = "张三"
obj.innerHTML = "<a href='http://www.baidu.com'>百度</a>";
```

```
修改pinut内容

obj=document.getElementById('i2')
<input type="text" id="i2">
obj.value
""
obj.value = "abc"
"abc"
```

```
<select id="i3">
             <option value="11">上海1</option>
             <option value="12">上海2</option>
             <option value="13">上海3</option>
         </select>
         
  obj = document.getElementById('i3');
  obj.value
  obj.value = "13"
```

### input标签（框内字示例）

```
<body >
     <div style="width: 600px;margin: 0 auto;">
         <input id="i1" onfocus="Focus();" onblur="Blur();" type="text" value="请输入关键字">
     </div>

<script>
    function Focus(){
        var tag = document.getElementById('i1');
        var val = tag.value;
        if(val == "请输入关键字"){
             tag.value = "";
        }
    }
    function Blur(){
          var tag = document.getElementById('i1');
          var val = tag.value;
          if(val.length == 0){
               tag.value = "请输入关键字";
          }
    }
</script>
</body>
</html>
```

### 样式操作

```
obj= document.getElementById('i1');

obi.className = "c1 c2";

获取name
obj.className
obj.classList

添加样式
obj.classList.add('c3')

删除样式
obj.classList.remove('c2')


```

直接设置style值

```
obj= document.getElementById('i1');

obj.style.color = 'red';

obj.style.fontSize = '16px';
obj.style.backgroundColor = 'red';

```

### 属性操作

```
attributes        查看
getAttribute      设置
removeAttribute   删除

obj = document.getElementById("i1")

设置value
obj.setAttribute('value','nnnn');

obj

查看所有属性
obj.attributes
```



#### 添加标签

```
<body >
     <input type="button" onclick="AddEle();" value="+" />
     <input type="button" onclick="AddEle2();" value="+" />
<div id="i1">
    <p><input type="text" /></p>
</div>
<script>
    function AddEle(){
         var tag = "<p><input type='text' /></p>";
         document.getElementById('i1').insertAdjacentHTML("beforeEnd",tag);
    }

    function AddEle2(){

           var tag = document.createElement('input');
           tag.setAttribute('type','text');
           tag.style.fontSize = '16px';
           tag.style.color = 'red';

           var p = document.createElement('p');
           p.appendChild(tag);

           document.getElementById('i1').appendChild(p);
    }

</script>
</body>
```

### 提交事件

任何标签通过dom都可以提交

```
<body >
    <form id="f1" action="http://www.phicomm.com">
        <input type="text" />
        <input type="submit" value="提交"/>
        <a onclick="submitForm();">提交</a>
    </form>
<script>
    function submitForm(){
       document.getElementById('f1').submit()
    }
</script>
</body>
```

### 删除提示

 var v = confirm('真的要删除吗？')  v:true false

```
<body >
    <form id="f1">
        <input type="text" />
        <a onclick="submitForm();">删除</a>
    </form>
<script>
    function submitForm(){
           var v = confirm('真的要删除吗？')
           console.log(v);
    }

</script>
</body>
```

重定向

```
location.href
location.href = ""  重定向 跳转
location.reload()   页面刷新
location.href = loaction.href    

```

清楚定时

```
var ol = setInterval(function()){},5000)
clearInterval(ol);                 #清楚

var o2 = setTimeout(function(){},50000);  #执行一次秦楚
clearTimeout(o2);                         #清楚




<body >
     <div id="status"></div>
     <input type="button" value="删除" onclick="DeleteEle();"/>

<script>
    function DeleteEle(){
         document.getElementById('status').innerText = "已删除";
         setTimeout(function (){
                document.getElementById('status').innerText = "";
         }, 3000);
    }
</script>
</body>
```

### 动作(js)  样式(css)  结构(html) 相互独立

作用域示例

```
<input id='i1' type='button' ondbclick='ClickOn(this)'>
```



```
<body>
    <table border="1" width="300px;">
        <tr><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>1</td><td>2</td><td>3</td></tr>
    </table>
<script>
    var myTrs = document.getElementsByTagName("tr");
    var len = myTrs.length;
    for(var i=0;i<len;i++){
        myTrs[i].onmouseover = function(){
              this.style.backgroundColor = "red";
        }

         myTrs[i].onmouseout = function(){
              this.style.backgroundColor = "";
        }
    }
</script>
</body>
```

###事件

```
onabort	    图像加载被中断	
onblur	    元素失去焦点	
onchange	用户改变域的内容	
onclick	    鼠标点击某个对象	
ondblclick	鼠标双击某个对象	
onerror	    当加载文档或图像时发生某个错误	
onfocus	    元素获得焦点	
onkeydown	某个键盘的键被按下	
onkeypress	某个键盘的键被按下或按住	
onkeyup	    某个键盘的键被松开	
onload	    某个页面或图像被完成加载	
onmousedown	某个鼠标按键被按下	
onmousemove	鼠标被移动	
onmouseout	鼠标从某元素移开	
onmouseover	鼠标被移到某元素之上	
onmouseup	某个鼠标按键被松开	
onreset	    重置按钮被点击	
onresize	窗口或框架被调整尺寸	
onselect	文本被选定	
onsubmit	提交按钮被点击	
onunload	用户退出页面
```

### 绑定事件第三种

```
mymain.addEventListener("click",function(){console.log("main")},true); 
true   捕捉模式(从上到下)
false  冒泡模式(从下到上)
```



```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #main{
        background-color: red;
        width:300px;
        height:400px;
    }
        #content{
        background-color:pink;
        width:200px;
        height:300px;
        }
    </style>
</head>
<body>
     <div id="main">
         <div id="content"></div>
     </div>

<script>
    var mymain = document.getElementById("main");
    var mycontent = document.getElementById("content");
    mymain.addEventListener("click",function(){console.log("main")},true);
    mycontent.addEventListener("click",function(){console.log("content")},true);
</script>
</body>
```

<https://www.jianshu.com/p/3cb5c6f2421c/>



#### jquery

<http://jquery.cuishifeng.cn/>

<http://www.oyksoft.com/soft/12273.html>

```
1.id

<body>
   <div id="i1">test</div>

<script src="jquery.js"></script>
<script>
    $("#i1")
</script>

2.标签
$(".c1")
#("a")
$("#i1,a, .c1")

3.层级
$("#i1>a") 子孙
$("#i1 a") 儿子

4.属性
<a han="123">ttt</a>
$('[han="123"]')
$('[han]')

$("input[type='text']")
<input type="text">
```

### 多选反选示例

- $('#tb :checkbox').prop('checked');              获取值

- $('#tb :checkbox').prop('checked',true);      设置值

- jquery方法内置循环：$('#tb:checkbox').xxx

- $('#tb:checkbox').each(function(k){

  ​        k当前索引

  ​        this,DOM,当前循环的元素 $(this)

     })

  var v = 条件 ？真值：假值

```
<body>

      <input type="button" value="全选" onclick="checkALL();" />
      <input type="button" value="取消" onclick="cancleALL()" />
      <input type="button" value="反选" onclick="reverseALL()" />


      <table border="1">
          <thead>
               <tr>
                   <th>选项</th>
                   <th>IP</th>
                   <th>PORT</th>
               </tr>
          </thead>
          <tbody id="tb">
             <tr>
                 <td><input type="checkbox" /></td>
                 <td>192.168.1.1</td>
                 <td>80</td>
             </tr>
             <tr>
                 <td><input type="checkbox" /></td>
                 <td>192.168.1.1</td>
                 <td>80</td>
             </tr>
             <tr>
                 <td><input type="checkbox" /></td>
                 <td>192.168.1.1</td>
                 <td>80</td>
             </tr>
          </tbody>
      </table>

<script src="jquery.js"></script>

<script>
    function checkALL(){
        $('#tb :checkbox').prop('checked',true);
    }
    function cancleALL(){
        $('#tb :checkbox').prop('checked',false);
    }
    function reverseALL(){
        $(':checkbox').each(function(k){
            //this，代指当循环的每一个元素
            // if(this.checked){
            //     this.checked = false;
            // }else{
            //     this.checked = true;
            // }

            // if($(this).prop('checked')){
            //     $(this).prop('checked',false);
            // }else{
            //     $(this).prop('checked',true);
            // }

            var v = $(this).prop('checked')?false:true;
            $(this).prop('checked',v);

            })
    }
</script>

```







