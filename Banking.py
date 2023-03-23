class Program():
    #Main Menu program
    def showMainMenu():
        #Initializes user input to 0
        userInput = 0

        #Prints the Main Menu screen and asks for user input
        try: 
            print("MAIN MENU")
            print("1. Select Account")
            print("2. Exit")
            userInput = int(input())
        
        #Error handling if user enters something invalid
        except:
            userInput = 0

        #Displays the search account prompt
        if userInput == 1:
            Bank.searchAccount()

        #Exits the program
        elif userInput == 2:
            print("Thank you for banking with us.")

        #Error handling if the user enters something invalid
        else:
            print("Please enter a valid input (either 1 or 2).")
            Program.showMainMenu()

    #Account Menu program
    def showAccountMenu():
        #Initializes user input to 0
        userInput2 = 0

        #Prints the account menu
        print("ACCOUNT MENU")
        print("Account Number: ", Account.getAccountNumber(Bank.account))
        print("Account Holder Name: ", Account.getAccountHolderName(Bank.account))
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit Account")
        
        #Prompts the user for input
        try: 
            userInput2 = int(input())

        #Error handling if the user enters something invalid
        except:
            userInput2 = 0
            print("Please enter a valid input.")
            Program.showAccountMenu()

        #Disaplays the current balance of the account
        if userInput2 == 1:
            print("Current Balance: $", Account.getCurrentBalance(Bank.account))
            Program.showAccountMenu()

        #Deposit section
        elif userInput2 == 2:
            try: 
                userInput3 = float(input("How much would you like to deposit?"))

            except:
                userInput3 = 0
                print("Please enter a valid input")

            #Goes to the correct deposit method
            if userInput3 > 0:
                if Bank.savings == True:
                    SavingsAccount.deposit(userInput3)

                elif Bank.checquing == True:
                    ChecquingAccount.deposit(userInput3)

        #Withdrawl section
        elif userInput2 == 3:
            try: 
                userInput3 = float(input("How much would you like to withdraw?"))

            except:
                userInput3 = 0
                print("Please enter a valid input.")

            #Goes to the correct withdraw method
            if userInput3 > 0:
                if Bank.savings == True:
                    SavingsAccount.withdraw(userInput3)

                elif Bank.checquing == True:
                    ChecquingAccount.withdraw(userInput3)

            else:
                print("Please enter a valid input.")
                Program.showAccountMenu()
        
        #Returns to the main menu
        elif userInput2 == 4:
            Program.showMainMenu()

        #Error handling if the user enters something invalid
        else:
            print("Please enter a valid input (1-4).")
            Program.showAccountMenu()

    #Runs the program
    def run():
        Program.showMainMenu()

class Account():

    #Initializes the attributes of an account
    def __init__(self, number, name, interest, balance):
        self.number = number
        self.name = name
        self.interest = interest
        self.balance = balance

    #Gets the account number
    def getAccountNumber(self):
        return self.number

    #Gets the account name
    def getAccountHolderName(self):
        return self.name

    #Gets the rate of interest
    def getRateOfInterest(self):
        return self.interest

    #Gets the current balance
    def getCurrentBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__():
        pass
    
    #Withdraw section
    def withdraw(number):
        #Tells the user they cannot withdraw that much
        if number > Account.getCurrentBalance(Bank.account):
            print("You are not able to withdraw that amount.")
            Program.showAccountMenu()

        #Withdraws money from the account
        else:
            newBalance = Account.getCurrentBalance(Bank.account) + number
            Account.getCurrentBalance = newBalance
            print("Your new balance is: $", newBalance)
   
    #Deposits money into the account
    def deposit(number):
        newBalance = Account.getCurrentBalance(Bank.account) + number
        Account.getCurrentBalance = newBalance
        print("Your new balance is: $", newBalance)

class ChecquingAccount(Account):
    def __init__():
        pass
    
    def withdraw(number):
        #Tells the user they cannot withdraw that amount
        if number > Account.getCurrentBalance(Bank.account) - 5000:
            print("You are not able to withdraw that amount.")
            Program.showAccountMenu()

        #Withdraws money from the account
        else:
            newBalance = Account.getCurrentBalance(Bank.account) + number
            Account.getCurrentBalance = newBalance
            print("Your new balance is: $", newBalance)

    #Deposits money to the account
    def deposit(number):
        newBalance = Account.getCurrentBalance(Bank.account) + number
        Account.getCurrentBalance = newBalance
        print("Your new balance is: $", newBalance)

class Bank():

    #Creates account objects for each person
    account = 0
    account1 = Account(1, "Jerry", 0.1, 15000)
    account2 = Account(2, "Jasmine", 0.1, 30400)
    account3 = Account(3, "Melanie", 0.1, 983345)
    account4 = Account(4, "Bob", 0.1, 29875)
    account5 = Account(5, "Phil", 0.1, 18763)

    #Initializes the checks to false
    savings = False
    checquing = False

    def searchAccount():

        #Prompts the user for an account number
        print("Please enter the Account Number or enter 0 to go to the Main Menu.")
        try:
            accountNumber = int(input())
            
        #Error handling if the user enters something invalid
        except:
            accountNumber = 6

        #Returns to the main menu
        if accountNumber == 0:
            Program.showMainMenu()

        #Valid account number was entered, account is set to that value
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

        #Error handling if the user enters something invalid
        else:
            print("Please enter a valid Account Number (1-5).")
            Bank.searchAccount()

#Runs the program
Program.run()
