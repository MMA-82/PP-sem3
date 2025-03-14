"""
Пользователь вводит строку текста.
Выведите каждое слово с новой строки.
Слова нумеруются, начиная с единицы.
Слова выводятся отсортированными согласно кодировке Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""
text_list = input('Введите строку: ').split()
text_list.sort()

max_len = max([len(word) for word in text_list])
max_len1 = len(max(text_list, key=len))

for i, word in enumerate(text_list, 1):
    print(f'{i} {word:>{max_len}}')
