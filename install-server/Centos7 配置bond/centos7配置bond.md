***

https://www.imooc.com/article/15741

http://m.blog.csdn.net/hnhuangyiyang/article/details/52448996

- /etc/sysconfig/network-scripts/route-bond0 静态路由示例

  ```
   100.0.0.0/8 via 100.126.0.253
  ```

  需要禁用NetworkManager
  ​

  systemctl stop NetworkManager.service

  systemctl disable NetworkManager.service

  ​

