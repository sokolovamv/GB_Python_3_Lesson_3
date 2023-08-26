# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются, начиная с 1
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, 
# чтобы у самого длинного слова был один пробел между ним и номером строки

user_text = input('Введите текст: ')

# символы в тексте
marks = '''«»—!()[]{};?@#$%:'"\,./^&amp;*_'''

# убираем знаки препинания
for i in user_text:
    if i in marks:
        user_text = user_text.lower().replace(i, "")

# делаем из текста список
list_of_user_text = user_text.split()

# длина максимального слова
max_len_of_word = max([len(word) for word in list_of_user_text])

# отсортированный список
sort_list = sorted(list_of_user_text)

# находим максимальное слово
for word in sort_list:
    if len(word) == max_len_of_word:
        max_word = word

# отсортированный список и выравненный (считаем, что меньше 100 слов)
for num, value in enumerate(sort_list, start = 1):
    if num < 10 and sort_list.index(max_word) >= 9:
        print(num, value.rjust(max_len_of_word + 1))
    else:
        print(num, value.rjust(max_len_of_word))