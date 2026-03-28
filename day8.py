'''list_1 = [1,2,4,"python",[5,6,"pavan"],["but","hat'"]]
print(list_1[5][0][1])

print(9+7)
print([1,2]+[9])
print('kha'+'hha')'''
#concatenation--> blends anything of the same type only, if it is integers it will add , if it is lists or string it
#will combine them together
'''print(set((1,2)+(2,3)))'''

#tuple()
#-->tuple is a collection of different data types
'''
t = (1,2,'pavan', 3 ,[5,6])
print(t[2][2])

t = (12, 89,'Python',(23,'pavan',[67,'puthon is a language',(7,8)],[8,('python',[34,9])]))
print(t[3][2][1][6])

a,b = 5,6
c,d= a,b
print(c,d)'''

i = int(input('enter a year'))
if (i%4==0 and i%100!=0) or i%400==0:
        print('leap year')
else: print('not  a leap')

