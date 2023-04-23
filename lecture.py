
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


number = (int(input('Введите число: ')))
print(fib(number))

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# # быстрая сортировка
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)


# print(quicksort([10, 5, 2, 3]))
# # сортировка слиянием
# def merge_sort(nums):
#     # делим все элементы попалам,пока их не останется по 1
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         # начинаем упорядочивать создаем пары и
#         # сравниваем элементы между собой и записываем в список nums[k]
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         # проверям остались ли значения и добавляем их в конец
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1


# nums = [38, 27, 43, 3, 9, 10, 5]
# merge_sort(nums)
# print(nums)
