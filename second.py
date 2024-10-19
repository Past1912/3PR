def count_vowels(text):
    vowels = 'aeiou'
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# Пример использования:
input_txt = input('Введите текст: ')
number_of_vowels = count_vowels(input_txt)
print(f'Количество гласных в тексте: {number_of_vowels}')