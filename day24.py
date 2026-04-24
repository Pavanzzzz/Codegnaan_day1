'''
class BankAC:
    def __init__(self,balance):
        self.__balance = balance
    def deposite(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
Acc = BankAC(15000)
Acc.deposite(7000)
print(Acc.get_balance())

inheritance
--------
--> this allows a child class 9subclass0 to aquire the attrivutes and method of a parent
class(base class) this is called inheritance

1.Single inheritance
---------------
-->using single method of the class from base class is single inheritance

class parent:
    def display(self):
        print('this is parent method')
class child(parent):
    def display(self):
        super().display()
        print('This is child method')
any = child()
any.display()
-----------------
2.Multiple

super()
-->this is used to call methods of the parent class from the child class


class Father:
    def skill_(self):
        print("Father: hard working")
class Mother:
    def skill_2(self):
        print('Mother: Cooking')
class Child(Father,Mother):
    def All_skills(self):
        print('Child: Coding')
ny = Child()
ny.skill_()
ny.skill_2()
ny.All_skills()



Multi-level
----------
-->
this occurs when a class inherits from a child class,creating a grandparent--> Parent -->child in the structure
                      


class Grandparent:
    def Show_Grandparent(self):
        print('what up granny')

class Parent(Grandparent):
    def Show_Parent(self):
        print("Parent")
class child(Parent):
    def Show_child(self):
        print("I'm child")
any = child()
any.Show_Grandparent()
any.Show_Parent()
any.Show_child()



Hierarchical
---------
-->This occurs when multiple child classes inherit from a single parent class,this process is called hierarchical

class parent:
    def Parent(self):
        print('i am death')
class child_1(parent):
    def child_(self):
        print('I am 1st ')
class child_2(parent):
    def _child(self):
        print('I am me')
class child_3(child_1,child_2):
    pass

thing = child_3()
thing.Parent()
thing.child_()
thing._child()



hybrid inheritance
----------------
-->This is a combination of 2 or more types of inheritances like single inheritance and multiple inheritance or heirarchical
in a single class




Polymorphism
---------
-->This allows a object of different classes to be treated as an instancce of the same base class , with methods
behaving differently based on the actual object type.
eg....
print(len('python'))
print(len([1,2,3]))


Method Overloading
------------------
-->This deffines multiple methods with the same name but different parameter(number, type , or order) in the same
class


class calculator:
    def add (self,a,b,c):
        return a+b+c
cal = calculator()
print(cal.add(1,2,3))
print(cal.add(5,6,11))


import pyttsx3
engine = pyttsx3.init()
class animal:
    def speak(self):
        return 'sound'
class dog(animal):
    def speak(self):
        engine.say('bow bow')
do = dog()
print(do.speak())
engine.runAndWait()



class someone:
    def __init__(self,a,b):
        self.a = a
        self.b= b
    def __add__(self,other):
        return someone(self.a + other.a,self.b+other.b)
    def __str__(self):
        return f"({self.a},{self.b})"
any = someone(2,3)
so = someone(5,9)
print(any+so)'''

#data abstraction
'''this hides complex implementation details,exposing only essential features via abstract class or interface.
'''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
Circle = circle(5)
print(Circle.area())







        
