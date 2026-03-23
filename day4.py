''' Statements are divided into 3 , control statements ,condition statements and loop statement
if - statement
if-else
if-elif-else

age = int (input())
if age>=18:print('eligible')


n = int(input('enter attendance:'))
if n>75: print('eligible')
elif n<75 and n>50: print('EOD')
else: print('re-registration')

a = int(input())
if a>17:print('yes')
else: print("no , you have to wait for ", 18-a,"years")

tickets_price = int(input("enter the total amount spent on tickets:"))
if tickets_price>=1000:print("new ticket price:",tickets_price - (tickets_price/10),"\nDiscount:10%")
else:print('no discount')

num1 = float(input())
ope = input()
num2 = int(input())
if ope == 'x' : print(num1*num2)
elif ope == '/' : print(num1/num2)
elif ope == '+' :print(num1+num2)
elif ope == '-' :print(num1-num2)
else:print('error')'''



print("enter the equation with spaces between each charachter") 
eqn = list(input().split())
a = int(eqn[0])
b = eqn[1]
c = int(eqn[2])
if b == 'x' : print(a*c)
elif b == '/' : print(a/c)
elif b == '+' :print(a+c)
elif b == '-' :print(a-c)
else: print('error')


