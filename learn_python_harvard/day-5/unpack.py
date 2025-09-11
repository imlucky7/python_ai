from typing import Any

def weightedTotal(math: float, physics: float, chemistry: float) -> float:
    return (math * 0.5 + physics * 0.7 + chemistry * 0.03) / 10

def f(*args: int,  **kwargs: Any) -> None:
    """
    *args -> variable number of arguments
    *kwargs -> variable number of named arguments
    """
    print ("Positional:", args)
    print("Named:", kwargs)

"""
unpack list 
"""
marks = [65, 35, 56]

print(weightedTotal(*marks))


"""
maintaining sequence
"""
print(weightedTotal(math=65, chemistry=56, physics=35))

"""
unpack in sequence
""" 
marksDics = {"math": 65, "chemistry": 56, "physics": 35}
print(weightedTotal(**marksDics))

f(100, 50, 20)
# Output:
# Positional: (100, 50, 20)
# Named: {}

f(name="Alice", age=30)

f(1, 2, 3, name="Alice", age=30)
# Output:
# Positional: (1, 2, 3)
# Named: {'name': 'Alice', 'age': 30} 