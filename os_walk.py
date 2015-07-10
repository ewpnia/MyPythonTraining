# -*- coding: utf-8 -*-

import os

# rootdir = r"D:\Holemar\1.notes\28.Python\test"
rootdir = os.getcwd()   # 获取当前工作路径

# os.walk 返回一个三元组，
# 其中parent表示所在目录, dirnames是所有目录名字的列表, filenames是所有文件名字的列表
for parent,dirnames,filenames in os.walk(rootdir):

    # 所在目录
    print("parent is:" + parent)

    # 遍历此目录下的所有目录(不包含子目录)
    for dirname in dirnames:
        print(" dirname is:" + dirname)

    # 遍历此目录下的所有文件
    for filename in filenames:
        print(" filename with full path:" + os.path.join(parent, filename))


# 列表显示出某目录下的所有文件及目录(不包括子目录的内容)
ls = os.listdir(rootdir)

# -----------------------------------------------------------------------------------------------


# 示例输出

# parent is:D:\ICBC
# dirname is:Code
# dirname is:sztc2
# dirname is:工作记录
# dirname is:文档
# filename with full path:D:\ICBC\.tags
# filename with full path:D:\ICBC\.tags_sorted_by_file
# filename with full path:D:\ICBC\615行内实例
# filename with full path:D:\ICBC\ICBC控制台.txt
# filename with full path:D:\ICBC\ICBC行内格式.txt
# filename with full path:D:\ICBC\ldd信息.rar
# filename with full path:D:\ICBC\办公相关.txt
# parent is:D:\ICBC\Code
# filename with full path:D:\ICBC\Code\fstoicbcmsghandler.cpp
# filename with full path:D:\ICBC\Code\fstoicbcmsghandler.h
# filename with full path:D:\ICBC\Code\icbcassistantsegment.h
# filename with full path:D:\ICBC\Code\icbcbcomclient.cpp
# filename with full path:D:\ICBC\Code\icbcbcomclient.h
# filename with full path:D:\ICBC\Code\icbcbcomserver.cpp
# filename with full path:D:\ICBC\Code\icbcbcomserver.h
# filename with full path:D:\ICBC\Code\icbcprotocol.cpp
# filename with full path:D:\ICBC\Code\icbcprotocol.h
# filename with full path:D:\ICBC\Code\icbcthread.cpp
# filename with full path:D:\ICBC\Code\icbcthread.h
# filename with full path:D:\ICBC\Code\icbctimer.cpp
# filename with full path:D:\ICBC\Code\icbctimer.h
# filename with full path:D:\ICBC\Code\icbctofsmsghandler.cpp
# filename with full path:D:\ICBC\Code\icbctofsmsghandler.h
# parent is:D:\ICBC\sztc2
# filename with full path:D:\ICBC\sztc2\cfg.tar
# filename with full path:D:\ICBC\sztc2\cvob.tar
# filename with full path:D:\ICBC\sztc2\icbc.tar
# filename with full path:D:\ICBC\sztc2\localcvob.tar
# filename with full path:D:\ICBC\sztc2\schema .tar
# filename with full path:D:\ICBC\sztc2\tools.tar
# parent is:D:\ICBC\工作记录
# filename with full path:D:\ICBC\工作记录\2013-11-25.docx
# filename with full path:D:\ICBC\工作记录\2013-11-26.docx
# filename with full path:D:\ICBC\工作记录\2013-11-27.docx
# filename with full path:D:\ICBC\工作记录\2013-11-28.docx
# filename with full path:D:\ICBC\工作记录\2013-12-02.docx
# filename with full path:D:\ICBC\工作记录\2013-12-03.docx
# filename with full path:D:\ICBC\工作记录\2013-12-04.docx
# filename with full path:D:\ICBC\工作记录\2013-12-05.docx
# filename with full path:D:\ICBC\工作记录\ICBC-子进程.zip
# filename with full path:D:\ICBC\工作记录\~$13-12-05.docx
# filename with full path:D:\ICBC\工作记录\总体进程.docx
# parent is:D:\ICBC\文档
# dirname is:一期文档
# filename with full path:D:\ICBC\文档\AIX编译报错 No licenses available 如何解决.
# docx
# filename with full path:D:\ICBC\文档\ICBC-SZTC_测试情况_v0.2.xlsx
# filename with full path:D:\ICBC\文档\回应报文格式.txt
# filename with full path:D:\ICBC\文档\工行前置需求说明书（20131024）.doc
# filename with full path:D:\ICBC\文档\总行.深圳同城通讯前置方案.doc
# filename with full path:D:\ICBC\文档\深中行与人行前置接口说明.doc
# parent is:D:\ICBC\文档\一期文档
# filename with full path:D:\ICBC\文档\一期文档\工商银行接口概要设计.doc
# filename with full path:D:\ICBC\文档\一期文档\深圳同城前置系统安装配置文档.doc
# filename with full path:D:\ICBC\文档\一期文档\深圳同城前置系统日常维护手册.doc
# filename with full path:D:\ICBC\文档\一期文档\深圳同城安装步骤.doc
# >>>





# -----------------------------------------------------------------------------------------------------------

import os
    
#常用函数有三种：分隔路径，找出文件名，找出盘符(window系统)，找出文件的扩展名。
spath = "d:/test/test.7z"

# 下面三个分割都返回二元组
# 分隔目录和文件名
p,f = os.path.split(spath)  # 注意二元组的接收
print("dir is:" + p)    # 打印: d:/test
print(" file is:" + f)  # 打印: test.7z

# 分隔盘符和文件名
drv,left = os.path.splitdrive(spath)
print(" driver is:" + drv)   # 打印: d:
print(" left is:" + left)    # 打印: /test/test.7z

# 分隔文件和扩展名
f,ext = os.path.splitext(spath)
print(" f is: " + f)    # 打印: d:/test/test
print(" ext is:" + ext) # 打印: 7z



# -----------------------------------------------------------------------------------------------------------


# 迭代 walk，返回 "(路径，子目录列表，文件列表)"，可配合 fnmatch 做通配符过滤。
import fnmatch
import os

for path, dirs, files in os.walk("."):
    for f in files:
        if fnmatch.fnmatch(f, "*.py"):
            print os.path.join(path, f)
# ./main.py
# ./bak/amqplib_test.py
# ./bak/eventlet_test.py
# ./bak/extract_text.py
# ./bak/fabric_test.py