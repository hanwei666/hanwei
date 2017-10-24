#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__='han'
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from core import server

run=server.RPC_Server()
