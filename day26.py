'''#handling earrors
--------------
try block
-->the try block will test hte block of code for errors.
try:
    print(b)
except block
-------------
-->this block take any earrors
else blockelse key word to define a blockof code to be excuted if no earror were raised
--------------
-->
finally block
---------------
-->this block will execute eaither try block have any error or no earror

try:
    print(b)
except:
    print("this block can handle earror")

try:
    a = 9
    b = 10
    c = 8
    print(a+b)
except:
    print("earror here ")
else:
    print("no earror in the code")
finally:
    print("the try-except block is finished")'''



    
try:
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
        
    result = a / b
    print("Result:", resul)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")
except NameError:
    print('There is a name error')

finally:
    print("Execution completed.")

