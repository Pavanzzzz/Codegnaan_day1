'''
variables are named storage location that is used to hold data in the memory , to make it simple it is the label which points out to a value --> storage placeholders

rules for defining variables
--> A-Z , a-z,0-9
-->start with uppercase,lowercase letters,even with an underscore _
-->But u cannot start with symbols(@#$%....)and nnumbers too.

better preferable way is go with general purpose
'''
'''
a= 1
b=7
a=33
#Python is dynamicallly typed meaning the datatype need not be deffined and only the recent value to the variable with same name is pointed
name = 'pavan sai'
message = ' Tmothee is coming for the Oscars'
year = 2027
moviie = 'Dune: Messiah'
print(name,message,year,moviie)

#assigning muultiple vlues to variables
a,b,c = 1,2,3
print(a,b,c)

#assign same value to multiple variables
x=y=x=8
print(x,y,x)

#keywords are reserved words which will have specific usage , there are 35 keywords in python
#python is case sensitive
#identifiers are names given to variables,functions,classes,objects.... , you cannot use keyword as an identifier
#literals are fixed values to a identifier
# Built in datatypes - > Numeric,Boolean,Collections
#Numeric --> int,float,complex
#complex --> specific conversations(real and imaginary)

count = 45
print(count)
print(type(count))

value = 3+6j
print(value)
print(type(value))
#it cannot be j6 because variables can start with letters but not with numbers''''''

age = True
print(age)
n= complex(float(int(age)))
print(n)
print(type(n))
#complex cannot be changed to int or float rest all can be chhanged

a= int(input('enter a value'))
print(a)'''
#cricket stats
name = input('enter cricketer name')
centuries = int(input('enter number of centuries'))
average = float(input('enter average of the cricketer'))
runs = int(input('enter runs scored in the latest match'))
balls = int(input('enter balls played in the latest match'))
match_average = (runs%balls)*100



