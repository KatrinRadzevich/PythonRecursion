# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power_of_number(num_1: int, num_2: int) -> int:
    """Возведение num_1  в степень num_2 рекурсией"""
    if num_2 == 1:
        return num_1
    if num_2 == 0:
        return 1
    return num_1 * power_of_number(num_1, num_2 - 1)


a = int(input('Введите число,котоое хотите возвести в степень: '))
b = int(input('Введите степень: '))
print(power_of_number(a, b))
