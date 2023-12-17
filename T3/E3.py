class BankAccount:
    def __init__(self, account_number="", holder="", balance=0.0, account_type=""):
        self.account_number=account_number
        self.holder=holder
        self.balance=balance
        self.account_type=account_type

    def get_account_number(self):
        return self.account_number
    def set_account_number(self,account_number):
        self.account_number = account_number

    def get_holder(self):
        return self.holder
    def set_holder(self,holder):
        self.holder=holder

    def get_balance(self):
        return self.balance
    def set_balance(self,balance):
        self.balance=balance

    def get_account_type(self):
        return self.account_type
    def set_account_type(self,account_type):
        self.account_type=account_type
    
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"You deposit {amount}$, your balance is {self.balance}$.")
        else:
            print("Invalid deposit amount. Amount must be bigger than 0")
    
    def withdraw(self,amount):
        if amount>0 and amount<= self.balance:
            self.balance-=amount
            print(f"Withdrew {amount}$, your balnce is {self.balance}$.")
        else:
            print("Invalid withdrawal. Either the amount is invalid or insufficient funds.")

    def print_info(self):
        print("Account Balance")
        print(f"Your account number is {self.account_number}")
        print(f"Account holder: {self.holder}")
        print(f"Actual balance: {self.balance}")
        print(f"Account type: {self.account_type}")

account= BankAccount("111222333", "Pablo S", 2000.0, "Savings")
account.print_info()

account.deposit(1000)
account.withdraw(300)