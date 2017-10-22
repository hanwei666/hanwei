## centos6.6安装pip9

### 1.安装依赖包

```
yum -y install gcc
yum install zlib zlib-dev  
yum install openssl
yum install openssl-devel

```

### 2.下载python2.7.10，可直接到python官网下载，并选择相应版本.

```
./configure 
make
makeinstall
```

###3.把系统自带的2.6移除（依然会保留2.6版本：/usr/bin/python2.6）

```
rm -f /usr/bin/python  
```

### 4.把python执行软连接连接到2.7

```
ln -s /usr/local/bin/python2.7 /usr/bin/python  
```

### 5.编辑yum命令，把路径指明为2.6，因为yum必须基于2.6版本

```
vi /usr/bin/yum 
```

把文件头部的#!/usr/bin/python改成#!/usr/bin/python2.6 
保存退出，yum即可正常使用。如若有其他命令、软件不能正常使用，仿照yum配置文件的修改方法，修改其配置文件即可。 
至此，更新完毕。

###6.安装setuptools，下载setuptools-18.0.1.tar.gz，解压后，进入setuptools-18.0.1，执行：

```
python setup.py install
```

###7.安装pip，下载pip-9.1.0.tar.gz，解压后进入pip-9.1.0，执行：

```
python setup.py install
```

