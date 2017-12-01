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