# # -*- coding: utf-8 -*-
# import GlobalPara as G_Para
# import json
#
#
#
# def test1():
#     filename = G_Para.get_value('filename')
#     print(filename)
#
#
# G_Para._init()
# file2 = 'nodelist.json'
# with open(file2, 'r', encoding="utf-8") as file:
#     nodelist = json.load(file)
#     # print(nodelist)
#
# shortID_dict = nodelist.get('测试节点')
# shortID_dict_no_use = nodelist.get('心跳节点')
# print(shortID_dict)
# print(shortID_dict_no_use)
#
# G_Para.set_value('shortID', shortID_dict)
# G_Para.set_value('shortID_hertBeat', shortID_dict_no_use)
# shortID = G_Para.get_value('shortID')
# shortID_hertBeat = G_Para.get_value('shortID_hertBeat')
#
# print('------------------------------------')
# print(shortID)
# print(shortID_hertBeat)

# from ctypes import windll as win32
# WM_CHAR = 0x0102
#
# try:
#     hWnd = win32.user32.FindWindowW('SecureCRT Application', None)
#     print(hWnd)
#     assert hWnd
#     hEdit = win32.user32.FindWindowExW(hWnd, None, 'Serial-COM13 - SecureCRT', None)
#     assert hEdit
# except AssertionError:
#     print('SecureCRT not found')
# else:
#     for char in 'Hello, 世界\n':
#         win32.user32.SendMessageW(hEdit, WM_CHAR, ord(char), None)


import os
import copy
from datetime import *


xlist = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.bin']
if len(xlist) == 0:
    print('未找到 .bin 文件')
else:
    for file_old in xlist:
        print('原始文件名：', file_old)
        file_new = copy.deepcopy(file_old)
        date_now = date.today()
        date_now = date_now.strftime('%Y%m%d')
        file_new = file_new.replace('.bin', date_now + '.bin')
        try:
            os.rename(file_old, file_new)
            print('重命名成功：', file_new)
        except:
            print('重命名失败')
