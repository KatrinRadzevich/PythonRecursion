# В списке хранятся числа. Нужно выбрать четные числа и составить список пар(число,квадрат)
# 1, 2, 3, 5, 8, 15, 23, 38
#  ->[(2,4), (8, 64), (38, 1444)]
# list = [1, 2, 3, 5, 8, 15, 23, 38]
# list_2 = []
# for i in list:
#     if i % 2 == 0:
#         list_2.append((i, i**2))

# print(list_2)
# //////////////////////////////////////////////
# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list_2 = select(int, list1)
# print(list_2)
# list_2 = where(lambda x: x % 2 == 0, list1)
# print(list_2)
# list_2 = list(select(lambda x: (x, x**2), list_2))
# print(list_2)
# //////////////////////////////////////////////
list1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_2 = map(int, list1)
print(list_2)
list_2 = filter(lambda x: x % 2 == 0, list1)
print(list_2)
list_2 = list(map(lambda x: (x, x**2), list_2))
print(list_2)