def main():
    hello()
    name = input("What's your name? ")
    name = name.strip().title()
    hello(name)
    first, last = name.split(' ')
    hello(last)

def hello(name="world!"):    
    print(f"Hello, {name}")


main()