def upper(*words: str) -> None:
    uppercased = map(str.upper, words) # map function to apply a function on iterable
    print(*uppercased)
    #print(list(uppercased))
    #for word in uppercased:
     #   print(word, sep= "", end=" ")


def main():
    upper("This", "is", "python")


if __name__ == "__main__":
    main()
