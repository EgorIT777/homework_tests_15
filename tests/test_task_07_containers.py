import unittest

from task_07_containers.main import search_serial_number_new_container


class Test07SearchSerialNumberNewContainer(unittest.TestCase):
    def test_main(self):
        """
        Проверяем обычный кейс. При вводе [165, 163, 160, 160, 157, 157, 155, 154] должны получить 3
        """
        new_list = [], []
        number_of_containers = int(input('Введите количество контейнеров: '))
        for i in range(number_of_containers):
            print('Введите вес контейнера: ', end=' ')
            new_list[0].append(int(input()))
        new_list[1].append(int(input('Введите вес нового контейнера: ')))
        return new_list



if __name__ == '__main__':
    unittest.main()
