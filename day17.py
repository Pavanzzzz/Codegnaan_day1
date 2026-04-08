'''

breaking it into smaller,simpler subproblems.
Recursion is especially useful for problems that can be
divided into identical smaller tasks, such as mathetical
calculations,tree traversals or divide and conquer
algorithms.






def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit pin:")
        if len(user_pin)== 4 and user_pin == details['ATM PIN']:
            print(" Welcome")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print('invalid attempt . attempts left:',self.remaining_attempts)
            else:
                print('card blocked')
                return False


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
        elif h == 2:
        M = int

        
else:print("invaalid pin")






an = 'Python is a language'
def any(an):
    vowels =  []
    consonant = []
    for i in an :
        if i in 'aeiouAeiou': vowels.append(i)
        elif i not in 'aeiouAeiou ' : consonant.append(i)
    print(vowels,consonant)

any(an)'''




















