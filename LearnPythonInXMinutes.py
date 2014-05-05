# -*- coding: utf-8 -*-


# None 是对象
None  # => None

# 不要用相等 `==` 符号来和None进行比较
# 要用 `is`
"etc" is None  # => False
None is None  # => True

# 'is' 可以用来比较对象的相等性
# 这个操作符在比较原始数据时没多少用，但是比较对象时必不可少

# None, 0, 和空字符串都被算作 False
# 其他的均为 True
0 == False  # => True
"" == False  # => True

# 合并列表
li + other_li  # => [1, 2, 3, 4, 5, 6] - 并不会改变这两个列表

# 通过拼接来合并列表
li.extend(other_li)  # li 是 [1, 2, 3, 4, 5, 6]

# 用 in 来返回元素是否在列表中
1 in li  # => True

# 你可以将元组解包赋给多个变量
a, b, c = (1, 2, 3)     # a 是 1，b 是 2，c 是 3
# 如果不加括号，将会被自动视为元组
d, e, f = 4, 5, 6
# 现在我们可以看看交换两个数字是多么容易的事
e, d = d, e     # d 是 5，e 是 4

# 用 get 方法来避免 KeyError
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# get 方法支持在不存在的时候返回一个默认值
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4

# setdefault 是一个更安全的添加字典元素的方法
filled_dict.setdefault("five", 5)  # filled_dict["five"] 的值为 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] 的值仍然是 5

>>> filled_dict['five'] = 6
>>> filled_dict
{'a': 1, 'b': 2, 'five': 6}

# 集合储存无顺序的元素
empty_set = set()
# 初始化一个集合
some_set = set([1, 2, 2, 3, 4])  # filled_set 现在是 set([1, 2, 3, 4])

# Python 2.7 之后，大括号可以用来表示集合
filled_set = {1, 2, 2, 3, 4}  # => {1 2 3 4}

# 向集合添加元素
filled_set.add(5)  # filled_set 现在是 {1, 2, 3, 4, 5}
# 不能直接add 列表，必须为可hash对象
# >>> b = range(10)
# >>> for x in b:
# ...     d.add(x)

# 用 & 来计算集合的交
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# 用 | 来计算集合的并
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}
# 会把重复元素消除

# 用 - 来计算集合的差
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# 用 in 来判断元素是否存在于集合中
2 in filled_set  # => True
10 in filled_set  # => False

# 匿名函数
(lambda x: x > 2)(3)  # => True

# 我们新建的类是从 object 类中继承的
class Human(object):

     # 类属性，由所有类的对象共享
    species = "H. sapiens"

    # 基本构造函数
    def __init__(self, name):
        # 将参数赋给对象成员属性
        self.name = name

    # 成员方法，参数要有 self
    def say(self, msg):
        return "%s: %s" % (self.name, msg)

    # 类方法由所有类的对象共享
    # 这类方法在调用时，会把类本身传给第一个参数
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法是不需要类和对象的引用就可以调用的方法
    @staticmethod
    def grunt():
        return "*grunt*"


# 实例化一个类
i = Human(name="Ian")
print i.say("hi")     # 输出 "Ian: hi"

j = Human("Joel")
print j.say("hello")  # 输出 "Joel: hello"

# 访问类的方法
i.get_species()  # => "H. sapiens"

# 改变共享属性
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# 访问静态变量
Human.grunt()  # => "*grunt*"

