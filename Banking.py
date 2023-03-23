class Program():
    def showMainMenu():
        userInput = 0
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
        userInput2 = 0
        print("ACCOUNT MENU")
        print("Account Number: ", Account.getAccountNumber(Bank.account))
        print("Account Holder Name: ", Account.getAccountHolderName(Bank.account))
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit Account")
        
        try: 
            userInput2 = int(input())

        except:
            userInput2 = 0
            print("Please enter a valid input.")
            Program.showAccountMenu()

        if userInput2 == 1:
            print("Current Balance: $", Account.getCurrentBalance(Bank.account))
            Program.showAccountMenu()

        elif userInput2 == 2:
            try: 
                userInput3 = float(input("How much would you like to deposit?"))

            except:
                userInput3 = 0
                print("Please enter a valid input")

            if userInput3 > 0:
                if Bank.savings == True:
                    SavingsAccount.deposit(userInput3)

                elif Bank.checquing == True:
                    ChecquingAccount.deposit(userInput3)

        elif userInput2 == 3:
            try: 
                userInput3 = float(input("How much would you like to withdraw?"))

            except:
                userInput3 = 0
                print("Please enter a valid input.")

            if userInput3 > 0:
                if Bank.savings == True:
                    SavingsAccount.withdraw(userInput3)

                elif Bank.checquing == True:
                    ChecquingAccount.withdraw(userInput3)

            else:
                print("Please enter a valid input.")
                Program.showAccountMenu()
        
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

class SavingsAccount(Account):
    def __init__():
        pass
    
    def withdraw(number):
        if number > Account.getCurrentBalance(Bank.account):
            print("You are not able to withdraw that amount.")
            Program.showAccountMenu()

        else:
            newBalance = Account.getCurrentBalance(Bank.account) + number
            Account.getCurrentBalance = newBalance
            print("Your new balance is: $", newBalance)
   
    def deposit(number):
        newBalance = Account.getCurrentBalance(Bank.account) + number
        Account.getCurrentBalance = newBalance
        print("Your new balance is: $", newBalance)

class ChecquingAccount(Account):
    def __init__():
        pass
    
    def withdraw(number):
        if number > Account.getCurrentBalance(Bank.account) - 5000:
            print("You are not able to withdraw that amount.")
            Program.showAccountMenu()

        else:
            newBalance = Account.getCurrentBalance(Bank.account) + number
            Account.getCurrentBalance = newBalance
            print("Your new balance is: $", newBalance)

    def deposit(number):
        newBalance = Account.getCurrentBalance(Bank.account) + number
        Account.getCurrentBalance = newBalance
        print("Your new balance is: $", newBalance)

class Bank():
    account = 0
    account1 = Account(1, "Jerry", 0.1, 15000)
    account2 = Account(2, "Jasmine", 0.1, 30400)
    account3 = Account(3, "Melanie", 0.1, 983345)
    account4 = Account(4, "Bob", 0.1, 29875)
    account5 = Account(5, "Phil", 0.1, 18763)

    savings = False
    checquing = False

    def searchAccount():
        print("Please enter the Account Number or enter 0 to go to the Main Menu.")
        try:
            accountNumber = int(input())
            
        except:
            accountNumber = 6

        if accountNumber == 0:
            Program.showMainMenu()

        elif accountNumber >= 1 and accountNumber <= 5:
            if accountNumber == 1:
                Bank.account = Bank.account1
                Bank.savings = True

            elif accountNumber == 2:
                Bank.account = Bank.account2
                Bank.checquing = True

            elif accountNumber == 3:
                Bank.account = Bank.account3
                Bank.savings = True

            elif accountNumber == 4:
                Bank.account = Bank.account4
                Bank.checquing = True

            elif accountNumber == 5:
                Bank.account = Bank.account5
                Bank.checquing = True
        
            Program.showAccountMenu()

        else:
            print("Please enter a valid Account Number (1-5).")
            Bank.searchAccount()

Program.run()
