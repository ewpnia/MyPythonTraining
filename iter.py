# -*- coding: utf-8 -*-

# 自制迭代器对象

class Data(object):
    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        return DataIter(self)

class DataIter(object):
    def __init__(self,data):
        self._index = 0
        self._data = data._data

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data[self._index]
        self._index += 1
        return d

if __name__ == '__main__':
    d = Data(1, 2, 3)

    for x in d:
        print x

# --------------------------------------------

# Python自带迭代器iter()
# 
# class Data(object):
#   def __init__(self):
#       self._data = []
# 
#   def add(self, x):
#       self._data.append(x)
#   
#   def data(self):
#       return iter(self._data)
# 
# >>> d = Data()
# >>> d.add(1)
# >>> d.add(2)
# >>> d.add(3)
# >>> for x in d.data(): print x
# 1
# 2
# 3