# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом
# все не в порядке
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам
word = 'пара-ра-ра-рам рам-пам-папам па-ра-па-да пак-мав'
def anti_vowel(text):
   text = list(text)
   for i in text[::-1]:
       if i in 'б,в,г,д,ж,з,й,к,л,м,н,п,р,с,т,ф,х,ц,ч,ш,щ,ъ,ь,-':
          text.remove(i)
   return str(''.join(text))
print(anti_vowel(word))

aaa = anti_vowel(word).replace("-", "")
# print(aaa)
lll = (aaa.split())
# # lll = ['4', '4', '4', '4']
# # # print(type(phrase))
# print(lll)
# print(len(lll[0]))

# # total_cost = []
# # for letter in word:
# #     # print(letter, cost_list[letter])
# #     total_cost == cost_list2[letter]
# # print(total_cost)

def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False


def char(x):
    return x == x


print(same_by(char, lll))


# def rhythm(str):
#     str = str.split()
#     (print(str))
#     list = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list.append(result)
#         print(list)
#     return len(list) == list.count(list[0])

# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()
# if rhythm(str):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')