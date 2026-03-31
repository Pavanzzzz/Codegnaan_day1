'''any_ = "Python is a programming language"
vowel_cou =0
space_cou =0
con_cou = 0
for j in any_:
    if j in "AEIOUaeiou":
        vowel_cou += 1
    elif j in " ":
        space_cou += 1
    elif j not in "AEIOUaeiou ":
        con_cou += 1
print(vowel_cou)
print(space_cou)
print(con_cou)'''


#j is the initial vaariable in the above for loop
'''a= 9
for j in range(1,-5,-1):
    print(j)'''
#range()--->used when you want the loop to go through all the numbers between
    #the range mentioned (start,end,step)
'''
i = input()
for j in range(len(i)-1,-1,-1):
    print (i[j])

so = 123
s = str(so)
st = "pavan sai"
print(list(st))
a,b = 1,2
b=[(a,b),(c,d)]
print(dict(b))
b = "pavansai"
print(b[::-1])
'''
a = "pavansai"
b=""

for i in range(len(a)-1,-1,-1):
    b += a[i]
print(b)
if a is b : print("palindrome")
else: print("not")



