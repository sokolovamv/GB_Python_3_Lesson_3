# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

user_list = [1, 2, 3, 2, 3, 3, 'xxx', 'a', 'aa', 'aa']
new_list = []

for i in user_list:
    if user_list.count(i) > 1 and i not in new_list:
        new_list.append(i)
print(new_list)