#！/usr/bin/env python
from db import web_db
from sqlalchemy.orm import sessionmaker



USER_LIST = [ ]

DB = web_db.DB_Control()
info = DB.Tables['info']
info_obj = DB.Session.query(info).all()

def info_table():
    for t in info_obj:
        i = t.id
        u = t.username
        z = t.group
        e = t.email
        g = t.gender
        temp = {'id': i,'username': u, 'group': z,'email': e, 'gender': g }
        USER_LIST.append(temp)



    return

def add_info(i,u,z,e,g):
    table=DB.Tables['info']
    new_table =table(id=i,username=u,group=z,email=e,gender=g)
    DB.Session.add(new_table)
    DB.Session.commit()


info_table()
