'''v = input('enter a letter')
if v in "aeiouAEIOU":
          print('vowel')
else: print('consonant')''' '''

time = input("Enter time in 24hrs format: ").split(':')

hours = int(time[0])
minutes = int(time[1])


if hours > 23 or minutes > 59:
    print("error")

else:
    
    if hours > 12:
        hours -= 12

    print(hours, ":", minutes)'''

'''
list_1 = [1,2,3,"Python",[1,2,["Python","Java"],"Language"]]
print(list_1[4][2][0][3])

list = [3,4,5,[4,'pavan'],9]
print(list[3][1][1])


time = input().split(':')
hours = int(time[0])
minutes = int(time[1])
if hours>12 and minutes<60:
        print(f"{hours-12}:{minutes}pm")
else:print('error')'''



#methods
''' append()--- this method is used to add new items into list it will only go to the last index of the list
extend()--- extend take only lists and strings and adds in the last index as single items
remove()--- this will remove the item or value directly
pop()

mutable--->could directly modify on the variable 
immutable-->I can not modify directly on the variable--> string

list = [1,2,3,4]
list.append(5)
list.extend([2])
list_1 = list
print(list_1)'''



list = [1,2,3,4,['pavan']]
list.remove(list[4])
print(list.pop(1))
#print(list)





