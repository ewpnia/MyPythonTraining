# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------------------------------------------

str = '(page 1 of 2000)'  # 获取2000
li = str.split(' ')      # li : ['(page', '1', 'of', '2000)']
result = li[3][:-1]       # result : '2000'
result = li[-1][:-1]       # result : '2000'

>>> re.search(r'(?:\w+\d+\w+)(\d+)', str).group()
'2000'

# ---------------------------------------------------------------------------------------------------------------

>>> str.split(',')
['abc', '123', 'xyz']               # 分隔符‘，’不会返回

>>> re.split(r'\W', str)
['abc', '123', 'xyz']               # 分隔符‘，’不会返回

>>> re.split(r'(\W)', str)
['abc', ',', '123', ',', 'xyz']     # 分隔符‘，’返回

# ---------------------------------------------------------------------------------------------------------------

# 把某字符串中的内容换成等长的*

>>> def repl(m):
... print m.group()
... return "*" * len(m.group())
...
>>> re.subn(r"[a-z]+", repl, "abc,123,x")
abc
x
('***,123,*', 2)

# ---------------------------------------------------------------------------------------------------------------

# 两个变量的交换：

a, b = b, a

# ---------------------------------------------------------------------------------------------------------------

# 不要用可变对象作为默认参数值
# (Don’t use mutable as defaults)
def function(x, l=[]):          # 不要这么干
def function(x, l=None):        # 更好的一种方式
    if l is None:
       l = []

# ---------------------------------------------------------------------------------------------------------------

d = {1: "1", 2: "2", 3: "3"}
for key, val in d.items()       # 调用items()后会构建一个完整的list对象
for key, val in d.iteritems()   # 只有在迭代时每请求一次才生成一个值

# ---------------------------------------------------------------------------------------------------------------

# 使用isinstance 而不是type

# 不要这样做：
if type(s) == type(""): ...
if type(seq) == list or \
    type(seq) == tuple: ...

# 应该是这样：
if isinstance(s, basestring): ...
if isinstance(seq, (list, tuple)): ...

# 需要注意的是这里使用basestring而不是str是因为
# 你可能会用一个unicode对象去检查是否为string,例如：
# >>> a=u'aaaa'
# >>> print isinstance(a, basestring)
# True
# >>> print isinstance(a, str)
# False

# ---------------------------------------------------------------------------------------------------------------

freqs = {}
for c in "abracadabra":
    try:
        freqs[c] += 1
    except:
        freqs[c] = 1

# 一种更好的方案如下：
freqs = {}
for c in "abracadabra":
    freqs[c] = freqs.get(c, 0) + 1

# 一种更好的选择 collection类型defautdict：
from collections import defaultdict
freqs = defaultdict(int)
    for c in "abracadabra":
        freqs[c] += 1

# ---------------------------------------------------------------------------------------------------------------

# namedtuple()     # 用指定的域创建元组子类的工厂函数
# deque            # 类似list的容器，快速追加以及删除在序列的两端
# Counter          # 统计哈希表的dict子类
# OrderedDict      # 记录实体添加顺序的dict子类
# defaultdict      # 调用工厂方法为key提供缺省值的dict子类

# ---------------------------------------------------------------------------------------------------------------

__eq__(self, other)      # 定义相等操作的行为, ==.
__ne__(self, other)      # 定义不相等操作的行为, !=.
__lt__(self, other)      # 定义小于操作的行为, <.
__gt__(self, other)      # 定义不大于操作的行为, >.
__le__(self, other)      # 定义小于等于操作的行为, <=.
__ge__(self, other)      # 定义大于等于操作的行为, >=.

# ---------------------------------------------------------------------------------------------------------------


# 如果y等于1就把3赋值给x,否则把2赋值给x
x = 3 if (y == 1) else 2

# func1将被调用如果y等于1的话，反之func2被调用。
# 两种情况下，arg1和arg2两个参数都将附带在相应的函数中。
(func1 if y == 1 else func2)(arg1, arg2)

# 类似地，下面这个表达式同样是正确的
x = (class1 if y == 1 else class2)(arg1, arg2)


# ---------------------------------------------------------------------------------------------------------------


# 创建类时，你可以使用__getitem__，让你的类像字典一个工作
class MyClass(object):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
 
    def __getitem__(self, item):
        return getattr(self, item)
 
x = MyClass(10, 12, 22, 14)

# 因为有了__getitem__，你就能够通过对象x的x[‘a’]获取a的值


# 如果添加如下语句：
def __getitem__(self, item):
     if item is Ellipsis:
         return [self.a, self.b, self.c, self.d]
     else:
         return getattr(self, item)

# 我们就可以使用x[…]获取的包含所有项的序列
# >>> x = MyClass(11, 34, 23, 12)
# >>> x[...]
# [11, 34, 23, 12]

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# 条件参数列表
# 在实际开发中，我们会遇到如下一种需求：
# 1. 默认条件有 (a, b, c, d ...)，总之很多。
# 2. 调用者可以传递 (b = False, c = False) 来提供 "非" 条件，其他默认为 True。
# 3. 或者传递 (b = True, c = True)，其他默认为 False。
# 4. 还可以用 (all = True, ...) 来明确指定默认值。

def test(**on):
    # 全部条件列表
    accept_args = ("a", "b", "c", "d", "e")

    # 默认条件
    default = on.pop("all", None)

    # 如果没有显式指明默认条件，则检查参数列：
    #   1. 如果有任何一个 True 条件则默认值为 False。
    #   2. 如果全部为 False，则默认值为 True。
    if default is None: 
        default = not(True in on.values())

    # 使用 setdefault 补全参数字典
    for k in accept_args: 
        on.setdefault(k, default)

    return on


print test(b = False, e = False)                
# 显示：{'a': True, 'c': True, 'b': False, 'e': False, 'd': True}

print test(c = True)                            
# 显示：{'a': False, 'c': True, 'b': False, 'e': False, 'd': False}

print test(a = True, e = False)                 
# 显示：{'a': True, 'c': False, 'b': False, 'e': False, 'd': False}

print test(all = True, c = False, e = True)     
# 显示：{'a': True, 'c': False, 'b': True, 'e': True, 'd': True}

print test(all = True, c = False, e = False)    
# 显示：{'a': True, 'c': False, 'b': True, 'e': False, 'd': True}

print test(all = False, c = True, e = True)     
# 显示：{'a': False, 'c': True, 'b': False, 'e': True, 'd': False}


# ---------------------------------------------------------------------------------------------------------------

# “+=” 与 “...= ... + ...” 是不一样的
# 后者会生成新的对象

>>> list_a = []
>>> print id(list_a)
37022536

>>> list_a += [1]
>>> list_a
[1]
>>> print id(list_a)
37022536

>>> list_a = list_a + [2]
>>> list_a
[1, 2]
>>> id(list_a)
37022496

