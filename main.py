"""Калькулятор з меню. Усі обчислення — у модулі calc.py."""
from calc import add, sub, mul, div

MENU = """
1 — додавання
2 — віднімання
3 — множення
4 — ділення
0 — вихід"""


def read_two():
    """Прочитати два числа з клавіатури."""
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))
    return a, b


def main():
    while True:
        print(MENU)
        choice = input("Ваш вибір: ")
        if choice == "0":
            print("До побачення!")
            break
        elif choice == "1":
            a, b = read_two()
            print("Результат:", add(a, b))
        elif choice == "2":
            a, b = read_two()
            print("Результат:", sub(a, b))
        elif choice == "3":
            a, b = read_two()
            print("Результат:", mul(a, b))
        elif choice == "4":
            a, b = read_two()
            result = div(a, b)
            if result is None:
                print("Ділити на нуль не можна")
            else:
                print("Результат:", result)
        else:
            print("Невідомий пункт меню")


if __name__ == "__main__":
    main()
