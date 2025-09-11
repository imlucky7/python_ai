amount = 0


def withdraw(n: int) -> None:
    global amount
    amount -= n


def deposit(n: int) -> None:
    global amount
    amount += n


def main():
    print("Balance", amount)
    deposit(100)
    withdraw(50)
    print("Balance", amount)


if __name__ == "__main__":
    main()
