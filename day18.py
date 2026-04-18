any = lambda so : so + 10
print(any(6))

some = lambda a,b: a+b
print(some(5,2))

''' lambda function()
------------
this is also called anonymous function...
a lambda can take n number of arguments but have only one expression

syntax-----
lamda(keyword) arguments: expression




List Comprehension:
------------
--> This is offers the shorter syntax when you want to create a new list from the existing list

syntax
-----
        Variable_name = [ expression loop and addition]

old_list = [1,2,3,4,5]
new_list = [j+1 for j in old_list if j%2==0]
print(new_list)

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)'''

a = int(input())
for i in range(1,a+1):
    print('*'*i)
