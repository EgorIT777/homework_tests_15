def get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    cells_num = int(input('Введите кол-во клеток: '))
    cells_list = []
    result = []
    for i in range(cells_num):
        print('Эффективность', (i + 1), 'клетки: ', end= ' ')
        effic_cell = int(input())
        cells_list.append(effic_cell)
    for index in range(cells_num):
        if cells_list[index] < index:
            result.append(cells_list[index])
    print()
    print('Неподходящие значения: ', ' '.join(map(str, result)))



def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
