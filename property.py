# -*- coding: utf-8 -*-


class Person():
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def set_age(self, age):
        self.age = age

    def my_get_age(self):
        return self.age

    get_age = property(my_get_age)
    

# attr = property( function )
# 作用是把 attr 设置为该类的属性，
# 该属性为调用 function 所获得的返回值
# >>> from property import Person
# >>> p = Person('Tony', 'Stack')
# >>> p.set_age(10)
# >>> p.get_age             <-注意属性没括号
# 10
# >>> p.my_get_age()        <-调用函数
# 10