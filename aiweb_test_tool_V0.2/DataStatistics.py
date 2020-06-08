# -*- coding: utf-8 -*-
import re
import GlobalPara as G_Para
import MyFiles


def downlink_sucess_rate(shortID, result_dict, filename='新建文本文档.txt', target_node='0001'):
    print(filename)
    f = open(filename, encoding='utf-8')
    rows = len(f.readlines())
    f = open(filename, encoding='utf-8')
    # sample_str = '     0000  75 33 30 30 30 31 31 31  31 31 31 31 31 31 31 31  u3000111 11111111'
    nun_per_nodes = 50.0  # 单节点测试次数
    rows_cnt = 0  # 读取行数计数
    valid_rows_cnt = 0  # 有效行计数
    node_num = 0  # 解析出的节点编号
    data_time_now = '-'
    data_time = '-'
    packet_cnt = -1
    result_dict[target_node] = 0
    test_cycle_cnt = 0
    while rows_cnt < rows:
        str_check = f.readline().strip()
        rows_cnt = rows_cnt + 1
        if str_check[:5] == 'Frame':
            data_time_now = str_check[-26:-7]
        if str_check[:9] == 'recv_pong'and str_check[:13] !='recv_pong not':  # 定位目标数据的位置
            #node_num = hex(int(str_check[10:13]))  # 获取当前节点小名，并转换为16进制
            node_num = re.match(r'recv_pong (.*) ', str_check)
            try:
                node_num = hex(int(node_num.group(1)))
            except:
                MyFiles.log_list('节点格式转换异常')
            else:
                node_num = str(node_num).upper().replace('0X','').zfill(4)
                packet_cnt_now = str_check[-3:-1]  # 获取当前数据包计数
                if node_num == target_node:  # 比较当前数据包所属节点 Short ID 与 目标节点是否一致
                    if packet_cnt < int(packet_cnt_now):
                        packet_cnt = int(packet_cnt_now)
                        result_dict[target_node] = result_dict[target_node] + 1
                        data_time = data_time_now
                    else:
                        MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                              % (target_node, str(result_dict[target_node]).rjust(2),
                                 int(result_dict[target_node]) / nun_per_nodes * 100, data_time))
                        test_cycle_cnt += 1
                        success_rate = int(result_dict[target_node]) / nun_per_nodes
                        MyFiles.result_to_excel(target_node,data_time,success_rate,test_cycle_cnt,0,shortID)
                        result_dict[target_node] = 0
                        packet_cnt = 0
        if rows_cnt == rows - 1:
            MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                        % (target_node, str(result_dict[target_node]).rjust(2),
                           int(result_dict[target_node]) / nun_per_nodes * 100, data_time))
            test_cycle_cnt += 1
            success_rate = int(result_dict[target_node]) / nun_per_nodes
            MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 0, shortID)
            result_dict[target_node] = 0
            packet_cnt = 0


