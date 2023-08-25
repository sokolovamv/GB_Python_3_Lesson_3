# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

text = """
«Спартак» — российский футбольный клуб из Москвы. Основан 18 апреля 1922 года. 
Самый популярный российский клуб по исследованию «Яндекса», 
один из самых популярных футбольных клубов страны по исследованию ВЦИОМ. 
Входит в топ-20 самых популярных клубов Европы. Самый титулованный футбольный клуб России. 
12-кратный чемпион СССР, 10-кратный чемпион России, 10-кратный обладатель Кубка СССР, 
4-кратный обладатель Кубка России, обладатель Суперкубка России, 
6-кратный обладатель Кубка Содружества, полуфиналист трёх главных клубных европейских турниров 
(Кубка европейских чемпионов, Кубка обладателей кубков и Кубка УЕФА). 
Лучший российский клуб в истории Лиги чемпионов. С советских времён распространено клише 
«Спартак — народная команда»
"""

# символы в тексте
marks = '«»,.()—'
# вспомогательный список, в котором хранится неотсортированная информация о количестве слов
end_list = []

# убираем знаки препинания
for i in text:
    if i in marks:
        text = text.lower().replace(i, "")

# количество слов в тексте
list_of_text = text.split()
print(f'Количество слов в тексте: {len(list_of_text)}')

# количество уникальных слов в тексте
unique_list_of_text = [i for i in set(list_of_text)]
print(f'Количество уникальных слов в тексте: {len(unique_list_of_text)}')

# список с кортежами: уникальное слово и количество слов
for i in unique_list_of_text:
    end_list.append((i, list_of_text.count(i)))

# отсортированный список по количеству слов
sort_list = sorted(end_list, key=lambda elem: elem[1], reverse=True)

# рейтинг - 10 самых встречаемых слов
for i, value in enumerate(sort_list[0:10], start = 1):
    print(i, *value, 'раз(а)')




