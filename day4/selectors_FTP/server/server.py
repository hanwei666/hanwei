#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'wei.han'
import os,sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

import socket
import selectors
import logging,configparser,pickle

class Ftp_Server(object):
    '''
    selectors FTP IO多路复用
    '''
    def __init__(self):
        self.Sel = selectors.DefaultSelector()
        self.Action = {}#存储每个链接命令,以conn作为标识
        self.File_Obj = {}#存储每个链接地FTP文件信息,以conn作为标识
        #获取配置文件
        self.Get_Conf()
        #创建socket
        self.Handle()

    def Handle(self):
        sock = socket.socket()
        sock.bind((self.IP,self.Port))
        sock.listen()
        sock.setblocking(False) #设置不都塞
        #注册selectors事件
        self.Sel.register(sock,selectors.EVENT_READ,self.Accept)
        while True:
            events = self.Sel.select()
            for key,mask in events:
                callback = key.data
                callback(key.fileobj,mask) #等于执行self.Accept

    def Get_Conf(self):
        '''
        获取配置信息
        '''
        conf = configparser.ConfigParser()
        conf.read('conf.ini')
        self.IP = conf['SERVER']['ip']
        self.Port = int(conf['SERVER']['port'])

    def Accept(self,sock,mask):
        '''接收新来地链接'''
        conn,addr = sock.accept()
        print('客户端:',addr)
        conn.setblocking(False)#设置不都塞
        self.Sel.register(conn,selectors.EVENT_READ,self.Read)

        #pass

    def Read(self,conn,mask):
        '''
        读取客户端过来的命令
        '''
        try:
            cmd = conn.recv(1024)
            if cmd:
                cmd_dict = pickle.loads(cmd)
                if cmd_dict['act'] == 'upload':
                    conn.send(b'ready') #发送确认信息防止粘包
                    self.Action[conn] = cmd_dict#参数存储字典
                    #重新注册事件,以更换回掉函数,进入接收文件大小
                    self.Sel.unregister(conn)
                    self.Sel.register(conn,selectors.EVENT_READ,self.UpLoad_Get_FileSize)
                    print(self.Action[conn])
                elif cmd_dict['act'] == 'download':
                    conn.send(b'ready')#发送信息防止粘包
                    self.Action[conn] = cmd_dict
                    #重新注册事件,以更换回掉函数,进入发送文件大小
                    self.Sel.unregister(conn)
                    self.Sel.register(conn,selectors.EVENT_READ,self.Download_Send_FileSize)

            else:
                self.Sel.unregister(conn)
                conn.close()
        except Exception as e:
            self.Sel.unregister(conn)
            conn.close()
            print(e)

    def Download_Send_FileSize(self,conn,mask):
        '''
        发送文件大小
        '''

        data = {'size':0}
        print('文件下载:',self.Action[conn]['cloudfile'])
        chk = conn.recv(1024)#接收一个激活信号
        filename = self.Action[conn]['cloudfile']
        if os.path.isfile(filename):#判断文件是否存在
            data['size'] = os.path.getsize(filename)
            conn.send(pickle.dumps(data))#发送文件大小
            f =  open(filename,'rb')
            self.File_Obj[conn] = {
                'file_obj':f
            }
            # 重新注册监听事件
            self.Sel.unregister(conn)
            self.Sel.register(conn,selectors.EVENT_READ,self.DownLoad_Send_FileDta)
        else:
            conn.send(pickle.dumps(data))# 发送0大小，标识文件不存在
            # 回到read回调监听
            self.Sel.register(conn,selectors.EVENT_READ,self.Read)
            del self.Action[conn]

    def DownLoad_Send_FileDta(self,conn,mask):
        '''
        发送下载文件数据
        :param conn: 
        :param mask: 
        :return: 
        '''

        chk = conn.recv(1024)#接收接货信号
        file_obj = self.File_Obj[conn]['file_obj']
        for line in file_obj:
            conn.send(line)
        file_obj.close()

        self.Sel.unregister(conn)
        self.Sel.register(conn,selectors.EVENT_READ,self.Read)
        del self.Action[conn]
        del self.File_Obj[conn]


    def UpLoad_Get_FileSize(self,conn,mask):
        '''
        接收客户端发送过来的文件大小
        :param conn: 
        :param mask: 
        :return: 
        '''

        print('文件上传',self.Action[conn]['localfile'])
        file_size = pickle.loads(conn.recv(1024))
        if file_size['size'] == 0:
            print('客户端文件不存在,取消发送')
            # 解绑事件，重新进入命令监听事件
            self.Sel.unregister(conn)
            self.Sel.register(conn,selectors.EVENT_READ,self.Read)
        else:
            new_filename = self.Action[conn]['localfile']
            print('收到客户端发送大小:',file_size)
            f = open(new_filename,'wb')
            # 将文件信息记录入全局字典
            self.File_Obj[conn] = {
                'file_obj':f,
                'tmp_file':new_filename,#临时文件名
                'file_size':file_size['size'],#文件总大小
                'recved_size':0,#已接收大小
                'save_as':self.Action[conn]['cloudfile']
            }
            conn.send(b'ok')#发送验证数据给客户端，防止粘包
            # 重新注册事件，将下一个活动IO交给接收文件数据函数处理
            self.Sel.unregister(conn)
            self.Sel.register(conn,selectors.EVENT_READ,self.UpLoad_Get_FileData)

    def UpLoad_Get_FileData(self,conn,mask):
        '''
        接收文件数据
        :param conn: 
        :param mask: 
        :return: 
        '''
        filesize = self.File_Obj[conn]['file_size']
        recved_size = self.File_Obj[conn]['recved_size']
        if filesize - recved_size == 0:#文件接收完毕
            # 解绑事件
            self.Sel.unregister(conn)
            # 重新注册事件监听
            self.Sel.register(conn,selectors.EVENT_READ,self.Read)
            del self.Action[conn] #删除临时数据
            self.File_Obj[conn]['file_obj'].close()#关闭文件
            print(conn.recv(1024).decode())
            print('完成接收,关闭文件')
            # self.ReNmae(self.File_Obj[conn]['tmp_file'],self.File_Obj[conn]['save_as'])
            del self.File_Obj[conn]#删除文件句柄

        else:
            if filesize - recved_size < 1024:
                size = filesize - recved_size
            else:
                size = 1024
            file_data = conn.recv(size)
            self.File_Obj[conn]['recved_size'] += len(file_data)
            self.File_Obj[conn]['file_obj'].write(file_data)



Ftp_Server()


