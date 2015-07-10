#-*- coding: utf-8 -*-

# 一些特殊属性，当你定义一个类和调用类的实例时
# 可以获得的一些默认属性 。

class Student:
	"""This test class"""
	name = "ss"
	
	def __init__(self):
		self.name = "bb"

	def Run(self):
		"""People run."""

	@staticmethod
	def RunStatic():
		print "In Static method..."



print "Student.__dict__",Student.__dict__
print "Student.__doc__",Student.__doc__
print "Student.__name__",Student.__name__
print "Student.__module__",Student.__module__
print "Student.__bases__",Student.__bases__
print


obj = Student()
print "obj.__dict__",obj.__dict__
print "obj.__doc__",obj.__doc__
print "obj.__module__",obj.__module__
print "obj.__class__",obj.__class__