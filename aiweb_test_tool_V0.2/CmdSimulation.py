# -*- coding: utf-8 -*-
import time
import GlobalPara as G_Para
import MyFiles
from pywinauto.application import Application


def downlink_test(shortID, cmd, packet_cnt_range=3, packet_intervals=1):
    autoCmd = WinControl()
    packet_cnt = 1  # 包计数
    while packet_cnt <= packet_cnt_range:
        for shortID_cnt in range(len(shortID)):
            packet_cnt_str = str(packet_cnt).zfill(3)
            shortID_str = shortID[shortID_cnt].zfill(4)
            cmd_dict = {
                'ping': 'at{VK_ADD}ping,' + shortID_str + ',08' + shortID_str + '38' + packet_cnt_str.zfill(3),
                # 20s上行测试开启
                'st1': 'at{VK_ADD}st,' + shortID_str + ',Wd40001'+ packet_cnt_str,
                # 120s上行测试开启
                'st2': 'at{VK_ADD}st,' + shortID_str + ',Wd50001'+ packet_cnt_str,
                # 120s上行测试关闭
                'st3': 'at{VK_ADD}st,' + shortID_str + ',Wd50000'+ packet_cnt_str,
                # 下行测试
                'st4': 'at{VK_ADD}st,' + shortID_str + ',Wd3' + packet_cnt_str + '01234567890123456789',
                # 下行测试成功率回读
                'st5': 'at{VK_ADD}st,' + shortID_str + ',Wd6' + packet_cnt_str + '1',
            }
            send_packet = cmd_dict[cmd]
            autoCmd.typecmd(send_packet)
            MyFiles.task_info_show(send_packet)
            time.sleep(packet_intervals)
        packet_cnt = packet_cnt + 1


def task_ping(interval=5):
    MyFiles.task_info_show('at+ping 自动发送测试开始')
    downlink_test(shortID, 'ping', 50, interval)
    MyFiles.task_info_show('at+ping 自动发送测试结束')


def task_st(interval=5):
    MyFiles.task_info_show('下行测试开始')
    downlink_test(shortID, 'st4', 50, interval)
    MyFiles.task_info_show('下行测试结束')


def task_up20s_on(interval=5):
    cnt = 0
    MyFiles.task_info_show('20s上行测试开始')
    downlink_test(shortID, 'st1', 5, interval)
    while cnt != 200:
        cnt = cnt + 1
        time.sleep(10)  # 阻塞式休眠
        MyFiles.task_info_show('20s上行测试中。。。')
    MyFiles.task_info_show('20s上行测试结束')


def task_up120s_on_1(interval=5):
    MyFiles.task_info_show('待测节点上行心跳开启中')
    downlink_test(shortID, 'st2', 5, interval)
    MyFiles.task_info_show('待测节点上行心跳开启完成')


def task_up120s_on_2(interval=5):
    MyFiles.task_info_show('非待测节点上行心跳开启中')
    downlink_test(shortID_hertBeat, 'st2', 5, interval)
    MyFiles.task_info_show('非待测节点上行心跳开启完成')


def task_up120s_off(interval=5):
    MyFiles.task_info_show('待测节点上行心跳关闭中')
    downlink_test(shortID, 'st3', 5, interval)
    MyFiles.task_info_show('待测节点上行心跳关闭完成')


def comp_test(cnt=1):
    global shortID, shortID_hertBeat
    shortID = G_Para.get_value('shortID')
    shortID_hertBeat = G_Para.get_value('shortID_hertBeat')
    print(shortID)
    print(shortID_hertBeat)
    MyFiles.task_info_show('综合测试开始')
    task_up120s_off()
    task_up120s_on_2()
    for i in range(cnt):
        task_ping()
        task_up20s_on()
        task_st()
    task_up120s_on_1()
    MyFiles.task_info_show('综合测试结束')


class WinControl:
    def __init__(self):
        self.app = Application()
        self.app.connect(
            path=r"C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe")
        self.win = self.app.window()

    def typecmd(self, cmd=''):
        self.win.type_keys(cmd + '{ENTER}', set_foreground=True)
        # self.win.minimize()


if __name__ == '__main__':
    win = WinControl()
    # win.start()
    for i in range(5):
        win.typecmd('ps')
