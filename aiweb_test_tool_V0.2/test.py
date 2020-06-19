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
#
#
# import os
# import copy
# from datetime import *
#
#
# xlist = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.bin']
# if len(xlist) == 0:
#     print('未找到 .bin 文件')
# else:
#     for file_old in xlist:
#         print('原始文件名：', file_old)
#         file_new = copy.deepcopy(file_old)
#         date_now = date.today()
#         date_now = date_now.strftime('%Y%m%d')
#         file_new = file_new.replace('.bin', date_now + '.bin')
#         try:
#             os.rename(file_old, file_new)
#             print('重命名成功：', file_new)
#         except:
#             print('重命名失败')


# from turtle import *
#
# # 设置色彩模式是RGB:
# colormode(255)
#
# lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# width(lv)
#
# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
#
# penup()
# bk(l)
# pendown()
# fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed("fastest")
#
# draw_tree(l, 4)
#
# done()
#
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import threading
# # import asyncio
# #
# # @asyncio.coroutine
# # def hello():
# #     print('Hello world! (%s)' % threading.currentThread())
# #     yield from asyncio.sleep(1)
# #     print('Hello again! (%s)' % threading.currentThread())
# #
# # loop = asyncio.get_event_loop()
# # tasks = [hello(), hello()]
# # loop.run_until_complete(asyncio.wait(tasks))
# # loop.close()

# nums = [1, 2, 3, 4]
# sums = [0]
#
# for i in range(len(nums)):
#     sums.append(sums[i]+nums[i])
#     # print(sums)
# sums = sums[1:]
# # print(sums)

# # arr = [4, 3, 1, 1, 3, 3, 2]
# # k = 3
# arr = [1]
# k = 1
# dict = {}
# list = []
# for key in arr:
#     dict[key] = dict.get(key, 0) + 1
# for k, v in dict.items():
#     list.append(v)
# # print(list)
# list = sorted(list)
# # print(list)
# while len(list)!=0:
#     if list[0] <= k:
#         k = k - list[0]
#         list.pop(0)
#         # print(list)
#     else:
#         # print(len(list))
#         break
# print(len(list))
# from collections import Counter
# arr = [1]
# k = 1
#
# word = Counter(arr)
# res = sorted(word.items(), key=lambda item: item[1])
# n = len(res)
# for i in range(len(res)):
#     if res[i][1] <= k:
#         k -= res[i][1]
#         n -= 1
#     else:
#         break
# print(n)
# arr = [2,4,1,8,3,5,1,3]
# k = 3
# dict = {}
# list = []
# for key in arr:
#     dict[key] = dict.get(key, 0) + 1
# # for key, value in dict.items():
# #     list.append(dict.items())
# # print(list)
# list = sorted(dict.items(), key=lambda item: item[1])
# # print(list)
# # print(list[0][1])
# while len(list) != 0:
#     if list[0][1] <= k:
#         k = k - list[0][1]
#         print(list[0][1])
#         print(k)
#         list.pop(0)
#         print(list)
#     else:
#         print(len(list))
#         print(len(list))
#         break
# print(len(list))
#
# from collections import Counter
# class Solution:
#     def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
#         # word = Counter(arr)
#         res = sorted(Counter(arr).items(),key = lambda item:item[1])
#         n = len(res)
#         for i in range(len(res)):
#             if res[i][1]<=k:
#                 k-=res[i][1]
#                 n-=1
#             else:
#                 break
#         return n

nums = [2, 2, 3, 4]
sum = 0
list_len = len(nums)
if list_len < 3:
    sum = 0
else:
    list = sorted(nums)
    for i, a in enumerate(list[:-2]):
        for j, b in enumerate(list[i + 1:-1]):
            for k, c in enumerate(list[i + j + 2:]):
                cnt = a + b
                if cnt > c:
                    sum = sum + 1
                elif cnt == c:
                    continue
print(sum)

# import bisect
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         # won't exceed 1000
#         # integer is [0, 1000]
#         # Time complexity : O(N**2*logN)
#         # Space complexity : O(1)
#         res = 0
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] == 0: continue
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == 0: continue
#                 a, b = nums[i], nums[j]
#                 index = bisect.bisect_right(nums, a + b - 1) - 1
#                 res += index - j
#         return res


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 2 pointers -- 对撞型 -- 2sum类
        if not nums or len(nums) < 3:
            return 0

        _num = 0
        nums = sorted(nums)

        # i 对应于最大的那条边
        for i in range(len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    _num += right - left
                    right -= 1
                else:
                    left += 1

        return _num
