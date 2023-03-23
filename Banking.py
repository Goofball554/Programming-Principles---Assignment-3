class Program():
    def showAccountMenu(accountNumber):
        try: 
            print("ACCOUNT MENU")
            print("Account Number: ", accountNumber)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            userInput2 = int(input())

        except:
            userInput2 = 0

        if userInput2 == 1:
            pass
        
        elif userInput2 == 2:
            pass

        elif userInput2 == 3:
            pass
        
        elif userInput2 == 4:
            Program.showMainMenu()

        else:
            print("Please enter a valid input (either 1 - 5).")
            Program.showAccountMenu()
        


    def showMainMenu():
        try: 
            print("MAIN MENU")
            print("1. Select Account")
            print("2. Exit")
            userInput = int(input())
        
        except:
            userInput = 0

        if userInput == 1:
            print("Available Accounts:")
            print("Account Number | Account Name")
            print("1 | Bobby")
            print("2 | Joe")
            print("3 | Jasmine")
            print("4 | Melanie")
            print("5 | Richard")

            try:
                accountNumber = int(input())
            
            except:
                print("Please enter a valid input (1 - 5).")

            if accountNumber >= 1 and accountNumber <= 5:
                Program.showAccountMenu(accountNumber)

            else:
                print("Please enter a valid input (1 - 5).")

        elif userInput == 2:
            pass

        else:
            print("Please enter a valid input (either 1 or 2).")
            Program.showMainMenu()

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
