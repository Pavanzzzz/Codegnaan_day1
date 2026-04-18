''' constructor(__init__)
------------------------
a constructor is a special method used to initialize object data
__init__()



class student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID

    def display(self):
        print(self.name,self.ID)
stu_1 = student('kanna',567)
stu_1.display()'''



'''Access specifiers
---------
1.Public
SYNTAX -- name
we can use it anywhere in the program
2.Protected
syntax -- name
this is only for internal use
3.Private
syntax-- __name
this one is restricted

  


class some:
    def __init__(self):
        self.public = 'Public'
        self.protected = 'Protected'
        self.private = 'Private'
any = some()
print(any.public)
print(any.protected)
print(any.private)
'''

UBI_KANNA_details = {
    "Name": "KANNA",
    "ATM_PIN": "9999",
    "Balance": 10000
}

print("Welcome to UBI ATM")
print("Please insert your ATM card")

# 🔐 3 Attempts for PIN
attempts = 3

while attempts > 0:
    user_pin = input("Enter your PIN: ")

    if user_pin == UBI_KANNA_details["ATM_PIN"]:
        print("✅ Login Successful")

        # 🔁 Menu Loop
        while True:
            print("\n1. Withdraw\n2. Deposit\n3. Change PIN\n4. Check Balance\n5. Exit")
            choice = int(input("Enter your choice: "))

            # Withdraw
            if choice == 1:
                amt = int(input("Enter amount: "))
                if amt <= UBI_KANNA_details["Balance"]:
                    UBI_KANNA_details["Balance"] -= amt
                    print(f"💰 Withdrawn Successfully. Balance: {UBI_KANNA_details['Balance']}")
                else:
                    print("❌ Insufficient Balance")

            # Deposit
            elif choice == 2:
                amt = int(input("Enter amount: "))
                if amt % 100 == 0:
                     UBI_KANNA_details["Balance"] += amt
                    print(f"💰 Deposited Successfully. Balance: {UBI_KANNA_details['Balance']}")edr
                else:
                    print("❌ Enter amount in multiples of 100")

            # Change PIN
            elif choice == 3:
                old_pin = input("Enter old PIN: ")

                if old_pin == UBI_KANNA_details["ATM_PIN"]:
                    new_pin = input("Enter new PIN: ")
                    confirm_pin = input("Confirm new PIN: ")

                    if len(new_pin) == 4 and new_pin == confirm_pin:
                        if new_pin != old_pin:
                            UBI_KANNA_details["ATM_PIN"] = new_pin
                            print("✅ PIN Changed Successfully")
                        else:
                            print("❌ New PIN cannot be same as old PIN")
                    else:
                        print("❌ PIN must be 4 digits and match")
                else:
                    print("❌ Wrong old PIN")

            # Check Balance
            elif choice == 4:
                print(f"💳 Current Balance:UBI_KANNA_details['Balance']}")

            # Exit
            elif choice == 5:
                print("🙏 Thank you for using KANNA ATM")
                break

            else:
                print("❌ Invalid choice")

        break  # exit after successful session

    else:
        attempts -= 1
        print(f"❌ Wrong PIN! Attempts left: {attempts}")

        if attempts == 0:
            print("🚫 Your card is blocked")UBI_KANNA_details = {
    "Name": "KANNA",
    "ATM_PIN": "9999",
    "Balance": 10000
}

print("Welcome to UBI ATM")
print("Please insert your ATM card")

# 🔐 3 Attempts for PIN
attempts = 3

while attempts > 0:
    user_pin = input("Enter your PIN: ")

    if user_pin == UBI_KANNA_details["ATM_PIN"]:
        print("✅ Login Successful")

        # 🔁 Menu Loop
        while True:
            print("\n1. Withdraw\n2. Deposit\n3. Change PIN\n4. Check Balance\n5. Exit")
            choice = int(input("Enter your choice: "))

            # Withdraw
            if choice == 1:
                amt = int(input("Enter amount: "))
                if amt <= UBI_KANNA_details["Balance"]:
                    UBI_KANNA_details["Balance"] -= amt
                    print(f"💰 Withdrawn Successfully. Balance: {UBI_KANNA_details['Balance']}")
                else:
                    print("❌ Insufficient Balance")

            # Deposit
            elif choice == 2:
                amt = int(input("Enter amount: "))
                if amt % 100 == 0:
                     UBI_KANNA_details["Balance"] += amt
                    print(f"💰 Deposited Successfully. Balance: {UBI_KANNA_details['Balance']}")
                else:
                    print("❌ Enter amount in multiples of 100")

            # Change PIN
            elif choice == 3:
                old_pin = input("Enter old PIN: ")

                if old_pin == UBI_KANNA_details["ATM_PIN"]:
                    new_pin = input("Enter new PIN: ")
                    confirm_pin = input("Confirm new PIN: ")

                    if len(new_pin) == 4 and new_pin == confirm_pin:
                        if new_pin != old_pin:
                            UBI_KANNA_details["ATM_PIN"] = new_pin
                            print("✅ PIN Changed Successfully")
                        else:
                            print("❌ New PIN cannot be same as old PIN")
                    else:
                        print("❌ PIN must be 4 digits and match")
                else:
                    print("❌ Wrong old PIN")

            # Check Balance
            elif choice == 4:
                print(f"💳 Current Balance:UBI_KANNA_details['Balance']}")

            # Exit
            elif choice == 5:
                print("🙏 Thank you for using KANNA ATM")
                break

            else:
                print("❌ Invalid choice")

        break  # exit after successful session

    else:
        attempts -= 1
        print(f"❌ Wrong PIN! Attempts left: {attempts}")

        if attempts == 0:
            print("🚫 Your card is blocked")

