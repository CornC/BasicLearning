'''
@Description: python 类的练习
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-07 17:12:41
@LastEditors  : CornC.fcx
@LastEditTime : 2019-12-18 16:20:07
'''

# 钟表类
from time import time, localtime, sleep

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法可以访问类变量，但不能访问实例变量 调用时，实例改变类变量时，其变量只会在实例中改变
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

# 装饰器  @property

class Person(object):

    # slots 限定了 Person 类只绑定这两个属性
    # __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器
    @age.setter
    def age(self, age):
        self._age = age

    def display(self):
        print(self._name + '  ' + self._age)

# 继承
class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade


#　静态方法
from math import sqrt

class Triangle(object):

    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a
    
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c 

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

# 多态和重写
from abc import ABCMeta, abstractclassmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractclassmethod
    def sound(self):
        pass

class Dog(Pet):
    
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)
    
    
class Cat(Pet):
    
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

if __name__ == "__main__":
    
    # clock = Clock.now()
    # while True:
    #     print(clock.show_time())
    #     sleep(1)
    #     clock.run()
    # a, b, c = 3, 4, 5

    # if Triangle.is_valid(a, b, c):
    #     t = Triangle(a, b, c)
    #     print(t.area())

    stu = Student('王大锤', 15, '初三')