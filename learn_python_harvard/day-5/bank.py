class Account:
    def __init__(self):
        self._balance: float = 0

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, n: float):
        self._balance += n

    def withdraw(self, n: float):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    """ 
    NOT CORRECT! "_balance" is protected and used outside of the class in which it is declared
    Variable name with underscore is considered as protected 
    and should change it's state directly
    """
    #account._balance = 100 
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
