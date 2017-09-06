#!/usr/bin/env python
# _* encoding:utf-8 _*_

import threading
import paramiko

class FtpClient(object):

    def __init__(self):
        self.ssh = paramiko.SSHClient()

    def sftp_connect(self,hostname,username,passwd,port):
        transport = paramiko.Transport((hostname,port))
        transport.connect(username=username,password=passwd)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def ssh_connect(self,ip,username,passwd,port):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=ip,port=port,username=username,password=passwd)

    def cmd_ssh(self):
        while True:
            choice = input(">>:")
            cmd = choice.split()[0]
            if cmd == '':
                continue
            if cmd == "exit":
                exit()
            stdin,stdout,stderr =self.ssh.exec_command(cmd)
            res,err = stdout.read(),stderr.read()
            resilt = res if res else err
            print(resilt.decode())


    def get(self,*args):
        data = args[0].split()[1]
        self.sftp.get(data,data)

    def put(self,*args):
        data = args[0].split()[1]
        self.sftp.put(data,data)

    def interactive(self):
        while True:
            choice = input(">>")
            if choice == '':
                continue
            if choice == "exit":
                exit()
            str_cmd = choice.split()
            if hasattr(self,"%s"%str_cmd[0]):
                func = getattr(self,"%s"%str_cmd[0])
                func(choice)
            else:
                print("输入的命令不存在!")
                continue





def login():
    while True:
        username = input("请输入用户名:")
        if username == '':
            continue
        password = input("请输入密码:")
        if password == '':
            continue
        port = input("请输入端口:")
        if port == '':
            continue
        try:
            port=int(port)
        except ValueError as e:
            print(e,"你输入的端口不是数字!")
        return [username,password,port]


host_list = ["192.168.80.11","192.168.80.12"]
host_action = ["执行命令","上传/下载文件"]

msg = {
    "0" : "ftp. cmd_ssh",
    "1" : "ftp.interactive"
}


def main():
    while True:
        for index,host in enumerate(host_list):
            print(index,host)
        choice = input("请选择主机:")
        try:
            host_list[int(choice)]
        except IndexError as e:
            print("输入错误",e)
            continue


        while True:
            for index,host in enumerate(host_action):
                print(index,host)
            choice_action = input("请选择:")

            if not choice_action.isdigit():
                print("编号不合法:")
                continue

            hostname = host_list[int(choice)]
            if choice_action in msg.keys():
                data = login()
                username = data[0]
                password = data[1]
                port = data[2]
                ftp = FtpClient()
                ftp.ssh_connect(hostname,username,password,port)
                ftp.sftp_connect(hostname,username,password,port)
                eval(msg[choice_action])()

            else:
                print("输入的命令不存在!")
                continue


t = threading.Thread(target=main,args=())
t.start()