import sys
import cowsay


def main():
    if len(sys.argv) == 2:
        cowsay.cheese("hello, " + sys.argv[1])


if __name__ == "__main__":
    main()
