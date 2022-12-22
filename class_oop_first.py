class Account:
    '''
    This class is used for creating bank accounts
    '''
    openBalance = 0
    instance_count = 0

    def __init__(self, acNumber, name, openBalance, typeAccount):
        self.acNumber = acNumber
        self.name = name
        self.openBalance = openBalance
        self.typeAccount = typeAccount
        Account.instance_count += 1
        print("Account created")


    def __str__(self):
        print(self.name)
        print("AC number: " + str(self.acNumber))
        print("AC balance: " + str(self.openBalance))
        print("AC type: " + str(self.typeAccount))
        return ""

    def deposit(self, amount):
        self.openBalance += amount
        return 0

    def withdraw(self, amount):
        if(amount > self.openBalance):
            print("Insufficient balance")
            return 0
        else:
            self.openBalance -= amount
            return 0

    def get_balance(self):
        #print("Your balance is ")
        return self.openBalance


if __name__ == '__main__':
    acc1 = Account('123', 'John', 10.05, 'current')
    acc2 = Account('345', 'John', 23.55, 'savings')
    acc3 = Account('567', 'Phoebe', 12.45, 'investment')
    print(acc1)
    print(acc2)
    print(acc3)
    acc1.deposit(23.45)
    acc1.withdraw(12.33)
    print('balance:', acc1.get_balance())

    print('Number of Account instances created:', Account.instance_count)

