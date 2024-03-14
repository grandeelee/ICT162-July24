class BankAccount:
    """
    Represents a bank account with basic operations like deposit, withdraw, and transfer.

    Attributes:
        _interestRate (float): The annual interest rate for all BankAccount instances (class variable).
        _accountId (int): The unique identifier for the bank account.
        _balance (float): The current balance of the bank account.

    Methods:
        __init__(self, id, amount):
            Initializes a BankAccount instance.

        deposit(self, amount):
            Deposits the given amount into the bank account.

        withdraw(self, amount):
            Withdraws the specified amount from the bank account if sufficient balance is available.

        transfer(self, ba, amount):
            Transfers the specified amount from this bank account to another if sufficient balance is available.

        accumulateInterest(self):
            Increases the account balance by applying the annual interest rate.

        __str__(self):
            Returns a formatted string representation of the bank account.

    Properties:
        accountId:
            Gets the account ID.

        balance:
            Gets or sets the account balance.

    Note:
        - The interest rate is a class-level attribute shared among all BankAccount instances.
        - To access and modify the balance, use the 'balance' property.

    Usage:
        # Create a new bank account
        account = BankAccount(12345, 1000.0)

        # Deposit money
        account.deposit(500.0)

        # Withdraw money
        account.withdraw(200.0)

        # Transfer money to another account
        another_account = BankAccount(54321, 200.0)
        account.transfer(another_account, 300.0)

        # Accumulate interest
        account.accumulateInterest()

        # Print the account information
        print(account)
    """
    _interestRate = 0.03

    def __init__(self, id, amount): 
        self._accountId = id 
        self._balance = amount 
    
    @property 
    def accountId(self): 
        return self._accountId 
    
    @property 
    def balance(self): 
        return self._balance 

    @balance.setter 
    def balance(self, amt): 
        self._balance = amt 

    def deposit(self, amount=20):
        """
        Deposit the specified amount into the bank account.

        Args:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        self._balance += amount

    def withdraw(self, amount=20):
        """
        Withdraw the specified amount from the bank account if sufficient balance is available.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def transfer(self, ba, amount):
        """
        Transfer the specified amount from this bank account to another if sufficient balance is available.

        Args:
            ba (BankAccount): The destination bank account to transfer funds to.
            amount (float): The amount to be transferred.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        if self.withdraw(amount):
            ba.deposit(amount)
            return True
        return False

    def accumulateInterest(self):
        """
        Accumulate interest on the account balance based on the annual interest rate.

        This method increases the account balance by applying the annual interest rate.

        Returns:
            None
        """
        self._balance += self._balance * type(self)._interestRate

    def __str__(self):
        """
        Return a formatted string representation of the bank account.

        Returns:
            str: A string containing the account ID and balance, e.g., "12345 1300.00"
        """
        return f'{self._accountId} {self._balance:.2f}'

"""
a. A JuniorAccount is a BankAccount. A JuniorAccount has an additional guardian as instance variable. Write the Junior Account class as follows: 
i. The JuniorAccount class as a subclass of BankAccount 
ii. A constructor that has the id, guardian and balance. 
iii. Get property for guardian. 
iv. A withdraw method that limits withdrawal to maximum of 50 dollars. This method also returns true if the withdrawal is successful and false otherwise. 
v. An accumulateInterest method that computes adds the interest amount to the balance. Junior account holders earn 1% more. 
vi. The str method that returns all information of the junior account. 
b. Write an application to create a JuniorAccount object. Test the deposit, withdrawal and accumuateInterest methods. 
c. Identify, where applicable, methods that exhibit method overriding by replacement/refinement. 
"""


class JuniorAccount(BankAccount):
    def __init__(self, id, guardian, balance):
        super().__init__(id, balance)
        self._guardian = guardian

    @property
    def guardian(self):
        return self._guardian

    def withdraw(self, amount=20, guardian=None):
        # # override by replacement
        # if amount <= 50 and amount <= self.balance:
        #     self.balance -= amount
        #     return True
        # return False
        # override by refinement
        if guardian == self.guardian:
            return super().withdraw(amount)
        elif amount <= 50:
            return super().withdraw(amount)
        else:
            return False


    def accumulateInterest(self):
        # override by replacement
        # self.balance += self.balance * (type(self)._interestRate + 0.01)
        # override by refinement?
        super().accumulateInterest()
        self.balance += self.balance * 0.01

    def transfer(self, ba, amount, guardian=None):
        """
        Transfer the specified amount from this bank account to another if sufficient balance is available.

        Args:
            ba (BankAccount): The destination bank account to transfer funds to.
            amount (float): The amount to be transferred.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        if self.withdraw(amount, guardian):
            ba.deposit(amount)
            return True
        return False


    def __str__(self):
        return f'{super().__str__()} {self.guardian}'

if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("12345", 1000.0)
    # Deposit money
    account.deposit(500.0)
    # Withdraw money
    account.withdraw(200.0)
    # Transfer money to another account
    another_account = BankAccount("54321", 200.0)
    account.transfer(another_account, 300.0)
    # Accumulate interest
    account.accumulateInterest()
    # Print the account information
    print(account)

    # Creating a JuniorAccount object
    junior_acc = JuniorAccount("1234", "Grandee", 1000.00)
    # Depositing money
    junior_acc.deposit(500.00)
    # Trying to withdraw
    withdraw_success = junior_acc.withdraw(60.00, "jon")
    if withdraw_success:
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed. Exceeds limit or insufficient balance.")
    # Accumulating interest
    junior_acc.accumulateInterest()
    print(junior_acc.transfer(another_account, 60, "Grandee"))
    # Printing account information
    print(junior_acc)

