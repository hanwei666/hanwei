#!/usr/bin/env python
# _*_encoding:utf-8 _*_
__author__='han'
import os,sys
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from core import clinet

run = clinet.Rpc_Clinet()
run.Command()
