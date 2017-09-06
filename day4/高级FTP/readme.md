高级FTP
       
FTP/
├── auth       用户注册目录
│   ├── admin
│   ├── han
│   ├── hw
│   ├── __init__.py
│   └── zhang
├── client          客户端
│   ├── clinet.py
│   └── test.txt
├── conf            配置文件
│   ├── __pycache__
│   │   ├── settings.cpython-35.pyc
│   │   └── settings.cpython-36.pyc
│   └── settings.py
├── home            用户家目录
│   ├── admin
│   │   ├── a
│   │   │   └── a.txt
│   │   └── tets.txt
│   ├── han
│   │   └── test.txt
│   ├── hw
│   └── zhang
└── src
    └── server.py   服务端

       



使用说明：
         启动服务      \FTP\src\server.py
         启动客户端    \FTP\client\clinet.py 



         1.启动客户--->后选择登陆 --->输入账号admin 密码admin 
         2.每个用户只可以下载自己家目录的文件            admin----->家目录路径:FTP\home\admin 
         3.问价会下载的目录  -----> FTP\client     

