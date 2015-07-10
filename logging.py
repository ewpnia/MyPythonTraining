# -*- coding: utf-8 -*-

import os
import os.path
import logging


def initlog():
    
    # 生成一个日志对象
    logger = logging.getLogger()

    # 生成一个Handler。
    # logging支持许多Handler，
    # 象FileHandler, SocketHandler, SMTPHandler等，
    # 我由于要写文件就使用了FileHandler。
    # logfile是一个全局变量，它就是一个文件名，如：'crawl.log'
    logfile = 'test.log'
    hdlr = logging.FileHandler('sendlog.txt')

    # 成一个格式器，用于规范日志的输出格式。如果没有这行代码，那么缺省的
    # 格式就是："%(message)s"。也就是写日志时，信息是什么日志中就是什么，
    # 没有日期，没有信息级别等信息。logging支持许多种替换值，详细请看
    # Formatter的文档说明。这里有三项：时间，信息级别，日志信息
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # 将格式器设置到处理器上
    hdlr.setFormatter(formatter)

    # 将处理器加到日志对象上
    logger.addHandler(hdlr)

    # 设置日志信息输出的级别。logging提供多种级别的日志信息，如：NOTSET, 
    # DEBUG, INFO, WARNING, ERROR, CRITICAL等。每个级别都对应一个数值。
    # 如果不执行此句，缺省为30(WARNING)。可以执行：logging.getLevelName
    # (logger.getEffectiveLevel())来查看缺省的日志级别。日志对象对于不同
    # 的级别信息提供不同的函数进行输出，如：info(), error(), debug()等。当
    # 写入日志时，小于指定级别的信息将被忽略。因此为了输出想要的日志级别一定
    # 要设置好此参数。这里我设为NOTSET（值为0），也就是想输出所有信息
    logger.setLevel(logging.NOTSET)

    return logger


logging=initlog()
logging.info('注册')




# ***************************************************************************************************************************************************************




#为日志模块配置基本信息，包括filename, filemode, format, datefmt, level, stream
#filename, 日志保存地址，如果被配置了，则会自动创建fileHandler 作为handler
#filemode, 打开日志时的模式，默认为'a'，表示追加，如果设置为'w'则表示每次调用这个log都会覆盖原来的旧文档
#format, 日志输出的格式
#datefmt, 定义日期格式
#level, 设置日志级别，对于低于该基本的日志一律忽略, 模块默认的分六种，由高到低为：CRITICAL， ERROR，WARN，INFOR，DEBUG，NOTSET
#stream, 设置特定的初始流用于初始化streamHandler

logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG, format = '%(asctime)s - %(levelname)s: %(message)s') 
logging.debug('debug')
logging.debug('info')
logging.warning('warn')
logging.error('error')


# -------------------------------------------------------------------------------------------------------

# format形式：
# %(name)s              Logger的名字

# %(levelno)s           数字形式的日志级别

# %(levelname)s         文本形式的日志级别

# %(pathname)s          调用日志输出函数的模块的完整路径名，可能没有

# %(filename)s          调用日志输出函数的模块的文件名

# %(module)s            调用日志输出函数的模块名

# %(funcName)s          调用日志输出函数的函数名

# %(lineno)d            调用日志输出函数的语句所在的代码行

# %(created)f           当前时间，用UNIX标准的表示时间的浮点数表示

# %(relativeCreated)d   输出日志信息时的，自Logger创建以来的毫秒数

# %(asctime)s           字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒

# %(thread)d            线程ID。可能没有

# %(threadName)s        线程名。可能没有

# %(process)d           进程ID。可能没有

# %(message)s           用户输出的消息

# ------------------------------------------------------------------------------------------------------------------

#创建logger对象，对象之间有层级关系，子对象可以直接继承父对象的一些设置
p = logging.getLogger('root')
c1 = logging.getLogger('root.c1')
c2 = logging.getLogger('root.c2')


#关闭日志，并将所有内容写入到磁盘中
logging.shutdown()


#各种handler
#logger可以雇用handler来棒它处理日志，主要有FileHandler(输出到文件)跟StreamHandler(输出到控制台)两种
p = logging.getLogger('root')
console = logging.StreamHandler()
p.addHandler(console)