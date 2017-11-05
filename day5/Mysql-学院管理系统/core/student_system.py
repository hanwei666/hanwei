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
        menu_list = ['1.用户登录','2.注册用户']
        menu_dict = {
            '1.用户登录':self.Login,
            '2.注册用户':self.Register
        }
        while True:
            print('学员管理系统'.center(50,'-'))
            for menu in menu_list:
                print(menu)
            act = input("请选择(q推出)：")
            if act.isdigit() and int (act) <= len(menu_list) and len(menu_list) >0:
                func = menu_dict[menu_list[int(act)-1]]
                func()
                break
            elif act.strip() =='q':
                exit()
            else:
                print('选择错误！')
                continue
        self.Menu_For_Type()

    def Login(self):
        '''
        登陆接口
        :return: 
        '''
        while True:
            print("用户登录".center(50,'-'))
            username = input('请输入用户民：')
            password = input ('请输入密码：')
            password = self.Create_Pwd(password)
            table = self.DB.Tables['user']
            user_obj = self.DB.Session.query(table).filter(table.name==username).filter(table.pwd==password).first()
            if user_obj is None:
                print('\033[32m登录失败\033[0m')
                continue
            else:
                self.Is_Login = True
                self.Login_User = user_obj
                print('欢迎[%s]%s'%(user_obj.type.name,user_obj.name))
                break
        return self.Is_Login




    def Register(self):
        '''
        注册用户
        :return: 
        '''
        table = self.DB.Tables['user']
        user_info = {
            'name':'',
            'pwd':'',
            'qq':'',
            'email':''
        }
        while True:
            print('注册用户'.center(50,'-'))
            if user_info['name'] == '':
                username = input('请输入用户名:')
                user_obj = self.DB.Session.query(table).filter(table.name==username).first()
                if user_obj is not None:
                    print('用户名已经存在,请重新输入:')
                    continue
                else:
                    user_info['name'] = username
            else:
                password = input('请输入密码:')
                re_password = input('请再次输入密码:')
                if password != re_password:
                    print('两次密码不一致,请重新输入!')
                    continue
                else:
                    password = self.Create_Pwd(password)
                    user_info['pwd'] = password
                    qq = input('请输入QQ号:')
                    email = input('请输入邮箱账号:')
                    user_info['qq'] = qq
                    user_info['email'] = email
                    break
        type_obj_dict = self.Get_Role_Type()
        new_user = table(name=user_info['name'],pwd=user_info['pwd'],qq=user_info['qq'],email=user_info['email'])
        while True:
            print('注册类型'.center(50,'-'))
            type_list = []
            count = 1
            for type_obj in type_obj_dict:
                if type_obj_dict[type_obj].name != 'admin':
                    print(count,'.',type_obj_dict[type_obj].name)
                    type_list.append(type_obj_dict[type_obj].name)
                    count +=1
            act = input('请选择:').strip()
            if act.isdigit() and int(act) <= len(type_list) and len(act) >0:
                new_user.type = type_obj_dict[type_list[int(act)-1]]
                break
            else:
                print('选择错误!')
                continue
        self.DB.Session.add(new_user)
        self.DB.Session.commit()



    def Create_Pwd(self,pwd):
        return hashlib.md5(pwd.encode('utf8')).hexdigest()

##
    def Menu_For_Type(self):
        '''
        第二主页
        :return: 
        '''
        if self.Login_User is None:
            self.Login()
            self.Menu_For_Type()
        else:
            role_type = self.Login_User.type.name
            menu_dict = {
                'student':self.Menu_Student,
                'tacher':self.Menu_Teacher,
                'admin':self.Menu_Admin
            }
            if role_type in menu_dict:
                menu_dict[role_type]()
            else:
                print('角色类型错误！')
                exit()


##

    def Menu_Admin(self):
        '''
        管理员接口
        :return: 
        '''
        if self.Is_Login is False:
            print('用户没有登录!')
            exit()
        menu_list = ['1.创建学校','2.创建课程']
        menu_dict = {
            '1.创建学校':self.Create_School,
            '2.创建课程':self.Create_Course
        }
        while True:
            print(('欢迎管理员%s登录'%self.Login_User.name)).center(50,'-')
            for menu in menu_list:
                print(menu)
            act = input('请选择:(q推出)')
            if act.isdigit() and int(act) <= len(menu_dict) and int(act) >0:
                func = menu_dict[menu_list[int(act)-1]]
                func()
            elif act == 'q':
                self.Is_Login = False
                self.Login_User = None
                break
            else:
                print('\033[32m选择错误!\033[0m')
                continue
        self.Menu()

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
        table = self.DB.Tables['role_type']
        type_obj = self.DB.Session.query(table).all()
        type_dict = {}
        for t in type_obj:
            type_dict[t.name] = t
        return type_dict


