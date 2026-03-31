'''num = int(input())
if num == 2 :print('prime')
else:
    for i in range(2,num):
        if num%i == 0:
            print ('not a prime')
            
        break
    else: print('prime')


num = int(input())
c =0
for i in range (1,num+1):
    if num%i == 0:
         c += 1
if c == 2 : print('prime')
else: print('not a prime')


num  = int(input())

for j in range ( 2,num+1):
    count=0
    for i in range(1,j+1):
        if j%i==0: count+=1
    if count == 2: print(j)



lis = list(map(int,input().split(' ')))
for i in lis:
    count =0
    for j in range(1,i+1):
        if i%j == 0: count+=1
    if count == 2: print (i)'''


an = [2,356,8,6,3,2,8]
some =[]
for i in an:
    if i not in some:
        some.append(i)v 
print(some)
    
    
    
