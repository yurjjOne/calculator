"""Підключення власних функцій з tools.py через import."""
from tools import is_even, hypotenuse

if __name__ == "__main__":
    n = int(input("Ціле число: "))
    if is_even(n):
        print(n, "— парне")
    else:
        print(n, "— непарне")

    a = float(input("Катет a: "))
    b = float(input("Катет b: "))
    print("Гіпотенуза:", hypotenuse(a, b))
