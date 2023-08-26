# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

import random

# функция, перебирающая список по очереди
def filling_the_backpack(in_dict, in_weight):
    for key_dict, value_dict in in_dict.items():
        if value_dict <= in_weight:
            print(key_dict)
            in_weight -= value_dict

# функция, перепбирающая список рандомно
def filling_the_backpack_random(in_dict, in_weight):
    out_list =  []
    list_in_dict = [item for item in in_dict.items()]
    item_dict = random.choice(list_in_dict)
    while int(item_dict[1]) <= in_weight:
        out_list.append(item_dict)
        in_weight -= item_dict[1]
        item_dict = random.choice(list_in_dict)
        while item_dict in out_list:
            item_dict = random.choice(list_in_dict)
    return out_list
        
tourist_dict = {
    'Cпальный мешок': 2,
    'Палатка': 5,
    'Аптечка': 2,
    'Термобелье': 0.5,
    'Туристическая посуда': 1,
    'Термос': 0.5,
    'Средства личной гигиены': 2,
    'Еда': 5,
    'Документы': 0.1,
    'Куртка': 1,
    'Одежда для сна': 0.5,
    'Шапка': 0.2,
    'Перчатки': 0.2,
    'Солнцезащитный крем': 0.1,
    'Солнцезащитные очки': 0.2,
    'Полотенце': 0.1,
    'Повербанк': 0.5,
}


maximum_load_capacity = 10

# по  очереди 
print('Возьмите с собой:')
filling_the_backpack(tourist_dict, maximum_load_capacity)

# рандомный список
print('Возьмите с собой:')
print(*filling_the_backpack_random(tourist_dict, maximum_load_capacity))
