# 31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи|
# def fib(n):
#     if n in (0, 1):
#         return 1
#     return fib(n - 1) + fib(n - 2)


# number = (int(input('Введите число: ')))
# print(fib(number - 2))
# for i in range(2, number + 1):
#     print(fib(i - 2))

def f(n) -> int:
    '''Возвращает чило Фибоначчи по номеру'''
    if n == 0 or n == 1:
        return 1
    return f(n - 1) + f(n - 2)


n = int(input())
print(f(n - 2))
