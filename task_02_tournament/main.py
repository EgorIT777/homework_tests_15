def display_result(participants_names):
    """
    Выводим список имён участников в первый день

    :param participants_names: список имён участников, например: ["Артемий", "Влад", "Дима", "Женя"]
    :type participants_names: List[str]
    """
    print("Первый день:", participants_names)

def get_participants_names(names):
    """
    Получаем элементы списка только с чётными индексами.

    :param names: список имён, например: ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    :type names: List[str]

    :return: список имён с чётными индексами , например: ["Артемий", "Влад", "Дима", "Женя"]
    :rtype: List[str]
    """

    participants_names = []
    count = []
    for i in range(len(participants_names)):
        if i % 2 == 0:
            count.append(i)
    for i_names in (count):
        participants_names.append(names[i_names])

    return participants_names






if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
