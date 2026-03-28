'''
we can store data as key : value
keys are union and we cannn only give immutable datatypes in keys and no duplicates are allowed
values ----> all datatypes (mutable or immutable) , allows duplicates

methods-----
keys() ---- this is used to get all the keys
values() --- this is used to get all the values
clear()--- empties the dictionary 

pavan = {"pin" : 245,"lin" : 'yin', 9:8}
print(pavan.values())
print(pavan.keys())
print(pavan.clear())
print(pavan)


set{} -----> it does not allow duplicates , is an unordered collection
methods
-----
union-- this is to add  2 different sets without getting duplicates
pop() --- this removes the 0th index item from the set
remove() --- remove reemoves the item specified


any ={1,2,3,3,4,5,6,6,}
so = {4,9,10,6}
print(so.union(any))
print(any.intersection(so))
print(any.difference(so))
print(so.difference(any))
print(so.pop())'''


n = int(input('enter a pin'))
det = {'name':"pavan","age":21,'pin' :9171}
if n in det.values():print('correct pin')


#task ---> counting vowels,consonants in sentences using loop


