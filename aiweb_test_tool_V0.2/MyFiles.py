# -*- coding: utf-8 -*-
import sys
from result_storage import result_storage
import datetime
import tkinter as tk
from tkinter import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import re
import openpyxl
from openpyxl.styles import Alignment
from openpyxl.styles import numbers
from openpyxl.styles import PatternFill
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Series, Reference
import logging

import MyUI

class Myexcel(object):
    def __init__(self, file_name, file_path,sheet_name,sheet_header,):
        self.file_name = file_name
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet_header = sheet_header


    def creat_excel(self):
        pass

    def excel_write(sheet_num = 0,row = 1,col = 1,data = ''):
        pass

    def set_cell_color(column='a', row=1, data=100, test_num=0):
        pass

    def result_to_excel(target_node='', data_time='', success_rate=100.00, test_cycle_cnt=0, test_num=0, shortID_dict1=[], backup=0):
        pass

    def creat_bar_chart(test_num=0, chart_title=''):
        pass

def route_save():
    global  filename
    filename = e.get()
    excel_create()
    text.insert((1.0), '路径确认 ：%s \n'%(filename))
    text.insert((1.0), '---------------------------------------\n')
    window.update()