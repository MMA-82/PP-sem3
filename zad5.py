"""
Создайте вручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами нечетных элементов
исходного списка. Нумерация начинается с единицы.
"""
lst = [1, 2, 3, 1, 4, 5, 3, 7, 2]
new_lst = []
for num, el in enumerate(lst, 1):
    if el % 2 == 1:
        new_lst.append(num)
print(new_lst)
