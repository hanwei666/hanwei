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
    def __init__(self):
        self.Get_Conf()
        self.Tables = self.Table_Framework()
        self.Create_Default_Data()
        print('\033[36m链接成功！\033[0m')

    def Conn(self):
        '''
        链接数据库
        :return:
        '''
        conn_str = '%s+pymysql://%s:%s@%s/%s?charset=utf8'%(self.DB_TYPE,self.DB_USER,self.DB_PWD,self.DB_HOST,self.DB_NAME)

        self.Engine = create_engine(
            conn_str,
            encoding='utf8',
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
        config.read(os.path.join(path,'db','config.ini'))
        self.DB_TYPE = config['DB']['type']
        self.DB_HOST = config['DB']['host']
        self.DB_USER = config['DB']['user']
        self.DB_PWD = config['DB']['pwd']
        self.DB_NAME = config['DB']['db_name']

    def Table_Framework(self):
        Base = self.Conn()

        class User(Base):
            __tablename__ = 'user'
            id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
            name = Column(String(32),nullable=False)
            pwd = Column(String(32),nullable=False)

            def __rep__(self):
                return '<User>name=%s,id=%s'%(self.name,self.id)

        class Info(Base):
            __tablename__ = 'info'
            id = Column(Integer, nullable=False,primary_key=True,autoincrement=True)
            username = Column(String(32),nullable=False)
            group = Column(String(32),nullable=False)
            email = Column(String(32),nullable=False)
            gender = Column(String(32),nullable=False)

            def __rep__(self):
                return '<Info>username=%s,group=%s,email=%s,gender=%s' % (self.username, self.group,self.email,self.gender)

        Base.metadata.create_all(self.Engine)
        # 返回表结构对象字典
        table_dict = {
            'user' : User,
            'info' : Info
        }

        return table_dict

    def Create_Pwd(self,pwd):
        return hashlib.md5(pwd.encode("utf8")).hexdigest()

    def Create_Default_Data(self):
        table = self.Tables['user']
        default_user_list = self.Session.query(table).all()
        if len(default_user_list) == 0:
            user_admin = table(name='admin',pwd=self.Create_Pwd('admin'))
            self.Session.add_all([user_admin])
            self.Session.commit()



if __name__ == '__main__':
    db = DB_Control()

