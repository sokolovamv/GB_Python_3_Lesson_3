# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ - имя друга, а значение - кортеж - вещей. Ответьте на вопросы:
# Какие вещи  взяли  3 друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутсвует
# Для решения используйте операции с множествами. 
# Код должен расширяться на любое большее количество друзей.


def filling_of_backpack(amount_of_people: int) -> dict:
    dict_of_clothes = {}
    for _ in range(amount_of_people):
        name = input('Введите имя друга: ')
        dict_of_clothes[name] = tuple(input('Введите через пробел вещи, которые он взял').split())
    return dict_of_clothes

def unique_clothes(in_dict: dict) -> list:
    list_of_dict = [value for value in in_dict.values()]
    compare_clothes = list_of_dict[0]
    for i in range(len(list_of_dict) - 1):
        compare_clothes = set(compare_clothes) & set(list_of_dict[i+1])
    return compare_clothes


amount_of_friends  = int(input('Введите количество друзей, которые собираются в поход: '))

list_clothes = filling_of_backpack(amount_of_friends)
print(unique_clothes(list_clothes))