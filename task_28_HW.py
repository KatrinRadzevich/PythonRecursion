# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя

# 2 2
#     4

def sum_of_numbers(num_1: int, num_2: int) -> int:
    """Сумма num_1  и num_2 рекурсией"""
    if num_1 < 0 or num_2 < 0:
        return print('Числа должны быть неотрицательными')
    if num_2 == 0:
        return num_1
    return sum_of_numbers(num_1 + 1, num_2 - 1)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(sum_of_numbers(a, b))