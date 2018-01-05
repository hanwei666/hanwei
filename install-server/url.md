 ### 聂云峰笔记

https://note.youdao.com/share/?id=be5857b36726467e218ac8d6969f5c11&type=note#/

## tcpdump 抓包

http://www.cnblogs.com/ggjucheng/archive/2012/01/14/2322659.html

 

## 清理缓存内存

http://www.ha97.com/4337.html

 

## nginx ip限制

http://blog.sina.com.cn/s/blog_721cd3390101e8xv.html

 

## zabbix安装

http://www.cnblogs.com/mrwang1101/p/5513158.html

 

## zabbix rpm 安装

http://www.cnblogs.com/enjoycode/p/zabbix_3_installation_on_centos_7.html

 

 

## 安装Beanstalkd队列以及PHP代码测试

http://blog.csdn.net/johnny880730/article/details/50536179

 

## yum安装LNMP

http://www.cnblogs.com/xiaoit/p/3991037.html

报错处理 

http://blog.163.com/oracle_wwf/blog/static/213030127201211305636623/   

 

 

## zabbix监控交换机

http://www.jb51.net/article/56972.htm

 

## binlog恢复

http://www.cnblogs.com/sandea/p/5205792.html

http://orangeholic.iteye.com/blog/1698736

 

 

## zabbix自定义监控

http://yangrong.blog.51cto.com/6945369/1542271

 

 

## 僵尸进程

http://www.linuxde.net/2013/07/14924.html

## 思科三层交换机划分vlan

http://www.doc88.com/p-996568390191.html

http://wenku.baidu.com/link?url=7hT_8zfC8pbvbiiYM_zJsUhVLRNWHowJWTateQ97AhUYzxU31REnHwExdG5-Y4tjLEWBhTohYxX9LMmDeABBLBRbYqr0nSVXQ5Z0yvj-9bS

 

 

## openvpn

<http://19930412.blog.51cto.com/6974556/1760900>

<https://segmentfault.com/a/1190000000637898>

<http://william1989.blog.51cto.com/9997022/1623842>

 

openvpn-2.2.2.tar.gz

 

iptables -t nat -A POSTROUTING -s 10.82.8.0/24 -o eth0 -j SNAT--to-source 10.230.1.236

iptables -I FORWARD -s 10.82.8.0/24 -m state --state NEW -jACCEPT

iptables -I FORWARD -m state --state RELATED,ESTABLISHED -jACCEPT

iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT 

service iptables save

service iptables restart

 

 

## openvpn 链接 freeradius

http://wangzan18.blog.51cto.com/8021085/1736459/

 

 

## Zimbra邮件系统的环境部署(centos6.7)

 

http://wandiankafei.blog.51cto.com/10878910/1742186

 

## 安全删除binlog日志

http://www.cnblogs.com/wangxiaoqiangs/p/5336273.html

 

 

## scp远程拷贝，不用输入密码的方法 

http://blog.itpub.net/27042095/viewspace-745587/

 

 

## 免秘钥

<http://blog.csdn.net/five3/article/details/8648484>

 

## zabbix监控IO

http://blog.csdn.net/leezqang/article/details/50175969

## zabbix监控进程

http://yangrong.blog.51cto.com/6945369/1542271

 

http://blog.csdn.net/u012062455/article/details/53259682

## 邮件报警配置

http://www.jb51.net/article/56973.htm

 

## ntp服务搭建

http://www.cnblogs.com/jim-hwg/p/4606821.html

 

## ntp报错处理

http://www.blogjava.net/spray/archive/2008/07/10/213964.html

 

## centos 配置代理上网

http://blog.csdn.net/fwj380891124/article/details/42168683

 

## yum服务搭建

http://www.centoscn.com/CentosServer/www/2014/0829/3601.html

http://www.tuicool.com/articles/EFFBfmM

6.6

http://www.osyunwei.com/archives/7918.html

 

## zabbix升级

http://www.iyunv.com/thread-283752-1-1.html

 

## url监控

<http://www.linuxidc.com/Linux/2016-11/137638p8.htm>

 

 

## 如何重置硬盘遭到“损坏”的Linux系统root用户密码

<http://www.cnblogs.com/mannyzhoug/p/how-to-reset-linux-password-when-disk-with-need-fsck.html>

 

## CentOS 6.5下利用Rsyslog+LogAnalyzer+MySQL部署日志服务器

 

http://www.cnblogs.com/mchina/p/linux-centos-rsyslog-loganalyzer-mysql-log-server.html

 

## mysql 创建远程登陆账号

<http://www.cnblogs.com/codeAB/p/6391022.html>****

** **

** **

**createuser yukang identified by 'testABCa1!'**

