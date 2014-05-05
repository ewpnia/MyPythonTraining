# -*- coding: utf-8 -*-

# 生成斐波那契數列

# 传统做法
# def fab(max): 
#     n, a, b = 0, 0, 1 
#     while n < max: 
#         print b 
#         a, b = b, a + b 
#         n = n + 1


# 使用 yield .仅仅把 print b 改为了 yield b，
# 就在保持简洁性的同时获得了 iterable 的效果。
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

for n in fab(5): 
    print n 

# 简单地讲，yield 的作用就是把一个函数变成一个 generator，
# 带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
# 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，
# 每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
# 下次迭代时，代码从 yield b 的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。


# 也可以手动调用 fab(5) 的 next() 方法
# （因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），
# 这样我们就可以更清楚地看到 fab 的执行流程

 # >>> f = fab(5) 
 # >>> f.next() 
 # 1 
 # >>> f.next() 
 # 1 
 # >>> f.next() 
 # 2 
 # >>> f.next() 
 # 3 
 # >>> f.next() 
 # 5 
 # >>> f.next() 
 # Traceback (most recent call last): 
 #  File "<stdin>", line 1, in <module> 
 # StopIteration
 
# 当函数执行结束时，generator 自动抛出 StopIteration 异常，
# 表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。

# 使用 isgeneratorfunction 判断
#  >>> from inspect import isgeneratorfunction 
#  >>> isgeneratorfunction(fab) 
#  True

# 类的定义和类的实例
#  >>> import types 
#  >>> isinstance(fab, types.GeneratorType) 
#  False 
#  >>> isinstance(fab(5), types.GeneratorType) 
#  True

# fab 是无法迭代的，而 fab(5) 是可迭代的：
#  >>> from collections import Iterable 
#  >>> isinstance(fab, Iterable) 
#  False 
#  >>> isinstance(fab(5), Iterable) 
#  True


#------------------------------------------------------------------------------
#另一个例子
#-------------------------------------------------------------------------------

# 另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，
# 会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。
# 通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：

def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return 

>>> r = read_file(r"D:\123.txt")
>>>
>>> r.next()
......