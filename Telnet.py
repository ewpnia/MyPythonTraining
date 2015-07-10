# -*- coding: utf-8 -*-

import telnetlib
import time


def do_telnet(Host, username, password, finish, commands):
    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host)

    # 输入登录用户名 
    tn.read_until('login: ')
    tn.write(username + '\n')

    # 输入登录密码 
    tn.read_until('Password: ')
    tn.write(password + '\n')

    tn.read_until(finish,1)
    for command in commands:
        tn.write('%s\n' % command)
        time.sleep(1)
        print tn.read_very_eager()

    #执行完毕后，终止Telnet连接
    tn.write('exit\n')
    tn.close()


if __name__ == '__main__':
    # 配置选项  
    Host = '172.168.9.1'    # Telnet服务器IP
    username = 'aps-djw'    # 登录用户名
    password = 'djw'        # 登录密码
    finish = '$'           # 命令提示符（标识着上一条命令已执行完毕）


    xml_no = [
        '102', '103', '104', '106', '10601',
        '10701', '10702', '112', '206', '402',
        '404', '406', '501', '602', '603',
        '604', '605', '606', '607', '608',
        '609', '611', '614', '615', '617',
        '618', '619', '620', '622', '624',
        '625', '630', '632', '634', '636',
        '638', '640', '644', '661', '663',
        '664', '666', '680', '681', '687',
        '803', '804', '805',
    ]
    format = './mqput szfs.%s.001.01.xml QMBANK CBHB_BANK_1'
    xml_list = [format % no for no in xml_no]
    # print xml_list
    

    commands = [
        # 'ls',
        # 'pwd',
        # 'cd /cvob/app/sztc2/source/cbhb',
        # 'ls -l | grep fsmsg',
        'cd mqput',
        # './mqput szfs.620.001.01.xml QMBANK CBHB_BANK_1',
    ]

    commands.extend(xml_list)

    # print commands
    do_telnet(Host, username, password, finish, commands)

    



# tn.write('ls\n')
# # 防止网络时延导致数据还没从socket完全取回来
# time.sleep(1)
# print tn.read_very_eager()
# print tn.read_until(finish,1)



# python的telnetlib里有多个read方法，分别是
# read_all()
# read_until()
# read_lazy()
# read_very_lazy()
# read_eager()
# read_very_eager()