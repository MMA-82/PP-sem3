"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""
from random import randint

lst = [randint(0, 10) for i in range(10)]
print('Дан список: ', *lst)
d_lst = list(set([i for i in lst if lst.count(i) > 1]))

# for i in lst:
#     if lst.count(i) > 1:
#         d_lst.append(i)
print('Вывод списка дубликатов: ', *d_lst)
