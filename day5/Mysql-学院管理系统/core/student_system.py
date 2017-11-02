#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__ = "han"
import sys,os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

import hashlib,webbrowser

from core import db_sql

class View_Interface(object):
    def __int__(self):
        self.Is_Login = False
        self.Login_User = None
        self.DB = db_sql.DB_Control()


    def Menu(self):
        '''
        主页
        :return: 
        '''
        pass

    def Login(self):
        '''
        登陆接口
        :return: 
        '''
        pass

    def Register(self):
        '''
        注册用户
        :return: 
        '''
        pass

    def Create_Pwd(self):
        pass

##
    def Menu_For_Type(self):
        '''
        第二主页
        :return: 
        '''
        pass

##

    def Menu_Admin(self):
        '''
        管理员接口
        :return: 
        '''
        pass

    def Create_School(self):
        '''
        创建学校
        :return: 
        '''
        pass

    def Create_Course(self):
        '''
        创建课程
        :return: 
        '''
        pass


###

    def Menu_Teacher(self):
        '''
        教师接口
        :return: 
        '''
        pass

    def Create_Class(self):
        '''
        创建班级
        :return: 
        '''
        pass

    def Choose_Student(self):
        '''
        将学员加入到班级
        '''
        pass

    def Start_Class(self):
        '''
        开始上课
        :return: 
        '''
        pass

    def Homework_Correcting(self):
        '''
        批改作业
        :return: 
        '''
        pass

###

    def Menu_Student(self):
        '''
        学生接口
        :return: 
        '''
        pass

    def Sel_Student(self):
        '''
        学生选课
        :return: 
        '''
        pass


    def Submit_Homework(self):
        '''
        提交作业
        :return: 
        '''
        pass

    def Show_Score(self):
        '''
        查看成绩
        :return: 
        '''
        pass

#########

    def Open_Homework(self):
        '''
        调用浏览器打开url
        :return: 
        '''
        pass

    def Sel_Class(self):
        '''
        选择班级上课或其他
        :return: 
        '''
        pass


    def Sel_Class_Record(self):
        '''
        选择班级上课记录
        :return: 
        '''
        pass

    def Sel_Course(self):
        '''
        选择班级课程
        :return: 
        '''
        pass


    def Sel_School(self):
        '''
        选择学校，返回选择的学校ORM
        :return: 
        '''
        pass

    def Sel_Teacher(self):
        '''
        选择教师，返回教师OBj
        :return: 
        '''
        pass




    def Get_Role_Type(self):
        '''
        返回角色类型字典
        :return: 
        '''
        pass



