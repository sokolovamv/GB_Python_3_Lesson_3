# Пользователь вводит строку текста
# Подсчитайте сколько раз встречается каждая буква в строке без использования count и с ним
# Реезультат сохраните в словаре, где ключ - символ, а значение - частота встречи символа в строке
# Обратите внимание на порядок ключей 
# Объяните почему они совпадают или не совпадают в ваших решениях

def delete_marks(in_text):
    # символы в тексте
    marks = ''' «»—!()[]{};?@#$%:'"\,./^&;*_'''
    # убираем знаки препинания
    for i in in_text:
        if i in marks:
            in_text = in_text.lower().replace(i, "")
    return in_text

def letter_count(in_text):
    out_dict = {}
    for counted_letter in in_text:
        number_of_letters = 0
        if counted_letter not in out_dict:
            for letter in in_text:
                if letter == counted_letter:
                    number_of_letters += 1
            out_dict[counted_letter] = number_of_letters 
    return out_dict

def letter_count_with_function(in_text):
    out_dict = {}
    for letter in in_text:
        number_of_letters = in_text.count(letter)
        if letter not in out_dict:
            out_dict[letter] = number_of_letters 
    return out_dict
        
user_text = delete_marks(input('Введите текст: '))
print(user_text)
print(f'Без count: {letter_count(user_text)}')
print(f'С помощью count: {letter_count_with_function(user_text)}')

# словари абсолютно одинаковые, потому цикл поочередно рассматривает каждую букву
