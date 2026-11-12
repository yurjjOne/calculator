"""Модуль calc — функції калькулятора (без вводу й виводу)."""


def add(a, b):
    """Сума двох чисел."""
    return a + b


def sub(a, b):
    """Різниця a - b."""
    return a - b


def mul(a, b):
    """Добуток двох чисел."""
    return a * b


def div(a, b):
    """Частка a / b; при діленні на нуль повертає None."""
    if b == 0:
        return None
    return a / b
