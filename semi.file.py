with open ('test.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, мир!')

with open ('test.txt', 'a', encoding='utf-8') as file:
    file.write('\nПривет, мир!')

with open ('test.txt', 'r', encoding='utf-8') as file:
    print(file.read())

with open ('test.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

data[1] = 'Новая строка\n' 

with open ('test.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)