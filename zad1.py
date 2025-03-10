
my_list = [1, 2, 3, 1, 2, 3]
print(list(set(my_list)))  # первый способ - переводим во множество

new_list = []
for i in my_list:  # второй способ - ищем в списке
    if i not in new_list:
        new_list.append(i)
print(new_list)
