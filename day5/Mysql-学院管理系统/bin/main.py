#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__ ="han"
import sys,os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from core.student_system import View_Interface

start = View_Interface()
start.Menu()
