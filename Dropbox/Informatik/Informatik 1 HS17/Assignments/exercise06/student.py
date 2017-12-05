from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(title.get_title())
        self.grades[title.get_title()] = title.get_grade()

    def get_list_modules(self):
        for n in self.modules:
            print(n)

    def get_grades(self):
        for n in self.modules:
            print(n+': '+str(self.grades[n]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
