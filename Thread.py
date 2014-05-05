# -*- coding:utf-8 -*-


from threading import Thread, currentThread, activeCount

# 创建 Thread 实例，传入待执行函数
def test(s):
    print "ident:", currentThread().ident
    print "count:", activeCount()
    print s

Thread(target = test, args = ("Hello",)).start()
# ident: 4353970176
# count: 3
# Hello



# 继承 Thread 实现自己的线程类。
class MyThread(Thread):
    def __init__(self, name, *args):
        super(MyThread, self).__init__(name = name)
        self.data = args

    def run(self):
        print self.name, self.data

MyThread("abc", range(10)).start()
# abc ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],)

