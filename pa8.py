class Account():
    def __init__(self, idIn, balanceIn): # note, the initializer is passed 2 parameters
        self.__id = idIn
        self.__balance = balanceIn
        self.__depositCount = 0
        self.__withdrawalCount = 0
        self.__depositSum = 0
        self.__withdrawalSum = 0
    def GetId(self):
        return self.__id
    def SetId(self, idIn):
        self.__id = idIn
    # write all of the other Get & Set methods
    def GetBalance(self):
        return self.__balance
    def SetBalance(self, balanceIn):
        self.__balance = balanceIn

    def GetDepositCount(self):
        return self.__depositCount
    def SetDepositCount(self, depositCountIn):
        self.__depositCount = depositCountIn

    def GetWithdrawlCount(self):
        return self.__withdrawalCount
    def SetWithdrawal(self, withdrawalIn):
        self.__withdrawalCount = withdrawalIn

    def GetDepositSum(self):
        return self.__depositSum
    def SetDepositSum(self, depositSumIn):
        self.__depositSum = depositSumIn

    def GetWithdrawalSum(self):
        return self.__withdrawalSum
    def SetWithdrawal(self,withdrawalSumIn):
        self.__withdrawalSum = withdrawalSumIn
       
    
    def Deposit(self, amount):
        self.__balance = self.__balance + amount
        self.__depositCount = self.__depositCount + 1
        # this method needs one more statement in it
        self.__depositSum += amount

    # other than the Get/Set methods, you need to write the Withdrawal method
    def Withdrawal(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__withdrawalCount += 1
            self.__withdrawalSum += amount
            return True
        else:
            return False

    # HINT: when writing the Withdrawal method, it likely needs to return a value to main indicating if it was successful or not.

def main():
    print("Account  Transaction     Amount      Balance")
    print("---------------------------------------------------------")

    acct1 = Account("ABC123", 1000)
    acct2 = Account("DEF456", 1000)

    inFile = open("pa8.trans", 'r')
    
    account = inFile.readline().strip()
    transactionType = inFile.readline().strip()
    amount = eval(inFile.readline())
    transactionStatus = ""

    while account != "ZZZ999":
        if account == acct1.GetId():
            if transactionType == "D":
                transactionType = "Deposit"
                acct1.Deposit(amount)
                
            elif transactionType == "W":
                transactionType = "Withdarwal"
                currentWithdrawal = acct1.Withdrawal(amount)
                if currentWithdrawal == False:
                    transactionStatus = "<denied>"
                
            currentBalance = acct1.GetBalance()

        elif account == acct2.GetId():
            if transactionType == "D":
                transactionType = "Deposit"
                acct2.Deposit(amount)

            elif transactionType == "W":
                transactionType = "Withdarwal"
                currentWithdrawal = acct2.Withdrawal(amount)
                if currentWithdrawal == False:
                    transactionStatus = "<denied>"

            currentBalance = acct2.GetBalance()

        print(format(account,'8'), format(transactionType,'12'), format(amount, '9.2f'), format(currentBalance,'12.2f'), "  ", format(transactionStatus))
        
        account = inFile.readline().strip()
        transactionType = inFile.readline().strip()
        amount = eval(inFile.readline())
        transactionStatus = ""

main()

