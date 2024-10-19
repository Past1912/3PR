def count_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count = 0

    for char in text:
        if char not in consonants and char != ' ':
            continue

        count += 1

    return count


# Пример использования:
input_txt = input('Введите текст: ')
ue_of_consonants = count_consonants(input_txt)
print(f'Количество согласных в тексте: {ue_of_consonants}')
