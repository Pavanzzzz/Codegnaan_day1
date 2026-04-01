'''i = int(input())
for j in range(1,11): 
    print(i,"X",j,"=",i*j)

    

an = "The best there is AAA."
c = 0
cc = 0
b =[]
d =[]
for i in an:
    if i.isupper():
        b.append(i)
    elif i.islower():
        d.append(i)
print("capital:",b)
print("small:",d)



details = {'name':"Teja","ATM PIN":'8978'}
i = input("enter atm pin:")
if len(i) == 4:
    if i in    details['ATM PIN']:
        print("correct")
    else: print('incorrect')


else:print("invaalid pin")'''


num = int(input('enter a number:'))
f = 0
for i in range(1,num):
    if num % i == 0:
        f += i
if f == num: print("it is a perfect number")
else:print("it ain't perfect") 
        
