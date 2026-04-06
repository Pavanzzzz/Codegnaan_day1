''' function()------>
function is a block of code which is reusable
---> two types 1.) built in or in built
type 2.) user define

1. --> they comes with program and they are already defined....
eg..
------  print(),sum(),map()......

2.user define
----------
--> this is created by person who is developing or using for development

Note
----
-->it's starts with def keyword followed by func name
    and it has calling func....
    you have to call the function for it to work
eg :    def func_name():#in the brackets here you put variables which are called parameters
        .......
        func_name()# here inside the parenthesis they are called arguments'''
'''
a,b=1,2
def add(a,b):
    print(a+b)
add(a,b)

a=5
def even_odd(a):
    if a%2==0:
        print('even')
    else: print('odd')
even_odd(a=2)



a = int(input())
def prime_check(b):
    count = 0
    for i in range(b):
        if b%1 == 0: count += 1
    if count == 1: print('prime')
    else : print('not prime')
prime_check(a)


a = input()
def palindrome_check(a):
    b = ''
    for i in a:
        b = i + b
    if a == b: print ('palindrome')
    else : print('not palindrome')
palindrome_check(a)'''

a = [1,2]
b= [1,2]
print(a is b)


