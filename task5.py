# 39. Даны два массива чисел. Требуется вывести те
# уникальные элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Элементы обоих
# массивов вводятся в две строки через пробел.
# 1 2 3 4 5 6
# 4 5 6 7 8 -> 1 2 3
n = int(input('Введите размер первого массива чисел: '))
m = int(input('Введите размер второго массива чисел: '))
list_1 = []
for i in range(n):
    list_1.append(
        int(input(f'Введите {i + 1} элемент первого массива чисел: ')))
list_2 = []
for i in range(m):
    list_2.append(
        int(input(f'Введите {i + 1} элемент второго массива чисел: ')))
print(list_1)
print(list_2)

same_list = []
res_list = []
for i in list_1:
    if i not in list_2:
        res_list.append(i)

print(res_list)
