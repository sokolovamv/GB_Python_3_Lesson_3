# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

# список повторяющихся элементов
user_list = [1, 2, 3, 2, 3, 3, 'xxx', 'a', 'aa', 'aa']
new_list = []

# список с дублирующимися элементами + проверка, что символ дублируется
for i in user_list:
    if user_list.count(i) > 1 and i not in new_list:
        new_list.append(i)
print(new_list)

# второй вариант с множествами
new_list_2 = [i for i in set(user_list) if user_list.count(i) > 1]
print(new_list_2)