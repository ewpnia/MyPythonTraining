# -*- coding: utf-8 -*-

# 把'1,2,3'转换为[1,2,3]
a = '1,2,3'

# 正确方法
result1 = [int(i) for i in a if i.isdigit()]
print result1


# 错误方法
result2 = a.split(',')
print result2
print [a]
print list(a)


# 把'1,2,3'转换为['1', ',', '2', ',', '3']
print list(a)
print '-' * 50
print


import string
string.split(str, ' ')   #将string转list，以空格切分
string.join(list, ' ')   #将list转string，以空格连接

m = ['9', '8']
string.join(m, ' ')
>>>"9 8"
# ''.join(m, ' ')报错，这样使用join只能有一个参数
# 可以这样：' '.join(m)

# 注意
# a = [1, 2]
# ''.join(a)会报错
# b = ['1', '2']
# ''.join(b)才会输出 "12"
# 即使用join把list转string时，list中的元素必须为string型，不能为int
>>> a = range(10)
>>> b = [lambda x:str(x) for x in a]
>>> b
[<function <lambda> at 0x0239AE70>, ...]
>>> b = [(lambda x:str(x))(x) for x in a]
>>> b
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



>>> s = "xxxxx"
>>> list(s)
['x', 'x', 'x', 'x', 'x']
>>> tuple(s)
('x', 'x', 'x', 'x', 'x')
>>> tuple(list(s))
('x', 'x', 'x', 'x', 'x')
>>> list(tuple(s))
['x', 'x', 'x', 'x', 'x']



# 列表和元组转换为字符串则必须依靠join函数
>>> "".join(tuple(s))
'xxxxx'
>>> "".join(list(s))
'xxxxx'
>>> str(tuple(s))
"('x', 'x', 'x', 'x', 'x')"


# -------------------------------------------------------------


# 把'abcd'转换成'*a*b*c*d*'
a = 'abcd'
b = '*'.join(a)         # b = 'a*b*c*d'
b = list(b)             # b = ['a', '*', 'b', '*', 'c', '*', 'd']
b.insert(0, '*')        # b = ['*', 'a', '*', 'b', '*', 'c', '*', 'd']
b.append('*')           # b = ['*', 'a', '*', 'b', '*', 'c', '*', 'd', '*']
c = ''.join(b)          # c = '*a*b*c*d*'
print 'c = ',c


# 错误示范
a = 'abcd'
b = '*' * ( len(a)+1 )
al = list(a)
bl = list(b)

for i,j in zip(bl,al):
    bl.insert( bl.index(i)+1, j )     # WRONG!

# 输出为*dcba****
# 因为index()返回第一次找到的‘*’的位置，但因为bl中全是*，因此每次都返回0

bl = ''.join(bl)
print 'bl= ',bl


# 真.正确示范
a = 'abcdefg'
b = '*' * ( len(a)+1 )
al = list(a)
bl = list(b)
flag = 0

for i,j in zip(bl,al):
    bl.insert( flag+1, j )    
    flag = bl.index(i, flag+1)
# 输出为*a*b*c*d*
# l.index("a", 2)表示从 l[2] 开始检索"a"

bl = ''.join(bl)
print 'bl= ',bl
print '-' * 50
print


# ----------------------------------------------------------------------------


# 以下代码有BUG， 当p中含有重复的元素时insert只能定位第一次出现的位置
# [1, 2, 3] ['a', 'b'] -> [1, 'a', 2, 'b', 3]
# [1, 2, 3] ['a', 'b', 'c'] -> [1, 'a', 2, 'b', 3, 'c']
# [1, 2, 3] ['a', 'b', 'c', 'd'] -> [1, 'a', 2, 'b', 3, 'c']

# import copy

p = [1, 2, 3]
q = ['a', 'b']

# p = [1, 1, 1]
# q = ['a', 'b']

# r = copy.deepcopy(p)
r = p[:]

for i,j in zip(r,q):
    r.insert( r.index(i)+1, j )

print 'r = ',r



# 修正后的代码
# 此时无论p、q哪个更长都可完成插入
# p = [1, 1, 1]
# q = ['a', 'b']

# p = [1,]
# q = ['a', 'b']

p = [1, 1, 1, 1, 1]
q = ['a', 'b']

r = []
length = max(len(p),len(q))

for i in range(length):
    if i < len(p):
        r.append(p[i])
    if i < len(q):
        r.append(q[i])

print 'r = ',r
print '-' * 50
print


# ---------------------------------------------------------------


# 实现index()功能
def my_index(li, sub):
    for i,j in enumerate(li):
        if sub == j:
            return i
    return 'error'

print my_index( [2, 'a', 3], 'a' )
print '-' * 50
print





