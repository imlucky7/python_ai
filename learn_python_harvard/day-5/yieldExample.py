from typing import Generator
#from typing import Iterator

# run the program with 1000000 iterations
def main():
    number: int = int(input("What's n?"))
    t = helperGenerator(number)  # helper(number)
    for s in t:
        print(s)


# It stores 1000000 times * in the memory and return; hence OOM exception
def helper(n: int) -> list[str]:
    temp: list[str] = []
    for i in range(n):
        temp.append("*" * i)
    return temp


# The generator function returns * in each iteraration; hence no OOM exception
def helperGenerator(n: int) -> Generator[str, None, None]:  # -> Iterator[str]:
    for i in range(n):
        yield "*" * i


if __name__ == "__main__":
    main()
