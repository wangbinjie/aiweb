# -*- coding: utf-8 -*-
import GlobalPara as G_Para
import json

def test1():
    filename = G_Para.get_value('filename')
    print(filename)

file2 = 'nodelist.json'
with open(file2, 'r', encoding="utf-8") as file:
    nodelist = json.load(file)
    # print(nodelist)

shortID_dict = nodelist.get('测试节点')
shortID_dict_no_use = nodelist.get('心跳节点')
print(shortID_dict)
print(shortID_dict_no_use)