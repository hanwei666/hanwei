#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR )
print(BASE_DIR)
HOST = "127.0.0.1"
PROT = 9999

AUTH = os.path.join(BASE_DIR,"auth")
HOME = os.path.join(BASE_DIR,"home")
CLIENT = os.path.join(BASE_DIR,"clinet")



