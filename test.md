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

