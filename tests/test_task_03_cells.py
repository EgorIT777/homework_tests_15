import unittest

from task_03_cells.main import select_cells


class Test03SelectCells(unittest.TestCase):
    def test_select_cells(self):
        """
        Проверяем обычный кейс. При параметрах [5, 3, 0, 6, 2, 10, 4]  должны получить [0 2, 4]
        """


    def test_select_cells_no_result(self):
        """
        Проверяем обычный кейс. При параметрах [1, 2, 3]  должны получить []
        """

    cells_num = int(input('Введите кол-во клеток: '))
    cells_list = []
    result = []
    for i in range(cells_num):
        print('Эффективность', (i + 1), 'клетки: ', end=' ')
        effic_cell = int(input())
        cells_list.append(effic_cell)
    for index in range(cells_num):
        if cells_list[index] < index:
            result.append(cells_list[index])
    print()
    print('Неподходящие значения:', ' '.join(map(str, result)))


if __name__ == '__main__':
    unittest.main()
