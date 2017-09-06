#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
import socket
import hashlib
import json,os,sys,time,pickle
from conf import settings

class FTPClient(object):

    home = None

    def connection(self,ip,port):
        self.sock = socket.socket()
        self.sock.connect((ip,port))

    def interactive(self):
        while True:
            choice = input("\033[32m%s>>#:\033[0m"%self.username).strip()
            if len(choice) == 0:continue
            cmd = choice.split()
            if hasattr(self,"cmd%s"%cmd[0]):
                func = getattr(self,"cmd%s"%cmd[0])
                func(cmd)
            else:
                print("\033[31m命令不存在！\033[0m")

    #用户注册
    def cmdreg(self):
        while True:
            print("\033[35m用户注册\033[0m")
            username = input("请输入用户名:")
            password = input("请输入密码:")
            passwd = input("请再输入密码:")
            total = input("请输入磁盘配额:")
            if password != passwd:
                print("密码输入不一致!")
                continue
            m = hashlib.sha1()
            m.update(passwd.encode('utf-8'))
            pas = m.hexdigest()
            data = {
                "action":"reg",
                "username":username,
                "password":pas,
                "total":total
            }
            self.sock.send(json.dumps(data).encode())
            get_data = self.response()
            if get_data["status_code"] == 253:
                print("\033[36m注册成功\033[0m")
                break
            if get_data["status_code"] == 252:
                print("\033[35m用户已经存在\033[0m")
                break

    #用户登录
    def cmdlogin(self):
        print("\033[35m用户登录\033[0m")
        user = input("请输入用户名:")
        passwd = input("请输入密码:")
        m = hashlib.sha1()
        m.update(passwd.encode())
        password = m.hexdigest()
        data = {
            "action":'login',
            "username":user,
            "password":password
        }
        self.sock.send(json.dumps(data).encode())
        get_data = self.response()
        if get_data.get('status_code') == 254:
            self.username = user
            self.home = os.path.join(settings.HOME,user)
            self.interactive()
            print("\033[35m登陆成功 \033[0m")
        elif get_data.get('status_code') == 255:
            print("\033[36m密码错误\033[0m")
        else:
            print("\033[36m用户不存在\033[0m")

    #接收数据
    def response(self):
        dat= self.sock.recv(4096)
        dat = json.loads(dat.decode())
        return dat

    #进度条
    def show_progress(self,total):
        received_size = 0
        current_percent = 0
        while received_size < total:
            if int((received_size / total) * 100) > current_percent:
                print("#", end="", flush=True)
                current_percent = int((received_size / total) * 100)

            new_size = yield
            received_size += new_size

    #下载
    def cmdget(self,*args):
        data = args[0]
        m = hashlib.md5()
        if len(data) == 1:
            print("\033[31m没有输入文件名：\033[0m")

        if not os.path.isfile(data[1]):       #下载的文件不存在 正常下载
            cmd_dic = {
                "action": 'get',
                "filename": data[1],
                "seek_size": 0
            }
            self.sock.send(json.dumps(cmd_dic).encode())
            f = open(data[1], 'wb')
        else:                                                #下载的文件存在为断点续传
            filesize = os.path.getsize(data[1])
            cmd_dic = {
                "action": 'get',
                "filename": data[1],
                "seek_size": filesize
            }
            self.sock.send(json.dumps(cmd_dic).encode())       #发送指令给server
            f = open(data[1], 'ab')

        status =self.response()                                 #接收server发送的文件大小
        if status['size'] != 'no':                              #如果要下载的文件在server端存在
            file_size = int(status['size'])
            received_size = 0
            progress = self.show_progress(file_size)             #进度条
            progress.__next__()                                   #进度条
            while received_size < file_size:
                if file_size - received_size > 4096:             #开始接收
                    size = 4096
                else:
                    size = file_size - received_size
                data = self.sock.recv(size)
                received_size += len(data)
                try:
                    progress.send(len(data))                       #进度条
                except StopIteration as e:
                    print("%100")
                f.write(data)
                m.update(data)
            else:
                f.close()
                chk_md5 = {"chk_md5":m.hexdigest()}
                self.sock.send(pickle.dumps(chk_md5))            #发送md5给server
                chk_md5 = pickle.loads(self.sock.recv(1024))     #接收server端的md5校验结果
                if chk_md5['chk_md5']:                          #如果等于True
                    print('\033[32m下载完成，文件MD5核对一致\033[0m')
                else:                                            #如果等于False
                    print('\033[31mMD5校验异常,请重新下载\033[0m')

                return

        else:
            print("\033[31m文件不存在\033[0m")
            return

    #上传
    def cmdput(self, *args):
        data = args[0]
        file = data[1]
        print(data[1])
        if os.path.isfile(file):
            file_size = os.path.getsize(file)
            msg = {
                "action": 'put',
                "status":True,
                "size" :file_size,
                "filename":file
                   }
            self.sock.send(json.dumps(msg).encode())
            msg_dic = pickle.loads(self.sock.recv(1024))
            if msg_dic["status"] == True:
                ret = msg_dic["size"]
                received_size = 0
                m = hashlib.md5()
                with open(file, 'rb')as f:
                    for lin in f:
                        data =self.sock.send(lin)
                        #received_size +=len(data)
                        m.update(lin)
                    chk_md5 = pickle.loads(self.sock.recv(1024))
                    if chk_md5['md5'] == m.hexdigest():
                        print("\033[32m文件上传成功\033[0m")
                    else:
                        print("\033[31m文件上传失败\033[0m")
            else:
                print("\033[31m你的磁盘空间不足!\033[0m")

        else:
            print("\033[31m文件不存在\033[0m")
            return

    #ls查看目录
    def cmdls(self,*args):
        data = args[0]
        if len(data) == 0:
            print("输入错误!")
            return
        msg = {"action":"ls"}
        if data[0] == "ls":
            self.sock.send(json.dumps(msg).encode())
            sponse = self.sock.recv(1024)
            response = json.loads(sponse.decode())
            if response.get('status') == True:
                print(response['cmd'].strip())
                return
        else:
            print("命令输入错误!")
            return

    #cd切换目录
    def cmdcd(self,*args):
        data =args[0]
        if len(data) == 1:
            print("\033[31m错误没有输入路径!\033[0m")
            return
        msg = {
            "action" : "cd",
            "dir" : data[1]
        }
        self.sock.send(json.dumps(msg).encode())
        response = self.response()
        if response.get('status') == True:
            print(response['cmd'])
            return

def run():
    ftp = FTPClient()
    ftp.connection("127.0.0.1",9999)

    menu = '''
    \033[33m
    1.登陆
    2.注册
    \033[0m
    '''
    msg = {
        "1":"ftp.cmdlogin",
        "2":"ftp.cmdreg"
    }

    while True:
        print(menu)
        choice = input("\033[32m请选择>>\033[0m")
        if choice == 'q':
            break
        if len(choice) == 0 or choice not in msg:continue
        eval(msg[choice])()

run()