**grantselect on idc.\* to 'yukang'@'%' identified by 'testABCa1!';**

** **

## 多网卡ip配置

 

service NetworkManager stop

chkconfig NetworkManager off

 

**iproute flush table 251**

** **

**iproute add default via 222.73.157.1 dev eth0 src 222.73.157.2 table 251**

** **

**iprule add from 222.73.157.2 table 251**

** **

**iproute flush table 252**

** **

**ip routeadd default via 140.206.217.193 dev eth1 src 140.206.217.200 table 252**

** **

**iprule add from 140.206.217.200 table 252**

** **

**iproute flush table 253**

** **

**iproute add default via 117.185.7.193 dev eth3 src 117.185.7.195 table 253**

** **

**iprule add from 117.185.7.195 table 253**

** **

**vim/etc/sysconfig/network**

** **

** **

** **

**NETWORKING=yes**

**HOSTNAME=localhost.localdomain**

**GATEWAY=222.73.157.1**

** **

## ftp搭建

<http://www.centoscn.com/CentosServer/ftp/2016/0502/7155.html>

 

## ip tables nat转发 

<http://blog.sina.com.cn/s/blog_6aad8abe01011p90.html>

 

## cacti

<http://www.cactifans.org/cacti/1349.html>

 

<http://earring.blog.51cto.com/402395/1422857>



 ## centos7 搭建Nextcloud 

https://linux.cn/article-8242-1.html



# centos6.6 搭建kickstart

http://www.cnblogs.com/mchina/p/centos-pxe-kickstart-auto-install-os.html

lvm
http://www.178linux.com/4269

```
# Partition clearing information
clearpart --all
# Disk partitioning information
part /boot --fstype="ext4" --size=200

#part / --fstype="ext4" --size=50000
part pv.01 --grow --size=1
volgroup VolGroup --pesize=4096 pv.01
logvol / --fstype=ext4 --name=lv_root --vgname=VolGroup --size=40000

part swap --fstype="swap" --size=8000
```



dhcp
http://www.linuxidc.com/Linux/2015-11/125040.htm



## centos6.6批量安装ubuntu14.04.5

```
system-config-kickstart 

http://www.linuxidc.com/Linux/2012-06/62441.htm
http://www.mamicode.com/info-detail-1646465.html
http://blog.sina.com.cn/s/blog_5459f60d01016rkb.html

##1
ks.cfg
lang en_US.UTF-8
langsupport en_US.UTF-8
keyboard us
mouse
timezone Asia/Shanghai
rootpw --disabled
#明文密码,不能少于6位,不然会中断自动应答,问你要强密码
#密文可以执行echo 1234567890 | openssl passwd -1 -stdin
#user www --fullname="www" --iscrypted --password $1$YKmaOIb5$/13bs7gCjaoH./ohFT0A7/
user www --fullname="www" --password 1234567890
install
url --url http://192.168.9.251/ubuntu
bootloader --location=mbr
zerombr yes
#两个硬盘,分区全部清除
#clearpart --all --initlabel  --drives=sda
clearpart --all --initlabel  
#size单位为M
#part / --fstype ext4 --size 51200
part swap --size 16000

part /boot --fstype ext4 --size=300

part pv.01 --grow --size=1
volgroup VolGroup --pesize=4096 pv.01
logvol / --fstype=ext4 --name=lv_root --vgname=VolGroup --size=580000
network --bootproto=dhcp --device=eth0
#静态ip
#network --bootproto=static --ip=192.168.5.168 --netmask=255.255.255.0 --gateway=192.168.5.112 \ nameserver=221.5.88.88 --device=eth0
firewall --disabled
skipx
%packages
@openssh-server

##2
然后修改一下 vim /var/lib/tftpboot/ubuntu-installer/amd64/boot-screens/txt.cfg：

default install
label install
        menu label ^Install
        menu default
        kernel ubuntu-installer/amd64/linux
        append ks=http://10.0.0.100/ks.cfg preseed/url=http://10.0.0.100/ubuntu-server.seed vga=788 initrd=ubuntu-installer/amd64/initrd.gz --- quiet 
label cli
        menu label ^Command-line install
        kernel ubuntu-installer/amd64/linux
        append tasks=standard pkgsel/language-pack-patterns= pkgsel/install-language-support=false vga=788 initrd=ubuntu-installer/amd64/initrd.gz --- quiet



##3
cp /var/www/html/ubuntu/preseed/ubuntu-server.seed /var/www/html/

然后 vim /var/www/html/ubuntu-server.seed

在文件末尾添加：

d-i live-installer/net-image string http://10.0.0.100/ubuntu/install/filesystem.squashfs
```

### ccentos7 bond

https://www.imooc.com/article/15741

