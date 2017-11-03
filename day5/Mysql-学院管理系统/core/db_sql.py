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
        print("\033[35m-------------------\033[0m")
        self.Get_Conf()
        self.Tables = self.Table_Framework()
        self.Create_Default_Data()
        print('\033[36m++++++++++++++++++++\033[0m')

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
        Base = self.Conn()
        class School(Base):
            '''
            学校
            '''
            __tablename__ = 'school'
            id = Column(Integer,primary_key=True)
            name = Column(String(32),nullable=False)
            address = Column(String(32),nullable=False)

            def __repr__(self):
                return '<School>%s[%s]'%(self.name,self.address)

        class Course(Base):
            '''
            课程
            '''
            __tablename__ = 'course'
            id = Column(Integer,primary_key=True)
            name = Column(String(32),nullable=False)
            teacher_id = Column(Integer,ForeignKey('user.id'))
            teacher = relationship('User',backerf='teacher_courses')
            school_id = Column(Integer,ForeignKey('school.id'))
            school = relationship('School',backref='courses')
            price = Column(Integer,nullable=False)

            def __repr__(self):
                return '<Coures>%s,讲师：%s校区：%s'%(self.name,self.teacher.name,self.school.name)

        class S_Class(Base):
            '''
            班级
            '''
            __tablename__ ='s_class'
            id = Column(Integer,primary_key=True)
            name = Column(String(32),nullable=False)
            course_id = Column(Integer,ForeignKey('course.id'))
            course = relationship('Course',backref='class')

            def __repr__(self):
                return '<Class>%s[%s]>'%(self.name,self.course.name)

        class Class_Students(Base):
            '''
            班级学生
            '''
            __tablename__ = 'class_students'
            id = Column(Integer,primary_key=True,autoincrement=True)
            class_id = Column(Integer,ForeignKey('s_class.id'))
            s_class = relationship('S_Class',backref='student')
            user_id = Column(Integer,ForeignKey('user.id'))
            student = relationship('User',backref='in_class')

            def __repr__(self):
                return '<Class_Student>姓名：%s[课程：%s-%s]'%(self.student.name,self.self.s_class.name,self.s_class.course.name)

        class Class_Record(Base):
            '''
            上课记录
            '''
            __tablename__ = "class_record"
            id = Column(Integer,primary_key=True,autoincrement=True)
            day = Column(Integer,nullable=False)
            class_id = Column(Integer,ForeignKey('s_class.id'))
            s_class = relationship('S_Class',backref='record')

            def __repr__(self):
                res = '[开课记录]%s(第%s天)'%(self.s_class.name,self.day)
                return res

        class Study_Record(Base):
            '''
            上课记录
            '''
            __tablename__ = 'study_record'
            id = Column(Integer,primary_key=True,autoincrement=True)
            class_record_id = Column(Integer,ForeignKey("class_record.id"))
            class_record = relationship('Class_Record',backref='study_record')
            student_id = Column(Integer,ForeignKey('user.id'))
            student = relationship('User',backref='study_record')
            task_url = Column(String(40))
            score = Column(Integer,nullable=False,default=0)

            def __repr__(self):
                res = '<study_record>%s在%s'%(self.student.name,self.class_record.name)
                res += '第%d天课程'%self.class_record.day
                if self.task_url == None:
                    res += '[作业未提交]'
                elif self.score == 0:
                    res += '[讲师未评分]'
                else:
                    res += '[%d分]'%self.score
                return res


        Base.metadata.create_all(self.Engine)


        class User(Base):
            '''
            用户
            '''
            __tablename__ = 'user'
            id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
            name = Column(String(32),nullable=False)
            pwd = Column(String(32),nullable=False)
            type_id = Column(Integer,ForeignKey('role_type.id'))
            type = relationship('Role_Type',backref='user')
            qq = Column(String(32))
            email = Column(String(32))

            def __repr__(self):
                return '<User>name=%s,type=%s'%(self.name,self.type.name)


        class Role_Type(Base):
            '''
            用户类型
            '''
            __tablename__ ='role_type'
            id = Column(Integer,primary_key=True,autoincrement=True)
            name = Column(String(8),nullable=False)

            def __repr__(self):
                return "<role_type>%s:%s"%(self.id,self.name)

        class User_Course(Base):
            '''
            选课程
            '''
            __tablename__ = 'user_course'
            id = Column(Integer,primary_key=True,autoincrement=True)
            user_id = Column(Integer,ForeignKey('user.id'))
            user = relationship('User',backrf="student_courses")
            course_id = Column(Integer,ForeignKey('course.id'))
            course = relationship('Course',backref='user',foreign_keys=[course_id])
            pay_status = Column(String(32))

            def __repr__(self):
                return "<user_course>user:%s,course:%s"%(self.user.name,self.course.name)



    def Create_Default_Data(self):
        table = self.Tables['role_type']
        type_obj = self.Session.query(table).all()
        if len(type_obj) == 0:
            type1 = table(name='student')
            type2 = table(name='teacher')
            type3 = table(name='admin')
            self.Session.add_all([type1,type2,type3])
            self.Session.commit()
            type_dict = {
                'student':type1,
                'teacher':type2,
                'admin':type3
            }
        else:
            type_dict = {}
            for i in type_obj:
                type_dict[i.name]=i
        table = self.Tables['user']
        default_user_list = self.Session.query(table).all()
        if len(default_user_list) == 0:
            user_admin = table(name='admin',pwd=self.Create_Pwd('admin'),type=type_dict['admin'])
            user_student = table(name='student',pwd=self.Create_Pwd('123.com'),type=type_dict['student'],qq='289959141',email='wei.han@phicomm.com')
            user_teacher = table(name='teacher',pwd=self.Create_Pwd('123.com'),type=type_dict['teacher'])
            self.Session.add_all([user_admin,user_student,user_teacher])
            self.Session.commit()


    def Create_Pwd(self,pwd):
        return hashlib.md5(pwd.encode('utf8')).hexdigest()



