"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""
from random import randint

things = {'лопата': 3, 'палатка': 5, 'веревка': 2, 'топор': 2, 'мангал': 4, 'вода': 1,
          'мясо': 5, 'каремат': 1, 'удочка': 2, 'бинокль': 1}
max_weight = randint(10, 20)
print(f'Максимальная вместимость рюкзака {max_weight} кг')

backpack = []
for k, v in things.items():
    if v <= max_weight:
        backpack.append(k)
        max_weight -= v
print('В рюкзак влезут только: ', *backpack)
