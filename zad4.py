"""
Создайте вручную список с повторяющимися элеметами.
Удалите из него все элементы, встречающиеся дважды.
"""
from collections import Counter

lst = [1, 4, 1, 2, 3, 5, 3, 7, 2]
print(lst)
dct2 = Counter(lst)  # сортирует по убыванию счетчика
dct = {}
for i in lst:
    # if i not in dct:
    # dct[i] = 0
    dct[i] = dct.get(i, 0) + 1
    # dct[i] += 1
for k, v in dct.items():
    if v == 2:
        lst.remove(k)  # удаляет одно вхождение
        lst.remove(k)
print(lst)
print(dct2)
