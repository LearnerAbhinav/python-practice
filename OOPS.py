class Atm:
    #(functions)- general for all vs (methods )- special function inside class
    # class ke andar method hota hai matlab func inside class is method

# creation of variable 
# init is an (constructor )- andar rkha code apne aap execute hota hai jaise he is class ka obj bnate h
    def __init__(self): 
        self.pin=""
        self.balance=0

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
            print("Create pin")
        elif user_input=="2":
            print("deposit")
        elif user_input=="3":
            print("withdraw")
        elif user_input=="4":
            print("check balance")
        elif user_input=="5":
            print("Byee!")
        
        
        