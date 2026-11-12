"""Задача 3.1 з П2 (корінь методом Ньютона), переписана як функція.

Було: увесь код у тілі програми разом з input і print.
Стало: функція sqrt_newton рахує і повертає результат, ввід/вивід — окремо.
"""


def sqrt_newton(a, eps=1e-6):
    """Корінь з a методом Ньютона: x = (x + a / x) / 2.

    Повертає пару (наближення, кількість кроків).
    Для a < 0 повертає None, для a == 0 — (0.0, 0).
    """
    if a < 0:
        return None
    if a == 0:
        return 0.0, 0
    x = a
    steps = 0
    while abs(x * x - a) >= eps:
        x = (x + a / x) / 2
        steps += 1
    return x, steps


if __name__ == "__main__":
    a = float(input("a = "))
    eps = float(input("eps = "))
    result = sqrt_newton(a, eps)
    if result is None:
        print("Число має бути невід'ємним")
    else:
        x, steps = result
        print("√a ≈", x)
        print("Кроків:", steps)
        print("Для порівняння a ** 0.5 =", a ** 0.5)
