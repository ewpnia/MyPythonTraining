# -*- coding: utf-8 -*-

print unicode('选择装饰器例子：', 'utf-8')
print unicode('1.无参装饰器', 'utf-8')
print unicode('2.有参装饰器', 'utf-8')
print unicode('3.装饰类', 'utf-8')
select = raw_input('>')

if select == '1':
    '''无参装饰器'''
    def decorator(F):
        def new_F(a, b):
            print("input", a, b)
            return F(a, b)
        return new_F

    @decorator
    def square_sum(a, b):
        return a**2 + b**2

    @decorator
    def square_diff(a, b):
        return a**2 - b**2

    print(square_sum(3, 4))
    print(square_diff(3, 4))

elif select == '2':
    '''有参装饰器'''
    def pre_str(pre=''):
        def decorator(F):
            def new_F(a, b):
                print(pre +' ' + 'input', a, b)
                return F(a, b)
            return new_F
        return decorator

    @pre_str('^_^')
    def square_sum(a, b):
        return a**2 + b**2

    @pre_str('T_T')
    def square_diff(a, b):
        return a**2 - b**2

    print(square_sum(3, 4))
    print(square_diff(3, 4))

elif select == '3':
    '''装饰类'''
    def decorator(aClass):
        class newClass:
            def __init__(self, age):
                self.total_display = 0
                self.wrapped = aClass(age)
            def display(self):
                self.total_display += 1
                print('total display', self.total_display)
                self.wrapped.display()
        return newClass

    @decorator
    class Bird:
        def __init__(self, age):
            self.age = age
        def display(self):
            print('My age is', self.age)

    eagleLord = Bird(5)
    for i in range(3):
        eagleLord.display()
