#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'wei.han'
import sys,os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

import socket
import selectors
import configparser,pickle

class Ftp_Clinet(object):
    '''
    selectorsFTP客户端
    '''

    def __init__(self):
        #创建客户端socket
        self.Client = socket.socket()
        #获取配置文件
        self.Get_Conf()
        #创建链接
        self.Conn()
        #进入命令循环
        self.Command()

    #链接server
    def Conn(self):
        self.Client.connect((self.IP,self.Port))

    def Command(self):
        '''
        按命令执行 
        '''
        while True:
            cmd = input('请输入命令:').strip()
            cmd_list = cmd.split()
            if len(cmd_list) == 3:
                if cmd_list[0] == 'put':
                    self.UpLoad(cmd_list)

                elif cmd_list[0] == 'get':
                    self.DownLoad(cmd_list)

                else:
                    print('\033[31m命令错误!\033[0m')
                    self.Show_Help()
                    continue


    def UpLoad(self,cmd_list):
        '''
        上传 
        '''
        data = {
            'act':'upload',
            'localfile':cmd_list[1],
            'cloudfile':cmd_list[2]
        }

        self.Client.send(pickle.dumps(data))
        #接收确认信息
        chk = self.Client.recv(1024)
        if chk.decode() == 'ready':
            print('服务端已经准备好，开始发送文件...')
            self.Send_File_Size(data)
        else:
            print('数据传输错误,程序中止')
            exit()

    def Send_File_Size(self,dict):
        '''
        发送文件大小 
        '''
        data = {'size':0}
        file_path = dict['localfile']
        if os.path.isfile(file_path):
            data['size'] = os.path.getsize(file_path)
            print("获取大小:",data['size'])
            f = open(file_path,'rb')
            self.Client.send(pickle.dumps(data))
            self.Send_File_Data(f)#发送数据
        else:
            print('文件不存在，无法上传')
            self.Client.send(pickle.dumps(data))

    def Send_File_Data(self,file_obj):
        '''
        发送数据
        '''
        #接收确认消息
        chk = self.Client.recv(1024)
        if chk.decode() == 'ok':
            print("发送数据")
            for line in file_obj:
                self.Client.send(line)
            file_obj.close()
            print('文件传输完毕!')
            #给服务端发送一个完成信号
            self.Client.send(b'upload completed')
        else:
            print("数据传输错误,程序中止")
            exit()

    def DownLoad(self,cmd_list):
        '''
        下载
        '''
        data = {
            'act':'download',
            'localfile': cmd_list[2],
            'cloudfile' : cmd_list[1]
        }
        self.Client.send(pickle.dumps(data))
        #接收确认消息
        chk = self.Client.recv(1024)
        if chk.decode() == 'ready':
            self.Client.send(b'ok')#发送一个消息以激活服务端监听回调
            self.Get_File_Size(data)
        else:
            print('数据传输错误，程序终止')
            exit()

    def Get_File_Size(self,dict):
        '''
        接收文件大小
        '''
        filesize = pickle.loads(self.Client.recv(1024))
        if filesize['size'] == 0:
            print("云端文件不存在")
        else:
            new_filename = dict['cloudfile']
            f = open(new_filename,'wb')
            dict['newfile'] = new_filename
            self.Save_File_Data(f,filesize['size'],dict)


    def Save_File_Data(self,file_obj,file_size,dict):
        '''
        接收数据
        '''
        recved_size = 0
        self.Client.send(b'ok')
        while file_size - recved_size >0:
            if file_size - recved_size <1024:
                size = file_size - recved_size
            else:
                size = 1024
            file_data = self.Client.recv(1024)
            recved_size += len(file_data)
            file_obj.write(file_data)
        else:
            print('download completed')
            file_obj.close()

    def Show_Help(self):
        '''
        打印帮助信息
        '''
        print('帮助'.center(50,'-'))
        print('上传文件: put [本地文件名] [云端文件名]')
        print('下载文件: get [云端文件名] [本地文件名]')

    def Get_Conf(self):
        '''
        获取配置信息
        '''
        conf = configparser.ConfigParser()
        conf.read('conf.ini')
        self.IP = conf['CLIENT']['ip']
        self.Port = int(conf['CLIENT']['port'])




Ftp_Clinet()
