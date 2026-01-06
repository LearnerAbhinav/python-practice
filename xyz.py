#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      abhin
#
# Created:     05-01-2026
# Copyright:   (c) abhin 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

class Atm:
    #(functions)- general for all vs (methods )- special function inside class
    # class ke andar method hota hai matlab func inside class is method

# creation of variable
# init is an (constructor )- andar rkha code apne aap execute hota hai jaise he is class ka obj bnate h
# jis object ke saath aap currenttly kaam kar rahe ho wahi self hai samjha
    def __init__(self):
        self.pin=""
        self.balance=0
        print(id(self))

        # i callled the menu method

        self.menu()

    def menu(self):
        user_input=input("""
                           Hello, how would you like to procead?
                        1.Enter 1 to create pin
                        2.Enter 2 to deposit
                        3.Enter 3 to withdraw
                        4.Enter 4 to check balance
                        5.Enter 5 to exit

""")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()

        else:
            print("Byee!")

    def create_pin(self):
        self.pin=int(input("Enter your pin"))
        print("Pin set successfully")

    def deposit(self):
        temp=int(input("Enter your pin"))
        if temp==self.pin:
            amount=int(input("Enter the amount you want to dposit"))
            self.balance=self.balance+amount
            print("Deposit Successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter the amount you want to withdraw"))
            if amount <= self.balance:
                self.balance=self.balance-amount
                print("Operation Succesfull")
            else:
                print("Entered amount exceeded than balance")
        else:
            print("The entered pin is inncorrect")
    def check_balance(self):
        temp=int(input("Enter your pin "))
        if temp == self.pin:
            print(self.balance())
        else:
            print("Invalid Pin")


sbi=Atm()
sbi.deposit()
sbi.withdraw()
print("\n")
print(sbi.balance)
