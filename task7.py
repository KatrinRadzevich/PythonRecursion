# 43. Дан список чисел. Посчитайте, сколько в
# нем пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют
# одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся
# на одной строке через пробел.
# 1 2 1 3 4 5 3 4 -> 3
# 1 2 1 3 4 3 1 -> 2
list_1 = [int(i) for i in input('Enter the elements: ').split()]

pair_count = 0
unik = list(set(list_1))
for i in range(len(unik)):
    for j in range(i+1, len(list_1)):
        if unik[i] == list_1[j]:
            pair_count += 1

print(list)
print(pair_count)
# list = [1, 2, 1, 3, 4, 5, 3, 4]
# # res_list = ', '
# # res_list = list

# # # final = list.intersection(res_list)
# # count = 0
# # for i in range(1, len(list)):
# #     if list[i] == list[i-1]:
# #         res_list.append(i)


# print(sorted(list))
# print(res_list)
# print(final)
# print(quicksort([10, 5, 2, 3]))
# # сортировка слиянием
def merge_sort(nums):
    # делим все элементы попалам,пока их не останется по 1
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        # начинаем упорядочивать создаем пары и
        # сравниваем элементы между собой и записываем в список nums[k]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        # проверям остались ли значения и добавляем их в конец
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


nums = [1, 2, 1, 3, 4, 3, 1, 0]
merge_sort(nums)
uniqe = list(set(nums))
print(nums)
print(uniqe)
pair_count = 0
for i in range(0, len(uniqe)):
    for j in range(i+1, len(uniqe)):
        if uniqe[i] == nums[j]:
            pair_count += 1
print(pair_count)


# a = [int(input('Введите элемент массива -> '))
#      for i in range(int(input('Введите размер массива -> ')))]

# counts = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             counts += 1

# print(f'В массиве {a} пар элементов, равных друг другу = {counts}')
