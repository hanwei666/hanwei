#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author_ ='han'
import os,sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


class RPC_Server(object):
    '''
    RPC服务端
    '''

    def __init__(self):
        pass


    def Get_Conf(self):
        '''
        换取配置文件
        :return: 
        '''
        pass

    def Handler(self):
        '''
        创建链接RabbitMQ信道和接收
        :return: 
        '''
        pass

    def Response(self):
        '''
        处理接收到的命令，
        再发命令执行结果
        :return: 
        '''
        pass

    def Command(self):
        '''
        执行命令
        :return: 
        '''
        pass

