class Car:
    def __init__(self, brand: str):
        if not brand:
            raise ValueError("Missing brand")
        self.brand = brand

    def __str__(self):
        return self.brand


class Hatchback(Car):
    def __init__(self, brand: str, color: str):
        super().__init__(brand)
        self.color = color

    def __str__(self):
        return f"{self.brand} car of {self.color} color"


class Sedan(Car):
    def __init__(self, brand: str, color: str):
        super().__init__(brand)
        self.color = color

    def __str__(self):
        return f"{self.brand} car of {self.color} color"


def main():
    alto800 = Hatchback("Maruti", "Red")
    print(alto800)
    print(Sedan("Hyundai", "Black"))


if __name__ == "__main__":
    main()
