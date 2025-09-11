def main():
    x = int(input("Enter a number to calculate square: "))
    print(f"Square value of {x} is", square(x))

def square(input):
    return pow(input, 2)

main()