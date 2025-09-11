# '-> str' hints return type hint
#n: int hints variable type
def meow(n: int) -> str:
    """It return meow number of times as input

    Args:
        n (int): Number of times of meow

    Returns:
        str: meow in each line
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

"""
pip install mypy 
mypy typeHintExample.py
mypy is a static type checker for Python code. Its main use is to analyze 
the Python programs without running them and to ensure your use of type 
hints (annotations) is correct and consistent.

autoDocstring extension to help generating docstring
"""