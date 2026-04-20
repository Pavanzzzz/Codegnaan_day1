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
'''

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
        
