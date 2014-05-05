# -*- coding: utf-8 -*-

# 本文件介绍Python中的random库

print '-' * 50
# -------------------------------------------------------------------------------

# random.random()
# 用于生成一个0到1的随机符点数: 0 <= n < 1.0

from random import random

print random()
print '-' * 50

# -------------------------------------------------------------------------------

# random.uniform(a, b)
# 用于生成一个指定范围内的随机符点数，
# 两个参数其中一个是上限，一个是下限。
# 如果 a > b，则生成的随机数n: a <= n <= b。
# 如果 a < b，则 b <= n <= a。

from random import uniform

print uniform(10,20)
print uniform(20,10)
print '-' * 50

# -------------------------------------------------------------------------------

# random.randint(a, b)
# 用于生成一个指定范围内的整数。
# 其中参数a是下限，参数b是上限，
# 生成的随机数n: a <= n <= b

from random import randint

print randint(12,20)
print randint(20,20)    #结果永远是20 
#print random.randint(20, 10)   #该语句是错误的。下限必须小于上限
print '-' * 50

# -------------------------------------------------------------------------------

# random.randrange(start, stop, step)
# 从指定范围内，按指定基数递增的集合中 
# 获取一个随机数

from random import randrange
# random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中
# 获取一个随机数。

# random.randrange(10, 100, 2)在结果上
# 与 random.choice(range(10, 100, 2) )等效

# -------------------------------------------------------------------------------

# random.choice(sequence)
# 从序列中获取一个随机元素
# 参数sequence表示一个有序类型:list, tuple, 字符串

from random import choice

print choice('Hello Python!')
print choice( ["JGood","is", "a","handsome", "boy"] )
print choice( ("Tuple","List") )
print '-' * 50

# -------------------------------------------------------------------------------

# random.shuffle(x, random)
# 用于将一个列表中的元素打乱

from random import shuffle

p = ["Python","is", "powerful","simple", "and so on..."] 
shuffle(p)  
print p  
print '-' * 50

# -------------------------------------------------------------------------------

# random.sample(sequence, k)
# 从指定序列中随机获取指定长度的片断。
# sample函数不会修改原有序列。

from random import sample

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
#从list中随机获取5个元素，作为一个片断返回  
slc = sample(li, 5)  
print slc
print li         #原有序列并没有改变。

print '-' * 50

# -------------------------------------------------------------------------------

"".join(random.sample(string.letters, 10))   # 生成指定长度的随机字符串很容易
# 'kMmSgPVWIi'

"".join(random.sample(string.letters, 10))
# 'feCTyRZrHv'


