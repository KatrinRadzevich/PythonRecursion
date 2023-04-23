# 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# [1, 2, 3, 1, 2, 1, 5, 4, 5] -> [1, 2, 3, 1, 2, 1, 1, 4, 1]
# import random
# list_marks = []
# size = 9
# for i in range(size):
#     list_marks.append(random.randint(1, 5))
# print(list_marks)
# max = 5
# min = 1


# def change_marks(numbers: list[int], max_mark: int) -> list[int]:
#     """Заменяет пятерки на 1"""
#     for i in range(len(numbers)):
#         if numbers[i] == max_mark:
#             numbers[i] = 1
#     return numbers


# result = [i if i != max else min for i in list_marks]
# result_list = change_marks(list_marks, max)
# print(result_list)


def change_marks(marks: list[int]) -> list[int]:
    """Рекурсивная замена макисмальных оценок минимальными"""

    max_mark = max(marks)
    min_mark = min(marks)
    marks[marks.index(max_mark)] = min_mark

    if max_mark not in marks:
        return marks
    return change_marks(marks)


print(change_marks([1, 2, 3, 1, 1, 3, 4, 4, 5, 4]))

a = [1, 2, 3, 1, 1, 3, 4, 5, 5, 5]
print(a.index(5))

a[a.index(5)] = 1000
print(a)
