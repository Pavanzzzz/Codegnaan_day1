'''------
generator() --- this is a special type of function that return as iterator

yield-------
it will take a pause and again resume, this is not nrml keyword can not be used in the nrml functions
this is used to produce a value and pause execution. 





def my_generator():
    yield 1
    yield 2
    yield 3
an = my_generator()
print(next(an))
print(next(an))
print(next(an))

def square_gen(n):
    for i in range(n):
        print (i*i)

square_gen(5)

def square_gen(n):
    for i in range(n):
        yield i*i

for val in square_gen(10):
    print(val)'''


def power_gen(n):
    for i in range(n):
        yield 2**i
for val in power_gen(10):
    print(val)


    
