# -*- coding: utf-8 -*-

# 子类继承父类后，声明子类的__init__方法时，
# 必须显式调用父类的__init__方法

class Father(object):
    def __init__(self, name):
        self.name = name
        print "Father's name is %s" % self.name

class Child(Father):
    def __init__(self, name):
        # Father.__init__(self, name)
        super(Child, self).__init__(name)
        self.name = name
        print "Child's name is %s" % self.name

# >>> f = Father("Dad")
# Father's name is Dad

# >>> c = Child("Boy")
# Father's name is Boy
# Child's name is Boy

>>> class Fruits(object):
...     def __init__(self, name):
...             self.name = name
...             print "This is Fruit: ", self.name



>>> class Orange(Fruits):
...     def __init__(self, color):
...             super(Orange, self).__init__(color)    # super后跟的是子类的__init__
...             self.color = color
...             print "My color is ", self.color

>>> f = Fruits("apple")
This is Fruit:  apple

>>> o = Orange("orange")
This is Fruit:  orange
My color is  orange

# python中子类调用父类方法几点细节(正确使用super)
# 子类的方法要显示调用父类的方法,不调用系统不会默认调用

# 调用方法有3种
# a) Father.__init__(self, name)
# b) super(Child, self).__init__(name)
# c) super().__init__(name)

# a方法是传统的调用方法,
# b是改进后的方法. 
# 区别是: 当基类的名字有改变时, a方法子类的中的相应代码也要改. b就不用改了
# 所以b方法要好一些. 方便代码的维护
# c方法呢, 是python3.x以上版本用的

# 需要注意的是; 如果使用super调用父类方法, 则父类必须是新式类.
# 新式类：就是所有类都必须继承的类，如果什么都不想继承，就继承到object类
# 经典类：没有父类