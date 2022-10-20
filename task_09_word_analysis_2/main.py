def get_input_parameters():
    """
    Получаем входное слово

    :return: например: abccba
    :rtype: str
    """
    word = input('Введите слово: ')
    return word




def display_result(is_palindrome):
    """
    Выводим информацию является ли строка палиндромом

    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    print(is_palindrome)



def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.

    :param word: слово, например: abccba
    :type word: str

    :return: является ли слово палиндром, например: True
    :rtype: bool
    """
    palindrome = 'Слово является палиндромом'
    not_palindrome = 'Слово не является палиндромом'
    for i in range(len(word) // 2):
        if word[i] == word[- 1 - i]:
          return palindrome
    else:
        return not_palindrome



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
