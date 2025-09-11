MOVIES = [
    " ben 10 ",
    " ekenbabu ",
    "terminator",
    "harry potter"
]
MOVIES.append("feluda")
MOVIES.extend(["move1", "movie2"])

def main():
    temp_store = [] 
    print(MOVIES)

    # One format of for loop
    for str in MOVIES:
        temp_store.append(str.strip().title())
    print(", ".join(temp_store))

    # List comprehension
    temp_list = [movie.strip().title() for movie in MOVIES if len(movie.strip()) > 8]
    # Dict comprehension
    temp_dict = {elem: len(elem) for elem in temp_list}
    print("Trick loop:", temp_dict)

    # Another format of for loop
    for index in range(len(MOVIES)):
        print(f"Movie no {index+1} is {MOVIES[index].strip().title()}")

if __name__ == "__main__":
    main()