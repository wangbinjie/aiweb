# -*- coding: utf-8 -*-
import GlobalPara as G_Para
import json



def test1():
    filename = G_Para.get_value('filename')
    print(filename)


G_Para._init()
file2 = 'nodelist.json'
with open(file2, 'r', encoding="utf-8") as file:
    nodelist = json.load(file)
    # print(nodelist)

shortID_dict = nodelist.get('测试节点')
shortID_dict_no_use = nodelist.get('心跳节点')
print(shortID_dict)
print(shortID_dict_no_use)

G_Para.set_value('shortID', shortID_dict)
G_Para.set_value('shortID_hertBeat', shortID_dict_no_use)
shortID = G_Para.get_value('shortID')
shortID_hertBeat = G_Para.get_value('shortID_hertBeat')

print('------------------------------------')
print(shortID)
print(shortID_hertBeat)