# -*- coding: utf-8 -*-
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import GlobalPara as G_Para
import MyFiles


def downlink_test(shortID, cmd, packet_cnt_range=3, packet_intervals=1):
    m = PyMouse()
    k = PyKeyboard()
    shortID_cnt = 0  # 短地址键值计数
    packet_cnt = 1  # 包计数
    send_packet = 'a'  # 组包用字符串
   # m.click(132, 29, 1, 1)  # 激活窗口，不知道还有啥好方法
    while packet_cnt <= packet_cnt_range:
        for shortID_cnt in range(len(shortID)):
            m.click(370, 850, 1, 1)  # 激活窗口，不知道还有啥好方法
            packet_cnt_str = str(packet_cnt)
            # shortID[shortID_cnt] = shortID[shortID_cnt].zfill(4)
            if cmd == 'ping':
                send_packet = 'at+ping,' + shortID[shortID_cnt].zfill(
                    4) + ',08' + shortID[shortID_cnt] + '38' + packet_cnt_str.zfill(8)
            elif cmd == 'st1':  # 20s上行测试开启
                send_packet = 'at+st,' + shortID[shortID_cnt].zfill(4) + ',Wd40001'
            elif cmd == 'st2':  # 120s上行测试开启
                send_packet = 'at+st,' + shortID[shortID_cnt].zfill(4) + ',Wd50001'
            elif cmd == 'st3':  # 120s上行测试关闭
                send_packet = 'at+st,' + shortID[shortID_cnt].zfill(4) + ',Wd50000'
            elif cmd == 'st4':  # 下行测试
                send_packet = 'at+st,' + shortID[shortID_cnt].zfill(4) +  ',Wd3' + packet_cnt_str.zfill(3) + '11111111111111111111111111'
            elif cmd == 'st5':  # 下行测试成功率回读
                send_packet = 'at+st,' + shortID[shortID_cnt].zfill(4) + ',Wd6' + packet_cnt_str.zfill(3) + '1'
            k.type_string(send_packet)
            k.tap_key(k.enter_key)
            MyFiles.log_list(send_packet)
            time.sleep(packet_intervals)
        packet_cnt = packet_cnt + 1


def task_ping(interval=5):
    MyFiles.log_list('at+ping 自动发送测试开始')
    downlink_test(shortID, 'ping', 50, interval)
    MyFiles.log_list('at+ping 自动发送测试结束')


def task_st(interval=5):
    MyFiles.log_list('下行测试开始')
    downlink_test(shortID, 'st4', 50, interval)
    #downlink_test(shortID, 'st5', 5, interval)
    MyFiles.log_list('下行测试结束')


def task_up20s_on(interval=5):
    cnt = 0
    MyFiles.log_list('20s上行测试开始')
    downlink_test(shortID, 'st1', 5, interval)
    while cnt != 200:
        cnt = cnt + 1
        time.sleep(10)  # 阻塞式休眠
        MyFiles.log_list('20s上行测试中。。。')
    MyFiles.log_list('20s上行测试结束')


def task_up120s_on_1(interval=5):
    MyFiles.log_list('待测节点上行心跳开启中')
    downlink_test(shortID, 'st2', 5, interval)
    MyFiles.log_list('待测节点上行心跳开启完成')


def task_up120s_on_2(interval=5):
    MyFiles.log_list('非待测节点上行心跳开启中')
    downlink_test(shortID_hertBeat, 'st2', 5, interval)
    MyFiles.log_list('非待测节点上行心跳开启完成')


def task_up120s_off(interval=5):
    MyFiles.log_list('待测节点上行心跳关闭中')
    downlink_test(shortID, 'st3', 5, interval)
    MyFiles.log_list('待测节点上行心跳关闭完成')

def comp_test(cnt = 1):
    global shortID, shortID_hertBeat
    shortID = G_Para.get_value('shortID')
    shortID_hertBeat = G_Para.get_value('shortID_hertBeat')
    print(shortID)
    print(shortID_hertBeat)
    MyFiles.log_list('综合测试开始')
    task_up120s_off()
    task_up120s_on_2()
    for i in range(cnt):
        task_ping()
        task_up20s_on()
        task_st()
    task_up120s_on_1()
    MyFiles.log_list('综合测试结束')
