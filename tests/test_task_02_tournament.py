import unittest

from task_02_tournament.main import get_participants_names


class Test02GetParticipantsNames(unittest.TestCase):
    def test_get_participants_names(self):
        """
        Проверяем обычный кейс. Выводим элементы списка только с чётными индексами.
        """

    participants_names = []
    count = []
    for i in range(len(participants_names)):
        if i % 2 == 0:
            count.append(i)
    for i_names in (count):
        participants_names.append(participants_names)





if __name__ == '__main__':
    unittest.main()
