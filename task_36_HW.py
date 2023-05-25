# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))
text = 'house=дом car=машина men=человек tree=дерево'
# text = input('Введите строку(например house=дом car=машина men=человек tree=дерево): ')
formated_string = dict(text)
# formated_string = (text.replace("=", " ").split())
print(formated_string)

result = tuple(map(lambda x: (x, x[2], ), formated_string))
print(result)
