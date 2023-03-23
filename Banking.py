class Program():
    def showMainMenu():
        print("1. Select Account")
        print("2. Exit")

        try: 
            userInput = int(input())
        except:
            userInput = 0

        if userInput == 1:
            Program.showAccountMenu()

        elif userInput == 2:
            pass

        else:
            print("Please enter a valid input (either 1 or 2).")
            Program.showMainMenu()

    def showAccountMenu():
        print("We got here")

    def run():
        Program.showMainMenu()
    
class Account():
    def __init__():
        pass

    def getAccountNumber():
        pass

    def getAccountHolderName():
        pass

    def getRateOfInterest():
        pass

    def getCurrentBalance():
        pass

    def deposit():
        pass

    def withdraw():
        pass
    
    pass

class SavingsAccount(Account):
    def __init__():
        pass
    
    def withdraw():
        pass
   
    pass

class ChecquingAccount(Account):
    def __init__():
        pass
    
    def withdraw():
        pass

    pass

class Bank():
    def searchAccount():
        pass
    
    pass


Program.run()
