# -*- coding: utf-8 -*-

from random import *


# 按一次回车键roll一次点，直到按Ctrl+C退出程序。
# 不同的的是第一个用的是randrange()函数，
# 第二个用的是range()函数和choice()函数。
while True:
    try:
        raw_input()
        print randrange(1, 101)
        # rolls = range(1,101)
        # print choice(rolls)
    except KeyboardInterrupt:
        break