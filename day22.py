'''
OOP's
-----
-->Object-oriented Language(OOP) is a style of programming where we model real
world things as objects that contain both data and functions()
-->reusable of code
-->And also scalable

Class
-----
--> class is a blue-print or template
object
-----
-->an instance of a class or an object is a real instance created from a class. it
is the actual thing that exists in memory while the program runs

'''
class car:
    def __init__(self,brand,color):
        self.brand= brand
        self.color = color
car1=car("BMW","Black")
car2=car("Toyoto","Red")
print(car1.brand)
