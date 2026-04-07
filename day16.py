'''num = 9
num2 = 15
def add(a,b):
    print(a+b)
add(num,num2)


a = 'pavan'
def name(b):
    print(b)
name(a='sai')
print(a)'''
 #arguments can be passed in calling function ,they work
#default value for arguments if arguments are not passed
''' arguments-----'''
#keyword
#default
#required
'''
a= 2
def prime_check(a):
    c = 0
    for i in range(1,a+1):
        if a%i==0:
            c += 1
    if c == 2 : print('prime')
    else: print('not prime')
prime_check(a=6)
prime_check(a = 2)
prime_check(a)'''
#passing values to vaariables using '=' in the calling function

'''
def any(c,b,a):
    print(b,a,c)
any(a = 2,c=3 ,b=1)'''


def any(*nums):
    print(nums[1])
any(1,2,3,4,5)
# '*' to store multiple values



#syntax errors
''' 1.)if a function parantheis is not closed or opened properly it will result in a syntax error
2.)statement should end with a proper column
3.)indentation errors
4.)type error
eg: print(8+'Python')
5.)attribution error




