"""
Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква
в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ - символ, а значение - 
частота встречи символа в строке.
Обратите внимание на порядок ключей. 
Объясните почему они совпадают или не совпадают в ваших решениях.
"""
from collections import Counter

txt = input('Введите строку: ')
dct = {}
for ltr in txt:
    dct[ltr] = txt.count(ltr)
print(dct)
print(Counter(txt))
