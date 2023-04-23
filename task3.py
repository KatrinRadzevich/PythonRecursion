# 35. Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
#  имеет 2 делителя: 1  и n(само число)
# num = int(input('Введите число: '))


# # def define(num: int) -> bool:
# # """Проверяет, является ли число простым"""
# # if num == 2 or num == 3:
# #     return True
# # elif num % 1 == 0 and num % num == 0 and num % 2 != 0 and num % 3 != 0:
# #     return True
# # return False
# def is_prime(number):
#     # Если число меньше 2, оно не является простым
#     if number < 2:
#         return False

#     # Перебираем числа от 2 до корня из числа (включительно)
#     for i in range(2, int(number**0.5) + 1):
#         # Если число делится без остатка на текущее значение, оно не является простым
#         if number % i == 0:
#             return False

#     # Если число не делится нацело ни на одно число от 2 до корня из числа, оно простое
#     return True


# print(is_prime(num))


def is_prime(n: int, divider: int) -> bool:
    """рекурсивная проверка простоты числа"""
    if divider == 1:
        return True
    if n % divider == 0:
        return False
    return is_prime(n, divider - 1)


n = 6
print(is_prime(n, n//2 + 1))

for i in range(n//2 + 1, 1, -1):
    print(i, n % i)
