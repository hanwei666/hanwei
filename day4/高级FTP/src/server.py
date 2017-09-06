#/usr/bin/env python
# _*_ encoding:utf-8 _*_

import socketserver
import json,pickle
from conf import settings
import os,hashlib,sys,time

STATUS_CODE ={
    250 : "输入的命令不存在",
    251 : "输入的命令为空",
    252 : "用户已经存在",
    253 : "注册成功",
    254 : "登陆成功",
    255 : "密码错误",
    256 : "用户不存在",
    257 : "发送文件大小",
    258 : "下载完成",
    259 : "断点续校验不一致",
    260 : "文件不存在"

}


class FTPHandler(socketserver.BaseRequestHandler):

    username = None
    total = None
    home = None
    ret = None
    free_space = None
    cd_dict = {}

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                print(self.data)
                break
            data = json.loads(self.data.decode())

            if data.get('action') is not None:
                if hasattr (self,"_%s"%data.get('action')):
                    func = getattr(self,"_%s"%data.get('action'))
                    func(data)
                else:
                    self.send_response(250)
                    print("输入的命令不存在")
                    return
            else:
                self.send_response(251)
                print("输入的命令为空")
                return


    #发送文件
    def send_response(self,status,data=None):
        response = {'status_code':status,"status_msg":STATUS_CODE[status]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    #接收文件
    def response(self):
        data = self.request.recv(1024)
        data = json.loads(data.decode())
        return data


    #用户注册
    def _reg(self,*args):
        data = args[0]
        username = data['username']
        password = data['password']
        total = data['total']
        user_auth = os.path.join(settings.AUTH,username)
        user_home = os.path.join(settings.HOME,username)
        if os.path.isfile(user_auth):
            self.send_response(252)
            print("用户已经存在")
        else:
            user_data= {
                "username":username,
                "password":password,
                "total":total
            }
            os.mkdir(user_home)
            with open(user_auth,'w') as f:
                json.dump(user_data,f)
            self.send_response(253)
            print("注册成功")

    #验证登陆
    def _login(self,*args):
        data = args[0]
        username = data['username']
        password = data['password']
        user_dir = os.path.join(settings.AUTH,username)
        if os.path.isfile(user_dir):
            with open(user_dir,'r') as f:
                user_data=json.load(f)
                if user_data['username'] == username and user_data['password'] == password:
                    self.username = username
                    self.ret = None
                    self.total = user_data['total']
                    self.home = os.path.join(settings.HOME,username)
                    self.send_response(254)
                    print("登陆成功")
                    for root,dirs,files in os.walk(self.home,True):
                        size = 0
                        size += sum([os.path.getsize(os.path.join(root,name)) for name in files])
                        print(size)
                        self.free_space = int(self.total) - size

                else:
                    self.send_response(255)
                    print("密码错误！")
                    return
        else:
            self.send_response(256)
            print("用户不存在！")
            return

    #文件下载
    def _get(self,*args):
        data= args[0]
        filename = data['filename']
        m = hashlib.md5()
        home_file = os.path.join(self.home,filename)
        if os.path.isfile(home_file):                    #判断文件是否存在
            file_size = os.path.getsize(home_file)
            self.send_response(260,{"size":file_size})
            ret = data["seek_size"]
            f = open(home_file,'rb')
            f.seek(ret)                                  #移动到断点位置
            for line in f:
                self.request.send(line)                  #发送给客户端
                m.update(line)
            else:
                f.close()
                chk_md5 = pickle.loads(self.request.recv(1024))   #接收客户端的MD5
                if chk_md5['chk_md5'] == m.hexdigest():          #判断MD5是否一致
                    data = {"chk_md5":True}
                else:
                    data = {"chk_md5":False}
                self.request.send(pickle.dumps(data))             #发送给客户端校验结果
                print("下载完成")
                return

        else:
            self.send_response(260, {"size": "no"})
            return

    #上传文件
    def _put(self,*args):
        data = args[0]
        if data["status"] == True:
            file_size = data['size']
            file = os.path.join(self.home,data['filename'])
            if os.path.isfile(file):
                if self.free_space > int(data['size']):
                    filesize = os.path.getsize(file)
                    dat = {
                        "status": True,
                        "size": filesize
                    }
                else:
                    filesize = os.path.getsize(file)
                    dat = {
                        "status": False,
                        "size": filesize
                    }
                f = open(file,'ab')
                self.request.send(pickle.dumps(dat))
            else:
                if self.free_space > int(data['size']):
                    dat = {
                        "size": 0,
                        "status": True
                    }
                else:
                    dat = {
                        "size": 0,
                        "status": False
                    }
                f = open(file,'wb')
                self.request.send(pickle.dumps(dat))
            received_size = 0
            data_size  = int(data['size'])
            m = hashlib.md5()
            while received_size < data_size:
                if data_size - received_size > 4096:
                    size = 4096
                else:
                    size = data_size - received_size
                data = self.request.recv(size)
                received_size += len(data)
                f.write(data)
                m.update(data)
            f.close()
            chk_md5 = {
                "md5" : m.hexdigest()
            }
            self.request.send(pickle.dumps(chk_md5))
            print("文件接收成功")
            return

    #ls切换目录
    def _ls(self,*args):
        data = args[0]
        if FTPHandler.cd_dict:
            os.chdir(FTPHandler.cd_dict['cmd'])
        else:
            cmd_dir = self.home
            os.chdir(cmd_dir)
        home_dir = os.getcwd()
        cmd  = "ls %s" % home_dir
        cmd = os.popen(cmd).read()
        msg = {'cmd':cmd,"status":True}
        self.request.send(json.dumps(msg).encode())
        return

    #cd切换目录
    def _cd(self,*args):
        data = args[0]
        file = data['dir']
        cmd_dir = "%s/%s" % (self.home,file)
        os.chdir(cmd_dir)
        cmd = os.getcwd()
        data = {"status":True,'cmd':cmd}
        self.request.send(json.dumps(data).encode())
        FTPHandler.cd_dict.update(data)
        return


def run():
    server = socketserver.ThreadingTCPServer((settings.HOST,settings.PROT),FTPHandler)
    server.serve_forever()

run()