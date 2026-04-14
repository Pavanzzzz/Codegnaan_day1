'''
import day5
print(day5.p)


user-define module
----------
--> This is developed by the user or programmer inside a file of python code and used by called import with filename...
syntax ---> import (keyword) file_name
            file_name.functionality
import My_module
print(My_module.Variable+5)

Built-in or Inbuilt
--------------
-->Aleady these are comes with installation and they are ready to use in the program
-->This is development by the developer

syntax----> import(keyword) module_name
            module_name.functionality


import math
print(math.log(10))'''

import random
for i in range(3):
    a = int(input())
    if a == random.randint(1,100):
        print('user wins')
        b = 1
        break
    else:print('user loses')

    

