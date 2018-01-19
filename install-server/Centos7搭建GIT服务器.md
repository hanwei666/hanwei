### Centos7搭建GIT服务器

1.安装git

```
yum install autoconf git
```

2.创建Gitolite用户

```
adduser git
passwd git
```

3.创建ssh公钥并将其复制到git用户

```
ssh-keygen 一路回车
```

```
cp sk.pub /home/git
source .bash_profile

su - git
mkdir ~/bin

git clone git://github.com/sitaramc/gitolite

gitolite/install -ln ~/bin
gitolite setup -pk sk.pub
```

4.

```
su - root
git clone git@192.168.80.100:gitolite-admin

```

```
ls gitolite-admin/
```

5.权限配置

```
vim gitolite-admin/conf/gitolite.conf 

@yunpan lisi zhangsan  #组和组的用户

repo gitolite-admin
    RW+     =   sk

repo testing
    RW+     =   @yunpan


repo sample
    RW+     =   @all
```

6.生成仓库

```
创建目录
mkdir /srv
cd /srv
git init --bare sample.git
chown -R git:git sample.git
```

7.不允许git用户登录

```
编辑 /etc/passwd文件

修改
git:x:1001:1001:,,,:/home/git:/bin/bash

修改为
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell
```

8.windows客户端设置

```
git config --global user.name "zhangsan"
git config --global user.email "1326921@163.com"
```

```
ssh-keygen -rsa
```

拷贝公钥id_rsa.pub到git服务器 /home/git目录

```
~/bin/gitolite setup -pk id_rsa.pub     
```

```
git clone git@192.168.80.100:/srv/sample.git 
git push origin master 


git add README 
git commit -m 'first commit'
git push origin master
```

9.最后用sourcetree打开sample目录输入git用户密码

<http://blog.51cto.com/7456193/1765879>

<http://www.linuxidc.com/Linux/2017-07/145764.htm>

<https://www.cnblogs.com/xchendevelop/articles/6568339.html>





