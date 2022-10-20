def get_input_parameters():
    """
    Получаем входное слово

    :return: входное слово, например: "привет"
    :rtype: str
    """
    word = input('Введите слово: ')
    word_list = list(word)
    unique_letters = 0

    for i in word_list:
        same_letters = 0
        for j in word_list:
            if j == i:
                same_letters += 1
        if same_letters == 1:
            unique_letters += 1
    print('Количество уникальных букв:', unique_letters)



def display_result(number_unique_letters):
    """
    Выводим количество уникальных букв в слове

    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """




def count_number_unique_letters(word):
    """
    Считаем количество уникальных букв в слове.

    :param word: входное слово, например: "привет"
    :type word: str

    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
