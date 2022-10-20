def get_input_parameters():
    """
    Получаем неотсортированный список чисел

    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """
    list_nums = []
    return list_nums








def display_result(sorted_list):
    """
    Выводим отсортированный список

    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    sorted_list = [1, 4, -3, 0, 10]
    print('Изначальный список:', sorted_list)
    list(sorted_list)


    print('Отсортированный список:', sort_list(sorted_list))














def sort_list(original_list):
    """
    Сортируем список

    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    for i in range(len(original_list)):
        for cur_elem in range(i, len(original_list)):
            if original_list[i] > original_list[cur_elem]:
                original_list[cur_elem], original_list[i] = original_list[i], original_list[cur_elem]
    return original_list
if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
