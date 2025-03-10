"""
Создайте вручную кортеж, содержащий элементы разных типов.
Получите из него словарь списков, где: 
ключ - тип элемента,
значение - список элементов данного типа.
"""
tpl = (10, 'ilne', 'line2', 3.14, 33, 'line3', 1.5)
type_dict = {}
for i in tpl:
    t = type(i).__name__
    if t not in type_dict:
        type_dict[t] = []
    type_dict[t].append(i)
print(type_dict)
