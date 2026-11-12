"""Додаткове завдання Л4: сума цифр рекурсією."""


def digit_sum_rec(n):
    """Сума цифр невід'ємного цілого n (рекурсивно)."""
    if n < 10:          # база: одна цифра
        return n
    return n % 10 + digit_sum_rec(n // 10)   # крок: остання цифра + решта


if __name__ == "__main__":
    print(digit_sum_rec(50525))   # 17
    n = int(input("Ціле невід'ємне число: "))
    print("Сума цифр:", digit_sum_rec(n))
