class Program():
    def showMainMenu():
        try: 
            print("MAIN MENU")
            print("1. Select Account")
            print("2. Exit")
            userInput = int(input())
        
        except:
            userInput = 0

        if userInput == 1:
            Bank.searchAccount()

        elif userInput == 2:
            print("Thank you for banking with us.")

        else:
            print("Please enter a valid input (either 1 or 2).")
            Program.showMainMenu()



    def showAccountMenu():
        print("ACCOUNT MENU")
        print("Account Number: ", Account.number)
        print("Account Holder Name: ", Account.name)
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit Account")
        
        try: 
            Bank.searchAccount()
            userInput2 = int(input())

        except:
            userInput2 = 0
            print("Please enter a valid input.")
            Program.showAccountMenu()

        if userInput2 == 1:
            Account.getCurrentBalance()
        
        elif userInput2 == 2:
            try: 
                userInput3 = round(float(input("How much would you like to deposit?")), 2)

            except:
                userInput3 = 0
                print("Please enter a valid input")

            if userInput3 == 0:
                pass

        elif userInput2 == 3:
            try: 
                userInput3 = round(float(input("How much would you like to withdraw?")), 2)

            except:
                userInput3 = 0
                print("Please enter a valid input.")

            if userInput3 == 0:
                pass
        
        elif userInput2 == 4:
            Program.showMainMenu()

        else:
            print("Please enter a valid input (1-4).")
            Program.showAccountMenu()

    def run():
        Program.showMainMenu()
    
class Account():
    def __init__(self, number, name, interest, balance):
        self.number = number
        self.name = name
        self.interest = interest
        self.balance = balance

    def getAccountNumber(self):
        return self.number

    def getAccountHolderName(self):
        return self.name

    def getRateOfInterest(self):
        return self.interest

    def getCurrentBalance(self):
        return self.balance

    def deposit(deposit):
        pass

    def withdraw(withdraw):
        pass
    
    pass

class SavingsAccount(Account):
    def __init__():
        pass
    
    def withdraw():
        pass
   
    def deposit():
        pass

    pass

class ChecquingAccount(Account):
    def __init__():
        pass
    
    def withdraw():
        pass

    def deposit():
        pass

    pass

class Bank():

    account1 = Account(1, "Jerry", 0.1, 15000)
    account2 = Account(2, "Jasmine", 0.1, 30400)
    account3 = Account(3, "Melanie", 0.1, 983345)
    account4 = Account(4, "Bob", 0.1, 29875)
    account5 = Account(5, "Phil", 0.1, 18763)
    
    def searchAccount():
        print("Please enter the Account Number.")
        try:
            accountNumber = int(input())
            
        except:
            accountNumber = 0

        if accountNumber >= 1 and accountNumber <= 5:
            Program.showAccountMenu()

        else:
            print("Please enter a valid Account Number (1-5).")

Program.run()
