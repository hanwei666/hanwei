#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__ ="han"
import sys,os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from sqlalchemy import Column,String,create_engine,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

import configparser,hashlib

class DB_Control(object):
    def __int__(self):

        self.Get_Conf()
        self.Tables = self.Table_Framework()
        self.Create_Default_Data()

    def Conn(self):
        conn_str = '%s+pymysql://%s:%s@%s/%s?charset=utf8'%(self.DB_TYPE,self.DB_USER,
                                                            self.DB_PWD,self.DB_HOST,self.DB_NAME)

        self.Engine = create_engine(
            conn_str,
            encoding='utf8'
            #echo=True
        )
        DB_BASE = declarative_base()
        Session_Class = sessionmaker(bind=self.Engine)
        self.Session = Session_Class()
        return DB_BASE

    def Get_Conf(self):
        '''
        获取配置文件
        :return: 
        '''
        config = configparser.ConfigParser()
        config.read(os.path.join(path,"conf",'config.ini'))
        self.DB_TYPE = config['DB']['type']
        self.DB_HOST = config["DB"]["host"]
        self.DB_USER = config["DB"]["user"]
        self.DB_PWD = config["DB"]["pwd"]
        self.DB_NAME = config["DB"]["db_name"]

    def Table_Framework(self):

        pass

    def Create_Default_Data(self):
        pass

    def Create_Pwd(self):
        pass



