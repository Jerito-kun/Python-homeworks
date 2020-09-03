# Домашняя работа, первое задание

"""
1. Написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел.
Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа

2. Написать функцию, которая на вход принимает список из целых чисел,
и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)

3. Создать декоратор для замера времени выполнения функции
"""

from time import time
from functools import wraps


def run_timer(func):  # Способ без использования дополнительных библиотек
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        print("%s --> выполнено за %f сек." % (wrapper.__name__, time() - start_time))

    return wrapper


def run_timer_wraps_mode(func):  # С использованием дополнительной библиотеки
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print("%s --> выполнено за %f сек." % (wrapper.__name__, time() - start_time))

    return wrapper


def trace(symbols):
    """
    Trace calls made to the decorated function.
    """

    def _trace(func):
        calls = [-1]

        @wraps(func)
        def inner(*args, **kwargs):
            calls[0] += 1
            function_data = f"{func.__name__}({','.join([str(arg) for arg in args])})"
            print(symbols * calls[0], end="")
            print(f"--> {function_data}")
            result = func(*args, **kwargs)
            print(symbols * calls[0], end="")
            print(f"<-- {function_data} == {result}")
            calls[0] -= 1
            return result

        return inner

    return _trace


@trace("____")
def fib(position):  # Каждое последующее число равно сумме двух предыдущих чисел последовательности Фибоначчи
    result = 1
    if position > 1:
        result = fib(position - 1) + fib(position - 2)
    return result


@run_timer_wraps_mode
def multiple_func(*nums, count=2):  # Функция возведения в степень
    powered_list = []
    for num in nums:
        powered_list.append(num ** count)
    print(powered_list)


def is_odd(number):  # Проверка на нечётные числа
    if number == 0:
        return False
    if number % 2 != 0:
        return True
    return False


def is_even(number):  # Проверка на чётные числа
    if number % 2 != 0:
        return False
    return True


def is_simple(number):  # Проверка на простоту числа
    if number == 0:  # Ноль не является простым числом по определению
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


@run_timer
def select_nums(numbers, selection_type="ODD"):  # Возвращение чисел по выбранному критерию
    check_functions = {'ODD': is_odd, 'EVEN': is_even, 'SIMPLE': is_simple}
    result = []
    for number in numbers:
        if check_functions[selection_type](number):
            result.append(number)
    print(result)


def main():
    print("Вызов функции возведения чисел в степень без указания степени (по умолчанию — в квадрат")
    multiple_func(1, 3, 5)
    print("Вызов функции возведения чисел в степень с указанием степени (в примере — в степень 10240")
    multiple_func(1, 3, 5, count=10240)
    print("Вывод списка только нечётных чисел для набора чисел 1, 2, 3, 4, 5, 6, 7")
    select_nums([1, 2, 3, 4, 5, 6, 7], "ODD")
    print("Вывод списка только чётных чисел для набора чисел 1, 2, 3, 4, 5, 6, 7")
    select_nums([1, 2, 3, 4, 5, 6, 7], "EVEN")
    print("Вывод списка только простых чисел для набора чисел 1, 2, 3, 4, 5, 6, 7")
    select_nums([1, 2, 3, 4, 5, 6, 7], "SIMPLE")
    print("Вывод числа Фибоначчи (№ 3 в последовательности)")
    fib(3)


if __name__ == "__main__":
    main()
