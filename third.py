def count_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count = 0

    for char in text:
        if char not in consonants and char != ' ':
            continue

        count += 1

    return count


# Пример использования:
input_text = input('Введите текст: ')
number_of_consonants = count_consonants(input_text)
print(f'Количество согласных в тексте: {number_of_consonants}')