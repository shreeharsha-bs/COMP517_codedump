import random
import datetime

class BasicAccount:
    '''
    This class describes a basic account at a bank. It has a global account number, name and users cannot overdraft

    It also has methods for depositing or withdrawing money, closing the account, printing the balalnce and getting
    general information on the account. You can also get a new card with an expiry date 3 years to the month on
    which the method is called.

    '''
    overdraft = False
    acNum = 0

    def __init__(self, acName, openingBalance):
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum
        self.acName = acName
        self.balance = openingBalance
        self.overdraftLimit = 0
        self.overdraft = BasicAccount.overdraft

    def __str__(self):
        return f"Hello {self.acName}, Your account number: {self.acNum}, Your balance amount is: £{self.balance}. You do not have a Premium Account to apply for an overdraft"

    def deposit(self, amount):
        try:

            if(amount < 0):
                raise ValueError

            if(self.initialOverdraft == self.overdraftLimit):  # Change balance when there's no overdraft
                self.balance += amount
            else:
                self.overdraftLimit += amount   # Change overdraft limit when there's a previous overdraft instead of the balance


        except ValueError:

            print("Invalid deposit amount")



    def withdraw(self, amount):
        try:
            if (self.balance - amount >= 0):  # amount < Balance
                self.balance -= amount
                print(f"{self.acName} has withdrawn £{amount}. New balance is £{self.balance}")

            else:
                print("Withdrawal amount exceeds current balance.")
                if(self.overdraft == True and self.overdraftLimit + self.balance - amount >= 0):  # Check overdraft and limit
                    self.overdraftLimit = self.overdraftLimit + self.balance - amount
                    self.balance = 0
                    print(f"{self.acName} has withdrawn £{amount}. New balance is £{self.balance} and overdraft available is £{self.overdraftLimit}")

                elif(self.overdraft == True and self.overdraftLimit + self.balance - amount < 0):
                    print("You have exceeded your overdraft limit, cannot withdraw amount")

                else:
                    print("You don't have an overdraft with your basic account")

        except ValueError:
            print("Invalid withdrawal amount")

    def getAvailableBalance(self):
        return self.balance

    def getBalance(self):
        if(self.overdraft == False):
            return self.balance
        else:
            return self.balance + self.overdraftLimit - self.initialOverdraft

    def printBalance(self):
        print(self.balance)

    def getName(self):
        return self.acName

    def getAcNum(self):
        return self.acNum

    def issueNewCard(self):
        self.cardNum = str(f'{random.randrange(0, (10**16)-1)}'.zfill(16))
        self.start = datetime.datetime.today().strftime('%m/%d/%Y')
        self.cardExp = (int(self.start.split('/')[0]),int(self.start.split('/')[-1])+3)
        return f"Hello, your new card has been issued, 16 digtit number: {self.cardNum} ; Expiry date: {cardExp}"

    def closeAccount(self):
        if(self.overdraft and (self.initialOverdraft == self.overdraftLimit)):
            self.withdraw(self.balance)
            return True
        elif(self.overdraft and (self.initialOverdraft != self.overdraftLimit)):
            print(f"Cannot close account because you've overdrawn by £{self.initialOverdraft -self.overdraftLimit - self.balance}")
            return False
        else:
            self.withdraw(self.balance)
            return True


class PremiumAccount(BasicAccount):
    '''
    This class is just like BasicAccount and inherits all methods but you can also overdraft and withdraw
    amounts up to the limit with this premium account.

    Also, the welcome message is more... welcoming

    '''

    overdraft = True

    def __init__(self, acName, openingBalance, initialOverdraft=0):
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum
        self.acName = acName
        self.overdraft = PremiumAccount.overdraft
        self.balance = openingBalance
        self.initialOverdraft = initialOverdraft  # Keep original overdraftlimit, needed when closing account conditions are checked
        self.overdraftLimit = initialOverdraft


    def setOverdraftLimit(self, overdraftLimit):
        self.overdraftLimit = overdraftLimit

    def __str__(self):
        return f"Welcome {self.acName}, You are a Premium Account holder. Your account number: {self.acNum}, Your balance amount: £{self.balance}, Overdraft amount available: £{self.overdraftLimit}"
