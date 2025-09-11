def main():
    try:
        x = int(input("What's X? "))
    except ValueError:
        print("X is not an integer")
    else:
        print(f"x is {x}")

if __name__ == "__main__":
    main()