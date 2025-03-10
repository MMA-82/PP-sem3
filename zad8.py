"""
Три друга взяли вещи в поход.
Сформируйте словарь, где ключ - имя друга, 
значение - кортеж вещей. Ответьте на вопросы:
Какие вещи взяли все три друга?
Какие вещи уникальны, есть только у одного друга?
Какие вещи есть у всех кроме одного, и имя того, 
у кого эта вещь отсутствует?
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

dct = {
    "Юра": ("палатка", "рюкзак", "котелок"),
    "Сергей": ("рюкзак", "палатка", "спички", "лопата"),
    "Олег": ("стул", "рюкзак", "продукты"),
}
first = list(dct.keys())[0]
res = set(dct[first])
for k, v in dct.items():
    res = res.intersection(set(v))
print('У всех есть:', *res)

dct_count = {}
for k, v in dct.items():
    for value in v:
        dct_count[value] = dct_count.get(value, 0) + 1
frnds = len(list(dct.keys())) - 1
things = []
for k, v in dct_count.items():
    if v == frnds:
        things.append(k)
for k, v in dct.items():
    for item in things:
        if item not in v:
            print(f'{item} есть у всех кроме {k}')
            break
one_thing = []
for k, v in dct_count.items():
    if v == 1:
        one_thing.append(k)
print('Вещи в единственном экземпляре: ', *one_thing)
print('Друзья взяли с собой: ', *dct_count)