def uplink_sucess_rate(cmd, shortID, result_dict, filename='新建文本文档.txt', target_node='0001'):
    f = open(filename, encoding='utf-8')
    rows = len(f.readlines())
    f = open(filename, encoding='utf-8')
    sample_str = '     0000  75 33 30 30 30 31 31 31  31 31 31 31 31 31 31 31  u3000111 11111111'
    nun_per_nodes = 100.0  # 单节点测试次数
    rows_cnt = 0  # 读取行数计数
    valid_rows_cnt = 0  # 有效行计数
    data_time_now = '-'
    data_time = '-'
    packet_cnt = 0
    time_interval = 0
    test_cycle_cnt = 0
    while rows_cnt < rows:
        str_check = f.readline().strip()
        rows_cnt = rows_cnt + 1
        if str_check[:5] == 'Frame':
            data_time_now = str_check[-26:-7]
        if str_check == 'procBody application data':  # 定位目标数据的位置，当前为目标数据的上一行
            str_check = f.readline().strip()
            rows_cnt = rows_cnt + 1
            str_check = f.readline().strip()
            rows_cnt = rows_cnt + 1
            rows_cnt = rows_cnt + 1
            if len(str_check) == len(sample_str.strip()):  # 判断数据长度是否满足要求
                if str_check[-17:-15] == cmd:  # 判断是否为 20/120s 下行数据
                    packet_cnt_now = str_check[-15:-12]  # 获取当前数据包计数
                    while str_check[:5] != 'saddr':
                        str_check = f.readline().strip()
                        rows_cnt = rows_cnt + 1
                    if str_check[6:10] == target_node:  # 比较当前数据包所属节点 Short ID 与 目标节点是否一致
                        if packet_cnt < int(packet_cnt_now):
                            packet_cnt = int(packet_cnt_now)
                            result_dict[target_node] = result_dict[target_node] + 1
                            data_time = data_time_now
                        else:
                            if cmd == 'u1':#20s间隔上行数据
                                if data_time == '-':
                                    data_time = data_time_now
                                time_interval = int(data_time_now[8:10])*24*3600+int(data_time_now[11:13])*3600+int(data_time_now[14:16])*60+int(data_time_now[17:19])\
                                                -int(data_time[8:10])*24*3600-int(data_time[11:13])*3600-int(data_time[14:16])*60-int(data_time[17:19])

                                if time_interval < 100:
                                    packet_cnt = int(packet_cnt_now)
                                    result_dict[target_node] = result_dict[target_node] + 1
                                    data_time = data_time_now
                                else:
                                    MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                                          % (target_node, str(result_dict[target_node]).rjust(2),
                                             int(result_dict[target_node]) / nun_per_nodes * 100, data_time))
                                    test_cycle_cnt += 1
                                    success_rate = int(result_dict[target_node]) / nun_per_nodes
                                    MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 1,shortID)
                                    result_dict[target_node] = 0
                                    packet_cnt = 0
                            if cmd == 'u2':#120s间隔上行数据
                                if test_cycle_cnt == 0:
                                    test_cycle_cnt += 1
                                else:
                                    MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                                                % (target_node, str(result_dict[target_node]).rjust(2),
                                                   int(result_dict[target_node]) / nun_per_nodes * 100, data_time))
                                    success_rate = int(result_dict[target_node]) / nun_per_nodes
                                    shortID_hertBeat = G_Para.get_value('shortID_hertBeat')
                                    MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 2,shortID_hertBeat)
                                    MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 3,shortID_hertBeat,1)
                                    test_cycle_cnt += 1
                                    result_dict[target_node] = 0
                                    packet_cnt = 0
                        valid_rows_cnt = valid_rows_cnt + 1
        if rows_cnt == rows - 1:
            if cmd == 'u1':
                # MyFiles.log_list('time_interval%d\n' % (time_interval))
                MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                            % (target_node, str(result_dict[target_node]).rjust(2),
                               int(result_dict[target_node]) / nun_per_nodes * 100, data_time))
                test_cycle_cnt += 1
                success_rate = int(result_dict[target_node]) / nun_per_nodes
                MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 1, shortID)
                result_dict[target_node] = 0
                packet_cnt = 0
            if cmd == 'u2':#最后一组使用当前包计数作为改组的总包数
                if packet_cnt == 0:
                    MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                                % (target_node, str(result_dict[target_node]).rjust(2),
                                   int(result_dict[target_node]) / nun_per_nodes * 100, data_time))
                    success_rate = int(result_dict[target_node]) / nun_per_nodes
                else:
                    MyFiles.log_list('节点编号：%s  成功次数:%s  成功率:%05.2f%% 测试时间：%s\n'
                                % (target_node, str(result_dict[target_node]).rjust(2),
                                   int(result_dict[target_node]) / packet_cnt * 100, data_time))
                    success_rate = int(result_dict[target_node]) / packet_cnt
                if test_cycle_cnt == 0:
                    test_cycle_cnt += 1
                shortID_hertBeat = G_Para.get_value('shortID_hertBeat')
                MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 2, shortID_hertBeat)
                MyFiles.result_to_excel(target_node, data_time, success_rate, test_cycle_cnt, 3, shortID_hertBeat, 1)
                result_dict[target_node] = 0
                packet_cnt = 0

def sucess_rate_ping():
    shortID = G_Para.get_value('shortID')
    result_dict = G_Para.get_value('result_dict')
    filename = G_Para.get_value('logName')
    for shortID_cnt in range(len(shortID)):
        target_node = shortID[shortID_cnt]
        downlink_sucess_rate(shortID, result_dict, filename, target_node)
        MyFiles.log_list( '---------------------------------------\n')
    MyFiles.creat_bar_chart(0, 'Ping 成功率统计图')
    MyFiles.excel_save()
    MyFiles.task_info_show('下行测试统计结果')


def sucess_rate_up20s():
    shortID = G_Para.get_value('shortID')
    result_dict = G_Para.get_value('result_dict')
    filename = G_Para.get_value('logName')
    for shortID_cnt in range(len(shortID)):
        target_node = shortID[shortID_cnt]
        uplink_sucess_rate(
            'u1', shortID, result_dict, filename, target_node)
        MyFiles.log_list( '---------------------------------------\n')
    MyFiles.creat_bar_chart(1, '20s 上行成功率统计图')
    MyFiles.excel_save()
    MyFiles.task_info_show('20s上行测试统计结果')


def sucess_rate_up120s():
    shortID = G_Para.get_value('shortID')
    shortID_hertBeat = G_Para.get_value('shortID_hertBeat')
    result_dict = G_Para.get_value('result_dict')
    filename = G_Para.get_value('logName')
    for shortID_cnt in range(len(shortID_hertBeat)):
        target_node = shortID_hertBeat[shortID_cnt]
        uplink_sucess_rate(
            'u2', shortID, result_dict, filename, target_node)
        MyFiles.log_list( '---------------------------------------\n')
    MyFiles.creat_bar_chart(2, '120s 上行成功率统计图')
    MyFiles.excel_save()
    MyFiles.task_info_show('120s上行测试统计结果')


def sucess_rate_all():
    MyFiles.task_info_show('一键统计开始')
    sucess_rate_ping()
    sucess_rate_up20s()
    sucess_rate_up120s()
    MyFiles.task_info_show('一键统计结束')