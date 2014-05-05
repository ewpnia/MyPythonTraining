# -*- coding: utf-8 -*-

# 一行代码输出1~100的和

print sum(range(101))

print reduce(( lambda x,y:x+y ), range(101))

print (1+100)*100/2

>>> def test(x):
...     return range(x)
...
>>> test(100)

print '-' * 50
print



# 不在for里面输出累加结果
# >>> result = 0
# >>> for i in range(101):
# ...     result += i
# ... else:
# ...     print result
# ...
# 5050




# n以内的斐波那契(Fibonacci)数列
def fib(n):
    # if n <= 2:
    #     return 1
    # else:
    #     return fib(n-1) + fib(n-2)
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b,a+b
    return result

fib(1000)


def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a+b

fibonacci(100)


print '-' * 50
print


# 浮点的MAGIC
# >>> 23.53+5.88+17.64
# 47.05
# 
# >>> 23.53+17.64+5.88
# 47.050000000000004