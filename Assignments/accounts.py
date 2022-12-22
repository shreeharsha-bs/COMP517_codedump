# Shreeharsha Satish, 201665390

import random
import datetime

class BasicAccount:
    '''
    This class describes a basic account at a bank. It has a global account number, name and users cannot overdraft

    It also has methods for depositing or withdrawing money, closing the account, printing the balance and getting
    general information on the account. You can also get a new card with an expiry date 3 years to the month on
    which the method is called.

    '''
    overdraft = False
    acNum = 0

    #  __init__(self, acName, openingBalance) - to initialize the bank account
    #  parameters - acName: string of name of account holder, openingBalance: float number of initial deposit
    #  doesn't return anything
    def __init__(self, acName, openingBalance):
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum
        self.name = acName
        self.overdraftLimit = 0
        self.initialOverdraft = 0
        self.balance = 0
        self.deposit(openingBalance)  # Use the deposit function to set openingBalance because of its error handling
        self.overdraft = BasicAccount.overdraft

    #  __str__(self) - summarizes the account
    #  parameters - self
    #  returns the name, acNum and balance
    def __str__(self):
        return f"Hello {self.name}, Your account number: {self.acNum}, Your balance amount is: £{self.balance}. You do not have a Premium Account to apply for an overdraft"

    #  deposit(self, amount) - allows money to be deposited to an account
    #  parameters - amount: float of money to be added to account
    #  returns nothing
    def deposit(self, amount):
        try:
            if(amount < 0):
                raise ValueError
            else:
                self.balance += amount
                return

        except ValueError:
            print("Invalid deposit amount")


    #  withdraw(self, amount) - allows money to be withdrawn from an account
    #  parameters - amount: float of money to be withdrawn from account depending on overdraft availability
    #  returns nothing
    def withdraw(self, amount):
        try:
            if(self.balance - amount >= 0):  # amount < Balance
                self.balance -= amount
                print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance}")

            else:
                if(self.overdraft == True and self.overdraftLimit + self.balance - amount >= 0):  # Check overdraft and limit
                    self.overdraftLimit = self.overdraftLimit + self.balance - amount
                    self.balance = self.overdraftLimit - self.initialOverdraft
                    print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance} and overdraft available is £{self.overdraftLimit}")
                    return

                elif(self.overdraft == True and self.overdraftLimit + self.balance - amount < 0):
                    print(f"You have exceeded your overdraft limit, cannot withdraw £{amount}")
                    return

                else:
                    print(f"You don't have an overdraft with your basic account, cannot withdraw £{amount}")
                    return

        except ValueError:
            print("Invalid withdrawal amount")


    #  getAvailableBalance(self)
    #  parameters - self (the object in question)
    #  returns the total balance available (actual balance + overdraft in case positive balance and just overdraft otherwise)
    def getAvailableBalance(self):
        if(self.balance > 0):
            return self.balance+self.overdraftLimit
        else:
            return self.overdraftLimit

    #  getBalance(self)
    #  parameters - self (the object in question)
    #  returns the net money (actual balance) which can be negative if you've overdrafted
    def getBalance(self):
        return self.balance

    #  printBalance(self)
    #  parameters - self (the object in question)
    #  prints the Balance instead of returning
    def printBalance(self):
        print(self.balance)
        return

    #  getName(self)
    #  parameters - self (the object in question)
    #  returns acName: string account holder name
    def getName(self):
        return self.name

    #  getAcNum(self)
    #  parameters - self (the object in question)
    #  returns acName: string format of account number
    def getAcNum(self):
        return str(self.acNum)

    #  issueNewCard(self)
    #  parameters - self (the object in question)
    #  returns nothing, prints description of the card created and its expiry date, 3 years from the month on which it was created
    def issueNewCard(self):
        self.cardNum = str(f'{random.randrange(0, (10**16)-1)}'.zfill(16))
        self.start = datetime.datetime.today().strftime('%m/%d/%Y')
        self.cardExp = (int(self.start.split('/')[0]),int(self.start.split('/')[-1][2:])+3)
        print(f"Hello, your new card has been issued, 16 digtit number: {self.cardNum} ; Expiry date: {self.cardExp}")
        return

    #  closeAccount(self)
    #  parameters - self (the object in question)
    #  returns True if account can be closed (no due overdraft) False otherwise
    def closeAccount(self):
        if(self.overdraft and self.balance < 0):
            print(f"Cannot close your account because it is overdrawn by £{-self.balance}")
            return False
        else:
            self.withdraw(self.balance)
            return True


class PremiumAccount(BasicAccount):  #inherits from the BasicAccount class
    '''
    This class is just like BasicAccount and inherits all methods but you can also overdraft and withdraw
    amounts up to the limit with this premium account.

    Also, the welcome message is more... welcoming

    '''

    overdraft = True


    #  __init__(self, acName, openingBalance, initialOverdraft) - to initialize the bank account
    #  parameters - acName: string of name of account holder, openingBalance: float number of initial deposit, initialOverdraft: float number of initial Overdraft
    #  doesn't return anything
    def __init__(self, acName, openingBalance, initialOverdraft):
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum
        self.name = acName
        self.overdraft = PremiumAccount.overdraft
        self.balance = 0
        self.initialOverdraft = 0
        self.overdraftLimit = 0
        self.deposit(openingBalance)  # Use the deposit function to set openingBalance because of its error handling
        self.setOverdraftLimit(initialOverdraft)  # Use the setOverdraftLimit function to set overdraft because of its error handling
        self.initialOverdraft = self.overdraftLimit  # Store the initialOverdraft as an instance variable, needed when closing account

    #  setOverdraftLimit(self) - sets overdraft limit
    #  parameters - newLimit: float number of new overdraft
    #  returns nothing
    def setOverdraftLimit(self, newLimit):
        try:
            if(newLimit < 0):
                raise ValueError
            else:  # The conditions below check whether the new overdraft limit is bigger or if it is made lesser, whether all the overdraft has been paid back  
                if(newLimit >= self.overdraftLimit):
                    self.initialOverdraft = newLimit + self.initialOverdraft - self.overdraftLimit  # This is to prevent any fraud from the use of this function
                    self.overdraftLimit = newLimit
                    return
                elif(newLimit < self.overdraftLimit and self.initialOverdraft==self.overdraftLimit):  # Freely change limit if nothing has been overdrafted
                    self.initialOverdraft = newLimit
                    self.overdraftLimit = newLimit
                    return
                else:
                    print("You cannot reduce your overdraft without paying it back, try again.")
                    return

        except ValueError:
            print("Invalid value entered, you need to enter a positive overdraft value")


    #  __str__(self) - summarizes the account
    #  parameters - self
    #  returns the name, acNum, balance and overdraft available
    def __str__(self):
        return f"Welcome {self.name}, You are a Premium Account holder. Your account number: {self.acNum}, Your balance amount: £{self.balance}, Overdraft amount available: £{self.overdraftLimit}"
