'''num = int(input('enter a number'))
for i in range(num-1,-1,-1):
    for j in range(i):
        print('*',end='')
    print() 

num = int(input())
for j in range(num):
    print(' ' *(num-j),end ='')
    for i in range(j+1):
        print('*',end=' ')
    print()
for h in range(num):
    if h == 0 :continue
    print(' '*h,end='')
    for p in range(num-h):
        print('*',end=' ')
    print()'''

    

details = {'name':"Teja","ATM PIN":'8978','balance':5000}
i = input("enter atm pin:")
if len(i) == 4:
    if i in    details['ATM PIN']:
        h = int(input('enter your choice \n1.withdrawl \n2.balance check'))
        if h == 1:
            u = int(input("enter amount:"))
            if details['balance']-u >=0:
                print('balance:',details['balance']-u)
            else:print('insufficient balance')

    else: print('incorrect pin')


else:print("invaalid pin")

